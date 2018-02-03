%define _unpackaged_files_terminate_build 1
%define oname cubicweb-vcwiki
Name: python-module-%oname
Version: 0.4.1
Release: alt1.1
Summary: Version controlled wiki component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-vcwiki/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/b1/bd/0d7aa520965beff6650c7218805fe71b3a50fdb7a1184fc8ed2f607b5453/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-docutils python-module-hglib
BuildPreReq: python-module-cubicweb-vcsfile
BuildPreReq: python-module-cubicweb-preview

Requires: cubicweb python-module-cubicweb-vcsfile
Requires: python-module-cubicweb-preview
%py_requires docutils hglib

%description
This is a version controlled wiki component for the CubicWeb framework.

It uses Mercurial as a content storage and can be edited both with your
favorite editor and the web GUI.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

