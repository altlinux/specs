%define mname collective
%define m2name tinymceplugins
%define oname %mname.%m2name.advfilelinks
Name: python-module-%oname
Version: 1.3.3
Release: alt1.dev0.git20141210
Summary: An advanced Plone TinyMCE plugin for handling links to files
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.tinymceplugins.advfilelinks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.tinymceplugins.advfilelinks.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-z3c.jbot
BuildPreReq: python-module-Products.TinyMCE
BuildPreReq: python-module-collective.mtrsetup
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
Requires: python-module-%mname.%m2name = %EVR
Requires: python-module-Zope2
%py_requires z3c.jbot Products.TinyMCE collective.mtrsetup
%py_requires Products.CMFCore zope.component zope.interface

%description
This is a plugin for TinyMCE editor for Plone.

It will replace in the less obtrusive way the standard plonelink plugin,
providing a version that handle in a different way links to File and
Image contents.

%package -n python-module-%mname.%m2name
Summary: Core files of %mname.%m2name
Group: Development/Python
%py_provides %mname.%m2name
%py_requires %mname

%description -n python-module-%mname.%m2name
Core files of %mname.%m2name.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/%m2name/__init__.py \
	%buildroot%python_sitelibdir/%mname/%m2name/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/%m2name/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/%m2name/__init__.py*

%files -n python-module-%mname.%m2name
%dir %python_sitelibdir/%mname/%m2name
%python_sitelibdir/%mname/%m2name/__init__.py*

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.dev0.git20141210
- Initial build for Sisyphus

