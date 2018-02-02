%define _unpackaged_files_terminate_build 1
%define oname cubicweb-tracker
Name: python-module-%oname
Version: 1.18.0
Release: alt1.1
Summary: Basic tracker with project, version, ticket for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-tracker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/67/1d/e75035177570a53ec38cd01293ef94c7ae17a898fd9c22ede0dbad3cd8c1/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-markdown
BuildPreReq: python-module-cubicweb-activitystream
BuildPreReq: python-module-cubicweb-localperms
BuildPreReq: python-module-cubicweb-iprogress
BuildPreReq: python-module-cubicweb-preview

Requires: cubicweb python-module-cubicweb-activitystream
Requires: python-module-cubicweb-localperms
Requires: python-module-cubicweb-iprogress
Requires: python-module-cubicweb-preview

%description
The tracker cube provides a basic issue tracker with projects, tickets
and versions to group tickets. It can be used out-of-the box but is
targeted as a base for more featurefull forges or configuration
management systems, such as the forge cube.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.18.0-alt1
- automated PyPI update

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.3-alt1
- Version 1.16.3

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.1-alt1
- Initial build for Sisyphus

