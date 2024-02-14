import streamlit as st
from calculation_module import calculate_reemployment_allowance

# アプリのタイトルを設定
st.title('再就職手当計算アプリ')

# ユーザー入力
st.header('入力情報')
age = st.number_input('年齢', min_value=0, step=1)
basic_allowance_daily = st.number_input('基本手当日額（円）', min_value=0)
prescribed_benefit_days = st.number_input('所定給付日数', min_value=0, step=1)
remaining_payment_days = st.number_input('支給残日数', min_value=0, step=1)

# 計算ボタン
if st.button('計算'):
    # 再就職手当と所定給付日数割合を計算
    reemployment_allowance, benefit_days_ratio = calculate_reemployment_allowance(age, basic_allowance_daily, prescribed_benefit_days, remaining_payment_days)
    
    # 結果を表示
    st.header('計算結果')
    st.write(f'再就職手当は、{int(reemployment_allowance):,}円です。')
    st.write(f'所定給付日数割合は、{int(benefit_days_ratio * 100)}%です。')
    
st.markdown("#### 支給額")
st.markdown("""
| 条件 | 計算式 |
| --- | --- |
| 支給残日数が所定給付日数の2/3以上 | 基本手当日額 × 支給残日数 × 70% |
| 支給残日数が所定給付日数の1/3以上 | 基本手当日額 × 支給残日数 × 60% |
""")

st.markdown("#### 基本手当日額の上限額")
st.markdown("""
| 年齢 | 基本手当日額の上限額 |
| --- | --- |
| 60歳未満 | 6,290円 |
| 60歳以上65歳未満 | 5,085円 |
""")


st.markdown("#### 雇用保険の基本手当の所定給付日数について")
st.markdown("雇用保険の基本手当の所定給付日数についての詳細は、[こちら](https://www.hellowork.mhlw.go.jp/insurance/insurance_benefitdays.html)をご覧ください。")