%define _unpackaged_files_terminate_build 1
%define sover 5

Name:    multispeech
Version: 4.6.4
Release: alt2

Summary: Multilingual speech server for Emacspeak
License: GPL-2.0
Group:   Sound
Url:     https://github.com/poretsky/multispeech
VCS:     https://github.com/poretsky/multispeech.git

Source: %name-%version.tar

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
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: librutts-devel
BuildRequires: libbobcat-devel
BuildRequires: libspeechd-devel

%description
Multispeech was primarily designed as a multilingual speech server for Emacspeak,
but it can be useful in some other circumstances as well,
when multilingual speech feedback is needed.
For instance, it can work in conjunction with
Speech Dispatcher
as its backend module.

Multispeech utilizes third party speech synthesis software to perform
actual TTS transformation. Being capable to detect language by text
nature it can automatically choose an appropriate TTS for each one.
For the moment English, German, French, Italian, Spanish, Portuguese
and Russian languages are supported.

%package -n lib%name%sover
Group: System/Libraries
Summary: Lib files for %name

%description -n lib%name%sover
%summary

%package -n speech-dispatcher-module-%name
Summary: SPD module fore %name
Group: Sound
Requires: speech-dispatcher
Requires: %name-common
Requires: ru_tts
Requires: mbrola-voices-en1

%description -n speech-dispatcher-module-%name
%summary

%package doc
Summary: doc files for %name
Group: Documentation
BuildArch: noarch

%description doc
%summary

%package common
Summary: Common files for %name
Group: Other
BuildArch: noarch

%description common
%summary

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

%check
%make_build check

%files
%_bindir/%name

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
