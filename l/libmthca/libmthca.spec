Name: libmthca
Version: 1.0.5
Release: alt2.qa2

Summary: Mellanox InfiniBand HCA Userspace Driver
License: GPL/BSD
Group: System/Libraries

Url: http://openib.org/
Source: http://openib.org/downloads/libmthca-1.0.5.tar
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildRequires(pre): rpm-build-compat
BuildPreReq: libibverbs-devel-static >= 1.1.2
Requires: libibverbs >= 1.1.2

# Automatically added by buildreq on Tue Aug 21 2007
BuildRequires: gcc-c++ glibc-devel-static libibverbs-devel

%description
libmthca provides a device-specific userspace driver for Mellanox HCAs
(MT23108 InfiniHost and MT25208 InfiniHost III Ex) for use with the
libibverbs library.

%package devel
Summary: Development files for the libmthca driver
Group: Development/C
Requires: %name = %version-%release libibverbs-devel

%description devel
Development files for the libmthca driver.

%package devel-static
Summary: Static development files for the libmthca driver
Group: Development/C
Requires: %name-devel = %version-%release libibverbs-devel-static

%description devel-static
Static version of libmthca that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup

%build
touch NEWS
%autoreconf
%configure
%make_build

%install
%makeinstall_std

install -d %buildroot%_includedir/%name
install -p -m644 src/*.h %buildroot%_includedir/%name

%files
%doc AUTHORS COPYING ChangeLog README
%_libdir/libmthca-rdmav2.so
%_sysconfdir/libibverbs.d/mthca.driver

%files devel
%_libdir/libmthca.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt2.qa2
- Rebuilt for debuginfo

* Sun Oct 17 2010 Michael Shigorin <mike@altlinux.org> 1.0.5-alt2.qa1
- fix FTBFS (macro name)
- minor spec cleanup according to packaging policy

* Tue Aug 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt2
- Rebuild (OFED 1.5.1)

* Fri May 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Version 1.0.5

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.0.4-alt2
- OFED 1.3.1

* Tue Aug 21 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.4-alt1
- Initial release
