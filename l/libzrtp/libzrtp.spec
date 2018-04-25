Name: libzrtp
Version: 1.0.6
Release: alt1

Group: System/Libraries
Summary: BZRTP is an opensource implementation of ZRTP keys exchange protocol.
Url: http://www.linphone.org/releases/sources/bzrtp
License: GPLv2

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
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
./autogen.sh
%configure \
    --disable-static \
    --enable-shared
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog NEWS README.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*

%changelog
* Wed Apr 25 2018 Alexei Takaseev <taf@altlinux.org> 1.0.6-alt1
- initial build for Sisyphus
