import re

def parse_mingzhi(mingzhi):
    """Parse mingzhi char and vowel

    Args:
        mingzhi (word): mingzhi char

    Returns:
        str: mingzhi root char, vowel
    """
    for vowel in ['ི', 'ུ', 'ེ', 'ོ']:
        if vowel in mingzhi:
            mingzhi = mingzhi.replace(vowel, '')
            return mingzhi, vowel
    return mingzhi, ''

def get_mingzhi_options(syl_parts, mingzhi_mapping):
    """Generate misspelled option by substituting similar sound mingzhi

    Args:
        syl_parts (dict): consit of all the possible component of a syllable which are sngonjug, mingzhi, jesjug and yangjug
        mingzhi_mapping (dict): mingzhi and its similar sound mingzhi

    Returns:
        list: misspelled options generated by substituting similar sound mingzhi
    """
    options = []
    cur_sngon_jug = syl_parts['sngon_jug']
    cur_mingzhi, mingzhi_vowel = parse_mingzhi(syl_parts['mingzhi'])
    cur_jes_jug = syl_parts['jes_jug']
    cur_yang_jug = syl_parts['yang_jug']
    if cur_mingzhi in mingzhi_mapping:
        for mingzhi_opt in mingzhi_mapping[cur_mingzhi]:
            cur_option = f'{cur_sngon_jug}{mingzhi_opt}{mingzhi_vowel}{cur_jes_jug}{cur_yang_jug}་'
            options.append(cur_option)
    return options
