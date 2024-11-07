import pandas as pd
import streamlit as st

data = pd.read_csv('/Users/i39986/Desktop/mnd/assignment_mnd/project/scores.csv') 
articles_data = pd.read_csv('/Users/i39986/Desktop/mnd/assignment_mnd/project/articles_xformed.csv')

st.title("Journalist Recommendation Powered by Gemma-2")
st.write("Select a newsroom to view top journalists and their relevant works")

newsrooms = sorted(data['newsroom'].unique())
selected_newsroom = st.selectbox("Choose a Newsroom:", newsrooms)

if selected_newsroom:
    filtered_data = data[data['newsroom'] == selected_newsroom]
    top_journalists = filtered_data.nlargest(3, 'score')

    for _, row in top_journalists.iterrows():
        journalist_email = row['journalist_email']
        
        st.markdown(
            f"""
            <h3 style='color: #4CAF50; margin-bottom: 5px;'>Journalist: {journalist_email}</h3>
            <p><strong>Score:</strong> {row['score']}</p>
            <p><strong>Reasons:</strong> {row['newsroom']}</p>
            <hr style="border: none; border-top: 1px solid #eee;" />
            """,
            unsafe_allow_html=True
        )

        journalist_articles = articles_data[articles_data['journalist_email'] == journalist_email].head(3)
        
        st.markdown("**Relevant Works:**")
        for _, article in journalist_articles.iterrows():
            st.markdown(
                f"""
                <div style='margin-bottom: 15px;'>
                    <p><strong>Headline:</strong> {article['headline']}</p>
                    <p><strong>Text:</strong> {article['text']}</p>
                    <p><strong>Style:</strong> {article['analysis_journalist']}</p>
                    <p><strong>Purpose:</strong> {article['analysis_notivation']}</p>
                    <p><strong>Relevant Event Around the Publish Date:</strong> {article['relevant_event']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


    st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>Designed by Vaibhav Saxena for MyNewsDesk</p>", unsafe_allow_html=True)


