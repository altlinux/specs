%define _unpackaged_files_terminate_build 1
%define pypi_name click

%def_with check

Name: python3-module-%pypi_name
Version: 8.1.7
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

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_check
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
rm src/click/_winconsole.py
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/click/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

