%define _unpackaged_files_terminate_build 1
%define pypi_name distlib

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.3
Release: alt1
Summary: Distribution utilities
License: Python
Group: Development/Python3
Url: https://pypi.org/project/distlib/
Vcs: https://github.com/pypa/distlib
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Distlib is a library which implements low-level functions that relate to
packaging and distribution of Python software. It is intended to be used as the
basis for third-party packaging tools.

%prep
%setup
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

# win files
rm -v distlib/*.exe

%build
%pyproject_build

%install
%pyproject_install

%check
export SKIP_ONLINE=yes
# required, see docs/tutorial.rst
export PYTHONHASHSEED=0
%pyproject_run -- python tests/test_all.py

%files
%python3_sitelibdir/distlib/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 15 2026 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1
- 0.4.1 -> 0.4.3

* Wed Jun 03 2026 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1
- 0.4.0 -> 0.4.1

* Thu Oct 16 2025 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1.1
- NMU: Fixed FTBFS.

* Fri Jul 18 2025 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.9 -> 0.4.0.

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 0.3.9-alt1
- 0.3.8 -> 0.3.9.

* Fri Dec 15 2023 Stanislav Levin <slev@altlinux.org> 0.3.8-alt1
- 0.3.7 -> 0.3.8.

* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 0.3.7-alt1
- 0.3.6 -> 0.3.7.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 0.3.6-alt1
- 0.3.5 -> 0.3.6.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1
- 0.3.4 -> 0.3.5.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1
- 0.3.1 -> 0.3.4.

* Mon Oct 26 2020 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus.

