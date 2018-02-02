%define _unpackaged_files_terminate_build 1
%define oname cubicweb-tag
Name: python-module-%oname
Version: 1.8.3
Release: alt1.1
Summary: tag component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-tag/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/fc/d4/35e66e5f5c251e1f27b44044817d6cfa221e6bc76c9c169d474b13111a76/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-yams

Requires: cubicweb
%py_requires yams

%description
The tag cube allows to add labels to an entity as a simple yet powerful
way to classify your content. Tags can be used to raffinate a for search
using facets.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Initial build for Sisyphus

