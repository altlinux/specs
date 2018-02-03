%define _unpackaged_files_terminate_build 1
%define oname cubicweb-preview
Name: python-module-%oname
Version: 1.2.4
Release: alt1.1
Summary: Enables adding a preview button in your forms
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-preview/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/72/a1/1e4e8a7c4a5fd5a157201071f4663220c0670740dbebb86cc5407e5efc8b/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
Enables adding a preview button in your forms.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

