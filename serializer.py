from exceptions import NotFoundTrack


class Track:
    def __init__(self, music):
        self.music = music
        try:
            self.track = self.music['track']
            self.title = self.track['title']
            self.subtitle = self.track['subtitle']
            self.image = self.track['images']['coverarthq']
            self.appleMusic_url = self.track['hub']['options'][0]['actions'][0]['uri']
            self.uri_ios: str = self.track['hub']['providers'][0]['actions'][1]['uri']
            self.uri_decoded = self.uri_ios.split('spotify:search:')[1]
        except KeyError:
            raise NotFoundTrack
