%define mname scikits
%define oname %mname.pulsefit
Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20141119
Summary: Scikits pulse-fitting package
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.pulsefit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/johnnylee/scikits.pulsefit.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: libnumpy-devel python-module-scipy

%py_provides %oname
%py_requires %mname

%description
Pulse-fitting library for identifying the positions and amplitudes of a
characteristic pulse shape.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
py.test

%files
%doc *.md example
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20141119
- Initial build for Sisyphus

