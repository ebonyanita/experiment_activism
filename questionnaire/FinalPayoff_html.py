


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
        <p>From the 14 rounds, round {selected_round} was randomly selected for payoff. In that round, you earned €{payoff_eur:.2f}.</p>
        <p>So if this experiment is randomly selected for payoff at the end of the session, then your payoff will be €{total_eur:.2f}.</p>
        """
    else:
        yield "<p>Your payment will be calculated and displayed shortly.</p>"
    yield components.next_button()


def meta_title_block(player, components, **api_kwargs):
    yield ""


def title_block(player, components, **api_kwargs):
    yield ""


# </hook-functions>