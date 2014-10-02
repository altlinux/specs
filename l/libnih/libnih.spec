Name: libnih
Version: 1.0.3
Release: alt1

Summary: Lightweight application development library
License: %gpl2only
Group: System/Libraries
URL: https://launchpad.net/libnih
Source: %name-%version.tar

Patch: %name-%version-%release.patch
Patch1: 0001-Fallback-to-lstat-if-dirent.d_type-is-not-available-.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libdbus-devel libexpat-devel

# For tests
BuildRequires: /dev/pts
BuildRequires: dbus

%description
libnih is a small library for C application development containing
functions that, despite its name, are not implemented elsewhere in
the standard library set.
libnih is roughly equivalent to other C libraries such as glib, except
that its focus is on a small size and intended for applications that sit
very low in the software stack, especially outside of /usr.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package dbus
Summary: %name D-Bus Bindings Library
Group: System/Libraries
Requires: %name = %version-%release

%description dbus
%name-dbus is a D-Bus bindings library that integrates with the main
loop provided by %name.

%package dbus-devel
Summary: Development files for %name-dbus
Group: Development/C
Requires: %name-dbus = %version-%release
Requires: %name-devel = %version-%release

# libnih uses private glibc symbol __abort_msg
%filter_from_requires /^libc\.so\.6(GLIBC_PRIVATE)\((64bit)\)\?$/d

%description dbus-devel
This package contains libraries and header files for
developing applications that use %name-dbus.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%check
make check

%files
%_libdir/%name.so.*

%files devel
%_includedir/%name.h
%_includedir/nih/
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_aclocaldir/%name.m4

%files dbus
%_libdir/%name-dbus.so.*

%files dbus-devel
%_bindir/nih-dbus-tool
%_man1dir/nih-dbus-tool.1*
%_includedir/%name-dbus.h
%_includedir/nih-dbus/
%_libdir/%name-dbus.so
%_libdir/pkgconfig/%name-dbus.pc

%changelog
* Mon Sep 22 2014 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- Fix pkgconfig directory path.
- Add "Fallback to lstat" patch from Debian.
- Initial build.

