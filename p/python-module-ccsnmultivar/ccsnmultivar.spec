%define oname ccsnmultivar

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20150207
Summary: Multivariate regression analysis of core-collapse simulations
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ccsnmultivar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bwengals/ccsnmultivar.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-numpy python-module-scipy
BuildPreReq: python-module-tabulate python-module-scikit-learn
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-numpy python3-module-scipy
BuildPreReq: python3-module-tabulate python3-module-scikit-learn
BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%py_requires numpy scipy tabulate sklearn

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
* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20150207
- Initial build for Sisyphus

