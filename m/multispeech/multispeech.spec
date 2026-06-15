%define _unpackaged_files_terminate_build 1
%define sover 5

Name:    multispeech
Version: 4.6.4
Release: alt3

Summary: Multilingual speech server for Emacspeak
License: GPL-2.0
Group:   Sound
Url:     https://github.com/poretsky/multispeech
VCS:     https://github.com/poretsky/multispeech.git

Source: %name-%version.tar
Source1: multispeech.blurb

Patch0: fix-spd-module-dir.patch

Requires: %name-common
Requires: ru_tts
Requires: mbrola-voices-en1

BuildRequires: libsndfile-devel
BuildRequires: libportaudio2-devel
BuildRequires: libsoundtouch-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-program_options-devel
BuildRequires: libpulseaudio-devel
BuildRequires: autoconf-archive
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: librutts-devel
BuildRequires: libbobcat-devel
BuildRequires: libspeechd-devel

%description
This speech server provides multilingual speech output for Emacspeak
using software TTS engines such as mbrola, espeak, ru_tts, etc.
At the moment English, German, French, Italian, Spanish,
Portuguese and Russian languages are supported.

The most prominent features are as follows:
- flexible configuration;
- easy adaptation to various speech engines;
- language autodetection capability;
- online voice control means.

%package -n lib%name%sover
Group: System/Libraries
Summary: Multilingual speech server - core shared library

%description -n lib%name%sover
This package provides core shared library.

%package -n speech-dispatcher-module-%name
Summary: Multilingual Speech Dispatcher backend
Group: Sound
Requires: speech-dispatcher
Requires: %name-common
Requires: ru_tts
Requires: mbrola-voices-en1

%description -n speech-dispatcher-module-%name
This module provides multilingual speech output for Speech Dispatcher
using software TTS engines such as mbrola, espeak, ru_tts, etc.
It is based on the Multispeech speech server.
At the moment English, German, French, Italian, Spanish,
Portuguese and Russian languages are supported.

The most prominent features are as follows:
- flexible configuration;
- easy adaptation to various speech engines;
- language autodetection capability;
- online voice control means.

%package doc
Summary: doc files for %name
Group: Documentation
BuildArch: noarch

%description doc
%summary

%package common
Summary: Multilingual speech server - common files
Group: Other
BuildArch: noarch

%description common
This package provides common configuration file used by all Multispeech
 implementations along with its documentation.

%prep
%setup
%autopatch -p1

%build
%autoreconf -if
%configure
%make_build

%install
%makeinstall_std sdmoduledir=%_libdir/speech-dispatcher-modules

rm -v %buildroot%_libdir/lib%name.so
install -D %SOURCE1 %buildroot%_datadir/emacs/site-lisp/emacspeak/blurbs/%name.blurb
mkdir -pv %buildroot%_datadir/emacs/site-lisp/emacspeak/servers
ln -s %_bindir/%name %buildroot%_datadir/emacs/site-lisp/emacspeak/servers/multispeech

%check
%make_build check

%files
%_bindir/%name
%_datadir/emacs/site-lisp/emacspeak/blurbs/%name.blurb
%_datadir/emacs/site-lisp/emacspeak/servers/multispeech

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files -n speech-dispatcher-module-%name
%_libdir/speech-dispatcher-modules/sd_%name

%files doc
%doc AUTHORS doc/interface.txt doc/prehistory.ChangeLog LICENSE README README.md
%_man1dir/*
%_man5dir/*
%dir %_datadir/doc/%name
%_datadir/doc/%name/*

%files common
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Tue Jun 16 2026 Artem Semenov <savoptik@altlinux.org> 4.6.4-alt3
- Packed the missing files.
- Updated descriptions

* Fri May 29 2026 Artem Semenov <savoptik@altlinux.org> 4.6.4-alt2
- Impruve make file

* Wed May 20 2026 Artem Semenov <savoptik@altlinux.org> 4.6.4-alt1
-- Updated to new version 4.6.4
- Package spleated to subpackages

* Sat Nov 01 2025 Artem Semenov <savoptik@altlinux.org> 4.6.3-alt1
- Updated to new version 4.6.3

* Mon Oct 13 2025 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt7
- Fixed install spd module

* Fri Oct 10 2025 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt6
- I586 build restored

* Mon Sep 22 2025 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt5
- Fixed build with bobcat 6.09.00

* Tue May 13 2025 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt4
- Excluded arch: %ix86

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt3
- Unnecessary dependencies removed

* Mon Dec 16 2024 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt2
- Fixed the build after the boost update

* Wed Sep 25 2024 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt1
- Initial build for Sisyphus (ALT bugg: 51045)
