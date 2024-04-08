import pytest
from IPYNBrenderer import render_Youtube_video
from IPYNBrenderer.custom_exception import InvalidURLException


class TestYTvideoRenderer:
    URL_test_success_data = [
        ("https://youtu.be/roO5VGxOw2s", "successfullly rendered"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s", "successfullly rendered"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", "successfullly rendered"),
    ]
    URL_test_bad_data = [
        ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),
        ("https://www.youtube.com/watch?v=roO5VGxOw00"),
        ("https://www.youtube.com/watch?v=roO5VGxOw__"),
        ("https://www.youtube.com/watch?v=roO5VGxOwpp"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),
        ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),
        ("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s"),
    ]

    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_YT_success(self, URL, response):
        assert render_Youtube_video(URL) == response

    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_Youtube_video(URL)
