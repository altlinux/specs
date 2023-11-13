%define rname mcl

Name: lib%rname
Version: 0.1.13
Release: alt1

Summary: A collection of C++20 utilities which is common to a number of merry's projects.
License: MIT
Group: System/Libraries

Url: https://github.com/merryhime/%rname
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/merryhime/%rname/archive/refs/tags/%version/%rname-%version.tar.gz
Source: %rname-%version.tar

Patch0: %rname-soname-alt.patch

BuildRequires: catch2-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libfmt-devel

%description
A collection of C++20 utilities which is common to a number of merry's projects.

%package devel
Summary: Header files for %name
Group: Development/C

%description devel
Header files for %name

%prep
%setup -n %rname-%version
%patch0 -p1

%build
%cmake \
	-DCMAKE_INSTALL_LIBDIR:PATH=%_libdir \
	-DBUILD_SHARED_LIBS:BOOL=TRUE
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README
%_libdir/%name.so.*

%files devel
%_libdir/cmake/%rname
%_libdir/%name.so
%_includedir/%rname

%changelog
* Mon Nov 13 2023 Nazarov Denis <nenderus@altlinux.org> 0.1.13-alt1
- New version 0.1.13.

* Mon May 29 2023 Nazarov Denis <nenderus@altlinux.org> 0.1.12-alt1
- Initial build for ALT Linux
