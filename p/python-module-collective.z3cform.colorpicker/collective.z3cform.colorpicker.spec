%define mname collective.z3cform
%define oname %mname.colorpicker
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20140621
Summary: Colorpicker widget for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.colorpicker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.z3cform.colorpicker.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-initgroups
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-z3c.form

%py_provides %oname
%py_requires %mname Products.CMFCore plone.app.z3cform zope.schema
%py_requires plone.z3cform zope.interface zope.component z3c.form

%description
collective.z3cform.colorpicker provides two different jQuery based
widgets:

* Farbtastic, a simple color picker.
* jPicker, a jQuery Color Picker Plugin supporting transparency.

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
%python_sitelibdir/collective/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20140621
- Initial build for Sisyphus

