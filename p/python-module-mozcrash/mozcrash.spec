%define oname mozcrash
Name: python-module-%oname
Version: 0.14
Release: alt1
Summary: Library for printing stack traces from minidumps left behind by crashed processes
License: MPL
Group: Development/Python
Url: https://pypi.python.org/pypi/mozcrash/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-mozfile python-module-mozlog

%py_provides %oname

%description
Library for printing stack traces from minidumps left behind by crashed
processes.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/*

%changelog
* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Initial build for Sisyphus

