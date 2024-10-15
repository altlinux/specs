%define _unpackaged_files_terminate_build 1
%define sover 0

Name:    rulex
Version: 3.8.5
Release: alt1

Summary: Russian pronunciation dictionary
License: GPL-2.0
Group:   Sound
Url:     https://github.com/poretsky/rulex

Source: %name-%version.tar

BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: make
BuildRequires: libdb6.1_tcl-devel

%description
Russian pronunciation dictionary RuLex is aimed primarily for use
together with the Russian TTS engine Ru_tts. When it is installed you
can instruct Ru_tts to use the dictionary by the command line switch
"-s /usr/local/share/freespeech/rulex.db".

%package -n lib%name%sover
Summary: Lib files to %name
Group: System/Libraries
Provides: lib%name = %EVR
Provides: %name = %EVR

%description -n lib%name%sover
%summary

%package -n lib%name-devel
Summary: Development files to %name
Group: Development/C++
Requires: %name = %EVR

%description -n lib%name-devel
%summary

%package doc
Summary: Doc files to %name
Group: Other
BuildArch: noarch
Requires: %name = %EVR

%description doc
%summary

%package utils
Summary: Doc files to %name
Group: Other
Requires: %name = %EVR

%description utils
%summary

%prep
%setup

%build
autoreconf -ifs
%configure --disable-static
%make_build db
%make_build lexholder

%install
%makeinstall_std

ln -s lexdb.h %buildroot%_includedir/rulexdb.h

%files doc
%dir %_datadir/doc/%name
%_datadir/doc/%name/README*
%_man1dir/*
%_man3dir/*

%files -n lib%name%sover
%_libdir/librulexdb.so.%sover
%_libdir/librulexdb.so.%sover.*
%_datadir/freespeech/%name.db

%files -n lib%name-devel
%_libdir/librulexdb.so
%_includedir/lexdb.h
%_includedir/rulexdb.h

%files utils
%_bindir/lexholder-ru
%_bindir/%name

%changelog
* Wed Aug 21 2024 Artem Semenov <savoptik@altlinux.org> 3.8.5-alt1
- Initial build for Sisyphus (ALT bug: 51042)
