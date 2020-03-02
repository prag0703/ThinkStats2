"""
This file contains solution to exercise 1.3
"""

from __future__ import print_function, division

import numpy as np
import sys
import math
import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass


def PregBabySex(resp):
    preg = nsfg.ReadFemPreg()
    return preg.babysex.value_counts()[1]


def PregMonthsCnt(resp, preg_months_cnt):

    """
    PregMonthsCnt returns the map for cnt of months of pregnancy
    """
    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()
    preg_months_cnt = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }

    for item in preg.moscurrp:
        if not math.isnan(item) and item != 0.0:
            preg_months_cnt[int(item)] = preg_months_cnt[int(item)] + 1

    print("Preg Months Cnt from female data = {}".format(preg_months_cnt))
    return preg_months_cnt


def main():
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()

    print("LIVE BIRTHS (ACCOUNTING FOR MULTI BIRTH) = {}".format(resp.births5.value_counts()[1]))
    print("R CURRENTLY PURSUING MEDICAL HELP TO GET PREGNANT = {}".format(resp.hlppgnow.value_counts()[1]))
    print("INFERTILITY SERVICES RECEIVED-1ST MENTION = {}".format(resp.typallpg.value_counts()[1]))
    print("VISITS IN LAST 12 MOS FOR MEDICAL HELP TO GET PREGNANT = {}".format(resp.numvstpg.value_counts()[1]))
    preg_months_cnt = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }

    for item in resp.moscurrp:
        if not math.isnan(item) and item != 0.0:
            preg_months_cnt[int(item)] = preg_months_cnt[int(item)] + 1

    print("Pregnancy Months Count data from Fem Resp data = {}".format(preg_months_cnt))

    preg_months_cnt_preg_data = PregMonthsCnt(resp, preg_months_cnt)

    assert preg_months_cnt == preg_months_cnt_preg_data

    age_sum = 0
    for item in resp.ager.iteritems():
        age_sum += item[1]

    avg_age = age_sum/len(resp)

    print("AVERAGE AGE AT AN INTERVIEW = {}".format(age_sum/len(resp)))

    assert PregBabySex(resp) == 4641

    print("All tests passed for exercise 1.3")


if __name__ == '__main__':
    main()
