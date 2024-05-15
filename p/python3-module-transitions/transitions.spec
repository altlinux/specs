%define _unpackaged_files_terminate_build 1
%define pypi_name transitions
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.1
Release: alt1

Summary: A lightweight, object-oriented Python state machine implementation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/transitions/
Vcs: https://github.com/pytransitions/transitions
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps -- check_pipfile1 --exclude %pyproject_deps_check_filter
%pyproject_builddeps -- check_pipfile2 --exclude %pyproject_deps_check_filter
# dot's output is polluted with
# Fontconfig error: Cannot load default config file: No such file: (null)
# if /etc/fonts/fonts.conf is missing
BuildRequires: fontconfig
# still required for rendering
BuildRequires: fonts-ttf-dejavu
%endif

%description
A lightweight, object-oriented finite state machine implementation in
Python.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync check_pipfile1 pip_reqfile requirements_test.txt
%pyproject_deps_resync check_pipfile2 pip_reqfile requirements_diagrams.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore tests

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 15 2024 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1
- 0.9.0 -> 0.9.1.

* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 0.9.0-alt2
- Fixed FTBFS (pytest-xdist 3).

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- 0.8.11 -> 0.9.0.
- use %%pyproject macros
- run tests outside tox (they don't work inside it: the issue is
  related to fontconfig)

* Fri Mar 11 2022 Stanislav Levin <slev@altlinux.org> 0.8.11-alt1
- 0.8.8 -> 0.8.11.

* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 0.8.8-alt1
- 0.2.3 -> 0.8.8.
- Enabled testing.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1.git20150114.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20150114
- Initial build for Sisyphus

