%define _unpackaged_files_terminate_build 1
%define oname cubicweb-card
Name: python-module-%oname
Version: 0.5.8
Release: alt1.1
Summary: card/wiki component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-card/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/d7/b5/a5ba81caa1abf0ece3f6a36a4005f0b2e9a46b1bea807ee692ce2bf03200/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-docutils python-module-cubicweb-preview
BuildPreReq: python-module-cubicweb-seo

Requires: cubicweb python-module-cubicweb-preview
Requires: python-module-cubicweb-seo

%description
This cube models cards that are like wiki pages.

Card entities have a title, an abstract and some textual content as
text, rest or html.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.8-alt1
- automated PyPI update

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1
- Initial build for Sisyphus

