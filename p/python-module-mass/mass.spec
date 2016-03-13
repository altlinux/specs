%define oname mass

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.dev4.git20150320.1
Summary: MASS is Music and Audio in Sample Sequences
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/music/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ttm/mass.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests xvfb-run
BuildPreReq: python-module-numpy python-module-matplotlib
BuildPreReq: python-module-scipy python-module-pygobject3
BuildPreReq: python-module-pycairo
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-numpy python3-module-matplotlib
BuildPreReq: python3-module-scipy python3-module-pygobject3
BuildPreReq: python3-module-pycairo
%endif

%py_provides %oname
%py_requires numpy matplotlib scipy gi cairo

%description
This project delivers routines for music oriented sound synthesis in a
sample based system. MASS can be though of as a sample level DAW system,
in which the objects manipulated are in fact the array of samples
describing the sound wave that will reach a listener ear.

%if_with python3
%package -n python3-module-%oname
Summary: MASS is Music and Audio in Sample Sequences
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy matplotlib scipy gi cairo

%description -n python3-module-%oname
This project delivers routines for music oriented sound synthesis in a
sample based system. MASS can be though of as a sample level DAW system,
in which the objects manipulated are in fact the array of samples
describing the sound wave that will reach a listener ear.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
export PYTHONPATH=$PWD
xvfb-run py.test -vv tests/*.py mass/*.py
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
xvfb-run py.test-%_python3_version -vv tests/*.py mass/*.py
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev4.git20150320.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev4.git20150320
- Initial build for Sisyphus

