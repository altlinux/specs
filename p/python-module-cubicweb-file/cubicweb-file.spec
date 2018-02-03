%define _unpackaged_files_terminate_build 1
%define oname cubicweb-file
Name: python-module-%oname
Version: 1.18.0
Release: alt1.1
Summary: file component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-file/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/2c/46/d4e37a7844574cab5b50d6dd23fa3aaa390507903f361d958ee4aa14af34/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-Pillow python-module-logilab-constraint
BuildPreReq: python-module-cubicweb-folder

%py_requires PIL
Requires: cubicweb

%description
This cube models Files (pdf document, word processor file, screenshots,
etc).

They are stored in the database and fulltext-indexed when possible.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.18.0-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.1-alt1
- Initial build for Sisyphus

