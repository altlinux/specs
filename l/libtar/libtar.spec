Name: libtar
Version: 1.2.11
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: C library for manipulating POSIX tar files
License: BSD
Group: System/Libraries

URL: http://www.feep.net/libtar/
Source: ftp://ftp.feep.net/pub/software/libtar/libtar-%version.tar.gz
Patch0: http://ftp.debian.org/debian/pool/main/libt/libtar/libtar_1.2.11-4.diff.gz
Patch1: libtar-1.2.11-tar_header.patch
Patch2: libtar-1.2.11-mem-deref.patch
Patch3: libtar-1.2.11-missing-protos.patch

# Automatically added by buildreq on Tue Mar 09 2010
BuildRequires: zlib-devel

%description
libtar is a C library for manipulating tar archives. It supports both the strict
POSIX tar format and many of the commonly-used GNU extensions.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the header files necessary for developing
programs which will use the %name library.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Patches and build magic borrowed from Fedora spec.

%build
%define ltversion %(echo %{version} | tr '.' ':')
subst 's/-rpath $(libdir)/-rpath $(libdir) -version-number %{ltversion}/' lib/Makefile.in
# sanitize the macro definitions so that aclocal can find them:
cd autoconf
sed '/^m4_include/d;s/ m4_include/ m4][_include/g' aclocal.m4 >psg.m4
rm -f acsite.m4 aclocal.m4
cd ..

cp -p /usr/share/libtool/config/config.sub autoconf
libtoolize --copy
aclocal -I autoconf
autoconf

%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_man3dir/*

%changelog
* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.2.11-alt1.1
- rebuild (with the help of girar-nmu utility)

* Wed Mar 10 2010 Victor Forsiuk <force@altlinux.org> 1.2.11-alt1
- Initial build.
