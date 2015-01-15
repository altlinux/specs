%define oname cubicweb-sioc
Name: python-module-%oname
Version: 0.1.0
Release: alt1
Summary: Specific views for SIOC (Semantically-Interlinked Online Communities)
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-sioc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
Specific views for SIOC (Semantically-Interlinked Online Communities).

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
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

