with a2:
    store = st.button("superstore data (small)")
    if store:
        auto = False
        netflix = False
        
        # cols = []
        # for i in data.columns:
        #     cols.append(i.lower().replace(" ","_"))
        # data.columns = cols
        # data = data.head(51)
        # data['order_date'] = pd.to_datetime(data['order_date'])

        # cols_to_drop = ["order_id","state","ship_date","region"]
        # for i in cols_to_drop:
        #     try:
        #         data = data.drop(columns = [i])
        #     except:
        #         pass

        # num_nan_values = 5
        # columns = ["region","product_name","customer_name","category"]
        # for i in columns:
        #     random_indices = np.random.choice(len(data), size=num_nan_values, replace=False)
        #     data.loc[random_indices, i] = np.nan

        # random_indices = np.random.choice(len(data), size=20, replace=False)
        # profit = []
        # for i in data["profit"]:
        #     profit.append(str(i))
        # data["profit"] = profit
        # for i in random_indices:
        #     data.loc[i, "profit"] = data.loc[i, "profit"].replace(".",",")

        # sales = []
        # for i in data["sales"]:
        #     i = str(i)+" €"
        #     sales.append(i)
        # data["sales"] = sales
        # data.to_csv("superstore_small.csv", index = False)

with a3:
    auto = st.button("car mpg (small)")
    if auto:
        store = False
        netflix = False
        
        # cols = []
        # for i in data.columns:
        #     cols.append(i.lower().replace(" ","_"))
        # data.columns = cols
        # data = data.head(51)
        # num_nan_values = 5
        # columns = ["brand","origin","cylinders"]
        # for i in columns:
        #     random_indices = np.random.choice(len(data), size=num_nan_values, replace=False)
        #     data.loc[random_indices, i] = np.nan

        # random_indices = np.random.choice(len(data), size=20, replace=False)
        # mpg = []
        # for i in data["mpg"]:
        #     mpg.append(str(i))
        # data["mpg"] = mpg
        # for i in random_indices:
        #     data.loc[i, "mpg"] = data.loc[i, "mpg"].replace(".",",")
        # model_year = []
        # for i in data["model_year"]:
        #     model_year.append(str(i))
        # data["model_year"] = model_year
        # for i in random_indices:
        #     data.loc[i, "model_year"] = data.loc[i, "model_year"].replace("0","00")
        # data.to_csv("car_mpg_small.csv", index = False)
    
with a4:
    netflix = st.button("netflix titles (small)")
    if netflix:
        store = False
        auto = False
        
        # data = data.head(51)
        # num_nan_values = 5
        # columns = ["title","director","country"]
        # for i in columns:
        #     random_indices = np.random.choice(len(data), size=num_nan_values, replace=False)
        #     data.loc[random_indices, i] = np.nan
        
        # random_indices = np.random.choice(len(data), size=20, replace=False)
        # release_year = []
        # for i in data["release_year"]:
        #     release_year.append(str(i))
        # data["release_year"] = release_year
        # for i in random_indices:
        #     data.loc[i, "release_year"] = data.loc[i, "release_year"].replace("20","30")
        # data.to_csv("netflix_titles_small.csv", index = False)