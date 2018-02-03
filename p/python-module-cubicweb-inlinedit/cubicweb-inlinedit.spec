%define _unpackaged_files_terminate_build 1
%define oname cubicweb-inlinedit
Name: python-module-%oname
Version: 1.3.0
Release: alt1.1
Summary: Extension of the `reledit` builtin feature
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-inlinedit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/38/c1/e6be2f5362cfa2900b98174ff92e6f9ccb2cedbf2792f2dbe18c0fa4fd03/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cwtags

Requires: cubicweb
%py_requires cwtags

%description
Extension of the reledit builtin feature.

Supports composite entity edition, along with a new
'edit-related-entity' view.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

