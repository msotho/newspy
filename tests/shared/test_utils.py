from datetime import datetime, timedelta, timezone

import pytest

from newspy.shared import utils


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("2022-07-17T07:49:34Z", datetime(2022, 7, 17, 7, 49, 34, tzinfo=timezone.utc)),
        (
            "2022-07-16T12:00:13+00:00",
            datetime(2022, 7, 16, 12, 0, 13, tzinfo=timezone.utc),
        ),
        (
            "2022-07-07T02:37:07.675501Z",
            datetime(2022, 7, 7, 2, 37, 7, 675501, tzinfo=timezone.utc),
        ),
        (
            "Mon, 19 Dec 2022 07:55:18 +0200",
            datetime(2022, 12, 19, 7, 55, 18, tzinfo=timezone(timedelta(seconds=7200))),
        ),
    ],
)
def test_create_published(test_input, expected):
    actual = utils.to_datetime(string=test_input)

    assert actual == expected
