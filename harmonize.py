#!/usr/bin/env python3

import argparse
import pandas
from re import sub
from csv import QUOTE_ALL


# Ordered list of variables to output for CDE
CDE_COLUMNS = ["subjectcode", "subjectageyears", "subjectage", "gender", "_3rdventricle", "_4thventricle",
               "rightaccumbensarea", "leftaccumbensarea", "rightamygdala", "leftamygdala", "brainstem", "rightcaudate",
               "leftcaudate", "rightcerebellumexterior", "leftcerebellumexterior", "rightcerebellumwhitematter",
               "leftcerebellumwhitematter", "rightcerebralwhitematter", "leftcerebralwhitematter", "csfglobal",
               "righthippocampus", "lefthippocampus", "rightinflatvent", "leftinflatvent", "rightlateralventricle",
               "leftlateralventricle", "rightpallidum", "leftpallidum", "rightputamen", "leftputamen",
               "rightthalamusproper", "leftthalamusproper", "rightventraldc", "leftventraldc", "opticchiasm",
               "cerebellarvermallobulesiv", "cerebellarvermallobulesvivii", "cerebellarvermallobulesviiix",
               "leftbasalforebrain", "rightbasalforebrain", "rightacgganteriorcingulategyrus",
               "leftacgganteriorcingulategyrus", "rightainsanteriorinsula", "leftainsanteriorinsula",
               "rightaorganteriororbitalgyrus", "leftaorganteriororbitalgyrus", "rightangangulargyrus",
               "leftangangulargyrus", "rightcalccalcarinecortex", "leftcalccalcarinecortex", "rightcocentraloperculum",
               "leftcocentraloperculum", "rightcuncuneus", "leftcuncuneus", "rightententorhinalarea",
               "leftententorhinalarea", "rightfofrontaloperculum", "leftfofrontaloperculum", "rightfrpfrontalpole",
               "leftfrpfrontalpole", "rightfugfusiformgyrus", "leftfugfusiformgyrus", "rightgregyrusrectus",
               "leftgregyrusrectus", "rightioginferioroccipitalgyrus", "leftioginferioroccipitalgyrus",
               "rightitginferiortemporalgyrus", "leftitginferiortemporalgyrus", "rightliglingualgyrus",
               "leftliglingualgyrus", "rightlorglateralorbitalgyrus", "leftlorglateralorbitalgyrus",
               "rightmcggmiddlecingulategyrus", "leftmcggmiddlecingulategyrus", "rightmfcmedialfrontalcortex",
               "leftmfcmedialfrontalcortex", "rightmfgmiddlefrontalgyrus", "leftmfgmiddlefrontalgyrus",
               "rightmogmiddleoccipitalgyrus", "leftmogmiddleoccipitalgyrus", "rightmorgmedialorbitalgyrus",
               "leftmorgmedialorbitalgyrus", "rightmpogpostcentralgyrusmedialsegment",
               "leftmpogpostcentralgyrusmedialsegment", "rightmprgprecentralgyrusmedialsegment",
               "leftmprgprecentralgyrusmedialsegment", "rightmsfgsuperiorfrontalgyrusmedialsegment",
               "leftmsfgsuperiorfrontalgyrusmedialsegment", "rightmtgmiddletemporalgyrus", "leftmtgmiddletemporalgyrus",
               "rightocpoccipitalpole", "leftocpoccipitalpole", "rightofugoccipitalfusiformgyrus",
               "leftofugoccipitalfusiformgyrus", "rightopifgopercularpartoftheinferiorfrontalgyrus",
               "leftopifgopercularpartoftheinferiorfrontalgyrus", "rightorifgorbitalpartoftheinferiorfrontalgyrus",
               "leftorifgorbitalpartoftheinferiorfrontalgyrus", "rightpcggposteriorcingulategyrus",
               "leftpcggposteriorcingulategyrus", "rightpcuprecuneus", "leftpcuprecuneus",
               "rightphgparahippocampalgyrus", "leftphgparahippocampalgyrus", "rightpinsposteriorinsula",
               "leftpinsposteriorinsula", "rightpoparietaloperculum", "leftpoparietaloperculum",
               "rightpogpostcentralgyrus", "leftpogpostcentralgyrus", "rightporgposteriororbitalgyrus",
               "leftporgposteriororbitalgyrus", "rightppplanumpolare", "leftppplanumpolare", "rightprgprecentralgyrus",
               "leftprgprecentralgyrus", "rightptplanumtemporale", "leftptplanumtemporale", "rightscasubcallosalarea",
               "leftscasubcallosalarea", "rightsfgsuperiorfrontalgyrus", "leftsfgsuperiorfrontalgyrus",
               "rightsmcsupplementarymotorcortex", "leftsmcsupplementarymotorcortex", "rightsmgsupramarginalgyrus",
               "leftsmgsupramarginalgyrus", "rightsogsuperioroccipitalgyrus", "leftsogsuperioroccipitalgyrus",
               "rightsplsuperiorparietallobule", "leftsplsuperiorparietallobule", "rightstgsuperiortemporalgyrus",
               "leftstgsuperiortemporalgyrus", "righttmptemporalpole", "lefttmptemporalpole",
               "righttrifgtriangularpartoftheinferiorfrontalgyrus", "lefttrifgtriangularpartoftheinferiorfrontalgyrus",
               "rightttgtransversetemporalgyrus", "leftttgtransversetemporalgyrus", "montrealcognitiveassessment",
               "minimentalstate", "agegroup", "handedness", "updrstotal", "updrshy", "adnicategory", "edsdcategory",
               "ppmicategory", "alzheimerbroadcategory", "parkinsonbroadcategory", "neurodegenerativescategories",
               "dataset", "apoe4", "rs3818361_t", "rs744373_c", "rs190982_g", "rs1476679_c", "rs11767557_c",
               "rs11136000_t", "rs610932_a", "rs3851179_a", "rs17125944_c", "rs10498633_t", "rs3764650_g",
               "rs3865444_t", "rs2718058_g", "fdg", "pib", "av45", "ab1_42", "t_tau", "p_tau", "ab1_40"]

# Ordered list of variables to output for Besta
BESTA_COLUMNS = ["subjectcode", "diagnosis_bsl", "yr_education", "cdr_score", "npi", "tmt_a", "tmt_b", "bestacategory"]


def main():
    # Parse command line arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("input_csv")
    args_parser.add_argument("output_cde_csv")
    args_parser.add_argument("output_besta_csv")
    args = args_parser.parse_args()

    # Read input CSV files to create Pandas data-frames
    df = pandas.read_csv(args.input_csv)

    # Harmonize data
    df_cde, df_besta = harmonize(df, CDE_COLUMNS, BESTA_COLUMNS)

    # Generate CSV files from data-frames
    df_cde.to_csv(args.output_cde_csv, index=False, quoting=QUOTE_ALL)
    df_besta.to_csv(args.output_besta_csv, index=False, quoting=QUOTE_ALL)

    # Workaround to avoid floating-point formatting on integer values
    content = [sub('"(\d+).0"', r'\1', l) for l in open(args.output_besta_csv, 'r')]
    with open(args.output_besta_csv, 'w') as f:
        f.writelines(content)

    # Workaround to avoid floating-point formatting on integer values
    content = [sub('"(\d+).0"', r'\1', l) for l in open(args.output_cde_csv, 'r')]
    with open(args.output_cde_csv, 'w') as f:
        f.writelines(content)


def harmonize(df, cde_cols, besta_cols):
    # Generate columns
    df['agegroup'] = df.apply(lambda row: group_by_age(row), axis=1)
    df['neurodegenerativescategories'] = df.apply(lambda row: neurodegeneratives(row), axis=1)

    # Sort columns
    df_cde = df.reindex(cde_cols, axis=1)
    df_besta = df.reindex(besta_cols, axis=1)

    return df_cde, df_besta


def group_by_age(row):
    age_years = row['subjectageyears']
    if pandas.isnull(age_years):
        if pandas.isnull(row['subjectagemonths']):
            return None
        else:
            age_years = 0
    if 50 <= age_years < 60:
        return "50-59y"
    if 60 <= age_years < 70:
        return "60-69y"
    if 70 <= age_years < 80:
        return "70-79y"
    if 80 <= age_years:
        return "+80y"
    return "-50y"


def neurodegeneratives(row):
    if row['alzheimerbroadcategory'] in ['AD', 'CN', 'MCI']:
        return row['alzheimerbroadcategory']
    elif row['parkinsonbroadcategory'] in ['PD', 'Other']:
        return row['parkinsonbroadcategory']
    else:
        return None


if __name__ == '__main__':
    main()
