%define _localstatedir %_var
%global libmajor 2

Summary: POSIX threads C++ access library
Name: clthreads
Version: 2.4.0
Release: alt1
License: LGPLv2+
Group: Development/Other
Url: http://kokkinizita.linuxaudio.org/linuxaudio/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%name-%version.tar.bz2
BuildRequires: gcc-c++

%description
Clthreads is a C++ wrapper library around the POSIX threads API.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Clthreads is a C++ wrapper library around the POSIX threads API. This package
contains libraries and header files for developing applications that use
%name.

%prep
%setup

# No need to call ldconfig during packaging
%__subst '\|/sbin/ldconfig|d' Makefile

# Preserve timestamps
%__subst 's|/install|/install -p|' Makefile
# fix romlint warnings BZ#751466
%__subst 's|-lpthread|-lpthread -lrt|' Makefile

%build
%make_build

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
make PREFIX=%buildroot%prefix LIBDIR=%_lib install

# create .so.x link
ln -s lib%name.so.%version %buildroot%_libdir/lib%name.so.%libmajor

%files
%doc AUTHORS COPYING
%_libdir/lib%name.so.*

%files devel
%_includedir/%name.h
%_libdir/lib%name.so

%changelog
* Sun May 21 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Linux Sisyphus.
