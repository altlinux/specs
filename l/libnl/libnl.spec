Name: libnl
Version: 1.1
Release: alt2.qa2

Summary: library for applications dealing with netlink sockets
License: LGPL
Group: System/Libraries
Url: http://www.suug.ch/~tgr/libnl/
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar
Source1: %name.ver

Patch1: %name-1.1-alt-version-script.patch

%description
libnl is a library for applications dealing with netlink sockets. The library
provides an interface for raw netlink messaging and various netlink family
specific interfaces.

%package devel
Summary: header files for libnl, a netlink sockets library
Group: System/Libraries
Requires: %name = %version

%description devel
libnl is a library for applications dealing with netlink sockets.

This package contains header files for libnl.

%prep
%setup
%patch1 -p2
cp %SOURCE1 lib/%name.ver

%build
%configure
%make

%install
%makeinstall

%files
%_libdir/libnl.so.*

%files devel
%_libdir/libnl.so
%_includedir/netlink
%_pkgconfigdir/%name-1.pc

%changelog
* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.qa2
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.qa1.1
- Rebuilt for soname set-versions

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libnl
  * postun_ldconfig for libnl
  * postclean-05-filetriggers for spec file

* Wed Oct 29 2008 Alexander Myltsev <avm@altlinux.ru> 1.1-alt2
- fix building with glibc-2.8.

* Sat Mar 01 2008 Alex V. Myltsev <avm@altlinux.ru> 1.1-alt1
- new version as requested by altbug #14504.
- WARNING: upstream developers do not maintain their API/ABI,
  and I am not motivated enough to do anything about it.
  Use this package at your own risk.

* Sun Aug 13 2006 Alex V. Myltsev <avm@altlinux.ru> 1.0-alt1.svn30
- SVN version: builds on x86_64, etc.

* Sat Aug 12 2006 Alex V. Myltsev <avm@altlinux.ru> 1.0-alt0.pre5
- Initial build for Sisyphus.

