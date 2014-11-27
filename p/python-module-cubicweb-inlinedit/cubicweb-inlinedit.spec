%define oname cubicweb-inlinedit
Name: python-module-%oname
Version: 1.2.1
Release: alt1
Summary: Extension of the `reledit` builtin feature
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-inlinedit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests cubicweb
BuildPreReq: python-module-cwtags

Requires: cubicweb
%py_requires cwtags

%description
Extension of the reledit builtin feature.

Supports composite entity edition, along with a new
'edit-related-entity' view.

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

