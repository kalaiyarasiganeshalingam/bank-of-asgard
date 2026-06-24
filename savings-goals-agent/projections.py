"""Deterministic compound-interest math for savings projections.

Plain arithmetic only — no LLM involved. The LLM call in server.py explains and frames
these numbers; it never computes them.
"""


def project_balance(monthly_amount: float, annual_rate: float, years: int) -> float:
    """Future value of a monthly annuity: depositing `monthly_amount` at the end of each
    month for `years` years, compounding monthly at `annual_rate` (e.g. 0.03 for 3% APY)."""
    months = years * 12
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:
        return round(monthly_amount * months, 2)
    future_value = monthly_amount * (((1 + monthly_rate) ** months - 1) / monthly_rate)
    return round(future_value, 2)


def project_milestones(
    monthly_amount: float,
    annual_rate: float = 0.03,
    years: tuple[int, ...] = (1, 5, 10),
) -> dict[str, float]:
    """Convenience wrapper: projected balance at each milestone in `years`."""
    return {f"{y}y": project_balance(monthly_amount, annual_rate, y) for y in years}
