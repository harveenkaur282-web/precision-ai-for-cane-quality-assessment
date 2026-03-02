from sklearn.model_selection import train_test_split

def split_data(data):
    X = data.drop("pol_percentage", axis=1)
    y = data["pol_percentage"]
    
    return train_test_split(X, y, test_size=0.2, random_state=42)