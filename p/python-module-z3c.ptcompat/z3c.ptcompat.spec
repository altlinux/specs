%define oname z3c.ptcompat

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.a2.git20130707.1
Summary: Compatibility-layer for Zope Page Template engines
License: ZPLv2.1
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/z3c.ptcompat.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This package implements a compatibility-layer between the following
Zope Page Template engines:

 * z3c.pt
 * zope.pagetemplate

If the environment-variable ``PREFER_Z3C_PT`` is set to a true value,
the ``z3c.pt`` engine will be used instead of ``zope.pagetemplate``.

%package -n python3-module-%oname
Summary: Compatibility-layer for Zope Page Template engines
Group: Development/Python3

%description -n python3-module-%oname
This package implements a compatibility-layer between the following
Zope Page Template engines:

 * z3c.pt
 * zope.pagetemplate

If the environment-variable ``PREFER_Z3C_PT`` is set to a true value,
the ``z3c.pt`` engine will be used instead of ``zope.pagetemplate``.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.ptcompat
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires lxml z3c.pt zope.app.form zope.app.pagetemplate
%py3_requires zope.app.publisher zope.tal zope.testing zope.viewlet

%description -n python3-module-%oname-tests
This package implements a compatibility-layer between the following
Zope Page Template engines:

 * z3c.pt
 * zope.pagetemplate

If the environment-variable ``PREFER_Z3C_PT`` is set to a true value,
the ``z3c.pt`` engine will be used instead of ``zope.pagetemplate``.

This package contains tests for z3c.ptcompat

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a2.git20130707.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a2.git20130707
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a2.git20130707
- Version 2.0.0a2

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

