Name: libtar
Version: 1.2.20
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: C library for manipulating POSIX tar files
License: BSD
Group: System/Libraries
Url: http://www.feep.net/libtar/

#Source: ftp://ftp.feep.net/pub/software/libtar/%name-%version.tar.gz
# VCS: http://repo.or.cz/libtar.git
# 6d0ab4c7
Source: %name-%version.tar
# (fc) don't strip while install
Patch: libtar-1.2.11-bz729009.patch

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
%patch -p1

# set correct version for .so build
%define ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %ltversion/' \
lib/Makefile.in

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_libdir/%name.so.*

%files devel
%_includedir/*.h
%_libdir/%name.so
%_man3dir/*

%changelog
* Thu Nov 13 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.20-alt1
- 1.2.20
- removed obsolete patches

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.11-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.2.11-alt1.1
- rebuild (with the help of girar-nmu utility)

* Wed Mar 10 2010 Victor Forsiuk <force@altlinux.org> 1.2.11-alt1
- Initial build.
