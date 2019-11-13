%define oname ccsnmultivar

Name: python3-module-%oname
Version: 0.0.5
Release: alt2

Summary: Multivariate regression analysis of core-collapse simulations
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ccsnmultivar/
# https://github.com/bwengals/ccsnmultivar.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires numpy scipy tabulate sklearn

BuildRequires: python3-module-html5lib python3-module-numpy-testing
BuildRequires: python3-module-pbr python3-module-scikit-learn
BuildRequires: python3-module-tabulate python3-module-unittest2
BuildRequires: python-tools-2to3


%description
This Python module aids the analysis of core-collapse supernova
gravitational waves. It is the companion code for this paper.

* Multivariate Regression of Fourier Transformed or Time Domain
  waveforms
* Hypothesis testing for measuring the influence of physical parameters
* Optionally incorporate additional uncertainty due to detector noise
* Approximate waveforms from anywhere within the parameter space
* Includes the Abdikamalov et. al. catalog for example use

%prep
%setup

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc AUTHORS *.md docs/*.rst Example_Catalogs
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.5-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.5-alt1.git20150207.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.5-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.5-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20150207
- Initial build for Sisyphus

