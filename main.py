import pandas as pd
from sklearn.linear_model import LinearRegression

while True:
    print("\n===== Utility Usage Prediction Tool =====")
    print("1. View Data")
    print("2. Add Data")
    print("3. Update Data")
    print("4. Predict Usage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            df = pd.read_csv("data.csv")
            print(df)

        elif choice == "2":
            month = int(input("Enter month: "))
            usage = int(input("Enter usage: "))

            df = pd.read_csv("data.csv")
            df.loc[len(df)] = [month, usage]
            df.to_csv("data.csv", index=False)

            print("Data added successfully!")

        elif choice == "3":
            month = int(input("Enter month to update: "))
            new_usage = int(input("Enter new usage: "))

            df = pd.read_csv("data.csv")

            if month in df["month"].values:
                df.loc[df["month"] == month, "usage"] = new_usage
                df.to_csv("data.csv", index=False)
                print("Data updated successfully!")
            else:
                print("Month not found!")

        elif choice == "4":
            df = pd.read_csv("data.csv")

            X = df[["month"]]
            y = df["usage"]

            model = LinearRegression()
            model.fit(X, y)

            future_month = int(input("Enter future month: "))

            future_df = pd.DataFrame(
                {"month": [future_month]}
            )

            prediction = model.predict(future_df)

            print(
                f"Predicted Usage: {prediction[0]:.2f}"
            )

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

    except Exception as e:
        print("Error:", e)