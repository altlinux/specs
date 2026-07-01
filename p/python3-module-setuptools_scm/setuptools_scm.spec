%define _unpackaged_files_terminate_build 1
%define mod_name setuptools_scm
%define pypi_name setuptools-scm

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
Provides: python3-module-%%{pep503_name %%pypi_name}+%1 = %%EVR \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%mod_name
Version: 10.2.0
Release: alt1
Summary: The blessed package to manage your versions by scm tags
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/setuptools-scm/
VCS: https://github.com/pypa/setuptools_scm/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: %name-%version-alt.patch
# manually manage extra dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
Requires: git-core mercurial
%py3_provides %pypi_name
# mapping from PyPI name
Provides: python3-module-%pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not yet packaged
%add_pyproject_deps_check_filter '^griffe.*'
%pyproject_builddeps_metadata_extra rich
%pyproject_builddeps_check
BuildRequires: git-core mercurial
%endif

%description
%pypi_name extracts Python package versions from git or hg metadata instead
of declaring them as the version argument or in a Source Code Managed (SCM)
managed file.

Additionally %pypi_name provides setuptools with a list of files that are
managed by the SCM (i.e. it automatically adds all the SCM-managed files to the
sdist). Unwanted files must be excluded via MANIFEST.in or configuring Git
archive.

%add_python_extra rich

%prep
%setup
%patch1 -p1
%pyproject_scm_init setuptools-scm-v%version
cd setuptools-scm
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
cd setuptools-scm
%pyproject_build

%install
cd setuptools-scm
%pyproject_install

%check
cd setuptools-scm
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
# change cwd to git root as it's expected by tests
cd ..
python -m pytest -vra -Wignore setuptools-scm/
ENDTESTS

%files
%_bindir/setuptools-scm
%python3_sitelibdir/setuptools_scm/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 30 2026 Stanislav Levin <slev@altlinux.org> 10.2.0-alt1
- 10.0.5 -> 10.2.0

* Wed Apr 01 2026 Stanislav Levin <slev@altlinux.org> 10.0.5-alt1
- 9.2.2 -> 10.0.5.

* Mon Oct 20 2025 Stanislav Levin <slev@altlinux.org> 9.2.2-alt1
- 9.2.1 -> 9.2.2.

* Tue Oct 14 2025 Stanislav Levin <slev@altlinux.org> 9.2.1-alt1
- 9.1.1 -> 9.2.1.

* Mon Aug 25 2025 Grigory Ustinov <grenka@altlinux.org> 9.1.1-alt1.1
- Bootstrap for python3.13.

* Tue Aug 12 2025 Stanislav Levin <slev@altlinux.org> 9.1.1-alt1
- 8.3.1 -> 9.1.1.

* Tue May 13 2025 Stanislav Levin <slev@altlinux.org> 8.3.1-alt1
- 8.2.1 -> 8.3.1.

* Wed Mar 19 2025 Stanislav Levin <slev@altlinux.org> 8.2.1-alt1
- 8.2.0 -> 8.2.1.

* Mon Feb 24 2025 Stanislav Levin <slev@altlinux.org> 8.2.0-alt1
- 8.1.0 -> 8.2.0.

* Tue May 07 2024 Stanislav Levin <slev@altlinux.org> 8.1.0-alt1
- 8.0.4 -> 8.1.0.

* Tue Oct 03 2023 Stanislav Levin <slev@altlinux.org> 8.0.4-alt1
- 8.0.3 -> 8.0.4.

* Mon Sep 25 2023 Stanislav Levin <slev@altlinux.org> 8.0.3-alt1
- 7.1.0 -> 8.0.3.

* Thu Jun 22 2023 Stanislav Levin <slev@altlinux.org> 7.1.0-alt2
- Fixed FTBFS (setuptools 68.0.0).
- Modernized packaging.

* Fri Jan 27 2023 Stanislav Levin <slev@altlinux.org> 7.1.0-alt1
- 7.0.5 -> 7.1.0.

* Tue Nov 01 2022 Michael Shigorin <mike@altlinux.org> 7.0.5-alt2
- fixed build --without check

* Fri Aug 05 2022 Stanislav Levin <slev@altlinux.org> 7.0.5-alt1
- 6.4.2 -> 7.0.5 (closes: #43460).

* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 6.4.2-alt2
- Fixed FTBFS (setuptools 61.0.0+).

* Fri Jan 21 2022 Stanislav Levin <slev@altlinux.org> 6.4.2-alt1
- 6.3.2 -> 6.4.2.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 6.3.2-alt2
- Fixed FTBFS (setuptools 58.3.0).

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 6.3.2-alt1
- 6.0.1 -> 6.3.2.

* Sun Apr 18 2021 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 4.1.2 -> 6.0.1.

* Mon Oct 05 2020 Stanislav Levin <slev@altlinux.org> 4.1.2-alt1
- 3.5.0 -> 4.1.2.

* Wed Feb 19 2020 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.3.3 -> 3.5.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.3.3-alt2
- Fixed testing against Pytest 5.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 3.3.3-alt1
- 2.1.0 -> 3.3.3.

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated to upstream version 2.1.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.15.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Michael Shigorin <mike@altlinux.org> 1.15.0-alt1.1
- R: git-core instead of full-blown git metapackage
- fix build --with python3 (actually the test)

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 1.15.0-alt1
- Version 1.15.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0-alt1.git20150812.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1.git20150812.1
- NMU: Use buildreq for BR.

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20150812
- Version 1.7.0

* Sun Jul 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150723
- Version 1.6.0

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

