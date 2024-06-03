%define _unpackaged_files_terminate_build 1
%define pypi_name graphviz
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.20.3
Release: alt2
Summary: Simple Python interface for Graphviz
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/graphviz/
VCS: https://github.com/xflr6/graphviz
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-%release.patch
Requires: graphviz
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: graphviz
# dot's output is polluted with
# Fontconfig error: Cannot load default config file: No such file: (null)
# if /etc/fonts/fonts.conf is missing
BuildRequires: fontconfig
%pyproject_builddeps_metadata_extra test
%endif

%description
%summary

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# pytest 8.1.1:
# - https://github.com/xflr6/graphviz/issues/219
# - https://github.com/pytest-dev/pytest/issues/12123
%pyproject_run -- python3 run-tests.py \
    --ignore ./tests/conftest.py \
    --ignore ./tests/backend/conftest.py

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 0.20.3-alt2
- Fixed FTBFS (Pytest 8.1.1).

* Thu Mar 21 2024 Stanislav Levin <slev@altlinux.org> 0.20.3-alt1
- 0.20.2 -> 0.20.3.

* Mon Mar 18 2024 Stanislav Levin <slev@altlinux.org> 0.20.2-alt1
- 0.20.1 -> 0.20.2.

* Wed Feb 28 2024 Stanislav Levin <slev@altlinux.org> 0.20.1-alt4
- Fixed FTBFS.

* Thu Jan 25 2024 Anton Vyatkin <toni@altlinux.org> 0.20.1-alt3
- Fixed FTBFS.

* Mon May 15 2023 Stanislav Levin <slev@altlinux.org> 0.20.1-alt2
- Added missing runtime requirement (dot).

* Mon May 15 2023 Anton Vyatkin <toni@altlinux.org> 0.20.1-alt1
- New version 0.20.1 (Closes: #42049).

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.19.1-alt2
- Fixed FTBFS (workaround for libpango-1.50.5).

* Fri Dec 17 2021 Anton Farygin <rider@altlinux.ru> 0.19.1-alt1
- 0.19.1

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 0.19-alt1
- 0.19

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 0.13.2-alt1
- first build for ALT

