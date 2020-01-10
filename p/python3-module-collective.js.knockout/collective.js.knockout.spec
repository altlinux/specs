%define _unpackaged_files_terminate_build 1
%define mname collective.js
%define oname %mname.knockout

%def_with check

Name: python3-module-%oname
Version: 3.2.1
Release: alt2.dev0.git20141027
Summary: knockout.js integration for Plone
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/collective.js.knockout
#Git: https://github.com/collective/collective.js.knockout.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%py3_provides %oname
%py3_requires %mname

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
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python3 setup.py test

%files
%doc *.rst docs/*
%python3_sitelibdir/collective/js/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth

%changelog
* Fri Jan 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 3.2.1-alt2.dev0.git20141027
- NMU: Remove python2 module build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1.dev0.git20141027.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2.1-alt1.dev0.git20141027.1
- (AUTO) subst_x86_64.

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1.dev0.git20141027
- Initial build for Sisyphus

