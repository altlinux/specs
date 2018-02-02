%define _unpackaged_files_terminate_build 1
%define oname cubicweb-subprocess
Name: python-module-%oname
Version: 0.3.0
Release: alt1.1
Summary: This cube helps to manage and monitor subprocesses
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-subprocess/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/dd/81/26b9ae6be5091019e6a0074adf0dec5074d1b8191a37bc4ff38d4a8d034a/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-cubicweb-file

Requires: cubicweb python-module-cubicweb-file

%description
This cube provides an easy way to run subprocesses using a dedicated
workflow.

Subprocesses can be configured (command line, environment, working
directory).

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

