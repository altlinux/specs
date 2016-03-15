%define oname repoze.dvselect

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt3.1
Summary: Select Deliverance rules / theme based on URI
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.dvselect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze deliverance repoze.urispace

%description
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

%package -n python3-module-%oname
Summary: Select Deliverance rules / theme based on URI
Group: Development/Python3
%py3_requires repoze deliverance repoze.urispace

%description -n python3-module-%oname
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.dvselect
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

This package contains tests for repoze.dvselect.

%package tests
Summary: Tests for repoze.dvselect
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

This package contains tests for repoze.dvselect.

%package docs
Summary: Documentation for repoze.dvselect
Group: Development/Documentation
BuildArch: noarch

%description docs
This package is a prototype of using repoze.urispace to select
Deliverance themes and rules based on the URI of the request.

This package contains documentation for repoze.dvselect.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files docs
%doc docs/*.rst
%doc docs/docroot
%doc docs/etc

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

