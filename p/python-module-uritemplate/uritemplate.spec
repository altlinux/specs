%define oname uritemplate

Name: python-module-%oname
Version: 0.6
Release: alt1

Summary: Python implementation of RFC6570, URI Template
License: Apache Software License
Group: Development/Python

Url: https://pypi.python.org/pypi/uritemplate

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python

%setup_python_module %oname

%description
This is a Python implementation of RFC6570, URI Template, and can expand
templates up to and including Level 4 in that specification.

%prep
%setup

%build
%python_build_debug
   
%install
%python_install

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Version 0.6

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

