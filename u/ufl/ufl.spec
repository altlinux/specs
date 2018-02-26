Name:           ufl
Version:        1.1.dev
Release:        alt1.bzr20120503
Summary:        Unified Form Language
Group:          Development/Tools
License:        LGPL v3+
URL:            http://www.fenics.org/
# bzr branch lp:ufl
Source:  %name-%version.tar.gz
Source1: http://www.fenics.org/pub/documents/ufl/ufl-user-manual/ufl-user-manual.pdf
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: python-module-%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel

%description
Unified Form Language.

%package doc
Summary: User manual for UFL
Group: Development/Documentation
BuildArch: noarch

%description doc
User manual for UFL (Unified Form Language).

%package -n python-module-%name
Summary: Python module of UFL
Group: Development/Python
BuildArch: noarch

%description -n python-module-%name
Python module of UFL (Unified Form Language).

%prep
%setup

%build
%python_build

%install
%python_install

install -d %buildroot%_docdir/%name
install -p -m644 %SOURCE1 %buildroot%_docdir/%name

%files
%doc COPYING ChangeLog README TODO
%_bindir/*
%_man1dir/*

%files doc
%_docdir/%name

%files -n python-module-%name
%python_sitelibdir_noarch/*

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.dev-alt1.bzr20120503
- New snapshot

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.dev-alt1.bzr20111207
- Version 1.0+

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.rc1-alt1.bzr20111122
- Version 1.0.rc1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.beta-alt1.bzr20110725.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.beta-alt1.bzr20110725
- Version 1.0.beta

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.bzr20110414
- Version 0.9.0

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.bzr20101117
- Version 0.5.4

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.bzr20100716
- Version 0.5.3

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.bzr20100614
- Version 0.5.2

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.bzr20091204
- Version 0.4.1

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.hg20090831.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.hg20090831
- Snapshot 20090831

* Wed Aug 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.hg20090819
- New snapshot

* Wed Jul 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Version 0.3.0

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
