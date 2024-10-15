%define _unpackaged_files_terminate_build 1
%define sover 7

Name:    ru_tts
Version: 6.2.3
Release: alt1
Epoch: 1

Summary: Compact and portable Russian speech synthesizer
License: MIT
Group:   Sound
Url:     https://github.com/poretsky/ru_tts

Requires: sox

Source: %name-%version.tar

BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: make
BuildRequires: librulex-devel

%description
An alternative implementation of the Phonemophone-5 Russian speech
synthesizer by the international laboratory of intelligent systems
BelSInt (the Speech Recognition and Synthesis Lab of the Institute of
Technical Cybernetics of the Academy of Sciences of the Byelorussian
SSR). The source code of the original implementation has been lost.
This implementation is the result of a reverse engineering of
the SDRV resident speech driver for MS-DOS, and it is officially
approved for publication under a free license by Boris Lobanov

%package -n librutts%sover
Summary: Lib files for %name
Group: System/Libraries
Provides: librutts = %EVR

%description -n librutts%sover
%summary

%Package -n librutts-devel
Summary: Devel files for %name
Group: Development/C++
Requires: librutts = %EVR

%description -n librutts-devel
%summary

%prep
%setup

%build
%autoreconf -ifs
%configure --with-dictionary --disable-static
%make_build

%install
%makeinstall_std DESTDIR=%buildroot PREFIX=%prefix

%files
%dir %_datadir/doc/ru-tts
%_datadir/doc/ru-tts/README*
%_bindir/ru_speak
%_bindir/ru_tts
%_man1dir/*
%_man3dir/*

%files -n librutts%sover
%_libdir/librutts.so.%sover
%_libdir/librutts.so.%sover.*

%files -n librutts-devel
%_includedir/ru_tts.h
%_libdir/librutts.so

%changelog
* Thu Aug 08 2024 Artem Semenov <savoptik@altlinux.org> 1:6.2.3-alt1
- Build new version and change license (ALT bug: 51041)

* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 20110405-alt1
- Removed old version
- tts-devel buildreq replaced by rpm-macros-tts

* Wed Dec 22 2010 Michael Pozhidaev <msp@altlinux.ru> 20101222-alt1
- Temporarily added old synthesizer binary

* Fri Nov 26 2010 Michael Pozhidaev <msp@altlinux.ru> 20101126-alt1
- VoiceMan configuration entry updated for VoiceMan version 1.5.0
- Package ru_tts-lexicon renamed to ru_tts-data

* Thu Dec 11 2008 Michael Pozhidaev <msp@altlinux.ru> 20081211-alt1
- Lexicon file moved to the separate noarch subpackage
- Added more legal permission from the author (Igor Poretsky)
- Added Russian descriptions

* Fri Sep 05 2008 Michael Pozhidaev <msp@altlinux.ru> 20080905-alt1
- Added VoiceMan configuration file

* Wed Sep 20 2006 Michael Pozhidaev <msp@altlinux.ru> 1.0-alt1
- initial rpm
