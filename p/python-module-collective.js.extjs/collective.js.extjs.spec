# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20130324.1.1
%define mname collective
%define oname %mname.js.extjs
Name: python-module-%oname
Version: 1.3
#Release: alt1.dev0.git20130324
Summary: ExtJS integration for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.extjs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/collective.js.extjs.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
%py_requires %mname.js

%description
This package integrates the Ext JS 3 library into Plone.

It provides:

* a resource directory (++resource++collective.js.extjs-resources/)
* a jquery adapter resource (++resource++ext-jquery-adapter.js)
* a generic setup profile, registering JavaScript and CSS to the portal
  registry.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/js/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.dev0.git20130324.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.dev0.git20130324.1
- (AUTO) subst_x86_64.

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0.git20130324
- Initial build for Sisyphus

