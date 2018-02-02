%define oname yams
Name: python-module-%oname
Version: 0.45.1
Release: alt1.1
Summary: Entity / relation schema
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/yams/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools python-module-logilab-common
BuildRequires: python-module-logilab-database python-module-six

%py_provides %oname

%description
Yet Another Magic Schema ! A simple/generic but powerful entities /
relations schema, suitable to represent RDF like data. The schema is
readable/writable from/to various formats.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc ChangeLog README
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.45.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.45.1-alt1
- Updated to upstream version 0.45.1.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.2-alt1
- Version 0.40.2

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.40.0-alt1
- Version 0.40.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.39.1-alt1
- Initial build for Sisyphus

