# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.git20140303.1.1.1.1
%define mname scikits
%define oname %mname.datasmooth

%def_with python3

Name: python-module-%oname
Version: 0.61
#Release: alt2.git20140303.1.1
Summary: Scikits data smoothing package
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.datasmooth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jjstickel/scikit-datasmooth.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools xvfb-run
#BuildPreReq: libnumpy-devel python-module-scipy
#BuildPreReq: python-module-pygobject3 python-module-pycairo
#BuildPreReq: python-module-cvxopt python-module-matplotlib
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: libnumpy-py3-devel python3-module-scipy
#BuildPreReq: python3-module-pygobject3 python3-module-pycairo
#BuildPreReq: python3-module-cvxopt python3-module-matplotlib
%endif

%py_provides %oname
%py_requires %mname numpy scipy cvxopt

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: libnumpy-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-future python-module-genshi python-module-jinja2 python-module-matplotlib python-module-mpmath python-module-numpy python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-numpy python3-module-pyparsing python3-module-pytest python3-module-setuptools
BuildRequires: libnumpy-py3-devel python-module-html5lib python-module-numpy-testing python-module-pygobject3 python-module-scipy python-module-setuptools python3-module-cvxopt python3-module-matplotlib python3-module-numpy-testing python3-module-pycairo python3-module-pygobject3 python3-module-scipy python3-module-setuptools rpm-build-python3 time

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

%if "%_libexecdir" != "%_libdir"
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.61-alt2.git20140303.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.61-alt2.git20140303.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.61-alt2.git20140303.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.61-alt2.git20140303.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.61-alt2.git20140303
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.61-alt1.git20140303
- Initial build for Sisyphus

