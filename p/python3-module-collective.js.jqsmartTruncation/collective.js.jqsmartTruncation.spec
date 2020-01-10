%define _unpackaged_files_terminate_build 1
%define mname collective
%define oname %mname.js.jqsmartTruncation

%def_with check

Name: python3-module-%oname
Version: 1.0.1
Release: alt2.dev0.git20120507
Summary: This Package provides smart truncation
License: GPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/collective.js.jqsmartTruncation/
#Git: https://github.com/collective/collective.js.jqsmartTruncation.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%py3_provides %oname
%py3_requires %mname.js

%description
Truncate text into the width of his container with the JQuery plugin
smart Truncation.

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
* Fri Jan 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.0.1-alt2.dev0.git20120507
- NMU: Remove python2 module build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.dev0.git20120507.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.dev0.git20120507.1
- (AUTO) subst_x86_64.

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20120507
- Initial build for Sisyphus

