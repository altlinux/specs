%define oname robotframework-ride
Name: python-module-%oname
Version: 1.3
Release: alt1.git20140627.1
Summary: RIDE :: Robot Framework Test Data Editor
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-ride/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/robotframework/RIDE.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-Paver python-module-setuptools
BuildPreReq: python-module-Pygments

%add_python_req_skip java javax org

%description
Robot Framework is a generic test automation framework for acceptance
level testing. RIDE is a lightweight and intuitive editor for Robot
Framework test data.

%prep
%setup

ln -s ../../lib src/robotide/
mkdir src/bin
ln -s ../ride.py src/bin/

%build
paver build

%install
paver install --root=%buildroot

%files
%doc *.txt *.rest
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20140627.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140627
- Initial build for Sisyphus

