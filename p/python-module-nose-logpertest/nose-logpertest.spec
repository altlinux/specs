%define oname nose-logpertest

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141127.1
Summary: Logging nose plugin to create log per test
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-logpertest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/taykey/nose-logpertest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides nose_logpertest

%description
This plugin creates a log file per test run by nose, holding the logs of
that specific test.

%package -n python3-module-%oname
Summary: Logging nose plugin to create log per test
Group: Development/Python3
%py3_provides nose_logpertest

%description -n python3-module-%oname
This plugin creates a log file per test run by nose, holding the logs of
that specific test.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20141127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141127
- Initial build for Sisyphus

