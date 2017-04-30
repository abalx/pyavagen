from PIL import Image
import pytest
import pyavagen
from pyavagen import validators, generators


class TestAvatar:
    @pytest.mark.parametrize(
        argnames="avatar_type,avatar_class,avatar_kwargs",
        argvalues=[
            (pyavagen.CHAR_AVATAR, pyavagen.CharAvatar, {'string': 'string'}),
            (pyavagen.SQUARE_AVATAR, pyavagen.SquareAvatar, {}),
            (pyavagen.CHAR_SQUARE_AVATAR, pyavagen.CharSquareAvatar, {'string': 'string'}),
        ]
    )
    def test_avatar_class_arg(self, avatar_type, avatar_class, avatar_kwargs):
        """
        'avatar_class' argument should return an avatar class defined
        to an avatar type.
        If a passed avatar type is undefined in 'Avatar' class then should
        raise AttributeError.
        """

        avatar = pyavagen.Avatar(
            avatar_type=avatar_type,
            size=2,
            **avatar_kwargs,
        )
        assert isinstance(avatar.avatar_class, avatar_class)

    def test_avatar_class_arg_with_none(self):
        """
        Should raise AttributeError if a passed avatar class is None.
        """

        with pytest.raises(AttributeError):
            pyavagen.Avatar(avatar_type=None)

    @pytest.mark.parametrize(
        argnames="avatar_type,avatar_kwargs",
        argvalues=[
            (pyavagen.CHAR_AVATAR, {'string': 'string'}),
            (pyavagen.SQUARE_AVATAR, {}),
            (pyavagen.CHAR_SQUARE_AVATAR, {'string': 'string'}),
        ]
    )
    def test_generate_method(self, avatar_type, avatar_kwargs):
        """
        'generate' method of 'Avatar' class should return Image.Image object.
        """

        avatar = pyavagen.Avatar(
            avatar_type=avatar_type,
            size=2,
            **avatar_kwargs,
        )

        assert isinstance(avatar.generate(), Image.Image)


class TestColorListMixin:
    @pytest.mark.parametrize(
        argnames="color_list",
        argvalues=[
            None,
            generators.COLOR_LIST_FLAT,
            generators.COLOR_LIST_MATERIAL,
        ]
    )
    def test_get_random_color_method(self, color_list):
        """Should return string that contains a color value."""

        color_list_object = generators.ColorListMixin(color_list=color_list)
        color_validator = validators.ColorValidator()(
            value=color_list_object.get_random_color(),
            field_name='field',
        )

        assert color_validator is None


class TestSquareAvatar:
    def test_generate_with_full_set(self):
        avatar = generators.SquareAvatar(
            size=4,
            border_color='black',
            blur_radius=2,
            border_size=2,
            rotate=2,
            squares_on_axis=2,
            color_list=pyavagen.COLOR_LIST_MATERIAL,
        )

        assert isinstance(avatar.generate(), Image.Image)


class TestCharAvatar:
    def test_generate_with_full_set(self):
        avatar = generators.CharAvatar(
            size=4,
            background_color='black',
            font_size=2,
            font_color='black',
            font_outline=True,
            color_list=pyavagen.COLOR_LIST_MATERIAL,
            string='string',
        )

        assert isinstance(avatar.generate(), Image.Image)


class TestCharSquareAvatar:
    def test_generate_with_full_set(self):
        avatar = generators.CharSquareAvatar(
            size=4,
            background_color='black',
            font_size=2,
            font_color='black',
            font_outline=True,
            color_list=pyavagen.COLOR_LIST_MATERIAL,
            string='string',
            border_color='black',
            blur_radius=2,
            border_size=2,
            rotate=2,
            squares_on_axis=2,
        )

        assert isinstance(avatar.generate(), Image.Image)