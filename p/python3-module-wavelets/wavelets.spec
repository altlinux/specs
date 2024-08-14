# upstream maintain this arch very bad
%ifarch ppc64le
%def_without check
%endif

%define oname wavelets

Name: python3-module-%oname
Version: 1.7.0
Release: alt1

Summary: Wavelet Transforms in Python

License: MIT and BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/PyWavelets
VCS: https://github.com/PyWavelets/pywt

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-mesonpy
BuildRequires: meson
BuildRequires: python3-module-Cython
BuildRequires: python3-module-numpy-testing
BuildRequires: libnumpy-py3-devel
BuildRequires: pytest3

%description
PyWavelets is a free Open Source library for wavelet transforms in Python.
Wavelets are mathematical basis functions that are localized in both time
and frequency.
Wavelet transforms are time-frequency transforms employing wavelets.
They are similar to Fourier transforms, the difference being that
Fourier transforms are localized only in frequency instead of in time
and frequency.

The main features of PyWavelets are:
- 1D, 2D and nD Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
- 1D, 2D and nD Multilevel DWT and IDWT
- 1D and 2D Stationary Wavelet Transform (Undecimated Wavelet Transform)
- 1D and 2D Wavelet Packet decomposition and reconstruction
- 1D Continuous Wavelet Tranfsorm
- Computing Approximations of wavelet and scaling functions
- Over 100 built-in wavelet filters and support for custom wavelets
- Single and double precision calculations
- Real and complex calculations
- Results compatible with Matlab Wavelet Toolbox (TM)

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
PyWavelets is a free Open Source library for wavelet transforms in Python.
Wavelets are mathematical basis functions that are localized in both time
and frequency.

This package contains tests for %oname.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
mkdir -p matplotlib
touch matplotlib/matplotlibrc
export XDG_CONFIG_HOME=$(pwd)

pushd %buildroot%python3_sitelibdir &>/dev/null

pytest-3 pywt/tests --verbose -p no:cacheprovider \
%ifarch ppc64le
    -k 'not test_cwt_complex and not test_cwt_method_fft'
    # see https://github.com/PyWavelets/pywt/issues/508
%endif
    %nil

popd &>/dev/null

%files
%doc LICENSE LICENSES_bundled.txt README.rst
%python3_sitelibdir/pywt
%python3_sitelibdir/pywavelets-%version.dist-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Aug 14 2024 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Automatically updated to 1.7.0.

* Tue Apr 02 2024 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Automatically updated to 1.6.0.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Automatically updated to 1.5.0.

* Sat Apr 29 2023 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1.1
- Disable check for ppc64le.

* Thu Feb 16 2023 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Automatically updated to 1.4.1.

* Tue Aug 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt3
- Added missing dep on `numpy.testing`.

* Thu Apr 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt2
- Rebuild for python3.7.

* Tue Apr 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
