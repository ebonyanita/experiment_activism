

from . import C, CountingTrial, RoundGrid, activism_update_html, round_header_html


# built-in hook renderer(s) (called automatically by oTree)


# <hook-functions>


def content_block(player, components, **api_kwargs):
    
            existing = CountingTrial.filter(player=player)
            if existing:
                current_trial = existing[-1]
                grid_str = current_trial.grid
            else:
                [first_grid] = RoundGrid.filter(
                    subsession=player.subsession, trial_index=0
                )
                CountingTrial.create(player=player, grid=first_grid.grid, num_ones=first_grid.num_ones)
                grid_str = first_grid.grid
            
            if player.round_number > C.NUM_ROUNDS_PART1:
                yield activism_update_html(player)
                yield f"""
            <p>Your work task time this round: <b>{player.actual_effort_time} seconds</b>.</p>
            """
            yield f"""
            <p>Count the number of 1s in the grid below and enter your answer:</p>
            <pre id="grid" class="grid-display">{grid_str}</pre>
            <input type="number" id="answer-input" min=0 max={C.MAX_ANSWER}>
            <button type="button" id="submit-answer">Submit</button>
            <p id="feedback"></p>
            """
            yield components.js_script('effort_task.js')
    


def meta_title_block(player, components, **api_kwargs):
    yield ""


def title_block(player, components, **api_kwargs):
    yield round_header_html(player)


# </hook-functions>