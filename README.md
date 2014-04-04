# pocketmiku

Linux tools for configuring a Pocket Miku (NSX-39).

All tools automatically detect the NSX-39 and use `amidi` to send MIDI data.

## Tools

### sendraw.py

Effectively the same as `amidi -S "..."`.

### setlyrics.py

Set the lyrics for the device based on a string of Japanese kana.

Example:

    python setlyrics.py さくらさくら

See the manual for the device for the list of possible mora. Aliases are also accepted. Note that since 「ん」 is ambiguous, you should use the more specific forms (`N\`, `m`, etc.).

### sample.py

Makes the device sing 「君が代」.

### test.py

Plays all possible mora in a repeating C scale.

## Modules

### `amidi`

Deals with detecting the device and using `amidi` to send MIDI data.

### `control`

Creates MIDI event strings. These are generic and don't actually depend on `amidi`, so if you have an alternative way to send MIDI data to the device, you can use this module to generate that MIDI data.

### `notes`

Contains mora to note number mappings used to program the lyrics on the device.
