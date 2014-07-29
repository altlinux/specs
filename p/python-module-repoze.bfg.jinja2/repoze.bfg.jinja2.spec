%define oname repoze.bfg.jinja2

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt3
Summary: Jinja2 template bindings for repoze.bfg
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.jinja2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPrereq: python-tools-2to3
%endif

%py_requires repoze.bfg jinja2 zope.interface zope.component

%description
These are bindings for the `Jinja2 templating system` for the
``repoze.bfg`` web framework.

%package -n python3-module-%oname
Summary: Jinja2 template bindings for repoze.bfg
Group: Development/Python3
%py3_requires repoze.bfg jinja2 zope.interface zope.component

%description -n python3-module-%oname
These are bindings for the `Jinja2 templating system` for the
``repoze.bfg`` web framework.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg.jinja2
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires repoze.bfg.testing

%description -n python3-module-%oname-tests
These are bindings for the `Jinja2 templating system` for the
``repoze.bfg`` web framework.

This package contains tests for repoze.bfg.jinja2.

%package tests
Summary: Tests for repoze.bfg.jinja2
Group: Development/Python
Requires: %name = %version-%release
%py_requires repoze.bfg.testing

%description tests
These are bindings for the `Jinja2 templating system` for the
``repoze.bfg`` web framework.

This package contains tests for repoze.bfg.jinja2.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*/tests
%exclude %python_sitelibdir/*/*/*/*/*/tests*

%files tests
%python_sitelibdir/*/*/*/tests
%python_sitelibdir/*/*/*/*/*/tests*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests
%exclude %python3_sitelibdir/*/*/*/*/*/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%python3_sitelibdir/*/*/*/*/*/tests*
%endif

%changelog
* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

