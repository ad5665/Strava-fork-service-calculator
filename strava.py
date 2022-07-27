from __future__ import annotations

import json
import pathlib
from typing import Any
import rich

from rich.console import Console
from rich.table import Table, Column

import requests

from models import Activity, Gear, Athelete


tokens = {
    "profile": "####################################",
    "activity": "####################################",
}


BASE_URL = "https://www.strava.com/api/v3"



def request_with_auth(url, token_type="profile", **kwargs) -> requests.Response:
    return requests.get(url, headers={
        "Authorization": f"Bearer {tokens.get(token_type)}",
    }, **kwargs)


def get_athlete_info() -> dict[str, Any]:
    resp = request_with_auth(f"{BASE_URL}/athlete")
    if not resp.ok:
        resp.raise_for_status()
    return Athelete.parse_obj(resp.json())


def get_activity_page(page=1) -> list[dict[str, Any]]:
    resp = request_with_auth(
        f"{BASE_URL}/athlete/activities",
        token_type="activity",
        params={"page": page}
    )

    if not resp.ok:
        resp.raise_for_status()

    return [Activity.parse_obj(activity) for activity in resp.json()]


def get_all_activities() -> list[dict[str, Any]]:
    all_activities = []

    for page in range(1, 100):
        activities = get_activity_page(page)
        rich.print(f"Found {len(activities)} activities")

        if not activities:
            break

        all_activities.extend(activities)
    return all_activities


def get_gear_by_id(id=None) -> dict[str, Any]:
    resp = request_with_auth(f"{BASE_URL}/gear/{id}")
    if not resp.ok:
        resp.raise_for_status()
    return Gear.parse_obj(resp.json())



def seconds_to_hours_and_minutes(seconds: int) -> str:
    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes:02d}m"

bikes = {
}


cache_file = pathlib.Path("cache.json")

if cache_file.exists():
    with cache_file.open() as f:
        all_activities = [Activity.parse_obj(a) for a in json.load(f)]
else:
    all_activities = get_all_activities()
    cache_file.write_text(json.dumps([activity.dict() for activity in all_activities]))


# Generate a table of all activities
def generate_table(activities: list[dict[str, Any]]) -> Table:
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Date", style="green bold")
    table.add_column("Time", style="green bold")
    table.add_column("Distance", style="green bold")
    table.add_column("Bike", style="green bold")
    table.add_column("Gear", style="green bold")
    table.add_column("Description", style="green bold")

    for activity in activities:
        table.add_row(
            activity.start_date_local.strftime("%Y-%m-%d"),
            seconds_to_hours_and_minutes(activity.elapsed_time),
            f"{activity.distance:.2f}km",
            bikes.get(activity.bike_id, ""),
            activity.gear_id,
            activity.name,
        )

    return table



table = Table(
    Column(header="Bike"),
    Column(header="Riding time"),
    Column(header="Total distance"),
    Column(header="Max speed"),
    Column(header="Average ride time"),
    Column(header="Average distance"),
    Column(header="Average elevation gain"),
    Column(header="Average speed"),
    Column(header="Average calories"),
    title=f"Bike stats"
)

for bike, id in bikes.items():
    filtered_activities = list(filter(lambda activity: activity.gear_id == id, all_activities))

    riding_time = sum(map(lambda activity: activity.moving_time, filtered_activities))
    total_distance = (sum(map(lambda activity: activity.distance, filtered_activities)) * 0.001) / 1.609
    max_speed = max(map(lambda activity: activity.max_speed, filtered_activities)) * 2.237
    average_ride_time = seconds_to_hours_and_minutes(sum(map(lambda activity: activity.moving_time, filtered_activities)) / len(filtered_activities))
    average_distance = total_distance / len(filtered_activities) * 2.237
    average_elevation_gain = sum(map(lambda activity: activity.total_elevation_gain, filtered_activities)) / len(filtered_activities) * 3.281
    average_speed = sum(map(lambda activity: activity.average_speed, filtered_activities)) / len(filtered_activities) * 2.237
    average_kj = sum(map(lambda activity: activity.kilojoules if activity.kilojoules else 0, filtered_activities)) / len([a for a in filtered_activities if a.kilojoules])

    table.add_row(
        bike,
        seconds_to_hours_and_minutes(riding_time),
        f"{total_distance:.2f} mi",
        f"{max_speed:.2f} mp/h",
        f"{average_ride_time}",
        f"{average_distance:.2f} mi",
        f"{average_elevation_gain:.2f} ft",
        f"{average_speed:.2f} mp/h",
        f"{average_kj:.2f} kj"
    )

console = Console()
console.print(table)








"""
https://developers.strava.com/playground/#/Athletes/getLoggedInAthlete
https://developers.strava.com/docs/getting-started/
https://developers.strava.com/docs/authentication/
https://developers.strava.com/docs/
https://developers.strava.com/docs/reference/#api-Gears-getGearById
http://www.hainke.ca/index.php/2018/08/23/using-the-strava-api-to-retrieve-activity-data/
"""