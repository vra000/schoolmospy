from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class EventItem(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: int
    source_id: str
    source: str
    start_at: str
    finish_at: str
    cancelled: bool | None = None
    lesson_type: str | None = None
    course_lesson_type: Any | None = None
    lesson_form: Any | None = None
    replaced: bool | None = None
    title: str | None = None
    begin_time: str | None = None
    end_time: str | None = None
    room_name: str | None = None
    room_number: str | None = None
    subject_id: int | None = None
    subject_name: str | None = None
    teacher: Any | None = "-"
    link_to_join: Any | None = None
    health_status: Any | None = None
    absence_reason_id: Any | None = None
    nonattendance_reason_id: Any | None = None
    homework: Any | None = None
    marks: Any | None = None
    is_missed_lesson: bool = False
    esz_field_id: int | None = None
    lesson_theme: Any | None = None
    teachers: list[Any] | None = None


class Events(BaseModel):
    total_count: int
    response: list[EventItem]
    errors: Any | None = None
