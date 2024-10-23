# import datetime
# import random

# import altair as alt
# import numpy as np
# import pandas as pd
# import streamlit as st

# # Show app title and description.
# st.set_page_config(page_title="Support tickets", page_icon="🎫")
# st.title("🎫 Support tickets")
# st.write(
#     """
#     This app shows how you can build an internal tool in Streamlit. Here, we are 
#     implementing a support ticket workflow. The user can create a ticket, edit 
#     existing tickets, and view some statistics.
#     """
# )

# # Create a random Pandas dataframe with existing tickets.
# if "df" not in st.session_state:

#     # Set seed for reproducibility.
#     np.random.seed(42)

#     # Make up some fake issue descriptions.
#     issue_descriptions = [
#         "Network connectivity issues in the office",
#         "Software application crashing on startup",
#         "Printer not responding to print commands",
#         "Email server downtime",
#         "Data backup failure",
#         "Login authentication problems",
#         "Website performance degradation",
#         "Security vulnerability identified",
#         "Hardware malfunction in the server room",
#         "Employee unable to access shared files",
#         "Database connection failure",
#         "Mobile application not syncing data",
#         "VoIP phone system issues",
#         "VPN connection problems for remote employees",
#         "System updates causing compatibility issues",
#         "File server running out of storage space",
#         "Intrusion detection system alerts",
#         "Inventory management system errors",
#         "Customer data not loading in CRM",
#         "Collaboration tool not sending notifications",
#     ]

#     # Generate the dataframe with 100 rows/tickets.
#     data = {
#         "ID": [f"TICKET-{i}" for i in range(1100, 1000, -1)],
#         "Issue": np.random.choice(issue_descriptions, size=100),
#         "Status": np.random.choice(["Open", "In Progress", "Closed"], size=100),
#         "Priority": np.random.choice(["High", "Medium", "Low"], size=100),
#         "Date Submitted": [
#             datetime.date(2023, 6, 1) + datetime.timedelta(days=random.randint(0, 182))
#             for _ in range(100)
#         ],
#     }
#     df = pd.DataFrame(data)

#     # Save the dataframe in session state (a dictionary-like object that persists across
#     # page runs). This ensures our data is persisted when the app updates.
#     st.session_state.df = df


# # Show a section to add a new ticket.
# st.header("Add a ticket")

# # We're adding tickets via an `st.form` and some input widgets. If widgets are used
# # in a form, the app will only rerun once the submit button is pressed.
# with st.form("add_ticket_form"):
#     issue = st.text_area("Describe the issue")
#     priority = st.selectbox("Priority", ["High", "Medium", "Low"])
#     submitted = st.form_submit_button("Submit")

# if submitted:
#     # Make a dataframe for the new ticket and append it to the dataframe in session
#     # state.
#     recent_ticket_number = int(max(st.session_state.df.ID).split("-")[1])
#     today = datetime.datetime.now().strftime("%m-%d-%Y")
#     df_new = pd.DataFrame(
#         [
#             {
#                 "ID": f"TICKET-{recent_ticket_number+1}",
#                 "Issue": issue,
#                 "Status": "Open",
#                 "Priority": priority,
#                 "Date Submitted": today,
#             }
#         ]
#     )

#     # Show a little success message.
#     st.write("Ticket submitted! Here are the ticket details:")
#     st.dataframe(df_new, use_container_width=True, hide_index=True)
#     st.session_state.df = pd.concat([df_new, st.session_state.df], axis=0)

# # Show section to view and edit existing tickets in a table.
# st.header("Existing tickets")
# st.write(f"Number of tickets: `{len(st.session_state.df)}`")

# st.info(
#     "You can edit the tickets by double clicking on a cell. Note how the plots below "
#     "update automatically! You can also sort the table by clicking on the column headers.",
#     icon="✍️",
# )

# # Show the tickets dataframe with `st.data_editor`. This lets the user edit the table
# # cells. The edited data is returned as a new dataframe.
# edited_df = st.data_editor(
#     st.session_state.df,
#     use_container_width=True,
#     hide_index=True,
#     column_config={
#         "Status": st.column_config.SelectboxColumn(
#             "Status",
#             help="Ticket status",
#             options=["Open", "In Progress", "Closed"],
#             required=True,
#         ),
#         "Priority": st.column_config.SelectboxColumn(
#             "Priority",
#             help="Priority",
#             options=["High", "Medium", "Low"],
#             required=True,
#         ),
#     },
#     # Disable editing the ID and Date Submitted columns.
#     disabled=["ID", "Date Submitted"],
# )

# # Show some metrics and charts about the ticket.
# st.header("Statistics")

# # Show metrics side by side using `st.columns` and `st.metric`.
# col1, col2, col3 = st.columns(3)
# num_open_tickets = len(st.session_state.df[st.session_state.df.Status == "Open"])
# col1.metric(label="Number of open tickets", value=num_open_tickets, delta=10)
# col2.metric(label="First response time (hours)", value=5.2, delta=-1.5)
# col3.metric(label="Average resolution time (hours)", value=16, delta=2)

# # Show two Altair charts using `st.altair_chart`.
# st.write("")
# st.write("##### Ticket status per month")
# status_plot = (
#     alt.Chart(edited_df)
#     .mark_bar()
#     .encode(
#         x="month(Date Submitted):O",
#         y="count():Q",
#         xOffset="Status:N",
#         color="Status:N",
#     )
#     .configure_legend(
#         orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
#     )
# )
# st.altair_chart(status_plot, use_container_width=True, theme="streamlit")

# st.write("##### Current ticket priorities")
# priority_plot = (
#     alt.Chart(edited_df)
#     .mark_arc()
#     .encode(theta="count():Q", color="Priority:N")
#     .properties(height=300)
#     .configure_legend(
#         orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
#     )
# )
# st.altair_chart(priority_plot, use_container_width=True, theme="streamlit")


import streamlit as st
import pandas as pd

# 데이터 정의
apple_data = {
    'hongro': {
        'name': '홍로',
        'quantity': 3064,
        'prices': [
            {'grade': '특2', 'quantity': 5, 'highest': 39000, 'lowest': 29900, 'average': 37180},
            {'grade': '특3', 'quantity': 81, 'highest': 56900, 'lowest': 21100, 'average': 49089},
            {'grade': '특4', 'quantity': 300, 'highest': 86000, 'lowest': 14900, 'average': 67292},
            {'grade': '특5', 'quantity': 403, 'highest': 96600, 'lowest': 15000, 'average': 63896},
            {'grade': '특6', 'quantity': 380, 'highest': 85900, 'lowest': 13300, 'average': 59890},
            {'grade': '특7', 'quantity': 276, 'highest': 70800, 'lowest': 13100, 'average': 59560},
            {'grade': '특8', 'quantity': 139, 'highest': 60000, 'lowest': 13100, 'average': 57106},
            {'grade': '상1', 'quantity': 263, 'highest': 45500, 'lowest': 13300, 'average': 35902},
            {'grade': '상2', 'quantity': 372, 'highest': 51600, 'lowest': 11500, 'average': 39017},
            {'grade': '상3', 'quantity': 201, 'highest': 44900, 'lowest': 11100, 'average': 33381},
            {'grade': '등외', 'quantity': 222, 'highest': 51200, 'lowest': 10000, 'average': 43192},
            {'grade': '보1', 'quantity': 422, 'highest': 20100, 'lowest': 8800, 'average': 14799}
        ]
    },
    'shinanoGold': {
        'name': '시나노골드',
        'quantity': 3256,
        'prices': [
            {'grade': '특2', 'quantity': 2, 'highest': 46900, 'lowest': 46900, 'average': 46900},
            {'grade': '특3', 'quantity': 154, 'highest': 64000, 'lowest': 46900, 'average': 55391},
            {'grade': '특4', 'quantity': 587, 'highest': 74300, 'lowest': 44700, 'average': 59111},
            {'grade': '특5', 'quantity': 709, 'highest': 83300, 'lowest': 41100, 'average': 60697},
            {'grade': '특6', 'quantity': 497, 'highest': 75000, 'lowest': 35000, 'average': 55251},
            {'grade': '특7', 'quantity': 253, 'highest': 66900, 'lowest': 25200, 'average': 48738},
            {'grade': '특8', 'quantity': 96, 'highest': 50000, 'lowest': 37100, 'average': 42382},
            {'grade': '상1', 'quantity': 414, 'highest': 53900, 'lowest': 17000, 'average': 47845},
            {'grade': '상2', 'quantity': 366, 'highest': 55000, 'lowest': 14900, 'average': 38673},
            {'grade': '상3', 'quantity': 76, 'highest': 45900, 'lowest': 12900, 'average': 32187},
            {'grade': '등외', 'quantity': 1, 'highest': 11600, 'lowest': 11600, 'average': 11600},
            {'grade': '보1', 'quantity': 107, 'highest': 29300, 'lowest': 11100, 'average': 18524}
        ]
    },
    'nomuraGold': {
        'name': '노무라골드',
        'quantity': 117,
        'prices': [
            {'grade': '특3', 'quantity': 1, 'highest': 48900, 'lowest': 48900, 'average': 48900},
            {'grade': '특4', 'quantity': 17, 'highest': 52900, 'lowest': 52900, 'average': 52900},
            {'grade': '특5', 'quantity': 34, 'highest': 58900, 'lowest': 58900, 'average': 58900},
            {'grade': '특6', 'quantity': 30, 'highest': 58900, 'lowest': 58900, 'average': 58900},
            {'grade': '특7', 'quantity': 13, 'highest': 43900, 'lowest': 43900, 'average': 43900},
            {'grade': '특8', 'quantity': 5, 'highest': 38900, 'lowest': 38900, 'average': 38900},
            {'grade': '상1', 'quantity': 3, 'highest': 48900, 'lowest': 48900, 'average': 48900},
            {'grade': '상2', 'quantity': 10, 'highest': 49900, 'lowest': 49900, 'average': 49900},
            {'grade': '상3', 'quantity': 1, 'highest': 40000, 'lowest': 40000, 'average': 40000},
            {'grade': '등외', 'quantity': 1, 'highest': 36900, 'lowest': 36900, 'average': 36900},
            {'grade': '보1', 'quantity': 2, 'highest': 25900, 'lowest': 25900, 'average': 25900}
        ]
    },
    'arisu': {
        'name': '아리수',
        'quantity': 880,
        'prices': [
            {'grade': '특3', 'quantity': 37, 'highest': 108900, 'lowest': 60100, 'average': 100986},
            {'grade': '특4', 'quantity': 103, 'highest': 126600, 'lowest': 33000, 'average': 93873},
            {'grade': '특5', 'quantity': 89, 'highest': 135500, 'lowest': 20000, 'average': 68842},
            {'grade': '특6', 'quantity': 42, 'highest': 120000, 'lowest': 15000, 'average': 43419},
            {'grade': '특7', 'quantity': 20, 'highest': 68900, 'lowest': 13300, 'average': 32200},
            {'grade': '특8', 'quantity': 4, 'highest': 30100, 'lowest': 19900, 'average': 27250},
            {'grade': '상1', 'quantity': 210, 'highest': 53900, 'lowest': 17000, 'average': 47845},
            {'grade': '상2', 'quantity': 211, 'highest': 63000, 'lowest': 14900, 'average': 38673},
            {'grade': '상3', 'quantity': 76, 'highest': 46900, 'lowest': 12900, 'average': 32187},
            {'grade': '등외', 'quantity': 25, 'highest': 35100, 'lowest': 11200, 'average': 21264},
            {'grade': '보1', 'quantity': 63, 'highest': 29300, 'lowest': 11100, 'average': 18524}
        ]
    },
    'gamhong': {
        'name': '감홍',
        'quantity': 1078,
        'prices': [
            {'grade': '특2', 'quantity': 7, 'highest': 116900, 'lowest': 60100, 'average': 76186},
            {'grade': '특3', 'quantity': 121, 'highest': 152000, 'lowest': 59900, 'average': 125284},
            {'grade': '특4', 'quantity': 192, 'highest': 169400, 'lowest': 59900, 'average': 115133},
            {'grade': '특5', 'quantity': 79, 'highest': 129000, 'lowest': 49900, 'average': 97592},
            {'grade': '특6', 'quantity': 20, 'highest': 100000, 'lowest': 40000, 'average': 90860},
            {'grade': '특7', 'quantity': 3, 'highest': 89900, 'lowest': 65900, 'average': 81900},
            {'grade': '상1', 'quantity': 414, 'highest': 114900, 'lowest': 41900, 'average': 80452},
            {'grade': '상2', 'quantity': 123, 'highest': 96900, 'lowest': 36600, 'average': 78876},
            {'grade': '상3', 'quantity': 11, 'highest': 68900, 'lowest': 36900, 'average': 57264},
            {'grade': '등외', 'quantity': 1, 'highest': 11600, 'lowest': 11600, 'average': 11600},
            {'grade': '보1', 'quantity': 107, 'highest': 49900, 'lowest': 28000, 'average': 37478}
        ]
    }
}

def main():
    st.set_page_config(page_title="안동농협공판장 사과 시세표", layout="wide")
    
    st.title("2024년 10월 4일")
    st.header("안동농협공판장 사과 시세표")
    
    # 품종 선택
    variety_names = {key: data['name'] for key, data in apple_data.items()}
    selected_variety = st.selectbox(
        "품종 선택",
        options=list(variety_names.keys()),
        format_func=lambda x: variety_names[x]
    )
    
    # 선택된 품종의 데이터 표시
    variety_data = apple_data[selected_variety]
    
    # 반입량 표시
    st.markdown(f"### {variety_data['name']} 반입량: **:green[{variety_data['quantity']:,} 상자]**")
    
    # DataFrame 생성
    df = pd.DataFrame(variety_data['prices'])
    
    # 가격 포맷팅 함수
    def format_price(x):
        return f"{x:,}"
    
    # 데이터프레임 스타일링
    styled_df = pd.DataFrame({
        '등급': df['grade'],
        '규격': ['박스 20kg'] * len(df),
        '수량': df['quantity'].apply(format_price),
        '최고가': df['highest'].apply(format_price),
        '최저가': df['lowest'].apply(format_price),
        '평균가': df['average'].apply(format_price)
    })
    
    # 테이블 표시
    st.dataframe(
        styled_df,
        column_config={
            '등급': st.column_config.TextColumn('등급', width='small'),
            '규격': st.column_config.TextColumn('규격', width='small'),
            '수량': st.column_config.TextColumn('수량', width='small'),
            '최고가': st.column_config.TextColumn('최고가', width='medium'),
            '최저가': st.column_config.TextColumn('최저가', width='medium'),
            '평균가': st.column_config.TextColumn('평균가', width='medium'),
        },
        hide_index=True,
        use_container_width=True
    )

    # 가격 분포 차트
    st.subheader("등급별 가격 분포")
    chart_data = pd.DataFrame({
        '등급': df['grade'],
        '최고가': df['highest'],
        '평균가': df['average'],
        '최저가': df['lowest']
    })
    st.line_chart(chart_data.set_index('등급'))

if __name__ == "__main__":
    main()