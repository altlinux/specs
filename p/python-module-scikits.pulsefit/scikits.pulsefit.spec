%define mname scikits
%define oname %mname.pulsefit

%def_disable check

Name: python-module-%oname
Version: 0.1.3
Release: alt3.git20141230
Summary: Scikits pulse-fitting package
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.pulsefit

# https://github.com/johnnylee/scikits.pulsefit.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: libnumpy-devel python-module-scipy

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
* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt3.git20141230
- Disabled check.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt2.git20141230
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20141230
- New snapshot

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20141119
- Initial build for Sisyphus

