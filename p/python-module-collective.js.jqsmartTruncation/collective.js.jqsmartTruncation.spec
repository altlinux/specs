# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20120507.1.1
%define mname collective
%define oname %mname.js.jqsmartTruncation
Name: python-module-%oname
Version: 1.0.1
#Release: alt1.dev0.git20120507
Summary: This Package provides smart truncation
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.jqsmartTruncation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.jqsmartTruncation.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
%py_requires %mname.js

%description
Truncate text into the width of his container with the JQuery plugin
smart Truncation.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1.dev0.git20120507.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.dev0.git20120507.1
- (AUTO) subst_x86_64.

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20120507
- Initial build for Sisyphus

