%define _unpackaged_files_terminate_build 1

%define oname robotsuite
Name: python-module-%oname
Version: 2.0.0
Release: alt1.1
Summary: Robot Framework test suite for Python unittest framework
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/robotsuite/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/robotsuite.git
Source0: https://pypi.python.org/packages/8c/b2/b035fc0b3cbf73c97b1384f996cfd620f28f17ce272aed08ff712bd9b026/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-lxml
BuildPreReq: python-module-six python-module-unittest2
BuildPreReq: python-module-robotframework

%description
This is an experimental package for wrapping Robot Framework test suites
into Python unittest suites to make it possible to run Robot Framework
tests as plone.testing's layered test suites.

%prep
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- automated PyPI update

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1.dev0.git20141001
- Initial build for Sisyphus

