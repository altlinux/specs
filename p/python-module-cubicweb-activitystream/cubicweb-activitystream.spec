%define _unpackaged_files_terminate_build 1
%define oname cubicweb-activitystream
Name: python-module-%oname
Version: 0.1.3
Release: alt1.1
Summary: Activity streams
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-activitystream/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/03/85/f9748b3c72c51094ef5938cc18283b3675adefcd81b1e2ab7d9a0ab24506/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
Activity streams.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1
- automated PyPI update

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

