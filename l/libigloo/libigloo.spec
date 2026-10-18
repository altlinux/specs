%define _unpackaged_files_terminate_build 1
%define sover 0

Name: libigloo
Version: 0.9.5
Release: alt1

Summary: Common C framework by the Icecast project
License: LGPL-2.0-or-later
Group: System/Libraries
Url: https://icecast.org/

# Source-url: https://downloads.xiph.org/releases/igloo/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: librhash-devel

%description
libigloo is a generic C framework. It is developed and used by the
Icecast project.

%package -n %name%sover
Summary: Common C framework by the Icecast project
Group: System/Libraries

%description -n %name%sover
libigloo is a generic C framework. It is developed and used by the
Icecast project.

This package contains the shared library.

%package devel
Summary: Development files of libigloo
Group: Development/C
Requires: %name%sover = %EVR

%description devel
libigloo is a generic C framework. It is developed and used by the
Icecast project.

This package contains the header files and the pkg-config file needed
to build programs with libigloo.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make_build check

%files -n %name%sover
%doc NEWS README
%_libdir/libigloo.so.%sover
%_libdir/libigloo.so.%sover.*

%files devel
%_includedir/igloo
%_libdir/libigloo.so
%_pkgconfigdir/igloo.pc

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- initial build for Sisyphus

