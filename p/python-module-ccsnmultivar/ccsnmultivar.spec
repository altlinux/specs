%define oname ccsnmultivar

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20150207.1.1.1
Summary: Multivariate regression analysis of core-collapse simulations
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ccsnmultivar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bwengals/ccsnmultivar.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-numpy python-module-scipy
#BuildPreReq: python-module-tabulate python-module-scikit-learn
#BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-numpy python3-module-scipy
#BuildPreReq: python3-module-tabulate python3-module-scikit-learn
#BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%py_requires numpy scipy tabulate sklearn

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-future python-module-mpmath python-module-numpy python-module-pytest python-module-scipy python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-numpy python3-module-pip python3-module-pycparser python3-module-pytest python3-module-scipy python3-module-setuptools
BuildRequires: python-module-numpy-testing python-module-pbr python-module-scikit-learn python-module-setuptools python-module-tabulate python-module-unittest2 python3-module-html5lib python3-module-numpy-testing python3-module-pbr python3-module-scikit-learn python3-module-setuptools python3-module-tabulate python3-module-unittest2 rpm-build-python3 time

%description
This Python module aids the analysis of core-collapse supernova
gravitational waves. It is the companion code for this paper.

* Multivariate Regression of Fourier Transformed or Time Domain
  waveforms
* Hypothesis testing for measuring the influence of physical parameters
* Optionally incorporate additional uncertainty due to detector noise
* Approximate waveforms from anywhere within the parameter space
* Includes the Abdikamalov et. al. catalog for example use

%if_with python3
%package -n python3-module-%oname
Summary: Multivariate regression analysis of core-collapse simulations
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy tabulate sklearn

%description -n python3-module-%oname
This Python module aids the analysis of core-collapse supernova
gravitational waves. It is the companion code for this paper.

* Multivariate Regression of Fourier Transformed or Time Domain
  waveforms
* Hypothesis testing for measuring the influence of physical parameters
* Optionally incorporate additional uncertainty due to detector noise
* Approximate waveforms from anywhere within the parameter space
* Includes the Abdikamalov et. al. catalog for example use
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.md docs/*.rst Example_Catalogs
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md docs/*.rst Example_Catalogs
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.5-alt1.git20150207.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.5-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.5-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20150207
- Initial build for Sisyphus

