# test_item.py
import unittest
from datetime import datetime
from item import Lyric, MusicScore, AudioRecording

class TestItem(unittest.TestCase):
    def test_lyric_encryption_decryption(self):
        lyric_content = "This is a lyric"
        lyric = Lyric(lyric_content)
        encrypted_content = lyric.encrypted_content
        self.assertNotEqual(encrypted_content, lyric_content.encode())
        decrypted_content = lyric.decrypt()
        self.assertEqual(decrypted_content, lyric_content)

    def test_music_score_encryption_decryption(self):
        score_content = "This is a music score"
        score = MusicScore(score_content)
        encrypted_content = score.encrypted_content
        self.assertNotEqual(encrypted_content, score_content.encode())
        decrypted_content = score.decrypt()
        self.assertEqual(decrypted_content, score_content)

    def test_audio_recording_encryption_decryption(self):
        audio_content = "This is an audio recording"
        audio = AudioRecording(audio_content)
        encrypted_content = audio.encrypted_content
        self.assertNotEqual(encrypted_content, audio_content.encode())
        decrypted_content = audio.decrypt()
        self.assertEqual(decrypted_content, audio_content)

    def test_timestamping(self):
        lyric = Lyric("Test lyric")
        self.assertIsInstance(lyric.creation_time, datetime)
        self.assertIsInstance(lyric.modification_time, datetime)
        self.assertEqual(lyric.creation_time, lyric.modification_time)

if __name__ == "__main__":
    unittest.main()