#import android
import androidhelper
droid = androidhelper.Android()
(id, result, error) = droid.recognizeSpeech("Say something")
print(result, error)
