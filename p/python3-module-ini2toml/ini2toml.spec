%define _unpackaged_files_terminate_build 1
%define pypi_name ini2toml

%def_with check

Name: python3-module-%pypi_name
Version: 0.15
Release: alt1
Summary: Automatically conversion of .ini/.cfg files to TOML equivalents
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/ini2toml
VCS: https://github.com/abravalheri/ini2toml.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage extras dependencies with metadata
AutoReq: yes, nopython3

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_metadata_extra testing
%pyproject_builddeps_metadata_extra experimental
%endif

%description
The original purpose of this project is to help migrating setup.cfg files to
PEP621, but by extension it can also be used to convert any compatible .ini/.cfg
file to TOML.

%package lite
Summary: %summary
Group: Development/Python3
Requires: %name
%pyproject_runtimedeps_metadata -- --extra lite
Provides: %name+lite = %EVR

%description lite
Extra 'lite' for %pypi_name.

%package full
Summary: %summary
Group: Development/Python3
Requires: %name
%pyproject_runtimedeps_metadata -- --extra full
Provides: %name+full = %EVR

%description full
Extra 'full' for %pypi_name.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -o=addopts=-Wignore

%files
%doc README.rst
%_bindir/%pypi_name
%python3_sitelibdir/ini2toml/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files lite
%files full
%changelog
* Tue May 14 2024 Stanislav Levin <slev@altlinux.org> 0.15-alt1
- 0.14 -> 0.15.

* Mon Apr 22 2024 Stanislav Levin <slev@altlinux.org> 0.14-alt1
- 0.13 -> 0.14.

* Fri Oct 27 2023 Stanislav Levin <slev@altlinux.org> 0.13-alt1
- 0.12 -> 0.13.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 0.12-alt1
- 0.11.3 -> 0.12.

* Thu Nov 24 2022 Stanislav Levin <slev@altlinux.org> 0.11.3-alt1
- 0.11.1 -> 0.11.3.

* Tue Nov 15 2022 Stanislav Levin <slev@altlinux.org> 0.11.1-alt1
- 0.11 -> 0.11.1.

* Fri Aug 12 2022 Stanislav Levin <slev@altlinux.org> 0.11-alt1
- 0.10 -> 0.11.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.10-alt1
- Initial build for Sisyphus.
