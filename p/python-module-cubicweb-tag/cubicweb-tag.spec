%define oname cubicweb-tag
Name: python-module-%oname
Version: 1.8.1
Release: alt1
Summary: tag component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-tag/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-yams

Requires: cubicweb
%py_requires yams

%description
The tag cube allows to add labels to an entity as a simple yet powerful
way to classify your content. Tags can be used to raffinate a for search
using facets.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Initial build for Sisyphus

