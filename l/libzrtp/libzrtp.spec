Name: libzrtp
Version: 5.3.71
Release: alt1

Group: System/Libraries
Summary: BZRTP is an opensource implementation of ZRTP keys exchange protocol.
Url: https://gitlab.linphone.org/BC/public/bzrtp
License: GPL-2.0

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libbctoolbox-devel libsqlite3-devel libxml2-devel

%description
BZRTP is an opensource implementation of ZRTP keys exchange protocol.
The library written in C 89 is fully portable and can be executed
on many platforms including both ARM  processor and x86.

%package devel
Summary: Headers, libraries and docs for the bzrtp library
Group: Development/C
Requires: %name = %version-%release

%description devel
BZRTP is an opensource implementation of ZRTP keys exchange protocol.
The library written in C 89 is fully portable and can be executed
on many platforms including both ARM  processor and x86.

This package contains header files and development libraries needed to
develop programs using the oRTP library.

%prep
%setup
%patch0 -p1

%build
%cmake -GNinja -Wno-dev -DBUILD_SHARED_LIBS=TRUE
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc *.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_datadir/BZRTP

%changelog
* Fri Aug 02 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.71-alt1
- new version.

* Thu Nov 22 2018 Alexei Takaseev <taf@altlinux.org> 1.0.6-alt2
- Fix build with gcc8

* Wed Apr 25 2018 Alexei Takaseev <taf@altlinux.org> 1.0.6-alt1
- initial build for Sisyphus
