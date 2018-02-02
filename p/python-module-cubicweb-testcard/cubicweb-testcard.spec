%define oname cubicweb-testcard
Name: python-module-%oname
Version: 0.5.0
Release: alt1.1
Summary: Test card extension for CubicWeb application based on the tracker cube
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-testcard/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-card python-module-markdown
BuildPreReq: python-module-cubicweb-tracker
BuildPreReq: python-module-cubicweb-comment

Requires: cubicweb python-module-cubicweb-card
Requires: python-module-cubicweb-tracker
Requires: python-module-cubicweb-comment

%description
This cube provides test card to extend tracker based applications. A
test card specify how to test a project or a ticket.

When starting a version, TestInstance are automatically created from
matching cards, and you should then run specified test, and set status
according to test'success or failre.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

