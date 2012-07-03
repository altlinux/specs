Name: libmlx4
Version: 1.0
Release: alt5.qa2

Summary: Mellanox InfiniBand HCA Userspace Driver
License: GPL/BSD
Group: System/Libraries

Url: http://openib.org/
Source: http://openib.org/downloads/%name-%version.tar
Packager: Stanislav Ievlev <inger@altlinux.org>

BuildRequires(pre): rpm-build-compat
BuildPreReq: libibverbs-devel-static >= 1.1.2
Requires: libibverbs >= 1.1.2

# Automatically added by buildreq on Tue Aug 21 2007
BuildRequires: gcc-c++ glibc-devel-static libibverbs-devel

%description
libmlx4 provides a device-specific userspace driver for Mellanox
ConnectX HCAs for use with the libibverbs library.

%package devel
Summary: Development files for the libmlx4 driver
Group: Development/C
Requires: %name = %version-%release

%description devel
Develpoment files for the libmlx4 driver.

%package devel-static
Summary: Static development files for the libmlx4 driver
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static version of libmlx4 that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

install -d %buildroot%_includedir
install -p -m644 src/*.h %buildroot%_includedir

#for biarch
mv	%buildroot%_sysconfdir/libibverbs.d/mlx4.driver \
	%buildroot%_sysconfdir/libibverbs.d/mlx4.driver-%_host_cpu

%files
%doc AUTHORS COPYING README
%_sysconfdir/libibverbs.d/*
%_libdir/libmlx4-rdmav2.so

%files devel
%_libdir/libmlx4.so
%_includedir/*

%files devel-static
%_libdir/libmlx4.a

%changelog
* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt5.qa2
- Rebuilt for debuginfo

* Sun Oct 17 2010 Michael Shigorin <mike@altlinux.org> 1.0-alt5.qa1
- fix FTBFS (macro name)
- minor spec cleanup according to packaging policy

* Tue Aug 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0-alt5
- OFED-1.5.1

* Tue Oct 13 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt4
- OFED-1.4.2

* Fri May 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Add devel package

* Fri Nov 07 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- improve biarch support

* Thu Sep 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- OFED 1.3.1

* Tue Aug 21 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial Release
