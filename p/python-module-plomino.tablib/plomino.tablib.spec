%define mname plomino
%define oname %mname.tablib
Name: python-module-%oname
Version: 1.1
Release: alt1
Summary: Integrate Kenneth Reitz's tablib with Plomino formulas 
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plomino.tablib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-initgroups
BuildPreReq: python-module-tablib python-module-unittest2
BuildPreReq: python-module-Products.CMFPlomino
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.hookable
BuildPreReq: python-module-zope.untrustedpython

%py_provides %oname
%py_requires %mname Products.CMFPlomino tablib Products.PythonScripts
%py_requires zope.interface zope.component

%description
Make Tablib by Kenneth Reitz available to PlominoUtils.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

