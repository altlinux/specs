%define oname z3c.ptcompat
Name: python-module-%oname
Version: 1.0
Release: alt1.bzr20111010
Summary: Compatibility-layer for Zope Page Template engines
License: ZPLv2.1
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:z3c.ptcompat
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
This package implements a compatibility-layer between the following
Zope Page Template engines:

 * z3c.pt
 * zope.pagetemplate

If the environment-variable ``PREFER_Z3C_PT`` is set to a true value,
the ``z3c.pt`` engine will be used instead of ``zope.pagetemplate``.

%package tests
Summary: Tests for z3c.ptcompat
Group: Development/Python
Requires: %name = %version-%release
%py_requires lxml z3c.pt zope.app.form zope.app.pagetemplate
%py_requires zope.app.publisher zope.tal zope.testing zope.viewlet

%description tests
This package implements a compatibility-layer between the following
Zope Page Template engines:

 * z3c.pt
 * zope.pagetemplate

If the environment-variable ``PREFER_Z3C_PT`` is set to a true value,
the ``z3c.pt`` engine will be used instead of ``zope.pagetemplate``.

This package contains tests for z3c.ptcompat

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.bzr20111010
- Version 1.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.8-alt1.bzr20110323.2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.8-alt1.bzr20110323.2
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.8-alt1.bzr20110323.1
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.8-alt1.bzr20110323
- Initial build for Sisyphus

