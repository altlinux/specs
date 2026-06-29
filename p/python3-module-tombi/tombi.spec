%define _unpackaged_files_terminate_build 1
# https://github.com/briansmith/ring/discussions/2753
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define pypi_name tombi
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.6
Release: alt1
Summary: TOML Toolkit
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tombi
Vcs: https://github.com/tombi-toml/tombi
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: vendor_rust.tar
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
Requires: %pypi_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# not packaged
%add_pyproject_deps_check_filter 'pytest-stub$'
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%package -n %pypi_name
Summary: %summary
Group: Development/Python3

%description -n %pypi_name
%summary.

%prep
%setup -a2
cat < vendor_cargoconf.toml >> .cargo/config.toml
%autopatch -p1
# upstream uses GHA to set version based on git tag
sed -i 's/@VERSION@/%version/' pyproject.toml Cargo.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
export CARGO_TERM_VERBOSE=true
export RUSTFLAGS="${RUSTFLAGS} -g"
export CARGO_PROFILE_RELEASE_STRIP='none'
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %pypi_name
%_bindir/tombi

%changelog
* Mon Jun 29 2026 Stanislav Levin <slev@altlinux.org> 1.1.6-alt1
- 1.1.5 -> 1.1.6

* Tue Jun 23 2026 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- 1.1.4 -> 1.1.5

* Mon Jun 22 2026 Stanislav Levin <slev@altlinux.org> 1.1.4-alt1
- 1.1.3 -> 1.1.4

* Thu Jun 11 2026 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.1.2 -> 1.1.3

* Mon Jun 08 2026 Stanislav Levin <slev@altlinux.org> 1.1.2-alt1
- 1.1.1 -> 1.1.2

* Fri May 29 2026 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.0 -> 1.1.1

* Mon May 25 2026 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- updated from 0.11.5 to 1.0.0

* Mon May 18 2026 Stanislav Levin <slev@altlinux.org> 0.11.5-alt1
- 0.11.4 -> 0.11.5.

* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 0.11.4-alt1
- Initial build for sisyphus.
