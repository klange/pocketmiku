# pocketmiku

Linux tools for configuring a Pocket Miku (NSX-39).

All tools automatically detect the NSX-39 and use `amidi` to send MIDI data.

    pip install pocketmiku

## Tools

### sendraw

Effectively the same as `amidi -S "..."`.

### setlyrics

Set the lyrics for the device based on a string of Japanese kana.

Example:

    python -m pocketmiku.tools.setlyrics さくらさくら

See the manual for the device for the list of possible mora. Aliases are also accepted. Note that since 「ん」 is ambiguous, you should use the more specific forms (`N\`, `m`, etc.).

## Modules

### `amidi`

Deals with detecting the device and using `amidi` to send MIDI data.

### `control`

Creates MIDI event strings. These are generic and don't actually depend on `amidi`, so if you have an alternative way to send MIDI data to the device, you can use this module to generate that MIDI data.

### `notes`

Contains mora to note number mappings used to program the lyrics on the device.


## Other Information

I am working to compile a complete set of functions to control programming of all banks as well as backing up and restoring lyrics (as is available from the web app).

The device has 16 banks of lyrics. Each bank can hold 64 lyric "characters". The first bank (bank 00) isn't accessible from a key on the device, which makes it useful for loading lyrics ad-hoc. The other 15 banks are the A, I, U, E, O keys, followed by Shift+A-O, followed by Vibrato+A-O. Only the last nibble of the bank number matters, the first nibble is seemingly ignored. Each bank is nonvolatile, if you program a bank it will stay that way through a restart. The webapp allows programming and reading all of the banks except seemingly bank 0.

There are also SysEx commands to request the currently selected bank, the current position in the lyrics, and possibly also to set the position in lyrics (note that this would be very useful when you can just explicitly set individual notes). Setting lyrics for a particular bank switches the device to that bank.

