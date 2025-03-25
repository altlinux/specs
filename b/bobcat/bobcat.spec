%define _unpackaged_files_terminate_build 1
%define sover 5

Name:    bobcat
Version: 5.11.01
Release: alt2

Summary: C++ library for managing child processes, streams/sockets, shared memory and config files
License: GPL-3.0-or-later
Group:   Development/C++
Url:     https://gitlab.com/fbb-git/bobcat

Source: %name-%version.tar
Patch0: %name-%version-ssl3.patch
Patch1: %name-%version-uint8.patch
Patch2: %name-%version-randommt.patch

BuildRequires: icmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libssl-devel-static
BuildRequires: libX11-devel
BuildRequires: libmilter-devel
BuildRequires: libreadline-devel
BuildRequires: yodl

%description
Bobcat is an acronym of Brokken's Own Base Classes And Templates. It is a
shared library implementing C++ classes that are frequently used in software
developed by Frank Brokken.
All of Frank's C++ programs hosted at GitLab depend on bobcat.

The Bobcat library contains a variety of C++ classes and templates, some of
them based on well-known Design Patterns.

%package -n lib%name%sover
Summary: C++ library for managing child processes, streams/sockets, shared memory and config files
Group:   System/Libraries
Provides: %name = %EVR

%description -n lib%name%sover
%summary

%package -n lib%name-devel
Summary: Devel files for %name
Group:   Development/C++

%description -n lib%name-devel
%summary

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
pushd bobcat
./build libraries all
./build man 
popd

%install
mkdir -pv %buildroot
pushd bobcat
sed -i 's|"/usr/lib"|"%_libdir"|g' INSTALL.im
./build install lhdm %buildroot
popd

rm -v %buildroot%_libdir/lib%name.a

%ifarch i586
%set_verify_elf_method textrel=relaxed
%endif

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*
%_man3dir/*
%_man7dir/*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so
%dir %_datadir/doc/libbobcat5-dev
%_datadir/doc/libbobcat5-dev/*

%changelog
* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 5.11.01-alt2
- Added description
- Cleaned-up the spec

* Fri Sep 27 2024 Artem Semenov <savoptik@altlinux.org> 5.11.01-alt1
- Initial build for Sisyphus
- SSL updated to build with openssl3
