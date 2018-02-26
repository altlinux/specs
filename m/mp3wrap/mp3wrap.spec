Name: mp3wrap
Version: 0.5
Release: alt1

Summary: Utility for MP3 wrapping (rolling multiple MP3s into one)

License: GPL
Group: Sound
Url: http://mp3wrap.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version-src.tar
Patch: %name.c.patch

%description
Mp3Wrap is a free command-line utility that wraps quickly two or more mp3 files in one
single large playable mp3, without losing filenames and ID3 informations
(and without need of decoding/encoding).

%prep
%setup -n %name-%version
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README AUTHORS
%_bindir/%name
%_man1dir/*

%changelog
* Wed Apr 27 2011 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- initial build for ALT Linux Sisyphus
