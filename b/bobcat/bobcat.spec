%define _unpackaged_files_terminate_build 1
%define sover 5

Name:    bobcat
Version: 5.11.01
Release: alt1

Summary: Library of C++ classes and templates handling child processes, streams/sockets, shared memory, config files, etc.
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
%summary

%package -n lib%name%sover
Summary: Library of C++ classes and templates handling child processes, streams/sockets, shared memory, config files, etc.
Group:   System/Libraries
Provides: %name = %EVR

%description -n lib%name%sover
%summary

%package -n lib%name-devel
Summary: Library of C++ classes and templates handling child processes, streams/sockets, shared memory, config files, etc.
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
* Fri Sep 27 2024 Artem Semenov <savoptik@altlinux.org> 5.11.01-alt1
- Initial build for Sisyphus
- SSL updated to build with openssl3
