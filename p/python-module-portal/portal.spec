%define oname portal
Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20130627.1
Summary: Portal - Apple's Provisioning Portal API and CLI
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/portal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jlopez/portal.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%py_provides %oname

%description
Portal is a Python module that hooks to Apple's undocumented
provisioning portal developer services as well as a command line utility
that allows you to perform tasks without suffering CTS from all the
clicking.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc AUTHORS CHANGES *.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.git20130627.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20130627
- Initial build for Sisyphus

