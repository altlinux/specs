%define mname collective
%define oname %mname.js.throttledebounce
Name: python-module-%oname
Version: 1.2
Release: alt1.git20101126
Summary: Installs the throttle / debounce plugin
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.throttledebounce/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.throttledebounce.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests

%py_provides %oname
%py_requires %mname.js

%description
jQuery throttle / debounce allows you to rate-limit your functions in
multiple useful ways.

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
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20101126
- Initial build for Sisyphus

