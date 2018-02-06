%define oname tkform
Name: python-module-%oname
Version: 0.9
Release: alt1.git20150220.1
Summary: A tkinter form-based GUI that wraps python scripts
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tkform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boscoh/tkform.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-tkinter

%py_provides %oname
%py_requires Tkinter

%description
tkform wraps an elegant form-based GUI around Python scripts using only
standard Python.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.md *.png tkform_ex*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9-alt1.git20150220.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20150220
- Initial build for Sisyphus

