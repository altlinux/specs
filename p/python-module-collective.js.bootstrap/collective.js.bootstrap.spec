%define mname collective.js
%define oname %mname.bootstrap
Name: python-module-%oname
Version: 3.0.3
Release: alt1.dev0.git20140612
Summary: Get twitter bootstrap as browser resources
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.bootstrap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.bootstrap.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-zope.filerepresentation
BuildPreReq: python-module-zLOG python-module-initgroups

%py_provides %oname
%py_requires %mname plone.app.jquery

%description
This addon provide twitter's bootstrap as browser resource.

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
%python_sitelibdir/collective/js/*
%python_sitelibdir/*.egg-info

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.3-alt1.dev0.git20140612
- Initial build for Sisyphus

