import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

def pregunta_01():

    return (tbl0.shape[0])

def pregunta_02():

    return (tbl0.shape[1])


def pregunta_03():

    return (tbl0.groupby("_c1").size())


def pregunta_04():

    return (tbl0.groupby("_c1").mean()["_c2"]) #ready


def pregunta_05():
 
    return (tbl0.groupby("_c1").max()["_c2"])


def pregunta_06():

    fourthColumn = tbl1["_c4"].unique()
    listCap = [x.upper() for x in fourthColumn]
    listCap.sort()
    return listCap


def pregunta_07():

    return (tbl0.groupby("_c1").sum()["_c2"])


def pregunta_08():
 
    df = tbl0
    df["suma"] = df["_c0"]+df["_c2"]
    return(df)


def pregunta_09():

    df = tbl0
    df["year"] = df["_c3"].apply(lambda x: x.split("-")[0])
    return df


def formatDataFrame(df):
    aux=sorted([i for i in df["_c2"]])
    aux=[str(i) for i in aux]
    return(":".join(aux))

def pregunta_10():

    total = tbl0.groupby("_c1").apply(formatDataFrame).to_frame().reset_index()
    total.rename(columns={0: "_c2"}, inplace=True)
    total.set_index("_c1", inplace=True)
    return (total)

def formatDataframe11(df):
    aux=sorted([i for i in df["_c4"]])
    aux=[str(i) for i in aux]
    return(",".join(aux))


def pregunta_11():

    ans =tbl1.groupby("_c0").apply(formatDataframe11).to_frame().reset_index()
    ans.rename(columns={0: "_c4"}, inplace=True)
    #ans.set_index("_c1", inplace=True)
    return (ans)


def pregunta_12():

    Joined=tbl2.set_index(["_c5a", "_c5b"]).groupby("_c0").groups
    dic={}
    for i in Joined.items():
        for j in sorted(i[1]):
            dic.setdefault(i[0],[]).append(f"{j[0]}:{j[1]}")
    return pd.DataFrame({"_c0":dic.keys(), "_c5":[",".join(value) for value in dic.values()]})


def pregunta_13():

    return((pd.merge(tbl2,tbl0).groupby("_c1").sum()["_c5b"]))