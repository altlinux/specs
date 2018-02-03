%define oname cubicweb-iprogress
Name: python-module-%oname
Version: 0.2.0
Release: alt1.1
Summary: Some adapters and view for stuff progressing to reach a milestone
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-iprogress/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://hg.logilab.org/cubes/iprogress
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
Some adapters and view for stuff progressing to reach a milestone.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Version 0.2.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

