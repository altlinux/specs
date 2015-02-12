%define oname mozlog
Name: python-module-%oname
Version: 2.10
Release: alt1
Summary: Robust log handling specialized for logging in the Mozilla universe
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/mozlog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-modules-json
BuildPreReq: python-module-blessings python-module-mozfile

%py_provides %oname
%py_requires blessings mozfile

%description
Robust log handling specialized for logging in the Mozilla universe.

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
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt1
- Version 2.10

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Version 2.9

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1
- Initial build for Sisyphus

