Name: test-audio
Version: 0.2
Release: alt1

Summary: simple audio test to save keypresses
License: public domain
Group: System/Configuration/Hardware

BuildArch: noarch

Source: %name-%version.tar

%define pcmfile %_datadir/sounds/alsa/Front_Center.wav
# The tools are hidden to trick shell findreq.
# Please define the shell variables before use.
%define acmd $APLAY -v -Vmono %pcmfile
%define areccmd $ARECORD -v -Vmono %pcmfile
%define pacmd $PAPLAY -v %pcmfile
# parecord cannot show a visual meter
#define pareccmd $PARECORD -v %pcmfile

%description
This package provides a command-line tool to test audio output through various
audio backends used on Linux-based systems.

%prep
%setup

%build
sed '
s!@ACMD@!%acmd!
s!@ARECCMD@!%areccmd!
s!@PACMD@!%pacmd!
' %name.sh.in > %name

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sat Mar 20 2021 Arseny Maslennikov <arseny@altlinux.org> 0.2-alt1
- Added direct PA client support.
- We now pass -v to playback commands.
- Test source outputs as well as sink inputs (with a VU meter).

* Tue Dec 17 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

