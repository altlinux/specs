%define oname robotframework-selenium2screenshots

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt2.git20140720
Summary: Robot Framework keyword library for capturing annotated screenshots with Selenium2Library
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-selenium2screenshots/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datakurre/robotframework-selenium2screenshots.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-robotframework
BuildPreReq: python-module-robotframework-selenium2library
BuildPreReq: python-module-Pillow python-module-docutils
BuildPreReq: python-module-decorator
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests python3-module-robotframework
BuildPreReq: python3-module-robotframework-selenium2library
BuildPreReq: python3-module-Pillow python3-module-docutils
BuildPreReq: python3-module-decorator
%endif

%py_requires PIL

%description
Robot Framework keyword library for capturing annotated screenshots with
Selenium2Library.

%if_with python3
%package -n python3-module-%oname
Summary: Robot Framework keyword library for capturing annotated screenshots with Selenium2Library
Group: Development/Python3
%py3_requires PIL

%description -n python3-module-%oname
Robot Framework keyword library for capturing annotated screenshots with
Selenium2Library.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst docs
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs
%python3_sitelibdir/*
%endif

%changelog
* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2.git20140720
- Added module for Python 3

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20140720
- Initial build for Sisyphus

