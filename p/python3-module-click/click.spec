%define _unpackaged_files_terminate_build 1
%define pypi_name click
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 8.4.2
Release: alt1
Summary: Composable command line interface toolkit
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/click/
Vcs: https://github.com/pallets/click.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# required by tests/test_utils.py::test_echo_via_pager
BuildRequires: /usr/bin/less
BuildRequires: /usr/bin/cat
%endif

%description
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 26 2026 Stanislav Levin <slev@altlinux.org> 8.4.2-alt1
- 8.4.1 -> 8.4.2

* Mon May 25 2026 Stanislav Levin <slev@altlinux.org> 8.4.1-alt1
- updated from 8.3.3 to 8.4.1

* Thu Apr 23 2026 Stanislav Levin <slev@altlinux.org> 8.3.3-alt1
- 8.3.2 -> 8.3.3.

* Mon Apr 06 2026 Stanislav Levin <slev@altlinux.org> 8.3.2-alt1
- 8.3.1 -> 8.3.2.

* Mon Nov 17 2025 Stanislav Levin <slev@altlinux.org> 8.3.1-alt1
- 8.3.0 -> 8.3.1.

* Wed Oct 22 2025 Stanislav Levin <slev@altlinux.org> 8.3.0-alt1
- 8.2.1 -> 8.3.0.

* Wed May 21 2025 Stanislav Levin <slev@altlinux.org> 8.2.1-alt1
- 8.1.8 -> 8.2.1.

* Mon Dec 23 2024 Stanislav Levin <slev@altlinux.org> 8.1.8-alt1
- 8.1.7 -> 8.1.8.

* Fri Aug 18 2023 Stanislav Levin <slev@altlinux.org> 8.1.7-alt1
- 8.1.6 -> 8.1.7.

* Mon Jul 24 2023 Stanislav Levin <slev@altlinux.org> 8.1.6-alt1
- 8.1.3 -> 8.1.6.

* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 8.1.3-alt2
- Fixed FTBFS (pytest 7.3.1).

* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 8.1.3-alt1
- 8.1.2 -> 8.1.3.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 8.1.2-alt1
- 8.0.3 -> 8.1.2.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 8.0.3-alt1
- 7.1.2 -> 8.0.3.

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 7.1.2-alt2
- NMU: don't pack tests, but pack click.testing

* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.1.2-alt1
- 7.1.2 released

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 7.0-alt1
- Version updated to 7.0

* Tue Apr 23 2019 Michael Shigorin <mike@altlinux.org> 6.7-alt1.1.1
- introduce doc knob (on by default)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 6.7-alt1
- new version 6.7 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0-alt1.dev.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 5.0-alt1.dev.git20150808.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.dev.git20150808
- New snapshot

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.dev.git20150725
- Version 5.0-dev

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.dev.git20141014
- Initial build for Sisyphus

