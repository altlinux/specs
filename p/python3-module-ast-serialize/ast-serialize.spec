%define _unpackaged_files_terminate_build 1
%define pypi_name ast-serialize
%define mod_name ast_serialize

# see Cargo.toml
%python3_set_limited_api 3.9

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1
Summary: Python bindings for mypy AST serialization
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ast-serialize
Vcs: https://github.com/mypyc/ast_serialize
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: vendor_rust.tar
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
%summary.

%prep
%setup -a2
%autopatch -p1
cat < vendor_cargoconf.toml >> .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export CARGO_TERM_VERBOSE=true
export RUSTFLAGS="${RUSTFLAGS} -g"
export CARGO_PROFILE_RELEASE_STRIP='none'
%pyproject_build

%install
%pyproject_install

%check
# .github/workflows/test.yml
%pyproject_run -- python test_ast_serialize.py

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 01 2026 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0

* Mon May 18 2026 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.0 -> 0.5.0.

* Fri May 15 2026 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.0 -> 0.4.0.

* Thu May 07 2026 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.2.2 -> 0.3.0.

* Thu Apr 30 2026 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1
- 0.2.1 -> 0.2.2.

* Wed Apr 29 2026 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1
- 0.2.0 -> 0.2.1.

* Thu Apr 23 2026 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- 0.1.2 -> 0.2.0.

* Wed Apr 08 2026 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1
- updated from 0.1.1 to 0.1.2

* Wed Apr 01 2026 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1
- Initial build for sisyphus.
