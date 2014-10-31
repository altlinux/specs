%define mname collective
%define oname %mname.wysiwyg_biografy
Name: python-module-%oname
Version: 0.2.2
Release: alt1.dev0.git20141028
Summary: The Plone user's biografy using the WYSIWYG editor
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.wysiwyg_biografy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.wysiwyg_biografy.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.users
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-unittest2 python-module-argparse

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlone plone.app.users zope.interface
%py_requires plone.app.form

%description
Simple product for Plone. It change the user Biografy field to use the
current WYSIWYG editor.

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
%doc *.rst docs/*
%python_sitelibdir/*

%changelog
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.dev0.git20141028
- Initial build for Sisyphus

