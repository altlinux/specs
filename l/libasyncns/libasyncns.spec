Name: libasyncns
Version: 0.8
Release: alt2

Summary: Asyncronous name service query library
License: LGPLv2.1+
Group: System/Libraries
Url: http://0pointer.de/lennart/projects/libasyncns/

Source0: %name-%version.tar.gz
Source1: %name.ver

Patch0: libasyncns-alt-version-script.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Oct 31 2009
BuildRequires: doxygen

%description
libasyncns is a C library for Linux/Unix for executing name service queries
asynchronously. It is an asynchronous wrapper around getaddrinfo(3) and
getnameinfo(3) from the libc.

%package devel
Summary: Development files for %name
Group: Development/C

Requires: %name = %version-%release

%description devel
libasyncns is a C library for Linux/Unix for executing name service queries
asynchronously. It is an asynchronous wrapper around getaddrinfo(3) and
getnameinfo(3) from the libc.

This package contains development files for libasyncns.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C

BuildArch: noarch

%description devel-doc
libasyncns is a C library for Linux/Unix for executing name service queries
asynchronously. It is an asynchronous wrapper around getaddrinfo(3) and
getnameinfo(3) from the libc.

This package contains doxygen documentation for libasyncns.

%prep
%setup -q
%patch0 -p1
cp %SOURCE1 libasyncns/

%build
%autoreconf
%configure \
	--disable-static \
	--enable-shared
%make_build
make doxygen

%install
%make_install DESTDIR=%buildroot install

%files
%doc README doc/README.html doc/style.css
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/asyncns.h
%_pkgconfigdir/libasyncns.pc

%files devel-doc
%doc doxygen/html

%changelog
* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2
- Rebuilt for soname set-versions

* Sat Oct 31 2009 Igor Zubkov <icesik@altlinux.org> 0.8-alt1
- 0.7 -> 0.8
- devel-doc subpackage is noarch now

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 0.7-alt2
- apply patch from repocop
- buildreq

* Thu Jan 01 2009 Alexander Myltsev <avm@altlinux.ru> 0.7-alt1
- new version (to satisfy the requirement of python-libasyncns).

* Tue Aug 07 2007 Igor Zubkov <icesik@altlinux.org> 0.3-alt2
- update summary (closes #11977)

* Tue Jun 05 2007 Igor Zubkov <icesik@altlinux.org> 0.3-alt1
- 0.2 -> 0.3

* Thu Mar 01 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt2
- fix build on x86_64 (thanks to ldv@)

* Sun Feb 18 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt1
- 0.1 -> 0.2

* Thu May 04 2006 Igor Zubkov <icesik@altlinux.ru> 0.1-alt2
- add post/postun sections for ldconfig

* Fri Apr 28 2006 Igor Zubkov <icesik@altlinux.ru> 0.1-alt1
- Initial build for Sisyphus
