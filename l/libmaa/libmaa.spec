Name: libmaa
Version: 1.4.7
Release: alt1

Summary: Library providing many low-level data structures
License: MIT
Group: System/Libraries

Url: http://sourceforge.net/projects/dict/
Source: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: mk-configure >= 0.29.1

%description
The libmaa library provides many low-level data
structures, including hash tables, sets, lists, debugging support, and
memory management. Although libmaa was designed and implemented as a
foundation for the kheperalong, the data structures are generally
applicable to a wide range of programming problems.

%package devel
Summary: Development files of libmaa
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files of libmaa.

%package devel-doc
Summary: Documentation for libmaa
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains development documentation for libmaa.

%prep
%setup

%define env \
unset MAKEFLAGS \
export PREFIX=%prefix \
export LIBDIR=%_libdir \
export SYSCONFDIR=%_sysconfdir \
export MANDIR=%_mandir

%build
%env
mkcmake

%check
%env
mkcmake test

%install
%env
export DESTDIR=%buildroot
mkcmake install

install -d %buildroot%_docdir/%name
install -p -m644 doc/*.ps %buildroot%_docdir/%name

%files
%doc doc/NEWS README doc/LICENSE doc/TODO
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-doc
%doc doc/libmaa.600dpi.ps

%changelog
* Sun May 17 2020 Aleksey Cheusov <cheusov@altlinux.org> 1.4.7-alt1
- Version 1.4.7

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- NMU: 1.3.1 (gcc-4.6 ready)

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0
- Disabled devel-static package

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Rebuilt for soname set-versions

* Mon Jun 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

