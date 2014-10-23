%define oname plone.controller
Name: python-module-%oname
Version: 1.8
Release: alt1
Summary: Controller for starting/stopping Plone services
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.controller/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.buildout.cluster

%py_provides %oname
%py_requires plone collective.buildout.cluster

%description
plone.controller is a wxpython visual controller for Zope2 / Plone.

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
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Initial build for Sisyphus

