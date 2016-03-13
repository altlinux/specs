%define oname BlastOff

%def_with python3

Name: python-module-%oname
Version: 0.3a2
Release: alt2.1
Summary: A Pylons application template providing a working site skeleton
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/BlastOff/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
A Pylons application template providing a working site skeleton
configured with SQLAlchemy, mako, repoze.who, ToscaWidgets, TurboMail,
WebFlash and (optionally) SchemaBot. The generated app is pre-configured
with authentication, login and registration forms, and (optionally)
email confirmation.

BlastOff helps accelerate Pylons application development by generating a
project with a number of pre-configured dependencies.

%package -n python3-module-%oname
Summary: A Pylons application template providing a working site skeleton
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Pylons application template providing a working site skeleton
configured with SQLAlchemy, mako, repoze.who, ToscaWidgets, TurboMail,
WebFlash and (optionally) SchemaBot. The generated app is pre-configured
with authentication, login and registration forms, and (optionally)
email confirmation.

BlastOff helps accelerate Pylons application development by generating a
project with a number of pre-configured dependencies.

%package -n python3-module-%oname-tests
Summary: Tests for BlastOff
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_findreq_skiplist %python3_sitelibdir/blastoff/template/+package+/tests/*.py_tmpl

%description -n python3-module-%oname-tests
A Pylons application template providing a working site skeleton
configured with SQLAlchemy, mako, repoze.who, ToscaWidgets, TurboMail,
WebFlash and (optionally) SchemaBot. The generated app is pre-configured
with authentication, login and registration forms, and (optionally)
email confirmation.

BlastOff helps accelerate Pylons application development by generating a
project with a number of pre-configured dependencies.

This package contains tests for BlastOff.

%package tests
Summary: Tests for BlastOff
Group: Development/Python
Requires: %name = %version-%release
%add_findreq_skiplist %python_sitelibdir/blastoff/template/+package+/tests/*.py_tmpl

%description tests
A Pylons application template providing a working site skeleton
configured with SQLAlchemy, mako, repoze.who, ToscaWidgets, TurboMail,
WebFlash and (optionally) SchemaBot. The generated app is pre-configured
with authentication, login and registration forms, and (optionally)
email confirmation.

BlastOff helps accelerate Pylons application development by generating a
project with a number of pre-configured dependencies.

This package contains tests for BlastOff.

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test.*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/test.*
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3a2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3a2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3a2-alt1.1
- Rebuild with Python-2.7

* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3a2-alt1
- Initial build for Sisyphus

