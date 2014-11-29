%define mname collective.z3cform
%define oname %mname.mapwidget
Name: python-module-%oname
Version: 2.1
Release: alt1.dev0.git20141110
Summary: z3c.form map widget
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.mapwidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.z3cform.mapwidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-initgroups
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-collective.geo.mapwidget
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-z3c.form

%py_provides %oname
%py_requires %mname collective.geo.mapwidget plone.z3cform zope.schema
%py_requires zope.interface zope.component z3c.form

%description
Map widget for z3c.form based on collective.geo.mapwidget.

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
%python_sitelibdir/collective/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.dev0.git20141110
- Initial build for Sisyphus

