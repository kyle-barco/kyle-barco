from datetime import datetime

import gifos
from zoneinfo import ZoneInfo

FONT_FILE_LOGO = "./fonts/vtks-blocketo.regular.ttf"
# FONT_FILE_BITMAP = "./fonts/ter-u14n.pil"
FONT_FILE_BITMAP = "./fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "./fonts/IosevkaTermNerdFont-Bold.ttf"
FONT_FILE_MONA = "./fonts/Inversionz.otf"


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Asia/Manila")).strftime("%Y")
    t.gen_text("KYLE_OS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mKyle Barco\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Krypton(tm) GIFCPU - 250Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):  # 64K Memory
        t.delete_row(7)
        if i < 30000:
            t.gen_text(
                f"Memory Test: {i}", 7, count=2, contin=True
            )  # slow down upto a point
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)  # buffer to be removed
    t.set_font(FONT_FILE_LOGO, 66)
    # t.toggle_show_cursor(True)
    os_logo_text = "KYLE OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mKYLE OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("kyle-barco", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Asia/Manila")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    import urllib.request, json
    ignore_repos = []
    git_user_details = gifos.utils.fetch_github_stats("kyle-barco", ignore_repos)
    user_age = gifos.utils.calc_age(4, 5, 2023)
    streak_data = None
    try:
        with urllib.request.urlopen("https://streak-stats.demolab.com/api?user=kyle-barco") as r:
            streak_data = json.loads(r.read().decode())
    except Exception:
        pass
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    user_details_lines = f"""
    \x1b[30;101mkyle-barco@GitHub\x1b[0m
    --------------
    \x1b[96mOS:     \x1b[93mArch Linux\x1b[0m
    \x1b[96mHost:   \x1b[93mPolytechnic University of the Philippines\x1b[0m
    \x1b[96mKernel: \x1b[93mInformation Technology\x1b[0m
    \x1b[96mUptime: \x1b[93m{user_age.years} years, {user_age.months} months, {user_age.days} days\x1b[0m
    \x1b[96mIDE:    \x1b[93mNeovim\x1b[0m
    
    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mEmail:      \x1b[93mbarco.jaztherkyle.delacerna@gmail.com\x1b[0m
    \x1b[96mLinkedIn:   \x1b[93mkyle-barco-09182b279\x1b[0m
    
    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits ({int(year_now) - 1}): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs: \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %: \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mCurrent Streak: \x1b[93m{streak_data.get('streak', 'N/A') if streak_data else 'N/A'} days\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[:5])}\x1b[0m
    """
    t.gen_text("\x1b[92mkyle-barco\x1b[0m\x1b[94m@\x1b[0m\x1b[93mKYLE_OS\x1b[0m \x1b[95m~\x1b[0m\x1b[93m>\x1b[0m ", 1, count=5)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mneofetc", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mneofetch\x1b[0m", 1, contin=True)

    t.toggle_show_cursor(False)
    crossLines = r"""



              \x1b[90m_ \x1b[0m
             \x1b[90m| |\x1b[0m
             \x1b[90m| |\x1b[0m
         \x1b[90m____| |____\x1b[0m
         \x1b[90m\        /\x1b[0m
          \x1b[90m\      /\x1b[0m
           \x1b[90m\    /\x1b[0m
            \x1b[90m\  /\x1b[0m
             \x1b[90m\/\x1b[0m
    """
    t.gen_text(crossLines, 10)

    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(True)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.gen_text("\x1b[92mkyle-barco\x1b[0m\x1b[94m@\x1b[0m\x1b[93mKYLE_OS\x1b[0m \x1b[95m~\x1b[0m\x1b[93m>\x1b[0m ", t.curr_row, count=5)
    t.gen_typing_text(
        "\x1b[92m# Have a blessed day kind stranger :D Thanks for stopping by!  - For His Glory alone",
        t.curr_row,
        contin=True,
    )
    # t.save_frame("fetch_details.png")
    t.gen_text("", t.curr_row, count=120, contin=True)

    t.gen_gif()
    readme_file_content = rf"""<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./output.gif">
    <source media="(prefers-color-scheme: light)" srcset="./output.gif">
    <img alt="KYLEOS" src="output.gif">
</picture>

<sub><i>Generated automatically using [KYLE OS](https://github.com/kyle-barco/kyle-barco) on {time_now}</i></sub>

<!-- <details>
<summary>More details</summary>

</details> -->
</div>

<br/>

[![GitHub Streak](https://streak-stats.demolab.com?user=kyle-barco&count_private=true&theme=nord&border_radius=10)](https://git.io/streak-stats)

<!-- Image deletion URL: NONE -->"""
    with open("README.md", "w") as f:
        f.write(readme_file_content)
        print("INFO: README.md file generated")


if __name__ == "__main__":
    main()
