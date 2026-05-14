%define _unpackaged_files_terminate_build 1
%define sover 2

Name:    rulex
Version: 3.9.1
Release: alt1

Summary: Russian pronunciation dictionary
License: GPL-2.0
Group:   Sound
Url:     https://github.com/poretsky/rulex
VCS:     https://github.com/poretsky/rulex.git

Source: %name-%version.tar

BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: make
BuildRequires: liblmdb-devel

%description
Russian pronunciation dictionary RuLex is aimed primarily for use
together with the Russian TTS engine Ru_tts. When it is installed you
can instruct Ru_tts to use the dictionary by the command line switch
"-s /usr/local/share/freespeech/rulex.db".

%package -n lib%name
Summary: Lib files to %name
Group: System/Libraries
Requires: %name-data
Provides: %name = %EVR
Obsoletes: librulex0 < %EVR

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: Development files to %name
Group: Development/C++

%description -n lib%name-devel
%summary

%package doc
Summary: Doc files to %name
Group: Documentation
BuildArch: noarch

%description doc
%summary

%package utils
Summary: Bin files to %name
Group: Other

%description utils
%summary

%package data
Summary: Data files fore %name
Group: Other

%description data
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

%files data
%_datadir/freespeech/%name.db

%files doc
%dir %_datadir/doc/%name
%_datadir/doc/%name/README*
%_man1dir/*
%_man3dir/*

%files -n lib%name
%_libdir/librulexdb.so.%sover
%_libdir/librulexdb.so.%sover.*

%files -n lib%name-devel
%_libdir/librulexdb.so
%_includedir/lexdb.h
%_includedir/rulexdb.h

%files utils
%_bindir/lexholder-ru
%_bindir/%name

%changelog
* Thu May 14 2026 Artem Semenov <savoptik@altlinux.org> 3.9.1-alt1
- Updated to new version 3.9.1
- Sover removed the tag is no longer needed.
- Changed buildreq from libdb6.1 to liblmdb

* Tue Oct 22 2024 Artem Semenov <savoptik@altlinux.org> 3.8.5-alt2
- Fixed summary for doc subpackage

* Wed Aug 21 2024 Artem Semenov <savoptik@altlinux.org> 3.8.5-alt1
- Initial build for Sisyphus (ALT bug: 51042)
