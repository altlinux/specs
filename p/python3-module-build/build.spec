%define _unpackaged_files_terminate_build 1
%define pypi_name build

%def_with check
%def_with uv

%define add_python_extra() \
%{expand:%%package -n %%name+%{1} \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%{expand:%%pyproject_runtimedeps_metadata -- --extra %{1}} \
%%description -n %%name+%{1}' \
Extra "%{1}" for %%pypi_name. \
%%files -n %%name+%{1} \
}

Name: python3-module-%pypi_name
Version: 1.2.1
Release: alt3

Summary: Simple, correct PEP 517 build frontend
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/build
VCS: https://github.com/pypa/build.git
BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

# manually manage extras dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_metadata_extra uv
%pyproject_builddeps_metadata_extra virtualenv
%endif

%if_with uv
%add_python_extra uv
%endif

%description
A simple, correct PEP 517 build frontend.

build will invoke the PEP 517 hooks to build a distribution package.
It is a simple build tool and does not perform any dependency management.

%package -n pyproject-build
Summary: Executable for python-build
Group: Development/Python3
# not autodetected dep
Requires: python3-module-%pypi_name

%description -n pyproject-build
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
%pyproject_run_pytest -vra -m 'not network'

%files
%doc README.md
%python3_sitelibdir/build/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n pyproject-build
%_bindir/pyproject-build

%changelog
* Sun May 19 2024 Michael Shigorin <mike@altlinux.org> 1.2.1-alt3
- Made uv subpackage conditional (on by default)
  since python3-module-uv is lacking on e2k right now.

* Wed May 08 2024 Stanislav Levin <slev@altlinux.org> 1.2.1-alt2
- Added uv subpackage.

* Fri Mar 29 2024 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.1.1 -> 1.2.1.

* Fri Mar 01 2024 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.3 -> 1.1.1.

* Thu Feb 15 2024 Stanislav Levin <slev@altlinux.org> 1.0.3-alt2
- Fixed FTBFS (setuptools 69.0.3).

* Thu Sep 14 2023 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1
- 0.10.0 -> 1.0.3.

* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.0 -> 0.10.0.

* Thu Oct 27 2022 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.0 -> 0.9.0.

* Mon Sep 26 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt2
- Fixed FTBFS (missing tests dependency on toml).

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.0 -> 0.8.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
