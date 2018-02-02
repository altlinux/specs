%define oname universal-analytics-python

%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1.git20141205.1.1
Summary: Universal Analytics Python Module
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/universal-analytics-python/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/analytics-pros/universal-analytics-python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides UniversalAnalytics

%description
This library provides a Python interface to Google Analytics, supporting
the Universal Analytics Measurement Protocol, with an interface modeled
(loosely) after Google's analytics.js.

%package -n python3-module-%oname
Summary: Universal Analytics Python Module
Group: Development/Python3
%py3_provides UniversalAnalytics

%description -n python3-module-%oname
This library provides a Python interface to Google Analytics, supporting
the Universal Analytics Measurement Protocol, with an interface modeled
(loosely) after Google's analytics.js.

%prep
%setup

echo %version >commit-version

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
#make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|python|python3|' Makefile
#make test
popd
%endif

%files
%doc *.rst *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.git20141205.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20141205.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141205
- Initial build for Sisyphus

