%define oname robotframework-selenium2library
Name: python-module-%oname
Version: 1.5.0
Release: alt1.git20141008
Summary: Web testing library for Robot Framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-selenium2library/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rtomac/robotframework-selenium2library.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-decorator
BuildPreReq: python-module-selenium python-module-robotframework
BuildPreReq: python-module-docutils

%description
Selenium2Library is a web testing library for Robot Framework that
leverages the Selenium 2 (WebDriver) libraries.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst doc/*.html demo
%python_sitelibdir/Selenium2Library
%python_sitelibdir/*.egg-info

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141008
- Initial build for Sisyphus

