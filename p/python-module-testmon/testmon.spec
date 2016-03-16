%define oname testmon

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.a6.git20150224.1
Summary: Test Runner for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/testmon/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tarpas/testmon.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pytest-cache python-module-watchdog
BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cache python3-module-watchdog
BuildPreReq: python3-module-coverage
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires pytest_cache watchdog coverage

%description
This is a semi-functional sneak peak into http://igg.me/at/testmon -
"Make your Python tests a breeze to execute"

%package -n python3-module-%oname
Summary: Test Runner for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires pytest_cache watchdog coverage

%description -n python3-module-%oname
This is a semi-functional sneak peak into http://igg.me/at/testmon -
"Make your Python tests a breeze to execute"

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
%endif

%python_install

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst exampleproject
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst exampleproject
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.a6.git20150224.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.a6.git20150224
- Version 0.1.1a6

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.a5.git20150224
- Initial build for Sisyphus

