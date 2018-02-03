%define _unpackaged_files_terminate_build 1
%define oname cubicweb-vcreview
Name: python-module-%oname
Version: 2.4.0
Release: alt1.1
Summary: Patch review system on top of vcsfile
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-vcreview/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/f1/48/99e0bd031946dde8ac5396e78761460d9107cad42a7822a1c0222a1a5fc3/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-vcsfile
BuildPreReq: python-module-cubicweb-comment
BuildPreReq: python-module-cubicweb-task
BuildPreReq: python-module-cubicweb-nosylist

Requires: cubicweb python-module-cubicweb-vcsfile
Requires: python-module-cubicweb-comment
Requires: python-module-cubicweb-task
Requires: python-module-cubicweb-nosylist

%description
This cube provides a code review system on top of the `vcsfile cube`. It
has been developed with the workflow we use at Logilab in mind, based on
`mercurial` and its `evolve` extension.

%prep
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus

