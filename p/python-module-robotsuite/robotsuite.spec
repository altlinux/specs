
%define oname robotsuite
Name: python-module-%oname
Version: 1.6.2
Release: alt1.dev0.git20141001
Summary: Robot Framework test suite for Python unittest framework
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/robotsuite/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/robotsuite.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-lxml
BuildPreReq: python-module-six python-module-unittest2
BuildPreReq: python-module-robotframework

%description
This is an experimental package for wrapping Robot Framework test suites
into Python unittest suites to make it possible to run Robot Framework
tests as plone.testing's layered test suites.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.dev0.git20141001
- Initial build for Sisyphus

