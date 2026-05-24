from random import choice
from playlist import Playlist
from state import State, NEXT
from pygame import mixer
from time import sleep


mixer.init()


class Radio:
    def __init__( self ):
        self.state = State.BEGIN

        self.playlist = {
            State.SONG: Playlist( State.SONG ),
            State.TRANSITIONAL: Playlist( State.TRANSITIONAL ),
            State.COMM_INTRO: Playlist( State.COMM_INTRO ),
            State.COMM: Playlist( State.COMM ),
            State.SEGMENT: Playlist( State.SEGMENT ),
            State.CALL_LETTER: Playlist( State.CALL_LETTER ) 
        }


    def play( self ):
        # 인트로 다음 음악을 연달아 재생
        if self.state == State.INTRO:
            self.nextState()     # 반드시 song
            song = mixer.Sound( self.playlist[ self.state ].nowPlaying() )
            
            try:
                intro = mixer.Sound( self.playlist[ self.state ].getIntro() )
                intro.play()
                sleep( intro.get_length() + 1 )
            except TypeError:
                print( "No Intro!" )

            print( self.playlist[ self.state ].songName )
            song.play()
            sleep( song.get_length() + 1 )

        # nowPlaying 호출 전, 직전 재생된 음악의 아우트로를 재생
        elif self.state == State.OUTRO:
            try:
                outro = mixer.Sound( self.playlist[ State.SONG ].getOutro() )
                outro.play()
                sleep( outro.get_length() + 1 )
            except TypeError:
                print( "No Outro!" )

        else:
            audio = mixer.Sound( self.playlist[ self.state ].nowPlaying() )
            print( self.playlist[ self.state ].songName )
            audio.play()
            sleep( audio.get_length() + 1 )


    def nextState( self ):
        self.state = choice( NEXT[ self.state ] )


    def printState( self ):
        print( self.state.name )


    def loop( self ):
        while True:
            self.nextState()
            self.play()