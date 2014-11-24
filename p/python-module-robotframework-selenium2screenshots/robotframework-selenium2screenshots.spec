%define oname robotframework-selenium2screenshots
Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20140720
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

%py_requires PIL

%description
Robot Framework keyword library for capturing annotated screenshots with
Selenium2Library.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst docs
%python_sitelibdir/*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20140720
- Initial build for Sisyphus

