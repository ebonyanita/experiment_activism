


from . import C


# built-in hook renderer(s) (called automatically by oTree)


# <hook-functions>


def content_block(player, components, **api_kwargs):
    selected_round = player.participant.selected_round or 'TBD'
    payoff = player.participant.payoff
    fee = float(player.session.config.get('participation_fee', 0))
    if payoff is not None:
        payoff_eur = float(payoff)
        total_eur = payoff_eur + fee
        yield f"""
        <h2>Your Results</h2>
        <p>Should this experiment be selected for payment, the round randomly chosen to determine your earnings is round {selected_round}.</p>
        <p>Your earnings from the experiment: €{payoff_eur:.2f}</p>
        <p>Fixed fee: €{fee:.2f}</p>
        <p><b>Your total payment: €{total_eur:.2f}</b></p>
        <p>Thank you for participating!</p>
        """
    else:
        yield "<p>Your payment will be calculated and displayed shortly.</p>"
    yield components.next_button()


def meta_title_block(player, components, **api_kwargs):
    yield ""


def title_block(player, components, **api_kwargs):
    yield ""


# </hook-functions>