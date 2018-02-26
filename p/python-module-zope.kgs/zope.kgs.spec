%define oname zope.kgs
Name: python-module-%oname
Version: 1.2.0
Release: alt2.1
Summary: Known-Good-Set (KGS) Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.kgs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope dateutil docutils lxml zc.buildout
%py_requires zope.pagetemplate

%description
This package has been developed to support the maintenance of a stable set of
Zope project distributions. It manages the controlled packages configuration
file and supports the generation of buildout configuration files that can be
used by developers.

%package tests
Summary: Tests for zope.kgs
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package has been developed to support the maintenance of a stable set of
Zope project distributions. It manages the controlled packages configuration
file and supports the generation of buildout configuration files that can be
used by developers.

This package contains tests for zope.kgs.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

