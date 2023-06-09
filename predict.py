import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('subway_delay_gb.pkl', 'rb') as file:
        subway_delay_gb = pickle.load(file)
    return subway_delay_gb

subway_delay_gb = load_model()

gradientBoostModel = subway_delay_gb["model"]
# sc_Month = subway_delay_gb["sc_Month"]
# sc_DayOfMonth = subway_delay_gb["sc_DayOfMonth"]
# sc_Hour = subway_delay_gb["sc_Hour"]
# sc_Min_Gap = subway_delay_gb["sc_Min_Gap"]
DayOfWeek_encoder = subway_delay_gb["DayOfWeek_encoder"]
Station_encoder = subway_delay_gb["Station_encoder"]
Line_encoder = subway_delay_gb["Line_encoder"]

def show_predict():
    st.title("TTC Subway Delay Prediction")

    st.write("""### We need some information to predict the delay time""")

    Station = ('VICTORIA PARK STATION', 'HIGH PARK STATION', 'SHEPPARD STATION',
       'LANSDOWNE STATION', 'BLOOR STATION', 'DUFFERIN STATION',
       'NORTH YORK CTR STATION', 'QUEEN STATION', 'RUNNYMEDE STATION',
       'ST ANDREW STATION', 'WELLESLEY STATION', 'KIPLING STATION',
       'YONGE SHP STATION', 'ST PATRICK STATION', 'KENNEDY BD STATION',
       'JANE STATION', 'OLD MILL STATION', 'WILSON CARHOUSE',
       'SHEPPARD WEST STATION', 'BAY STATION', 'FINCH STATION',
       'COXWELL STATION', 'ST CLAIR WEST STATION', 'DUPONT STATION',
       'YORK MILLS STATION', 'DUNDAS WEST STATION', 'OSGOODE STATION',
       'COLLEGE STATION', 'YONGE BD STATION', 'ST GEORGE YUS STATION',
       'MCCOWAN STATION', 'BROADVIEW STATION', 'EGLINTON STATION',
       'ROSEDALE STATION', 'PAPE STATION', 'GREENWOOD STATION',
       'LAWRENCE EAST STATION', 'KENNEDY SRT STATION',
       'ISLINGTON STATION', 'WARDEN STATION', 'DAVISVILLE STATION',
       'LAWRENCE STATION', 'EGLINTON WEST STATION', 'KEELE STATION',
       'MIDLAND STATION', 'YONGE UNIVERSITY LINE', 'ELLESMERE STATION',
       'UNION STATION', 'CHESTER STATION', 'GLENCAIRN STATION',
       'WILSON STATION', 'YORKDALE STATION', 'MUSEUM STATION',
       'DAVISVILLE HOSTLER', 'LESLIE STATION', 'DUNDAS STATION',
       'SHERBOURNE STATION', 'BLOOR DANFORTH SUBWAY', 'KING STATION',
       'GREENWOOD YARD', 'BATHURST STATION', 'LAWRENCE WEST STATION',
       'DONLANDS STATION', 'BAYVIEW STATION', 'DON MILLS STATION',
       "QUEEN'S PARK STATION", 'SPADINA YUS STATION',
       'SUMMERHILL STATION', 'ROYAL YORK STATION', 'MAIN STREET STATION',
       'OSSINGTON STATION', 'CASTLE FRANK STATION',
       'ST GEORGE BD STATION', 'CHRISTIE STATION', 'SCARB CTR STATION',
       'WILSON HOSTLER', 'WOODBINE STATION', 'ST CLAIR STATION',
       'SPADINA BD STATION', 'MCCOWAN STATION TO KEN', 'WILSON YARD',
       'GREENWOOD PORTAL', 'DAVISVILLE YARD', 'GREENWOOD WYE',
       'TORONTO TRANSIT COMMIS', 'BESSARION STATION', 'MCBRIEN BUILDING',
       'RONCEVALLES DIVISION', 'MCCOWAN YARD', 'GREENWOOD CARHOUSE',
       'DAVISVILLE CARHOUSE', 'DANFORTH DIVISION', 'KEELE YARD',
       'GREENWOOD SHOP', 'TRANSIT CONTROL CENTRE', 'SHEPPARD LINE',
       'CHESTER TO BROADVIEW', 'KENNEDY STATION TO KIP',
       'RUSSELL HILL EMERGENCY', 'FINCH TO DOWNSVIEW',
       'EGLINTON TO LAWRENCE S', 'YUS/BD/SHEPPARD SUBWAY',
       'EGLINTON WEST TO BLOOR', 'FENMAR AND WESTON', 'DUPLEX AVENUE',
       'SYSTEM WIDE', 'GUNN BUILDING', 'BLOOR TO KING STATIONS',
       'YUS/BD/SRT', 'ST GEORGE TO LAWRENCE', 'CHESTER TO CASTLEFRANK',
       'LYTTON EMERGENCY EXIT', 'ASQUITH SUBSTATION', 'DUNCAN SHOP',
       'BLOOR TO YORK MILLS', 'PAPE TO ST GEORGE', 'BLOOR TO DAVISVILLE',
       'INGLIS BUILDING', 'FINCH TO LAWRENCE STAT', '(APPROACHING)',
       'DAVENPORT BUILDING', 'VARIOUS', 'CLANTON PARK EMERGENCY',
       'PRINCE EDWARD VIADUCT', 'MOORE GATE', 'PLANT OPS BLDG',
       'EGLINTON TO FINCH', 'BLOOR YONGE LINES', 'KIPLING STATION (ENTER',
       'UNION STATION (DOWNSVI', 'JANE STATION (APPROACH',
       'DOWNSVIEW STATION', 'WOODBINE STATION (LEAV',
       'KENNEDY BD STATION (AP', 'YONGE-UNIVERSITY AND B',
       'OLD MILL STATION (EXIT', 'YONGE-UNIVERSITY LINE',
       'OLD MILL STATION (APPR', 'ST GEORGE STATION',
       'DUPONT STATION (APPROA', 'YORK MILLS STATION (AP',
       'SHEPPARD SUBWAY LINE', 'DUNDAS STATION E/S 1',
       'ISLINGTON STATION (APP', 'KENNEDY STATION (PALTF',
       'HIGH PARK STATION (ENT', 'YONGE UNIVERSITY SUBWA',
       'WILSON STATION (APPROA', 'ROYAL YORK STATION (AP', 'KENNEDY',
       'MCCOWAN STATION (APPRO', 'KENNEDY SRT STATION (A',
       'DUPONT STATION (LEAVIN', 'UNION STATION (ST ANDR',
       'ST GEORGE BD STATION -', 'WELLESLEY STATION (APP',
       'WOODBINE STATION (APPR', 'KIPLING STATION (LEAVI',
       'DOWNSVIEW STATION PLAT', 'ROYAL YORK STATION (LE',
       'ST CLAIR STATION (APPR', 'DAVISVILLE STATION - L',
       'YONGE - UNIVERSITY SUB', 'YORK MILLS STATION (LE',
       'DUNDAS STATION - EAST', 'KENNEDY BD STATION PLA',
       'UNION STATION (TO ST A', 'WARDEN STATION (LEAVIN',
       'KEELE STATION (APPROAC', 'YONGE UNIVESITY AND BL',
       'DONLANDS TO KIPLING ST', 'KIPLING STATION (APPRO',
       'SCARBOROUGH RAPID TRAN', 'SHEPPARD STATION (ENTE',
       'GLENCAIRN STATION (APP', 'KEELE STATION (EXITING', 'OSGOODE',
       'ROSEDALE STATION (APP', 'QUEEN STATION - EAST S',
       'KIPLING STATION (PLATF', 'COXWELL STATION (ENTER',
       'ST CLAIR WEST CENTRE T', 'CHESTER STATION (ENTER',
       'DUNDAS STATION - W/S', 'KENNEDY SRT STATION [A',
       'FINCH STATION BOOTH 2', 'YONGE-UNIVERSITY/BLOOR',
       'YONGE-UNIVERSITY SUBWA', 'ROYAL YORK STATION (EN',
       'YONGE STATION', 'CHRISTIE STATION (APPR', 'KENNEDY STATION',
       'KENNEDY BD STATION (EN', 'DUNDAS WEST STATION (A',
       'BLOOR-DANFORTH SUBWAY', 'YONGE UNIVERSITY',
       'EGLINTON STATION (APPR', 'JANE STATION (ENTERING',
       'LAWRENCE STATION (LEAV', 'ST ANDREW STATION (LEA',
       'DONLANDS STATION (APPR', 'SPADINA STATION',
       'WOODBINE STATION (EXIT', 'MCCOWAN STATION (DEPAR',
       'KENNEDY SRT STATION (E', 'FINCH STATION (APPROAC',
       'BLOOR/DANFORTH LINE', 'YONGE/UNIVERSITY - BLO',
       'SHERBOURNE STATION (EN', 'YONGE - UNIVERSITY LIN',
       'SHERBOURNE STATION (AP', 'KENNEDY BD STATION (EX',
       'GLENACAIRN STATION (AP', 'OSSINGTON STATION (APP',
       'BLOOR DANFORTH/YONGE U', 'KEELE STATION (CROSSIN',
       'ISLINGTON STATION (ENT', 'FINCH STATION (EXITING',
       'FINCH STATION (PLATFOR', 'DUPONT STATION (EXITIN',
       'YONGE STATION (EXITING', 'KENNEDY SRT STATION TO',
       'EGLINTON STATION (EXIT', 'YORKDALE STATION (EXIT',
       'YONGE/UNIVERSITY', 'FINCH STATION (LEAVING',
       'OSSINGTON STATION (EXI', 'BLOOR DANFORTH LINE',
       'DOWNSVIEW PARK STATION', 'LEAVING KENNEDY STATIO',
       'COXWELL STATION (LEAVI', 'ENTERING LESLIE STATIO',
       'SCARB CENTRE STATION', 'KENNEDY PLATFORM 1',
       'YONGE/UNIVERSITY LINE', 'FULL LINE', 'BLOOR STATION (STATION',
       'HIGH PARK STATION (APP', 'ISLINGTON STATION (LEA',
       'YONGE SHP STATION (LEA', 'DUNDAS STATION E/S', 'ST GEORGE STN',
       'DUNDAS STATION (W/S)', 'DONLANDS STATION (ENTE',
       'JANE STATION (EXITING)', 'COXWELL STATION (EXITI',
       'MUSEUM STATION (APPROA', 'KENNEDY BD STATION (LE',
       'KEELE STATION (ENTERIN', 'MCCOWAN STATION (ENTER',
       'KENNEDY SRT STATION (L', 'MUSEUM STATION (LEAVIN',
       'SHEPPARD STATION (APPR', 'ELLESMERE STATION DEPA',
       'DUNDAS STATION - WEST', 'YONGE-UNIVERSITY SUBW',
       'KIPLING STATION (EXITI', 'ISLINGTON STATION (EXI',
       'KENNEDY BD STATION (PL', 'UNION STATION (APPROAC',
       'ROSEDALE STATION (APPR', 'CHRISTIE STATION (LEAV',
       'BLOOR - DANFORTH LINE', 'UNION TO KING', 'BROADVIEW TO SHERBOURN',
       'UNION STATION (ENTERIN', 'BROADVIEW TO YONGE STA',
       '169 DANFORTH AVENUE', 'BROADVIEW AND DANFORTH',
       'WARDEN STATION (APPR', 'ST CLAIR STATION - UPP',
       'BROADVIEW TO ST GEORGE', 'DUPONT STATION ( APPRO',
       'ST CLAIR STATION PLEAS', 'CHESTER STATION (LEAVI',
       'LESLIE STATION APROACH', 'UNION STATION - SALES',
       'UNION STATION - BOOTH', 'ISLINGTON STATION ( AP',
       'KENNEDY BD STATION ( A', 'DUPONT STATION APPROAC',
       'WILSON STATION (EXITIN', 'ST CLAIR WEST', 'BAY LOWER',
       'VAUGHAN MC STATION', 'PIONEER VILLAGE STATIO',
       'YONGE UNIVERSITY AND B', 'FINCH WEST STATION',
       'YORK UNIVERSITY STATIO', 'HIGHWAY 407 STATION',
       'YONGE - UNIVERSITY BLO', 'KIPLING STATION TO KEN', 'TYSSE LINE',
       'SHEPPARD WEST MIGRATI', 'UNION TO ST GEORGE',
       'LAWRENCE EAST TO ELLES', 'SUBWAY OPS BUILDING',
       'EGLINTON WEST TO VMC', 'WARDEN TO KENNEDY STAT',
       'WELLBECK EMERGENCY', 'GREENWOOD TRACK AND ST', 'GREENWOOD SHOPS',
       'GO PROTOCOL - BARRIE L', 'SRT LINE', 'DAVISVILLE BUILD UP',
       'CHANGE OVERS / GENERAL', 'YONGE SHEP STATION',
       'YONGE-UNIVERSITY & BLO', 'KENNEDY BD TO KIPLING',
       'SCARBOROUGH CTR STATIO', 'NORTH YORK CENTRE STAT',
       'DAVISVILLE TO EGLINTON', 'DUPONT TO ST CLAIR WES',
       'YONGE/UNIVERSITY SUBWA', 'DAVISVILLE BUILD-UP',
       'GREENWOOD COMPLEX', 'UNION TO KING STATION',
       'YONGE UNIVERSTY SUBWAY', 'ST ANDREW TO SPADINA',
       'MUSEUM TO FINCH STATIO', 'WILSON TRAINING BUILDI',
       'SPADINA TO ST ANDREW', 'EASTBOUND - BETWEEN SH',
       'YORK MILLS CENTER TRAC', 'SHEPPARD-YONGE STATION', 'LINE 1',
       'YONGE UNIVERSITY/BLOOR', 'MCCOWAN YARD - 3 TRACK',
       'ST GEORGE YU STATION', 'YONGE/UNIVERSITY AND B',
       'FINCH TO EGLINTON STAT', 'WILSON DIVISION',
       'YORK MILLS CENTRE TRAC', 'YONGE / UNIVERSITY - B',
       'FINCH TO SHEPPARD STAT', 'YONGE/UNIVERSITY-SPADI',
       'EGLINTON STATION (MIGR', 'LAWRENCE EAST TO KENNE',
       'UNION STATION TO ST AN', 'TORONTO TRANSIC COMMIS',
       'SHEPPARD DISTRUBTION', 'BAYVIEW TO BESSARION',
       'WILSON TO ST CLAIR STA', 'SHEPPARD WEST TO UNION',
       'MAINLINE STORAGE', 'SHEPPARD WEST TO ST CL', 'KIPLING TO JANE',
       'YORK MILLS (APPROACHIN', 'TRANSIT CONTROL', 'NORTH HOSTLER',
       'WILSON NORTH HOSTLER', 'MCCOWAN CARHOUSE',
       'MIDLAND TO SCARBOROUGH', 'ST CLAIR TO FINCH STAT',
       "QUEEN'S QUAY - UNION", 'MCCOWAN TO KENNEDY STA',
       'FINCH STATION TO EGLIN', 'EGLINTON PSUDO STATION',
       'N/O SUMMERHILL TO S/O', 'DOWNVIEW PARK STATION',
       'MUSEUM TO EGLINTON STA', 'UNION STATION TO KING',
       'UNION STATION TOWARDS', 'YONGE-UNIVERSITY-SPADI',
       'N/B TOWARDS FINCH', 'WARDEN AND ST CLAIR',
       'BROADVIEW CENTRE TRACK', 'VMC TO LAWRENCE',
       'EGLINTON (MIGRATION)', 'YONGE-UNIVERSITY SPADI',
       'UNION STATION(TOWARD K', 'LINE 3 - SCARBOROUGH R',
       'ST. GEORGE STATION', 'YONGE UNIVERSITY SPADI',
       'GLENCARIN STATION', 'UNION STATION (TO KING',
       'LAWRENCE TO ST CLAIR S', 'BAY LOWER STATION',
       'SCARBOROUGH CENTRE STA', 'SHEPPARD-YONGE LINE 4',
       'GUNN BUILDING - 3RD FL', 'WILSON SOUTH HOSTLER',
       'KING TO COLLEGE', 'COLLEGE TO KING', 'DUFFERIN AND BLOOR',
       'YONGE STATION TO GREEN', 'MIGRATION POINT EGLINT',
       'LAWRECNE WEST TO FINCH', 'BLOOR-DANFORTH LINE',
       'LAWRENCE WEST TO FINCH', 'SHEPPARD-YONGE AND DON',
       'GLENAYR EMERGENCY EXIT', 'BROADVIEW TO WOODBINE',
       'KENNEDY SRT STATION LA', 'VICTORIA PARK TO WARDE',
       'WOODBINE TO BROADVIEW', 'CHESTER CENTRE TRACK',
       'ST ANDREW STATON', 'CLOSURE FINCH TO ST CL',
       'KENNEDY TO LAWRENCE EA', 'JANE TO OSSINGTON STAT',
       'WILSON YARD CARHOUSE', 'EGLINTON MIGRATION',
       'EGLINTON BUS TERMINAL', 'LAWRENCE STATION TO ST',
       'LAWRENCE TO ST.CLAIR S', 'ST GEORGE STATION TO B',
       'DUNDAS WEST TO KEELE S', 'YONGE-SHEPPARD STATION',
       'MAIN STREET STATION (E', 'LINE 1 BLOOR TO QUEEN',
       'OSSINGTON CENTRE TRACK', 'YONGE/SHEPPARD',
       'MAIN TO VICTORIA PARK', 'EATON CENTRE - DUNDAS',
       'WILSON TRACK & STRUCTU', 'LINE 3 - KENNEDY TO LA',
       'ST GEORGE TO BROADVIEW', 'YONGE AND BLOOR',
       'LINE 1 YONGE-UNIVERSIT', 'UNION STATION TO FINCH',
       'YONGE-UNIVERSITY', 'ALL OPEN CUTS', 'KIPLING TO KENNEDY STA',
       'SHEPPARD TO ST CLAIR S', 'SHEPPARD WEST TO WILSO',
       'GREENWOOD COMPLEX - TR', 'UNION TO SHEPPARD WEST',
       'EGLINTON MIGRATION POI', 'LINE 3 SCARBOROUGH SRT',
       'TORONTO TRANSIT CONTRO', 'ST CLAIR TO LAWRENCE S',
       'YONGE / UNIVERSITY / S', 'EATON CENTRE', 'WILSON TO LAWRENCE WES',
       'KENNEDY STATION TO WOO', 'WOODBINE STATION TO KE', 'VIADUCT',
       'KENNEDY TO MAIN STREET', 'WOODBINE TO KENNEDY ST',
       'YUS AND BLOOR DANFORTH', 'FINCH TO ST CLAIR STAT',
       'KENNEDY SRT STATION -', 'SUMMERHILL TO BLOOR', 'MIGRATION POINT',
       'KENNEDY SRT TO LAWRENC', 'PIONEER VILLAGE TO VAU',
       'CHRISTIE - ST GEORGE S', 'LINE 3 - KENNEDY TO MC',
       'SCARBOROUGH RAPID LINE', 'WILSON YARD HOSTLER 2',
       'DAVISVILLE BUILDUP', 'CASTLE FRANK - BROADVI', 'LINE 3 SRT',
       'SUMMER HILL STATION', 'YONGE', 'LINE 1 YONGE UNIVERSIT',
       'UNION STATION (TOWARDS', 'DAVISVILLE CAR HOUSE',
       'GREENWOOD CAR HOUSE', 'UNION STATION - ST AND',
       'MC COWAN STATION', 'UNION STATION - KING',
       'HIGH PARK TO KEELE STA', 'KIPLING TO ISLINGTON',
       'LANSDOWNE STATION AND', 'DUPONT STATION TO SPAD', 'UNION - KING',
       'GREENWOOD WYE DEPARTIN', 'KENNEDY SRT AND LAWREN', 'STATION',
       'EGLINTON TO FINCH STAT', 'YONGE/UNIVERSITY - LIN',
       'BETWEEN SHEPPARD AND S', 'SOUTH BOUND SOUTH OF L',
       'WILSON GARAGE', 'WILSON HOLSER', 'YONGE- UNIVERSITY AND',
       'BLOOR/DANFORTH AND YON', 'MUSEUM ( TUNNEL)',
       'ISLINGTON TO LANSDOWN', 'QUEENS PARK STATION')

    Line = ('BD', 'YU', 'SHP', 'SRT', 'BD LINE', 'BD/YUS',
       'BLOOR DANFORTH', '31 GREENWOOD', '60', '9 BELLAMY', '45 KIPLING',
       '504', '95 YORK MILLS', '500', 'SHEPPARD', '104 FAYWOOD', 'YU/BD',
       '60 STEELES WEST', '25 DON MILLS', '555', '36 FINCH WEST',
       '126 CHRISTIE', '37 ISLINGTON', '504 KING', '29 DUFFERIN',
       '116 MORNINGSIDE', 'BD/YU', '73 ROYAL YORK', 'BLOOR DANFORTH LINE',
       'YU/SHEP', '66', '341 KEELE', '510 SPADINA', '11 BAYVIEW',
       '63 OSSINGTON', '32 EGLINTON WEST', '129 MCCOWAN NORTH', 'YU / BD',
       'YU/ BD', 'YU-BD', 'BLOOR DANFORTH LINES', 'YUS', 'B/D', '999',
       'YONGE/UNIVERSITY/BLOOR', 'Y/BD', 'YU/BD LINES', 'YU & BD',
       'YUS AND BD', 'YUS/BD', '69 WARDEN SOUTH', 'YU/BD LINE',
       'LINE 2 SHUTTLE', '57 MIDLAND', '96 WILSON', '506 CARLTON'
    )

    DayofWeek = ('Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday')



    Station = st.selectbox("Station", Station)
    Line = st.selectbox("Subway Line", Line)
    DayofWeek = st.selectbox("Day of the Week", DayofWeek)
    Month = st.slider("Month", 1, 12)
    DayofMonth = st.slider("Day of the Month", 1, 31)
    Hour = st.slider("Hour", 1, 24)
    Min_Gap = st.slider("Minimum Gap", 1, 999)
   

    ok = st.button("Calculate Minimum Delay Time")
    if ok:
        X = np.array([[Station, Line, DayofWeek, Month, DayofMonth, Hour, Min_Gap]])
        X[:,0] = Station_encoder.transform(X[:,0])
        X[:,1] = Line_encoder.transform(X[:,1])
        X[:,2] = DayOfWeek_encoder.transform(X[:,2])
        X[:,3] = sc_Month.transform(X[:,3])
        X[:,4] = sc_DayOfMonth.transform(X[:,4])
        X[:,5] = sc_Hour.transform(X[:,5])
        # # X[:,6] = sc_Min_Gap.transform(X[:,6])
        # X_St_ndarray = X[:,0].values
        # X_St_2D = X_St_ndarray.reshape(-1, 1)
        # X[:,0] = Station_encoder.transform(X_St_2D)
        # X_Ln_ndarray = X[:,1].values
        # X_Ln_2D = X_Ln_ndarray.reshape(-1, 1)
        # X[:,1] = Line_encoder.transform(X_Ln_2D)
        # X_dof_ndarray = X[:,2].values
        # X_dof_2D = X_dof_ndarray.reshape(-1, 1)
        # X[:,2] = DayOfWeek_encoder.transform(X_dof_2D)
        X = X.astype(float)

        Minimum_Delay = gradientBoostModel.predict(X)
        st.subheader(f"The estimated minimum delay in trains is ${Minimum_Delay} minutes.")

