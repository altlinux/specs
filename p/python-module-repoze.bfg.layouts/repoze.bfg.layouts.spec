%define oname repoze.bfg.layouts

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt3
Summary: Dynamic layouts for repoze.bfg
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.layouts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.bfg repoze.bfg.skins zope.configuration
%py_requires chameleon.html

%description
repoze.bfg.layouts provides a site layout story for the repoze.bfg
framework. It uses familiar technologies like CSS3 to dynamically inject
dynamic content into static HTML.

%package -n python3-module-%oname
Summary: Dynamic layouts for repoze.bfg
Group: Development/Python3
%py3_requires repoze.bfg repoze.bfg.skins zope.configuration
%py3_requires chameleon.html

%description -n python3-module-%oname
repoze.bfg.layouts provides a site layout story for the repoze.bfg
framework. It uses familiar technologies like CSS3 to dynamically inject
dynamic content into static HTML.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg.layouts
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.bfg.layouts provides a site layout story for the repoze.bfg
framework. It uses familiar technologies like CSS3 to dynamically inject
dynamic content into static HTML.

This package contains tests for repoze.bfg.layouts.

%package tests
Summary: Tests for repoze.bfg.layouts
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.bfg.layouts provides a site layout story for the repoze.bfg
framework. It uses familiar technologies like CSS3 to dynamically inject
dynamic content into static HTML.

This package contains tests for repoze.bfg.layouts.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

