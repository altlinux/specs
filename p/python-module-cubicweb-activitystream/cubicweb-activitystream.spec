%define oname cubicweb-activitystream
Name: python-module-%oname
Version: 0.1.2
Release: alt1
Summary: Activity streams
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-activitystream/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
Activity streams.

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
* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

