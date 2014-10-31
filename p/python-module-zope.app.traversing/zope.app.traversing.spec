%define mname zope.app
%define oname %mname.traversing
Name: python-module-%oname
Version: 3.4.0
Release: alt1
Summary: Zope Application Traversal Support
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zope.app.traversing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.traversing

%py_provides %oname
%py_requires %mname zope.deprecation zope.traversing

%description
The zope.traversing package provides adapteres for resolving object
paths by traversing an object hierarchy. This also includes support for
traversal namespaces (e.g. ++view++, ++skin++, etc.) as well as
computing URLs via the @@absolute_url view.

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
%doc *.txt
%python_sitelibdir/zope/app/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

