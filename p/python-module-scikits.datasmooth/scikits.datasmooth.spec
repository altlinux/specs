%define mname scikits
%define oname %mname.datasmooth

%def_with python3

Name: python-module-%oname
Version: 0.61
Release: alt2.git20140303
Summary: Scikits data smoothing package
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.datasmooth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jjstickel/scikit-datasmooth.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests xvfb-run
BuildPreReq: libnumpy-devel python-module-scipy
BuildPreReq: python-module-pygobject3 python-module-pycairo
BuildPreReq: python-module-cvxopt python-module-matplotlib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: libnumpy-py3-devel python3-module-scipy
BuildPreReq: python3-module-pygobject3 python3-module-pycairo
BuildPreReq: python3-module-cvxopt python3-module-matplotlib
%endif

%py_provides %oname
%py_requires %mname numpy scipy cvxopt

%description
This is a scikit intended to include numerical methods for smoothing
data.

%if_with python3
%package -n python3-module-%oname
Summary: Scikits data smoothing package
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy cvxopt

%description -n python3-module-%oname
This is a scikit intended to include numerical methods for smoothing
data.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt docs/* examples
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/* examples
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.61-alt2.git20140303
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.61-alt1.git20140303
- Initial build for Sisyphus

