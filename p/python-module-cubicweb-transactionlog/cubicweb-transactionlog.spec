%define oname cubicweb-transactionlog
Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Collect entities and relations modifications happening in transactions
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-transactionlog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-logilab-constraint

Requires: cubicweb

%description
Collect entities and relations modifications happening in transactions.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

