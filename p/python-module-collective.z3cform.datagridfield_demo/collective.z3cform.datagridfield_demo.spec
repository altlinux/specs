%define mname collective.z3cform
%define oname %mname.datagridfield_demo
Name: python-module-%oname
Version: 0.7
Release: alt1.dev0.git20131028
Summary: Version of DataGridField for use with Dexterity / z3c.form - Demo views
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.z3cform.datagridfield-demo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.z3cform.datagridfield_demo.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-unittest2
#BuildPreReq: python-module-collective.z3cform.datagridfield

%py_provides %oname
%py_requires %mname five.grok plone.directives.form plone.app.z3cform
#py_requires collective.z3cform.datagridfield

%description
This package provides the demo views for
collective.z3cform.datagridfield. See that package for more information.

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
%python_sitelibdir/collective/z3cform/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.dev0.git20131028
- Initial build for Sisyphus

