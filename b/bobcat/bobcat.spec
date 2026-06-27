%define _unpackaged_files_terminate_build 1
%define sover 6

Name:    bobcat
Version: 6.14.00
Release: alt1

Summary: C++ library for managing child processes, streams/sockets, shared memory and config files
License: GPL-3.0-or-later
Group:   Development/C++
Url:     https://gitlab.com/fbb-git/bobcat

Source: %name-%version.tar

# alt patches
Patch0: %name-%version-i586-sys_t-cast.patch

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

%package doc
Summary: Doc files for %name
BuildArch: noarch
Group: Other

%description doc
%summary

%prep
%setup
%ifarch i586
%patch0 -p1
%endif

%build
%ifarch i586
%add_optflags -Wno-error=return-local-addr
%endif

export CXXFLAGS="%optflags --std=c++2a -Werror -fdiagnostics-color=never -ffat-lto-objects"
export CXX="g++"
sed -i 's/^#define CXX/\/\/ #define CXX/g' bobcat/INSTALL.im
sed -i 's/^#define CXXFLAGS/\/\/ #define CXXFLAGS/g' bobcat/INSTALL.im
sed -i 's/^#define DOC/\/\/ #define DOC/g' bobcat/INSTALL.im
sed -i 's/^#define HDR/\/\/ #define HDR/g' bobcat/INSTALL.im
sed -i 's/^#define LIB/\/\/ #define LIB/g' bobcat/INSTALL.im
echo "/* created during rpmbuild */"                            >> bobcat/INSTALL.im
echo "#define CXX         \"${CXX} -std=c++2a\""                           >> bobcat/INSTALL.im
echo "#define CXXFLAGS    \"${CXXFLAGS} -std=c++2a\""                      >> bobcat/INSTALL.im
echo "#define DOC         \"%_docdir/bobcat\""   >> bobcat/INSTALL.im
echo "#define HDR         \"%_includedir/bobcat\""          >> bobcat/INSTALL.im
echo "#define LIB         \"%_libdir\""                       >> bobcat/INSTALL.im
export ICMAKE_CPPSTD=--std=c++2a

pushd bobcat
./build libraries all
./build man 
popd

%install
mkdir -pv %buildroot
pushd bobcat
./build install lhdm %buildroot
popd

rm -v %buildroot%_libdir/lib%name.a

%ifarch i586
%set_verify_elf_method textrel=relaxed
%endif

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so

%files doc
%_docdir/%name
%_man3dir/*
%_man7dir/*

%changelog
* Mon Jun 22 2026 Artem Semenov <savoptik@altlinux.org> 6.14.00-alt1
- Updated to new version 6.14.00

* Sat May 23 2026 Artem Semenov <savoptik@altlinux.org> 6.13.00-alt1
- Updated to new version 6.13.00

* Wed Apr 22 2026 Artem Semenov <savoptik@altlinux.org> 6.12.01-alt1
- Updated to new version 6.12.01

* Wed Apr 15 2026 Artem Semenov <savoptik@altlinux.org> 6.12.00-alt1
- Updated to new version 6.12.00

* Wed Nov 12 2025 Artem Semenov <savoptik@altlinux.org> 6.11.00-alt1
- Updated to new version 6.11.00

* Fri Oct 10 2025 Artem Semenov <savoptik@altlinux.org> 6.10.00-alt2
- Fixed build on I586

* Thu Oct 09 2025 Artem Semenov <savoptik@altlinux.org> 6.10.00-alt1
- Updated to new version 6.10.00

* Sun Sep 21 2025 Artem Semenov <savoptik@altlinux.org> 6.09.00-alt1
- Updated to new version 6.09.00

* Tue May 13 2025 Artem Semenov <savoptik@altlinux.org> 6.08.00-alt1
- Updated to new version 6.08.00

* Tue May 13 2025 Artem Semenov <savoptik@altlinux.org> 6.07.01-alt1
- Updated to new version 6.07.01

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 5.11.01-alt2
- Added description
- Cleaned-up the spec

* Fri Sep 27 2024 Artem Semenov <savoptik@altlinux.org> 5.11.01-alt1
- Initial build for Sisyphus
- SSL updated to build with openssl3
