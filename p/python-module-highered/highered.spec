%define oname highered

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1.1.1
Summary: CRF Edit Distance
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/highered
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-numpy python-module-pyhacrf
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-numpy python3-module-pyhacrf
%endif

%py_provides %oname
%py_requires numpy pyhacrf

%description
Learnable Edit Distance Using PyHacrf.

%if_with python3
%package -n python3-module-%oname
Summary: CRF Edit Distance
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy pyhacrf

%description -n python3-module-%oname
Learnable Edit Distance Using PyHacrf.
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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.5-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus

