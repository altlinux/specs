%define oname Products.Ienablesettrace
Name: python-module-%oname
Version: 1.1
Release: alt1.dev.git20100530
Summary: Fork of Products.enablesettrace which also allows import of ipdb in restricted code
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.Ienablesettrace/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/markvl/Products.Ienablesettrace.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-Zope2

%description
To make a long story short: sometimes you need to break into the
debugger in the middle of a Script (Python). To prevent the frustrating
Unauthorized: import of 'pdb' is unauthorized message, use this
enablesettrace package.

This package supports importing the pdb and ipdb module.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20100530
- Initial build for Sisyphus

