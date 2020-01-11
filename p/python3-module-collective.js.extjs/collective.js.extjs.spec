%define _unpackaged_files_terminate_build 1
%define mname collective
%define oname %mname.js.extjs

%def_with check

Name: python3-module-%oname
Version: 1.3
Release: alt2.dev0.git20130324
Summary: ExtJS integration for Plone
License: GPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/collective.js.extjs/
#Git: https://github.com/4teamwork/collective.js.extjs.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%py3_provides %oname
%py3_requires %mname.js

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
%python3_sitelibdir/%mname/js/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth

%changelog
* Fri Jan 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.3-alt2.dev0.git20130324
- NMU: Remove python2 module build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.dev0.git20130324.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.dev0.git20130324.1
- (AUTO) subst_x86_64.

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0.git20130324
- Initial build for Sisyphus

