%define major_ver 1.2.0
%define minor_ver r43
%define sover 1

Name: libsmacker
Version: 1.2.0r43
Release: alt1
Summary: C library for decoding .smk Smacker Video files
License: LGPL-2.1-only
Group: Games/Other
Url: http://libsmacker.sourceforge.net/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: http://sourceforge.net/projects/libsmacker/files/libsmacker-1.2/%name-%version.tar.gz
BuildRequires: autoconf
BuildRequires: libtool

%description
libsmacker is a cross-platform C library which can be used for decoding Smacker
Video files produced by RAD Game Tools. Smacker Video was the king of video
middleware in the 1990s, and its 256-color compressed video format was used in
over 2600 software titles.

%package -n libsmacker%sover
Summary: C library for decoding .smk Smacker Video files
Group: System/Libraries

%description -n libsmacker%sover
libsmacker is a cross-platform C library which can be used for decoding Smacker
Video files produced by RAD Game Tools. Smacker Video was the king of video
middleware in the 1990s, and its 256-color compressed video format was used in
over 2600 software titles.

%package devel
Summary: Header files for libsmacker
Group: Development/C++
Requires: libsmacker%sover = %version

%description devel
Development and header files for libsmacker.

%prep
%setup -n %name-%version

%build
autoreconf -fiv
%configure

%install
%makeinstall_std
install -D -m0644 -t %buildroot%_includedir/ *.h
rm -f %buildroot%_libdir/*.{la,a}

%files -n libsmacker%sover
%doc COPYING
%doc README
%_libdir/libsmacker.so.%{sover}*

%files devel
%_includedir/smacker.h
%_includedir/smk*.h
%_libdir/libsmacker.so

%changelog
* Tue May 30 2023 Artyom Bystrov <arbars@altlinux.org> 1.2.0r43-alt1
- initial build for ALT Sisyphus

* Tue Jan 21 2020 Martin Hauke <mardnh@gmx.de>
- Initial package, version 1.1.1r35
