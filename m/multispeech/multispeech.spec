%define _unpackaged_files_terminate_build 1
%define sover 5

Name:    multispeech
Version: 4.6.2
Release: alt1

Summary: Multilingual speech server for Emacspeak
License: GPL-2.0
Group:   Sound
Url:     https://github.com/poretsky/multispeech

Source: %name-%version.tar
Requires: ru_tts
Requires: mbrola-voices-en1

BuildRequires: libsndfile-devel
BuildRequires: libportaudio2-devel
BuildRequires: libsoundtouch-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-locale-devel
BuildRequires: boost-program_options-devel
BuildRequires:  libboost_iostreams1.85.0
BuildRequires:  libboost_regex1.85.0
BuildRequires:  libboost_thread1.85.0
BuildRequires: libpulseaudio-devel
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
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

%prep
%setup

%build
%autoreconf -if
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

mkdir -pv %buildroot%_libdir/speech-dispatcher-modules
mv -v %buildroot%_bindir/sd_%name %buildroot%_libdir/speech-dispatcher-modules/

%files
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/%name
%_man1dir/*
%_man5dir/*
%dir %_datadir/doc/%name
%_datadir/doc/%name/*

%files -n lib%name%sover
%_libdir/lib%name.so
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*
%_libdir/speech-dispatcher-modules/sd_%name

%changelog
* Wed Sep 25 2024 Artem Semenov <savoptik@altlinux.org> 4.6.2-alt1
- Initial build for Sisyphus (ALT bugg: 51045)
