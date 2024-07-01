%define oname nitime

%def_with check

Name: python3-module-%oname
Version: 0.11
Release: alt1

Summary: Nitime: timeseries analysis for neuroscience data

License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/nitime
VCS: https://github.com/nipy/nitime

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-scipy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-matplotlib
%endif

%description
Nitime is library of tools and algorithms for the analysis of
time-series data from neuroscience experiments. It contains a
implementation of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to
the numerical machinery and make common analysis tasks easy to express
with compact and semantically clear code.

%package tests
Summary: Tests for Nitime
Group: Development/Python3
Requires: %name = %EVR

%description tests
Nitime is library of tools and algorithms for the analysis of
time-series data from neuroscience experiments. It contains a
implementation of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to
the numerical machinery and make common analysis tasks easy to express
with compact and semantically clear code.

This package contains tests for Nitime.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
# https://github.com/nipy/nitime/issues/214
%pyproject_run_pytest -k'not test_timeseries'

%files
%doc LICENSE README.txt THANKS
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests

%changelog
* Fri Jun 28 2024 Grigory Ustinov <grenka@altlinux.org> 0.11-alt1
- Automatically updated to 0.11.
- Built with check.

* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 0.10.2-alt1
- Automatically updated to 0.10.2.

* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt1
- Updated to upstream version 0.8.1.

* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt2
- python2 disabled

* Fri Sep 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1
- Updated to upstream version 0.7.

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5-alt1.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Version 0.5

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

