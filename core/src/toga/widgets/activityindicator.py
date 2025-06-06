from __future__ import annotations

from typing import Any, Literal

from .base import StyleT, Widget


class ActivityIndicator(Widget):
    def __init__(
        self,
        id: str | None = None,
        style: StyleT | None = None,
        running: bool = False,
        **kwargs,
    ):
        """Create a new ActivityIndicator widget.

        :param id: The ID for the widget.
        :param style: A style object. If no style is provided, a default style
            will be applied to the widget.
        :param running: Describes whether the indicator is running at the
            time it is created.
        :param kwargs: Initial style properties.
        """
        super().__init__(id, style, **kwargs)

        if running:
            self.start()

    def _create(self) -> Any:
        return self.factory.ActivityIndicator(interface=self)

    @property
    def enabled(self) -> Literal[True]:
        """Is the widget currently enabled? i.e., can the user interact with the widget?

        ActivityIndicator widgets cannot be disabled; this property will always return
        True; any attempt to modify it will be ignored.
        """
        return True

    @enabled.setter
    def enabled(self, value: bool) -> None:
        pass

    def focus(self) -> None:
        """No-op; ActivityIndicator cannot accept input focus."""
        pass

    @property
    def is_running(self) -> bool:
        """Determine if the activity indicator is currently running.

        Use ``start()`` and ``stop()`` to change the running state.

        True if this activity indicator is running; False otherwise.
        """
        return self._impl.is_running()

    def start(self) -> None:
        """Start the activity indicator.

        If the activity indicator is already started, this is a no-op.
        """
        if not self.is_running:
            self._impl.start()

    def stop(self) -> None:
        """Stop the activity indicator.

        If the activity indicator is already stopped, this is a no-op.
        """
        if self.is_running:
            self._impl.stop()
