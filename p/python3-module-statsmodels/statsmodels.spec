%define _unpackaged_files_terminate_build 1

%define pypi_name statsmodels
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.14.0
Release: alt2
Epoch: 1
Summary: Statistical computations and models for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/statsmodels/
Vcs: https://github.com/statsmodels/statsmodels
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%add_python3_req_skip models
# rename scikits.statsmodels => statsmodels
Provides: python3-module-scikits.statsmodels = %EVR
Obsoletes: python3-module-scikits.statsmodels <= 0.11.1-alt2.1

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra develop
# compat.pandas => pandas.testing
BuildRequires: python3-module-pandas-tests
%endif

%description
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%ifnarch armh
%check
# quite a few tests fail on armh. disable it for now
%endif
%pyproject_run -- bash -s <<-'ENDUNITTEST'
set -eu
mkdir empty
cd empty
python3 -c 'import statsmodels; statsmodels.test(["--skip-examples", "--only-smoke", "--skip-slow", "-n", "auto"], exit=True)'
ENDUNITTEST

%files
%doc LICENSE.txt
%doc README*.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Dec 07 2023 Stanislav Levin <slev@altlinux.org> 1:0.14.0-alt2
- Backported fix for build against Cython 3.0.

* Fri Jul 14 2023 Stanislav Levin <slev@altlinux.org> 1:0.14.0-alt1
- 0.11.1 -> 0.14.0.

* Wed Mar 24 2021 Ivan A. Melnikov <iv@altlinux.org> 1:0.11.1-alt2.1
- Enable parallel build.

* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 1:0.11.1-alt2
- Disable check for python3.9 bootstrap.

* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.11.1-alt1
- Updated to upstream version 0.11.1.
- Re-enabled tests.

* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:0.8.0-alt3
- Build for python2 disabled.

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.8.0-alt2
- NMU: disable build python2 module

* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.0-alt1
- Updated to upstream version 0.8.0.
- Disabled docs generation.

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731
- rm inessential BR: python3-module-pandas{,-tests} (incorrectly detected by buildreq).

* Fri Mar 25 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt3.git20150731
- BRs fixed with buildreq again (cleared off self-dependence and other
  unneeded pkgs with python-module-setuptools-18.1-alt3,
  python-2.7.11-alt2, and python-module-Cython-0.23.4-alt3).

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.7.0-alt2.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150731
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150323
- New snapshot

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150216
- Added requires statsmodels.stats.multitest

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt1.git20150216
- Initial build for Sisyphus

