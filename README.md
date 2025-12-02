
# SKU Technology Mapper

This Streamlit app allows you to upload an Excel file containing SKUs and maps each SKU to a predefined technology category.

## Features
- Upload `.xlsx` file
- Replace SKU with technology category
- Download updated Excel file

## Deployment on Streamlit Cloud
1. Push `app.py` and `requirements.txt` to your GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub repo.
3. Select `app.py` as the main file.
4. Deploy and use the app online.

## Future Upgrade
To integrate real web search, add Bing API logic in `map_to_technology()`.
