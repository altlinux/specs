# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20141027.1.1
%define mname collective.js
%define oname %mname.knockout
Name: python-module-%oname
Version: 3.2.1
#Release: alt1.dev0.git20141027
Summary: knockout.js integration for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.knockout
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.knockout.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
%py_requires %mname

%description
This product is an integration for knockout.js JavaScript framework into
Plone.

This will not doing anything by its own , but a developer can use this
package to starts developing knockout based features.

You can install that package in your Plone site to add the provided
(minified) version of knockout.js to the portal_javascript tool.
Optionally you can use/register the provided not-minified version.

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
%python_sitelibdir/collective/js/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1.dev0.git20141027.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2.1-alt1.dev0.git20141027.1
- (AUTO) subst_x86_64.

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.dev0.git20141027
- Initial build for Sisyphus

