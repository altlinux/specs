%define oname cubicweb-nosylist
Name: python-module-%oname
Version: 0.6.0
Release: alt1.1
Summary: Roundup like nosylist component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-nosylist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
This cube provides nosy-list "a la roundup" usable to notify users of
events they subscribed to such as content modification, state change,
etc.

A nosy list is an ad-hoc mailing list for entities where to which user
can register, or be automatically registered on some action.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This cube provides nosy-list "a la roundup" usable to notify users of
events they subscribed to such as content modification, state change,
etc.

A nosy list is an ad-hoc mailing list for entities where to which user
can register, or be automatically registered on some action.

This package contains tests for %oname.

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
%exclude %python_sitelibdir/*/test
%_datadir/cubicweb/*

%files tests
%python_sitelibdir/*/test

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1
- Version 0.6.0

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

