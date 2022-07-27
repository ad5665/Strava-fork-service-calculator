from __future__ import annotations

from typing import Any, Optional
from pydantic import BaseModel


class Athlete(BaseModel):
    id: int
    resource_state: int


class Map(BaseModel):
    id: str
    summary_polyline: Any
    resource_state: int


class Activity(BaseModel):

    def __repr__(self) -> str:
        return f"Activity(id={self.id}, name={self.name}, gear_id={self.gear_id}"

    resource_state: Optional[int] = None
    athlete: Optional[Athlete] = None
    name: Optional[str] = None
    distance: Optional[float] = None
    moving_time: Optional[int] = None
    elapsed_time: Optional[int] = None
    total_elevation_gain: Optional[int] = None
    type: Optional[str] = None
    workout_type: Optional[Any] = None
    id: Optional[int] = None
    external_id: Optional[str] = None
    upload_id: Optional[int] = None
    start_date: Optional[str] = None
    start_date_local: Optional[str] = None
    timezone: Optional[str] = None
    utc_offset: Optional[int] = None
    start_latlng: Optional[Any] = None
    end_latlng: Optional[Any] = None
    location_city: Optional[Any] = None
    location_state: Optional[Any] = None
    location_country: Optional[str] = None
    achievement_count: Optional[int] = None
    kudos_count: Optional[int] = None
    comment_count: Optional[int] = None
    athlete_count: Optional[int] = None
    photo_count: Optional[int] = None
    map: Optional[Map] = None
    trainer: Optional[bool] = None
    commute: Optional[bool] = None
    manual: Optional[bool] = None
    private: Optional[bool] = None
    flagged: Optional[bool] = None
    gear_id: Optional[str] = None
    from_accepted_tag: Optional[bool] = None
    average_speed: Optional[float] = None
    max_speed: Optional[int] = None
    average_cadence: Optional[float] = None
    average_watts: Optional[float] = None
    weighted_average_watts: Optional[int] = None
    kilojoules: Optional[float] = None
    device_watts: Optional[bool] = None
    has_heartrate: Optional[bool] = None
    average_heartrate: Optional[float] = None
    max_heartrate: Optional[int] = None
    max_watts: Optional[int] = None
    pr_count: Optional[int] = None
    total_photo_count: Optional[int] = None
    has_kudoed: Optional[bool] = None
    suffer_score: Optional[int] = None


class Gear(BaseModel):
    id: Optional[str] = None
    primary: Optional[bool] = None
    resource_state: Optional[int] = None
    distance: Optional[int] = None
    brand_name: Optional[str] = None
    model_name: Optional[str] = None
    frame_type: Optional[int] = None
    description: Optional[str] = None


class Bike(BaseModel):
    id: str
    primary: bool
    name: str
    nickname: str
    resource_state: int
    retired: bool
    distance: int
    converted_distance: float


class Athelete(BaseModel):
    id: Optional[int] = None
    username: Optional[Any] = None
    resource_state: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    bio: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[Any] = None
    sex: Optional[str] = None
    premium: Optional[bool] = None
    summit: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    badge_type_id: Optional[int] = None
    weight: Optional[float] = None
    profile_medium: Optional[str] = None
    profile: Optional[str] = None
    friend: Optional[Any] = None
    follower: Optional[Any] = None
    blocked: Optional[bool] = None
    can_follow: Optional[bool] = None
    follower_count: Optional[int] = None
    friend_count: Optional[int] = None
    mutual_friend_count: Optional[int] = None
    athlete_type: Optional[int] = None
    date_preference: Optional[str] = None
    measurement_preference: Optional[str] = None
    ftp: Optional[Any] = None
    bikes: Optional[list[Bike]] = None
    is_winback_via_upload: Optional[bool] = None
    is_winback_via_view: Optional[bool] = None
