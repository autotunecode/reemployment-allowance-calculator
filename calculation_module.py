def calculate_reemployment_allowance(age, basic_allowance_daily, prescribed_benefit_days, remaining_payment_days):
    """
    離職時の年齢、基本手当日額、所定給付日数、支給残日数によって再就職手当の計算を行う関数。
    :param age: 離職時の年齢
    :param basic_allowance_daily: 基本手当日額（円）
    :param prescribed_benefit_days: 所定給付日数
    :param remaining_payment_days: 支給残日数
    :return: 再就職手当（円）
    """
    # benefit_days_ratioの初期化
    benefit_days_ratio = 0  # 適切なデフォルト値に設定

    # 年齢に応じた基本手当日額の上限額の設定
    if age < 60:
        max_basic_allowance_daily = 6290
    else:
        max_basic_allowance_daily = 5085  # 60歳以上65歳未満の場合

    # 実際の基本手当日額を上限額で制限
    adjusted_basic_allowance_daily = min(basic_allowance_daily, max_basic_allowance_daily)

    # 支給残日数が所定給付日数の2/3以上ある場合の計算
    if remaining_payment_days >= (2/3) * prescribed_benefit_days:
        reemployment_allowance = adjusted_basic_allowance_daily * remaining_payment_days * 0.7
        benefit_days_ratio = 0.7  # 70%を設定
    # 支給残日数が所定給付日数の1/3以上ある場合の計算
    elif remaining_payment_days >= (1/3) * prescribed_benefit_days:
        reemployment_allowance = adjusted_basic_allowance_daily * remaining_payment_days * 0.6
        benefit_days_ratio = 0.6  # 60%を設定
    # それ以外の場合の計算
    else:
        # 年齢に応じた給付率の設定
        if age < 30:
            benefit_rate = 0.5
        elif 30 <= age < 45:
            benefit_rate = 0.6
        elif 45 <= age < 60:
            benefit_rate = 0.7
        else:
            benefit_rate = 0.8  # 60歳以上65歳未満の場合

        # 再就職手当の計算
        reemployment_allowance = adjusted_basic_allowance_daily * benefit_rate * min(prescribed_benefit_days, remaining_payment_days)
        # 所定給付日数割合の計算
        benefit_days_ratio = 0.6 if benefit_rate == 0.6 else 0.7

    return reemployment_allowance, benefit_days_ratio
