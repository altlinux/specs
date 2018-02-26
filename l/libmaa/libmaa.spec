Name: libmaa
Version: 1.3.1
Release: alt1

Summary: Client/server software, human language dictionary databases, tools for DICT protocol
License: GPLv2, LGPLv2
Group: System/Libraries

Url: http://sourceforge.net/projects/dict/
Source: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%description
Client/server software, human language dictionary databases, and tools
supporting the DICT protocol (RFC 2229).

%package devel
Summary: Development files of libmaa
Group: Development/C
Requires: %name = %version-%release

%description devel
Client/server software, human language dictionary databases, and tools
supporting the DICT protocol (RFC 2229).

This package contains development files of libmaa.

%package devel-static
Summary: Static library of libmaa
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Client/server software, human language dictionary databases, and tools
supporting the DICT protocol (RFC 2229).

This package contains static library of libmaa.

%package devel-doc
Summary: Documentation for libmaa
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
Client/server software, human language dictionary databases, and tools
supporting the DICT protocol (RFC 2229).

This package contains development documentation for libmaa.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

install -d %buildroot%_docdir/%name
install -p -m644 doc/*.ps %buildroot%_docdir/%name

%files
%doc COPYING* ChangeLog NEWS README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

#files devel-static
#_libdir/*.a

%files devel-doc
%_docdir/%name

%changelog
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

