%define mname collective
%define oname %mname.js.jqsmartTruncation
Name: python-module-%oname
Version: 1.0.1
Release: alt1.dev0.git20120507
Summary: This Package provides smart truncation
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.jqsmartTruncation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.jqsmartTruncation.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/js/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.dev0.git20120507
- Initial build for Sisyphus

