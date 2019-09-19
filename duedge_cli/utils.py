# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
TOOLS
"""

import shlex


def find_match_characters(string, pattern):
    """Find match match pattern string.
    Args:
        params: string
                pattern
    Returns:
    Raises:
    """
    matched = []
    last_index = 0

    if not string or not pattern:
        return matched

    if string[0] != pattern[0]:
        return matched

    for c in pattern:
        index = string.find(c, last_index)
        if index < 0:
            return []

        matched.append((c, index))
        last_index = index + 1

    return matched


def find_most_match_pattern(string, pattern):
    """Find most match pattern string.
    Args:
        params: string
                pattern
    Returns:
    Raises:
    """
    result = find_match_characters(string, pattern)

    length = len(string)
    word = [" "] * length
    score = 0

    for char, index in result:
        word[index] = char
        score -= index + 1

    return "".join(word), score


def guess_command(parts, paragraphs):
    """guess input command
    Args:
        params: parts
                paragraphs
    Returns:
    Raises:
    """
    probable_commands = []
    for paragraph in paragraphs:
        prefix = parts[:len(paragraph)]
        if prefix == paragraph:
            probable_commands.append((paragraph, []))

    if not probable_commands:
        similar_commands = []
        for paragraph in paragraphs:
            fixed_words = []
            fixed_score = []
            mismatch = False
            for exp, got in zip(paragraph, parts):
                word, score = find_most_match_pattern(exp, got)
                if 0 == score:
                    mismatch = True
                    break

                fixed_words.append(word)
                fixed_score.append(score)

            if not mismatch:
                similar_commands.append((fixed_score, paragraph, fixed_words))

        if not similar_commands:
            return None

        similar_commands.sort()
        max_similar_score = similar_commands[-1][0]
        while similar_commands:
            score, x, fixed_words = similar_commands.pop()
            if score == max_similar_score:
                probable_commands.append((x, fixed_words))

    cmd, fixed_words = probable_commands[0]

    if len(probable_commands) > 1:
        for x, fixed_words in probable_commands:
            if x != cmd:
                return probable_commands

    return probable_commands
