%define modulename modargs

Name: python-module-%modulename
Version: 1.7
Release: alt1

Summary: Simple command line argument parsing library
License: Free
Group: Development/Python

Url: https://pypi.python.org/pypi/python-modargs

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python

%setup_python_module %modulename
BuildArch: noarch

%description
modargs is a simple command line argument parsing library that infers
arguments from functions in a module.

%prep
%setup

%build
%python_build
   
%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Version 1.7

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

