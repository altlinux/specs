%define _unpackaged_files_terminate_build 1
%define mname collective.js
%define oname %mname.showmore

%def_with check

Name: python3-module-%oname
Version: 1.0
Release: alt2.a4
Summary: JS add-on to show/hide parts of a page
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/collective.js.showmore/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%py3_provides %oname
%py3_requires %mname

%description
collective.js.showmore provides a JQuery plugin.

The plugin hides a set of nodes and replaces them with a "Show more..."
link. When the link is clicked, the hidden nodes are made visible again.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
collective.js.showmore provides a JQuery plugin.

The plugin hides a set of nodes and replaces them with a "Show more..."
link. When the link is clicked, the hidden nodes are made visible again.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
install -d %buildroot%python3_sitelibdir/collective/js
cp -fR collective/js/showmore \
	%buildroot%python3_sitelibdir/collective/js/
cp -fR *.egg-info %buildroot%python3_sitelibdir/

%check
python3 setup.py test

%files
%doc *.txt docs/*
%python3_sitelibdir/collective/js/showmore
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/collective/js/showmore/tests

%files tests
%python3_sitelibdir/collective/js/showmore/tests

%changelog
* Fri Jan 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0-alt2.a4
- NMU: Remove python2 module build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.a4.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a4
- Initial build for Sisyphus

