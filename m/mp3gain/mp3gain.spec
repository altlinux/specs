Name: mp3gain
Version: 1.4.6
Release: alt1

Summary: MP3Gain analyzes and adjusts mp3 files so that they have the same volume.
Group: Sound
License: LGPL

Source: %name-%version.tar.bz2
Packager: Afanasov Dmitry <ender@altlinux.ru>

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same volume.

%prep
%setup -q

%build
make

%install
install -pD -m755 mp3gain %buildroot%_bindir/%name
install -pD -m644 lgpl.txt %buildroot%_docdir/%name-%version/LGPL.txt

%post
%pre

%files
%_docdir/%name-%version
%_bindir/%name

%changelog
* Mon Oct 06 2008 Afanasov Dmitry <ender@altlinux.org> 1.4.6-alt1
- initial build

