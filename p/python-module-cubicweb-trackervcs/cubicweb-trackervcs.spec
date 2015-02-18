%define oname cubicweb-trackervcs
Name: python-module-%oname
Version: 1.3.0
Release: alt1
Summary: vcsfile / tracker integration
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-trackervcs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cubicweb-vcsfile
BuildPreReq: python-module-cubicweb-tracker
BuildPreReq: python-module-cubicweb-vcreview
BuildPreReq: python-module-cubicweb-forge

Requires: cubicweb python-module-cubicweb-vcsfile
Requires: python-module-cubicweb-tracker
Requires: python-module-cubicweb-vcreview
Requires: python-module-cubicweb-forge

%description
Integrate tracker and vcsfile/vcreview cubes.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc PKG-INFO
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

