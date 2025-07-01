from low_variance_cols import df_reduced

related_features_to_drop = [
    # Health Insurance Coverage:
    "CURRINS", "CORRCOV",  # CurrIns_2122
    "INSGAP",  # InsGap_2122
    "INSTYPE", "K12Q03", "K12Q04", "K12Q12", "TRICARE", "K11Q03R", "HCCOVOTH",  # instype_2122
    "K3Q20", "K3Q22", "HOWMUCH", "K3Q21B",  # InsAdeq_2122, insurance_2122
    "MENBEVCOV",  # InsMentH_2122
    "K3Q20",  # benefits_2122
    "K3Q22",  # allows_2122
    "K3Q21B", "HOWMUCH",  # expense_2122
    "HEALTHKNOW", "KEEPINSADULT",  # InsNeed_2122
    "S4Q01",  # MedCare_2122
    "VIDEOPHONE",  # VideoPhone_2122
    "K3Q25",  # MedBills_2122

    # Care Coordination & Communication:
    "K5Q20_R", "S4Q01",  # HelpCoord_2122
    "K5Q21",  # ExtraHelp_2122
    "K5Q22",  # AllExtraHelp_2122
    "K5Q30",  # DrCommR_2122
    "K5Q31_R",  # OtherComm_2122
    "ALTHEALTH",  # AlterHC_2122
    "K4Q27",  # ForgoneCare_2122
    "C4Q04",  # frustrated_2122

    # Eye Care (Access & Quality)
    "EYEDOCTOR",  # EyeDoctor_2122
    "EYECARE1",  # EyeExam_2122
    "EYECARE2",  # EyeGlassContact_2122
    "EYECARE3",  # VisionDisorder_2122
    "VISIONSCREENOTHER",  # VisnScrnOther_2122
    "VISIONEXAMREC",  # RecEyeExam_2122

    # Preventive Medical & Dental Care:
    "S4Q01", "K4Q20R",  # PrevMed_2122
    "DOCROOM",  # VisitTime_2122
    "DOCPRIVATE",  # PrivateTalk_2122
    "K4Q30_R_1", "K4Q30_R_2", "K4Q30_R_3",  # DentCare_2122
    "DENTISTVISIT",  # PrevDent_2122
    "DENTALSERV1", "DENTALSERV7",  # DentCheck_2122
    "DENTALSERV2",  # DentCleaning_2122
    "DENTALSERV3",  # DentInstruct_2122
    "DENTALSERV4",  # DentXray_2122
    "DENTALSERV5",  # fluoride_2122
    "DENTALSERV6",  # sealant_2122
    "K2Q01_D",  # TeethCond_2122
    "CAVITIES", "GUMBLEED", "TOOTHACHES",  # OralProb_2122

    # Learning & Special Health Conditions:
    "K2Q30A", "K2Q30B", "SC_AGE_YEARS",  # learning_2122
    "K2Q35A", "K2Q35B", "K2Q35C", "K2Q35D",  # autism_2122, ASDSevInd_2122, ASDDrType_2122
    "AUTISMMED", "AUTISMTREAT",  # ASDMed_2122, ASDBehTreat_2122
    "K2Q35A_1_YEARS",  # ASDAge_2122
    "K2Q31A", "K2Q31B",  # ADHD_2122
    "K2Q43B",  # hearing_2122
    "BLINDNESS",  # vision_2122
    "FASD",  # FASD_22

    # Early Childhood Flourishing (6month - 5years):
    "K6Q70_R", "K6Q73_R", "K6Q71_R", "K6Q72_R",  # flrish0to5_2122
    "K6Q71_R", "K7Q84_R", "K7Q85_R",  # flrish6to17_2122
    "K6Q70_R", "K6Q71_R", "K6Q73_R", "SC_AGE_LT6",  # curious0to5_2122
    "K6Q72_R",  # smile_2122

    # School-Readiness & Social Skills (Age 3-5):
    "RECOGBEGIN",  # RecogBegin_2122
    "RECOGABC",  # RecogLetter_2122
    "WRITENAME",  # WriteName_2122
    "DISTRACTED",  # distracted_2122
    "PLAYWELL",  # PlayWell_2122

    # Family Resilience & Flourishing:
    "TALKABOUT",  # TalkAbout_2122
    "WKTOSOLVE",  # WrkToSolve_2122
    "STRENGTHS",  # strengths_2122
    "HOPEFUL",  # hopeful_2122
    "CtFamRes_2122",  # FamResilience_2122

    # Adverse Childhood Experiences (ACE):
    "ACE1",  # ACEincome2_2122
    "ACE3",  # ACEdivorce_2122
    "ACE4",  # ACEdeath_2122
    "ACE5",  # ACEjail_2122
    "ACE6",  # ACEdomviol_2122
    "ACE7",  # ACEneighviol_2122
    "ACE8",  # ACEmhealth_2122
    "ACE9",  # ACEdrug_2122
    "ACE10",  # ACEdiscrim_2122

    # Parental Stress & Aggravation and Concerns:
    "K8Q31",  # DiffCare_2122
    "K8Q32",  # bother_2122
    "K8Q34",  # angry_2122
    "K8Q35",  # EmSupport_2122
    "K8Q30",  # ParCoping_2122
    "ParAgg_ct",  # ParAggrav_2122
    "K6Q10", "S4Q01", "K4Q30_R_1", "K4Q30_R_2", "K4Q22_R", "K4Q24_R",  # DrAskConc_2122

    # Special Services & Education Plans & School:
    "K4Q36", "K4Q37",  # SpSerAge_2122
    "K6Q15", "SESCURRSVC",  # SpEducPln_2122
    "SESPLANYR",  # SpEdAge_2122
    "K7Q82_R", "K7Q83_R",  # SchlEngage_2122
    "REPEATED",  # ReptGrade_2122
    "K7Q02R_R",  # SchlMiss_2122
    "K7Q30", "K7Q31", "K7Q32",  # AftSchAct_2122
    "K7Q33",  # EventPart_2122
    "K7Q37",  # volunteer_2122
    "K10Q41_R",  # SchlSafe_2122

    # Work:
    "K7Q38",  # WorkPay_2122

    # Sepcialist Care:
    "K4Q26", "K4Q24_R"  # SpCareDiff_2122
             "SC_K2Q10", "SC_K2Q11", "SC_K2Q12", "SC_K2Q13", "SC_K2Q14", "SC_K2Q15", "SC_K2Q16", "SC_K2Q17",
    "SC_K2Q18", "SC_K2Q19", "SC_K2Q20", "SC_K2Q21", "SC_K2Q22", "SC_K2Q23", "SC_CSHCN",  # CSHCN_2122

    # Child Development:
    "K6Q12", "K6Q13A", "K6Q13B", "K6Q14A", "K6Q14B",  # DevScrnng_2122
    "K4Q36", "K4Q38",  # SpecServ_2122
    "K4Q37",  # SpSerAge_2122

    # Indicators:
    "K4Q27", "NOTELIG",  # ineligible_2122
    "AVAILABLE",  # unavailable_2122
    "APPOINTMENT",  # appointment_2122
    "TRANSPORTCC",  # transport_2122
    "NOTOPEN",  # NotOpen_2122
    "ISSUECOST",  # CostIssue_2122
    "HOSPITALSTAY",  # HospitalStay_2122
    "K4Q28X01", "K4Q28X02", "K4Q28X03", "K4Q28X_EAR",  # ForgoneHear_2122, ForgoneMH_2122
    "K5Q10",  # NoRefPrb_2122, NoRefPrb2_2122
    "HOSPITALER",  # ERVisit_2122

    # General Health:
    "K2Q01",  # ChHlthSt_2122
    "HCABILITY", "HCEXTENT",  # DailyAct_2122
    "K2Q38A", "K2Q38B", "K2Q33A", "K2Q33B", "K2Q32A",  # MEDB10ScrQ5_2122
    "K2Q32B", "K2Q34A", "K2Q34B", "K2Q36A", "K2Q36B",  # MEDB10ScrQ5_2122
    "K2Q60A", "K2Q60B", "K2Q37A", "K2Q37B", "K2Q30A",  # MEDB10ScrQ5_2122
    "K2Q30B", "K2Q35A", "K2Q35B", "K2Q31A", "K2Q31B",  # MEDB10ScrQ5_2122
    "SC_K2Q22", "SC_K2Q23", "C#_K2Q22", "C#_K2Q23",  # MEDB10ScrQ5_2122

    # Mental Health:
    "K4Q22_R",  # MentHCare_2122
    "TREATNEED",  # MentHDiff_2122
    "K4Q24_R",  # SpecCare_2122
    "K4Q26",  # SpCareDiff_2122

    # Breast Feed:
    "K6Q40",  # BrstEver_2122
    "K6Q40", "BREASTFEDEND_MO_S", "FRSTFORMULA_MO_S", "FRSTSOLIDS_MO_S", "K6Q41R_STILL",
    "K6Q42R_NEVER", "K6Q43R_NEVER",  # ExBrstFd_2122

    # BMI - Weight and Height
    "BMICLASS",  # BMI4_2122, BMI3_2122
    "OVERWEIGHT",  # ToldOverweight_2122
    "WGTCONC",  # WgtConcn_2122
    "BIRTHWT_L",  # LowBWght_2122
    "BIRTHWT_VL",  # VeryLBWght_2122

    # Activity:
    "PHYSACTIV",  # PhysAct_2122
    "OUTDOORSWKDAY",  # OutdrsWkDay_2122
    "OUTDOORSWKEND",  # OutdrsWkend_2122

    # Birth
    "K2Q05",  # BornPre_2122

    # Bully
    "BULLY",  # bully_2122
    "BULLIED_R",  # bullied_2122

    # Child information & Characteristics:
    "K7Q70R",  # argue_2122
    "MAKEFRIEND",  # MakeFriend_2122
    "SLEEPPOS",  # SleepPos_2122
    "SC_AGE_YEARS",  # age3_2122, age5_2122
    "SC_SEX",  # sex_2122
    "SC_HISPANIC_R; SC_RACE_R",  # race4_2122, raceAsia_2122, ace7_2122
    "FAMILY_R", "A1_MARITAL", "A2_MARITAL",  # famstruct_2122

    # Medical&Health Care:
    "S4Q01", "K4Q01", "K4Q02_R", "K4Q04_R", "K5Q10", "K5Q11", "K5Q40", "K5Q41",
    "K5Q42", "K5Q43", "K5Q44", "K5Q20_R", "K5Q21", "K5Q22", "K5Q30", "K5Q31_R", "K5Q32",  # MedHome_2122
    "ATHOMEHC",  # HomeCare_2122
    "ARRANGEHC",  # TimeCoord_2122
    "HOURSLEEP", "HOURSLEEP05",  # HrsSleep_2122

    # Parenting and Parents Info:
    "BESTFORCHILD", "DECISIONS", "DISCUSSOPT", "RAISECONC",  # ShareDec_2122
    "K9Q96",  # Mentor_2122
    "A1_PHYSHEALTH", "A1_RELATION", "A1_SEX", "A2_PHYSHEALTH", "A2_RELATION", "A2_SEX",  # MothPhyH_2122, FathPhyH_2122
    "A1_MENTHEALTH", "A2_MENTHEALTH",  # MotherMH_2122, FatherMH_2122
    "A1_EMPLOYED", "A2_EMPLOYED",  # EmploymentSt_2122
    "FPL_I1", "FPL_I2", "FPL_I3", "FPL_I4", "FPL_I5", "FPL_I6", "FPL_IF",  # WrkngPoorR_2122
    "K8Q21",  # ShareIdeas_2122
    "K6Q60_R",  # readto_2122
    "K6Q61_R",  # SingStory_2122
    "K8Q11",  # MealTogether_2122
    "HOPEFUL", "STRENGTHS", "TALKABOUT", "WKTOSOLVE",  # FamResilience_2122
    "K6Q27",  # JobChange_2122
    "CUTHOURS", "STOPWORK",  # StopCutWork_2122
    "AVOIDCHG",  # AvoidChng_2122
    "K6Q20",  # Care10hrs_2122
    "BEDTIME",  # BedTime_2122
    "HOUSE_GEN", "BORNUSA", "A1_BORN", "A2_BORN",  # PrntNativity_2122
    "HIGRADE_TVIS", "A1_GRADE", "A2_GRADE",  # AdultEduc_2122

    # Hobbies and Free-Time:
    "SCREENTIME",  # ScreenTime_2122

    # Adulting:
    "CHANGEAGE", "DOCPRIVATE", "GAINSKILLS", "TREATADULT", "TREATCHILD",  # Transition_2122

    # Household:
    "K9Q40",  # Smoking_2122
    "K9Q41",  # SmkInside_2122
    "FOODSIT",  # FoodSit_2122
    "K11Q60", "K11Q61", "K11Q62", "S9Q34", "EBTCARDS",  # FoodCash_2122
    "K10Q30", "K10Q31", "GOFORHELP",  # NbhdSupp_2122
    "K10Q40_R",  # NbhdSafe_2122
    "K10Q11", "K10Q12", "K10Q13", "K10Q14",  # NbhdAmenities_2122
    "K10Q20", "K10Q22", "K10Q23",  # NbhdDetract_2122
    "HHLANGUAGE",  # HHLanguage_2122
    "FAMCOUNT",  # FamCount_2122
    "A1_ACTIVE", "A2_ACTIVE",  # MilitarySt_2122

    # COVID RELATED:
    "VIDEOPHONECOVID",  # VideoCOVID_2122
    "COVIDCHECKUPS",  # PrevCOVID_2122
    "COVIDARRANGE",  # Childcare0to5COVID_2122, Childcare6to11COVID_2122
]

unique_features_to_drop = list(dict.fromkeys(related_features_to_drop))
print(f"Number of related features we're going to drop: {len(unique_features_to_drop)}")

# Here we'll drop the related features:
df_reduced.drop(columns=unique_features_to_drop, errors='ignore', inplace=True)
print("All features that are related to main features were successfully dropped!")
print("New shape of our dataset: ", df_reduced.shape)
