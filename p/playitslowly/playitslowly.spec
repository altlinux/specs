Name: playitslowly
Version: 1.4.0
Release: alt1
Summary: Play back audio files at a different speed or pitch
Group: Sound
License: GPLv3
Url: http://29a.ch/playitslowly/
Source: %name-%version.tar.gz
BuildArch: noarch

%setup_python_module %name
Requires: %packagename

# Automatically added by buildreq on Mon Sep 05 2011
# optimized out: python-base python-modules
BuildRequires: python-devel

%description
Play it slowly is a software to play back audio files at a different
speed or pitch. It does also allow you to loop over a certain part of
a file. It's intended to help you learn or transcribe songs. It can also
play videos thanks to gstreamer. Play it slowly is intended to be used
on a GNU/Linux system like Ubuntu. If you'd like to have a windows
version, write a comment.

Features:
- Plays every file gstreamer does (mp3, ogg vorbis, midi, even flv!)
- Can use alsa and jack
- Change speed and pitch
- Loop over certain parts
- Export to wav

%package -n %packagename
Group: Sound
Summary: Python module for playing audio files at a different speed or pitch
%description -n %packagename
Python module for playing audio files at a different speed or pitch

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/%name.*
%_pixmapsdir/%name.*

%files -n %packagename
%python_sitelibdir_noarch/%{name}*

%changelog
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0
- Closes: 26850

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt1.1
- Rebuild with Python-2.7

* Tue Sep 06 2011 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Initial build from scratch

