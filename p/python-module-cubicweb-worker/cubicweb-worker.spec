%define _unpackaged_files_terminate_build 1
%define oname cubicweb-worker
Name: python-module-%oname
Version: 3.2.0
Release: alt1
Summary: Asynchronous workers in your instance
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-worker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/df/aa/8cb373f76300a05e253c746ab050f2020ce2fcd96d3c0457eec057a34fbd/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-subprocess

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1
- automated PyPI update

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus

