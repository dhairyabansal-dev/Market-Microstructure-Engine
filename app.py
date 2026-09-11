"""Small Streamlit demo for the Market Microstructure Engine."""

import streamlit as st

from market_microstructure import (
    ExecutionModel,
    OrderBook,
    microprice,
    order_imbalance,
    quoted_spread,
    relative_spread,
)

st.set_page_config(page_title="Market Microstructure Engine", page_icon="📊", layout="wide")
st.title("Market Microstructure Engine")
st.caption("Simple interactive demo — order-book analytics and execution simulation")

st.sidebar.header("Order Book")
bid_size = st.sidebar.number_input("Best bid size", min_value=1.0, value=100.0)
ask_size = st.sidebar.number_input("Best ask size", min_value=1.0, value=50.0)
bid_price = st.sidebar.number_input("Best bid", min_value=0.01, value=99.0)
ask_price = st.sidebar.number_input("Best ask", min_value=0.01, value=101.0)
quantity = st.sidebar.number_input("Market order quantity", min_value=1.0, value=100.0)
side = st.sidebar.selectbox("Order side", ["buy", "sell"])

book = OrderBook()
book.update_bid(bid_price, bid_size)
book.update_bid(bid_price - 1, bid_size * 2)
book.update_ask(ask_price, ask_size)
book.update_ask(ask_price + 1, ask_size * 2)

metrics = st.columns(5)
metrics[0].metric("Mid price", f"{book.mid_price:.2f}")
metrics[1].metric("Spread", f"{quoted_spread(book):.2f}")
metrics[2].metric("Relative spread", f"{relative_spread(book) * 100:.2f}%")
metrics[3].metric("Microprice", f"{microprice(book):.4f}")
metrics[4].metric("Imbalance", f"{order_imbalance(book, 2):.2%}")

st.subheader("Order Book")
col1, col2 = st.columns(2)
with col1:
    st.write("**Bids**")
    st.dataframe(
        [{"Price": p, "Size": s} for p, s in sorted(book.bids.items(), reverse=True)],
        hide_index=True,
        use_container_width=True,
    )
with col2:
    st.write("**Asks**")
    st.dataframe(
        [{"Price": p, "Size": s} for p, s in sorted(book.asks.items())],
        hide_index=True,
        use_container_width=True,
    )

report = ExecutionModel().execute_market_order(book, side, quantity)
st.subheader("Execution Simulation")
exec_cols = st.columns(4)
exec_cols[0].metric("Filled", f"{report.filled_quantity:.2f}")
exec_cols[1].metric("Average price", f"{report.average_price:.2f}" if report.average_price else "—")
exec_cols[2].metric("Slippage", f"{report.slippage:.4f}" if report.slippage is not None else "—")
exec_cols[3].metric(
    "Implementation shortfall",
    f"{report.implementation_shortfall:.2f}" if report.implementation_shortfall is not None else "—",
)

st.info("This is a simplified research model. It consumes displayed liquidity only and is not a live trading simulator.")
