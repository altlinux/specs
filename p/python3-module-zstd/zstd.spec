%define _unpackaged_files_terminate_build 1
%define pypi_name zstd
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.7.3
Release: alt1

Summary: Zstd Bindings for Python

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/zstd/
Vcs: https://github.com/sergey-dryabzhinsky/python-zstd
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: gcc
BuildRequires: libzstd-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Simple Python bindings for the Zstd compression library.

%prep
%setup
%autopatch -p1
# Remove bundled zstd library
rm -r zstd
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export ZSTD_EXTERNAL=1
%pyproject_build

%install
%pyproject_install

%check
# there is no option to exclude tests via CLI
# speed tests check nothing but measure and report speed
rm tests/test_speed.py
%pyproject_run_unittest -v

%files
%python3_sitelibdir/%mod_name.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Apr 09 2026 Stanislav Levin <slev@altlinux.org> 1.5.7.3-alt1
- 1.5.7.2 -> 1.5.7.3.

* Tue Jun 24 2025 Stanislav Levin <slev@altlinux.org> 1.5.7.2-alt1
- 1.5.7.1 -> 1.5.7.2.

* Mon Jun 09 2025 Stanislav Levin <slev@altlinux.org> 1.5.7.1-alt1
- 1.5.7.0 -> 1.5.7.1.

* Tue Jun 03 2025 Stanislav Levin <slev@altlinux.org> 1.5.7.0-alt1
- 1.5.6.7 -> 1.5.7.0.

* Fri Apr 04 2025 Stanislav Levin <slev@altlinux.org> 1.5.6.7-alt1
- 1.5.6.6 -> 1.5.6.7.

* Tue Mar 04 2025 Stanislav Levin <slev@altlinux.org> 1.5.6.6-alt1
- 1.5.6.4 -> 1.5.6.6.

* Mon Feb 24 2025 Stanislav Levin <slev@altlinux.org> 1.5.6.4-alt1
- 1.5.6.1 -> 1.5.6.4.

* Thu Jan 09 2025 Stanislav Levin <slev@altlinux.org> 1.5.6.1-alt1
- 1.5.5.1 -> 1.5.6.1.

* Fri Oct 18 2024 Stanislav Levin <slev@altlinux.org> 1.5.5.1-alt1
- 1.5.0.4 -> 1.5.5.1.

* Mon Dec 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0.4-alt1
- Build new version.

* Tue Sep 29 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.5.1-alt1
- Initial build for Sisiphus.
