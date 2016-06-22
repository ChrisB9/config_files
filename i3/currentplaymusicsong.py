import os, json


def main():
    data = get_play_music_json()
    song = data["song"]
    time = data["time"]
    if data["playing"]:
        print(u'\u266B'+" "+song["title"]+": "+song["album"]+"/"+song["artist"]+" ("+str(round(get_song_duration_percentage(time["current"], time["total"]), 2)) + "%) |")
    else:
        print(u'\u266B'+" No Song")


def get_play_music_json():
    json_file = open(os.path.expanduser('~/.config/Google Play Music Desktop Player/json_store/playback.json'), "r")
    data = json.load(json_file)
    return data


def turn_ms_to_min(ms):
    return round(float(ms) / float(60000), 2)


def get_song_duration_percentage(current, total):
    return float(current) / float(total) * 100


if __name__ == "__main__":
    main()
