%define _unpackaged_files_terminate_build 1
%define pypi_name tox
%define mod_name %pypi_name
%define bash_completions_dir %_datadir/bash-completion/completions

%def_with check

Name: python3-module-%pypi_name
Version: 4.56.1
Release: alt1

Summary: Generic virtualenv management and test command line tool
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox/
VCS: https://github.com/tox-dev/tox
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
%pyproject_runtimedeps_metadata_extra completion
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata_extra completion
%if_with check
BuildRequires: /proc
# required by test_local_execute_terminal_size
BuildRequires: /dev/pts
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# required by tests/docs/test_manpage.py
BuildRequires: /usr/bin/man
%endif

%description
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

mv %buildroot%_bindir/tox{,.py3}
register-python-argcomplete tox.py3 > tox.py3
install -p -m 0644 -D -t '%buildroot%bash_completions_dir' tox.py3

%check
export VIRTUALENV_SYSTEM_SITE_PACKAGES=YES
export TOX_LIMITED_SHEBANG=1
export PIP_NO_BUILD_ISOLATION=NO
%pyproject_run_pytest -vra

%files
%_man1dir/tox.1.*
%_bindir/tox.py3
%bash_completions_dir/tox.py3
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 26 2026 Stanislav Levin <slev@altlinux.org> 4.56.1-alt1
- 4.56.0 -> 4.56.1

* Wed Jun 24 2026 Stanislav Levin <slev@altlinux.org> 4.56.0-alt1
- 4.55.1 -> 4.56.0

* Thu Jun 04 2026 Stanislav Levin <slev@altlinux.org> 4.55.1-alt1
- 4.55.0 -> 4.55.1

* Thu May 28 2026 Stanislav Levin <slev@altlinux.org> 4.55.0-alt1
- 4.54.0 -> 4.55.0

* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 4.54.0-alt1
- 4.53.0 -> 4.54.0.

* Wed Apr 15 2026 Stanislav Levin <slev@altlinux.org> 4.53.0-alt1
- 4.52.1 -> 4.53.0.

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 4.52.1-alt1
- 4.52.0 -> 4.52.1.

* Tue Mar 31 2026 Stanislav Levin <slev@altlinux.org> 4.52.0-alt1
- 4.50.3 -> 4.52.0.

* Tue Mar 31 2026 Stanislav Levin <slev@altlinux.org> 4.50.3-alt2
- Undone Python vandalism.

* Fri Mar 20 2026 Stanislav Levin <slev@altlinux.org> 4.50.3-alt1
- 4.50.1 -> 4.50.3.

* Thu Mar 19 2026 Stanislav Levin <slev@altlinux.org> 4.50.1-alt1
- 4.50.0 -> 4.50.1.

* Wed Mar 18 2026 Stanislav Levin <slev@altlinux.org> 4.50.0-alt1
- 4.49.1 -> 4.50.0.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 4.49.1-alt1
- 4.45.0 -> 4.49.1.

* Tue Feb 24 2026 Stanislav Levin <slev@altlinux.org> 4.45.0-alt1
- 4.42.0 -> 4.45.0.

* Fri Feb 20 2026 Stanislav Levin <slev@altlinux.org> 4.42.0-alt1
- 4.40.0 -> 4.42.0.

* Thu Feb 19 2026 Stanislav Levin <slev@altlinux.org> 4.40.0-alt1
- 4.38.0 -> 4.40.0.

* Wed Feb 18 2026 Stanislav Levin <slev@altlinux.org> 4.38.0-alt1
- 4.36.1 -> 4.38.0.

* Tue Feb 17 2026 Stanislav Levin <slev@altlinux.org> 4.36.1-alt1
- 4.36.0 -> 4.36.1.

* Mon Feb 16 2026 Stanislav Levin <slev@altlinux.org> 4.36.0-alt1
- 4.35.0 -> 4.36.0.

* Fri Feb 13 2026 Stanislav Levin <slev@altlinux.org> 4.35.0-alt1
- 4.32.0 -> 4.35.0.

* Mon Oct 27 2025 Stanislav Levin <slev@altlinux.org> 4.32.0-alt1
- 4.29.0 -> 4.32.0.

* Wed Sep 03 2025 Stanislav Levin <slev@altlinux.org> 4.29.0-alt1
- 4.28.4 -> 4.29.0.

* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 4.28.4-alt1
- 4.28.3 -> 4.28.4.

* Mon Jul 28 2025 Stanislav Levin <slev@altlinux.org> 4.28.3-alt1
- 4.28.1 -> 4.28.3.

* Wed Jul 23 2025 Stanislav Levin <slev@altlinux.org> 4.28.1-alt1
- 4.28.0 -> 4.28.1.

* Mon Jul 21 2025 Stanislav Levin <slev@altlinux.org> 4.28.0-alt1
- 4.27.0 -> 4.28.0.

* Wed Jun 18 2025 Stanislav Levin <slev@altlinux.org> 4.27.0-alt1
- 4.26.0 -> 4.27.0.

* Mon May 19 2025 Stanislav Levin <slev@altlinux.org> 4.26.0-alt1
- 4.25.0 -> 4.26.0.

* Fri Mar 28 2025 Stanislav Levin <slev@altlinux.org> 4.25.0-alt1
- 4.24.2 -> 4.25.0.

* Mon Mar 10 2025 Stanislav Levin <slev@altlinux.org> 4.24.2-alt1
- 4.24.1 -> 4.24.2.

* Mon Feb 10 2025 Stanislav Levin <slev@altlinux.org> 4.24.1-alt1
- 4.23.2 -> 4.24.1.

* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 4.23.2-alt1
- 3.27.1 -> 4.23.2 (closes: #49165).

* Wed Apr 17 2024 Stanislav Levin <slev@altlinux.org> 3.27.1-alt4
- Fixed FTBFS (setuptools 69.3.0).

* Mon Feb 12 2024 Stanislav Levin <slev@altlinux.org> 3.27.1-alt3
- Fixed FTBFS (Pytest 8).

* Fri Jan 26 2024 Stanislav Levin <slev@altlinux.org> 3.27.1-alt2
- Fixed FTBFS (Python 3.12).

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 3.27.1-alt1
- 3.27.0 -> 3.27.1.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 3.27.0-alt1
- 3.26.0 -> 3.27.0.

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 3.26.0-alt1
- 3.25.1 -> 3.26.0.

* Thu Jul 21 2022 Stanislav Levin <slev@altlinux.org> 3.25.1-alt1
- 3.24.5 -> 3.25.1.

* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 3.24.5-alt1
- 3.24.4 -> 3.24.5.

* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 3.24.4-alt1
- 3.24.3 -> 3.24.4.

* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 3.24.3-alt1
- 3.24.0 -> 3.24.3.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 3.24.0-alt1
- 3.23.1 -> 3.24.0.

* Fri May 07 2021 Stanislav Levin <slev@altlinux.org> 3.23.1-alt1
- 3.23.0 -> 3.23.1.

* Sat Apr 24 2021 Stanislav Levin <slev@altlinux.org> 3.23.0-alt1
- 3.20.1 -> 3.23.0.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 3.20.1-alt1
- 3.15.0 -> 3.20.1.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 3.15.0-alt3
- Stopped Python2 package build.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 3.15.0-alt2
- Unpinned pytest-mock.

* Tue May 12 2020 Stanislav Levin <slev@altlinux.org> 3.15.0-alt1
- 3.14.2 -> 3.15.0.

* Wed Apr 29 2020 Stanislav Levin <slev@altlinux.org> 3.14.2-alt2
- Fixed FTBFS.

* Thu Dec 12 2019 Stanislav Levin <slev@altlinux.org> 3.14.2-alt1
- 3.14.1 -> 3.14.2.

* Fri Nov 15 2019 Stanislav Levin <slev@altlinux.org> 3.14.1-alt1
- 3.14.0 -> 3.14.1.

* Fri Oct 11 2019 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.13.2 -> 3.14.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.13.2-alt2
- Fixed testing against Pytest 5.

* Fri Aug 02 2019 Stanislav Levin <slev@altlinux.org> 3.13.2-alt1
- 3.12.1 -> 3.13.2.

* Fri May 24 2019 Stanislav Levin <slev@altlinux.org> 3.12.1-alt1
- 3.11.1 -> 3.12.1.

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 3.11.1-alt1
- 3.11.0 -> 3.11.1.

* Thu May 16 2019 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.0 -> 3.11.0.

* Mon May 13 2019 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.0 -> 3.10.0.

* Wed May 01 2019 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.7.0 -> 3.9.0.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.1 -> 3.7.0.

* Mon Dec 31 2018 Stanislav Levin <slev@altlinux.org> 3.6.1-alt1
- 3.5.3 -> 3.6.1.

* Mon Oct 29 2018 Stanislav Levin <slev@altlinux.org> 3.5.3-alt1
- 3.5.2 -> 3.5.3.

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 3.5.2-alt1
- 3.2.1 -> 3.5.2.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 3.2.1-alt1
- 3.0.0 -> 3.2.1.

* Wed Apr 11 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.9.1 -> 3.0.0

* Thu Oct 19 2017 Stanislav Levin <slev@altlinux.org> 2.9.1-alt1
- Version 2.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

