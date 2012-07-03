Name: instant
Version: 1.0.0
Release: alt1.bzr20120320
Summary: Instant inlining of C and C++ code in Python
Group: Development/Python
License: GPL v2.1 / BSD
URL: http://fenics.org/wiki/Instant
# lp:instant
Source: %name-%version.tar.gz
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: python-module-%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel

%description
Instant is a Python module that allows for instant inlining of C and
C++ code in Python.

%package doc
Summary: Documentation for Instant
Group: Development/Documentation
BuildArch: noarch

%description doc
Instant is a Python module that allows for instant inlining of C and
C++ code in Python.

This package contains development documentation for Instant.

%package -n python-module-%name
Summary: Scripts for Instant
Group: Development/Python
BuildArch: noarch

%description -n python-module-%name
Instant is a Python module that allows for instant inlining of C and
C++ code in Python.

This package contains python module of Instant.

%prep
%setup

%build
%python_build

%install
%python_build_install --optimize=2

install -d %buildroot%_docdir/%name
cp -fR doc/html* doc/Instant.html %buildroot%_docdir/%name/

%files
%doc AUTHORS COPYING ChangeLog README TODO
%_bindir/*
%_man1dir/*

%files doc
%_docdir/%name

%files -n python-module-%name
%python_sitelibdir_noarch/*

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20120320
- New snapshot

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20111207
- Version 1.0.0

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta2.bzr20111128
- 1.0-beta2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.10-alt1.bzr20110623.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.bzr20110623
- Version 0.9.10

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20110315
- Version 0.9.9

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.hg20101106
- New snapshot

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.hg20100716
- New snapshot

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.hg20100215
- Version 0.9.8

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.hg20090831.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.hg20090831
- Snapshot 20090831

* Wed Aug 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.hg20090819
- New version

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus

