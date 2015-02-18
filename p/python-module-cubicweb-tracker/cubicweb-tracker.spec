%define oname cubicweb-tracker
Name: python-module-%oname
Version: 1.16.3
Release: alt1
Summary: Basic tracker with project, version, ticket for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-tracker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
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
%setup

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
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.3-alt1
- Version 1.16.3

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16.1-alt1
- Initial build for Sisyphus

