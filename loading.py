from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty


KV = '''
#:import cos math.cos
#:import sin math.sin
#:import pi math.pi
#:import radians math.radians
#:import chain itertools.chain
<SurroundingSlider>:
    a: self.angle_stop - self.angle_start
    segments: 50
    bar_width: 28
    cap_length: .3
    angle: radians(self.a * (self.value - self.min) / (self.max - self.min))
    _half_cap_angle: self.cap_length / self.radius
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Mesh:
            mode: 'triangle_strip'
            source: self.texture_back
            vertices:
                ((
                self.center_x + cos(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * self.radius,
                self.center_y + sin(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * self.radius,
                0, 1,
                self.center_x + cos(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * (self.radius + self.bar_width),
                self.center_y + sin(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * (self.radius + self.bar_width),
                0, 0,
                ) + tuple(chain(*[(
                self.center_x + cos(radians(self.angle_start + a * self.a) - pi / 2) * self.radius,
                self.center_y + sin(radians(self.angle_start + a * self.a) - pi / 2) * self.radius,
                .5, 1,
                self.center_x + cos(radians(self.angle_start + a * self.a) - pi / 2) * (self.radius + self.bar_width),
                self.center_y + sin(radians(self.angle_start + a * self.a) - pi / 2) * (self.radius + self.bar_width),
                .5, 0
                ) for a in (x / float(self.segments) for x in range(self.segments + 1))])) + (
                self.center_x + cos(radians(self.angle_stop) - pi / 2 - self._half_cap_angle) * self.radius,
                self.center_y + sin(radians(self.angle_stop) - pi / 2 - self._half_cap_angle) * self.radius,
                1, 1,
                self.center_x + cos(radians(self.angle_stop) - pi / 2 - self._half_cap_angle) * (self.radius + self.bar_width),
                self.center_y + sin(radians(self.angle_stop) - pi / 2 - self._half_cap_angle) * (self.radius + self.bar_width),
                1, 0,
                )) if self.angle_start and self.angle_stop and self.a and self.bar_width and self.radius else []
            indices: range(2 * self.segments + 6)
        Mesh:
            mode: 'triangle_strip'
            source: self.texture_fill
            vertices:
                ((
                self.center_x + cos(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * self.radius,
                self.center_y + sin(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * self.radius,
                0, 1,
                self.center_x + cos(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * (self.radius + self.bar_width),
                self.center_y + sin(radians(self.angle_start) - pi / 2 + self._half_cap_angle) * (self.radius + self.bar_width),
                0, 0,
                ) + tuple(chain(*[(
                self.center_x + (cos(radians(self.angle_start) + a * self.angle - pi / 2)) * self.radius,
                self.center_y + (sin(radians(self.angle_start) + a * self.angle - pi / 2)) * self.radius,
                .5, 1,
                self.center_x + (cos(radians(self.angle_start) + a * self.angle - pi / 2)) * (self.radius + self.bar_width),
                self.center_y + (sin(radians(self.angle_start) + a * self.angle - pi / 2)) * (self.radius + self.bar_width),
                .5, 0
                ) for a in (x / float(self.segments) for x in range(self.segments + 1))])) + (
                self.center_x + cos(radians(self.angle_start) + self.angle - pi / 2 - self._half_cap_angle) * self.radius,
                self.center_y + sin(radians(self.angle_start) + self.angle - pi / 2 - self._half_cap_angle) * self.radius,
                1, 1,
                self.center_x + cos(radians(self.angle_start) + self.angle - pi / 2 - self._half_cap_angle) * (self.radius + self.bar_width),
                self.center_y + sin(radians(self.angle_start) + self.angle - pi / 2 - self._half_cap_angle) * (self.radius + self.bar_width),
                1, 0
                )) if self.angle_start and self.angle_stop and self.a and self.bar_width and self.radius else []
            indices: range(2 * self.segments + 6)
'''

class SurroundingSlider(Widget):
    value = NumericProperty(0)
    angle_start = NumericProperty(360 -  33)
    angle_stop = NumericProperty(33)
    radius = NumericProperty(50)
    segments = NumericProperty(50)
    bar_width = NumericProperty(10)
    cap_length = NumericProperty(10)
    cap_texture_cut = NumericProperty(.2)
    min = NumericProperty(0)
    max = NumericProperty(1)
    a = NumericProperty(0)
    texture_back = StringProperty('slider_value_indicator_bar_empty.png')
    texture_fill = StringProperty('slider_value_indicator_bar_full.png')


Builder.load_string(KV)


if __name__ == '__main__':
    from textwrap import dedent

    APP_KV = dedent('''
    #:import glob glob.glob
    <SLabel@Label>:
        size_hint_x: None
        width: self.texture_size[0]
    FloatLayout:
        SurroundingSlider:
            size_hint: .5, .5
            radius: slider_radius.value * self.width / 2
            pos_hint: {'center': (.5, .5)}
            texture_back: spinner_back.text
            texture_fill: spinner_fill.text
            value: slider_value.value
            angle_start: slider_start.value
            angle_stop: slider_stop.value
            bar_width: slider_bar_width.value
            cap_length: slider_length.value
            segments: slider_segments.value
        GridLayout:
            cols: 2
            size_hint: 1, None
            height: 250
            pos_hint: {'x': 0, 'y': 0}
            spacing: 5
            paddig: 10, 10
            SLabel:
                text: 'value'
            Slider:
                id: slider_value
                min: 0
                max: 1
                value: .45
            SLabel:
                text: 'background'
            Spinner:
                id: spinner_back
                text: 'slider_value_indicator_bar_empty2.png'
                values: glob('*.png')
            SLabel:
                text: 'foreground'
            Spinner:
                id: spinner_fill
                text: 'slider_value_indicator_bar_full2.png'
                values: glob('*.png')
            SLabel:
                text: 'angle start'
            Slider:
                id: slider_start
                min: 0
                max: 360
                value: 300
            SLabel:
                text: 'angle stop'
            Slider:
                id: slider_stop
                min: 0
                max: 360
                value: 60
            SLabel:
                text: 'width'
            Slider:
                id: slider_bar_width
                min: 10
                max: 100
                value: 50
            SLabel:
                text: 'length of caps'
            Slider:
                id: slider_length
                min: 0
                max: 50
                value: 15
            SLabel:
                text: 'segments'
            Slider:
                id: slider_segments
                min: 2
                max: 1000
                step: 2
                value: 50
            SLabel:
                text: 'radius'
            Slider:
                id: slider_radius
                min: 0.01
                max: 1
                value: 1
    ''')

    class Application(App):
        def build(self):
            return Builder.load_string(APP_KV)

    Application().run()