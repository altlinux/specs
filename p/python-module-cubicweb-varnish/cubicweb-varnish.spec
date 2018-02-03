%define oname cubicweb-varnish
Name: python-module-%oname
Version: 0.3.0
Release: alt1.1
Summary: cubicweb varnish helper
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-varnish/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
This cubes enables a purge mechanism for a cubicweb website that is
sitting behind a varnish cache.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

