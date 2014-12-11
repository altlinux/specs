%define oname cubicweb-card
Name: python-module-%oname
Version: 0.5.4
Release: alt1
Summary: card/wiki component for the CubicWeb framework
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-card/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-docutils python-module-cubicweb-preview
BuildPreReq: python-module-cubicweb-seo

Requires: cubicweb python-module-cubicweb-preview
Requires: python-module-cubicweb-seo

%description
This cube models cards that are like wiki pages.

Card entities have a title, an abstract and some textual content as
text, rest or html.

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
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1
- Initial build for Sisyphus

