
Name: textlus-rhvoice
Version: 0.99
Release: alt1
Summary: The set of scripts to read text books with Textlus and RHVoice speech synthesizer
BuildArch: noarch
Group: Sound
License: %gpl3plus
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildRequires: rpm-build-licenses
Requires: textlus = %version-%release RHVoice sox lame

Source: %name-%version.tar.gz

%description 
You can use this package to read Russian books from text
files. Listening modes include the mode to listen in real-time as well
as mode for saving speech to set of mp3 files. For real-time moed the
bookmark support is available.

%prep
%setup -q
%build
%install
%__install -pD -m755 read-book %buildroot%_bindir/read-book
%__install -pD -m755 make-mp3-book %buildroot%_bindir/make-mp3-book
%__install -d -m755 %buildroot%_datadir/textlus
%__install -pD -m755 make-mp3-book-impl %buildroot%_datadir/textlus/make-mp3-book-impl

%files
%_bindir/*
%_datadir/textlus

%changelog
* Thu Jun 28 2012 Michael Pozhidaev <msp@altlinux.ru> 0.99-alt1
- Initial package
