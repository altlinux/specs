%define oname cubicweb-container

%def_disable check

Name: python-module-%oname
Version: 2.7.0
Release: alt2
Summary: "Generic container" services
License: LGPL
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/cubicweb-container/

Source: %name-%version.tar

BuildRequires: python-module-setuptools-tests cubicweb
BuildRequires: python-module-cubicweb-fastimport python-module-yams

Requires: cubicweb python-module-cubicweb-fastimport

%description
Provides "generic container" services.

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
* Tue Dec 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.0-alt2
- Disabled tests.

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus

