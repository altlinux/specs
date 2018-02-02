%define _unpackaged_files_terminate_build 1
%define oname cubicweb-worker
Name: python-module-%oname
Version: 3.2.0
Release: alt2.1
Summary: Asynchronous workers in your instance
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-worker/
BuildArch: noarch

Source: %{oname}-%{version}.tar.gz

BuildRequires: python-module-setuptools cubicweb
BuildRequires: python-module-cubicweb-subprocess
BuildRequires: python2.7(cwtags)

Requires: cubicweb python-module-cubicweb-subprocess

%description
Asynchronous workers in your instance.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus

