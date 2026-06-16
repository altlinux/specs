%define _unpackaged_files_terminate_build 1
%define optflags_lto %nil
%define pypi_name uv
%define mod_name %pypi_name
%define uv_version 0.11.21

%define pypi_name_uv_build uv-build
%define mod_name_uv_build uv_build
%define uv_build_version %uv_version
%define uv_build_backend_dir crates/uv-build
%define bash_completions_dir %_datadir/bash-completion/completions

%def_with check

Name: python3-module-%pypi_name
Version: %uv_version
Release: alt1
Summary: An extremely fast Python package installer and resolver
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/uv
Vcs: https://github.com/astral-sh/uv
Source: %name-%version.tar
Source1: vendor_rust.tar
Source2: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
Requires: %pypi_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: /usr/bin/cmake
BuildRequires: libssl-devel
%if_with check
%pyproject_builddeps_metadata
%endif

%description
An extremely fast Python package installer and resolver, written in Rust.
Designed as a drop-in replacement for common pip and pip-tools workflows.

%package -n %pypi_name
Summary: %summary
Group: Development/Python3
# uv executable was shipped in python package
Conflicts: python3-module-%pypi_name <= 0.5.26-alt1

%description -n %pypi_name
%summary.

%package -n %pypi_name_uv_build
Version: %uv_build_version
Summary: Executable for uv build backend
Group: Development/Python3

%description -n %pypi_name_uv_build
%summary.

%package build
Version: %uv_build_version
Summary: uv build backend
Group: Development/Python3
Requires: %pypi_name_uv_build

%description build
%summary.

%prep
%setup -a1
%autopatch -p1
cat < vendor_cargoconf.toml >> .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export CARGO_TERM_VERBOSE=true
%ifarch %ix86
# fails with upstream's lto=fat
export CARGO_PROFILE_RELEASE_LTO=false
%else
# build with debug info, fails on i586 with 'rustc-LLVM ERROR: out of memory'
export RUSTFLAGS="${RUSTFLAGS} -g"
export CARGO_PROFILE_RELEASE_STRIP='none'
%endif
%pyproject_build

# build uv build backend
pushd %uv_build_backend_dir
%pyproject_build
popd

%install
%pyproject_install

# install uv build backend
pushd %uv_build_backend_dir
%pyproject_install
popd

# install bash completion
# https://docs.astral.sh/uv/getting-started/installation/#shell-autocompletion
mkdir -p %buildroot%bash_completions_dir
%buildroot%_bindir/uv generate-shell-completion \
    bash > %buildroot%bash_completions_dir/uv
%buildroot%_bindir/uvx --generate-shell-completion \
    bash > %buildroot%bash_completions_dir/uvx

%check
# smoke tests: .github/workflows/build-binaries.yml
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
uv --help
python -m uv --help
uvx --help
ENDTESTS

pushd %uv_build_backend_dir
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
uv-build --help
python -m uv_build --help
ENDTESTS
popd

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pep427_name %pypi_name}-%uv_version.dist-info/

%files build
%python3_sitelibdir/%mod_name_uv_build/
%python3_sitelibdir/%{pep427_name %pypi_name_uv_build}-%uv_build_version.dist-info/

%files -n %pypi_name
%_bindir/uv
%_bindir/uvx
%bash_completions_dir/uv
%bash_completions_dir/uvx

%files -n %pypi_name_uv_build
%_bindir/uv-build

%changelog
* Mon Jun 15 2026 Stanislav Levin <slev@altlinux.org> 0.11.21-alt1
- 0.11.20 -> 0.11.21

* Thu Jun 11 2026 Stanislav Levin <slev@altlinux.org> 0.11.20-alt1
- 0.11.19 -> 0.11.20

* Thu Jun 04 2026 Stanislav Levin <slev@altlinux.org> 0.11.19-alt1
- 0.11.18 -> 0.11.19

* Tue Jun 02 2026 Stanislav Levin <slev@altlinux.org> 0.11.18-alt1
- 0.11.17 -> 0.11.18

* Fri May 29 2026 Stanislav Levin <slev@altlinux.org> 0.11.17-alt1
- 0.11.16 -> 0.11.17

* Tue May 26 2026 Stanislav Levin <slev@altlinux.org> 0.11.16-alt1
- updated from 0.11.15 to 0.11.16

* Tue May 19 2026 Stanislav Levin <slev@altlinux.org> 0.11.15-alt1
- 0.11.14 -> 0.11.15.

* Fri May 15 2026 Stanislav Levin <slev@altlinux.org> 0.11.14-alt1
- 0.11.11 -> 0.11.14.

* Thu May 07 2026 Stanislav Levin <slev@altlinux.org> 0.11.11-alt1
- 0.11.8 -> 0.11.11.

* Tue Apr 28 2026 Stanislav Levin <slev@altlinux.org> 0.11.8-alt1
- 0.11.7 -> 0.11.8.

* Thu Apr 16 2026 Stanislav Levin <slev@altlinux.org> 0.11.7-alt1
- 0.11.6 -> 0.11.7.

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 0.11.6-alt1
- 0.11.5 -> 0.11.6.

* Thu Apr 09 2026 Stanislav Levin <slev@altlinux.org> 0.11.5-alt1
- 0.11.3 -> 0.11.5.

* Thu Apr 02 2026 Stanislav Levin <slev@altlinux.org> 0.11.3-alt1
- 0.11.2 -> 0.11.3.

* Fri Mar 27 2026 Stanislav Levin <slev@altlinux.org> 0.11.2-alt1
- 0.11.1 -> 0.11.2.

* Wed Mar 25 2026 Stanislav Levin <slev@altlinux.org> 0.11.1-alt1
- 0.11.0 -> 0.11.1.

* Tue Mar 24 2026 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.10.12 -> 0.11.0.

* Fri Mar 20 2026 Stanislav Levin <slev@altlinux.org> 0.10.12-alt1
- 0.10.11 -> 0.10.12.

* Tue Mar 17 2026 Stanislav Levin <slev@altlinux.org> 0.10.11-alt1
- 0.10.10 -> 0.10.11.

* Mon Mar 16 2026 Stanislav Levin <slev@altlinux.org> 0.10.10-alt1
- 0.10.9 -> 0.10.10.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 0.10.9-alt1
- 0.10.8 -> 0.10.9.

* Wed Mar 04 2026 Stanislav Levin <slev@altlinux.org> 0.10.8-alt1
- 0.10.7 -> 0.10.8.

* Mon Mar 02 2026 Stanislav Levin <slev@altlinux.org> 0.10.7-alt1
- 0.10.5 -> 0.10.7.

* Tue Feb 24 2026 Stanislav Levin <slev@altlinux.org> 0.10.5-alt1
- 0.10.4 -> 0.10.5.

* Wed Feb 18 2026 Stanislav Levin <slev@altlinux.org> 0.10.4-alt1
- 0.10.3 -> 0.10.4.

* Tue Feb 17 2026 Stanislav Levin <slev@altlinux.org> 0.10.3-alt1
- 0.10.2 -> 0.10.3.

* Wed Feb 11 2026 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- 0.10.0 -> 0.10.2.

* Fri Feb 06 2026 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1
- 0.9.30 -> 0.10.0.

* Thu Feb 05 2026 Stanislav Levin <slev@altlinux.org> 0.9.30-alt1
- 0.9.29 -> 0.9.30.

* Wed Feb 04 2026 Stanislav Levin <slev@altlinux.org> 0.9.29-alt1
- 0.9.28 -> 0.9.29.

* Fri Jan 30 2026 Stanislav Levin <slev@altlinux.org> 0.9.28-alt1
- 0.9.25 -> 0.9.28.

* Wed Jan 14 2026 Stanislav Levin <slev@altlinux.org> 0.9.25-alt1
- 0.9.24 -> 0.9.25.

* Tue Jan 13 2026 Stanislav Levin <slev@altlinux.org> 0.9.24-alt1
- 0.9.18 -> 0.9.24.

* Wed Dec 17 2025 Stanislav Levin <slev@altlinux.org> 0.9.18-alt1
- 0.9.17 -> 0.9.18.

* Wed Dec 10 2025 Stanislav Levin <slev@altlinux.org> 0.9.17-alt1
- 0.9.16 -> 0.9.17.

* Mon Dec 08 2025 Stanislav Levin <slev@altlinux.org> 0.9.16-alt1
- 0.9.15 -> 0.9.16.

* Wed Dec 03 2025 Stanislav Levin <slev@altlinux.org> 0.9.15-alt1
- 0.9.14 -> 0.9.15.

* Tue Dec 02 2025 Stanislav Levin <slev@altlinux.org> 0.9.14-alt1
- 0.9.13 -> 0.9.14.

* Thu Nov 27 2025 Stanislav Levin <slev@altlinux.org> 0.9.13-alt1
- 0.9.12 -> 0.9.13.

* Wed Nov 26 2025 Stanislav Levin <slev@altlinux.org> 0.9.12-alt1
- 0.9.11 -> 0.9.12.

* Fri Nov 21 2025 Stanislav Levin <slev@altlinux.org> 0.9.11-alt1
- 0.9.10 -> 0.9.11.

* Tue Nov 18 2025 Stanislav Levin <slev@altlinux.org> 0.9.10-alt1
- 0.9.9 -> 0.9.10.

* Fri Nov 14 2025 Stanislav Levin <slev@altlinux.org> 0.9.9-alt1
- 0.9.4 -> 0.9.9 (closes: #56853).

* Mon Oct 20 2025 Stanislav Levin <slev@altlinux.org> 0.9.4-alt1
- 0.8.17 -> 0.9.4.

* Thu Sep 11 2025 Stanislav Levin <slev@altlinux.org> 0.8.17-alt1
- 0.8.16 -> 0.8.17.

* Wed Sep 10 2025 Stanislav Levin <slev@altlinux.org> 0.8.16-alt1
- 0.8.15 -> 0.8.16.

* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 0.8.15-alt1
- 0.8.14 -> 0.8.15.

* Wed Sep 03 2025 Stanislav Levin <slev@altlinux.org> 0.8.14-alt1
- 0.8.10 -> 0.8.14.

* Thu Aug 14 2025 Stanislav Levin <slev@altlinux.org> 0.8.10-alt1
- 0.8.9 -> 0.8.10.

* Tue Aug 12 2025 Stanislav Levin <slev@altlinux.org> 0.8.9-alt1
- 0.8.8 -> 0.8.9.

* Mon Aug 11 2025 Stanislav Levin <slev@altlinux.org> 0.8.8-alt1
- 0.8.6 -> 0.8.8.

* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 0.8.6-alt1
- 0.8.5 -> 0.8.6 (fixes: CVE-2025-54368).

* Wed Aug 06 2025 Stanislav Levin <slev@altlinux.org> 0.8.5-alt1
- 0.8.4 -> 0.8.5.

* Fri Aug 01 2025 Stanislav Levin <slev@altlinux.org> 0.8.4-alt2
- Packaged bash completion.

* Thu Jul 31 2025 Stanislav Levin <slev@altlinux.org> 0.8.4-alt1
- 0.8.3 -> 0.8.4.

* Fri Jul 25 2025 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1
- 0.8.2 -> 0.8.3.

* Wed Jul 23 2025 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1
- 0.8.0 -> 0.8.2.

* Fri Jul 18 2025 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.21 -> 0.8.0.

* Tue Jul 15 2025 Stanislav Levin <slev@altlinux.org> 0.7.21-alt1
- 0.7.20 -> 0.7.21.

* Thu Jul 10 2025 Stanislav Levin <slev@altlinux.org> 0.7.20-alt1
- 0.7.19 -> 0.7.20.

* Fri Jul 04 2025 Stanislav Levin <slev@altlinux.org> 0.7.19-alt1
- 0.7.18 -> 0.7.19.

* Wed Jul 02 2025 Stanislav Levin <slev@altlinux.org> 0.7.18-alt1
- 0.7.17 -> 0.7.18.

* Tue Jul 01 2025 Stanislav Levin <slev@altlinux.org> 0.7.17-alt1
- 0.7.15 -> 0.7.17.

* Thu Jun 26 2025 Stanislav Levin <slev@altlinux.org> 0.7.15-alt1
- 0.7.14 -> 0.7.15.

* Tue Jun 24 2025 Stanislav Levin <slev@altlinux.org> 0.7.14-alt1
- 0.7.13 -> 0.7.14.

* Mon Jun 16 2025 Stanislav Levin <slev@altlinux.org> 0.7.13-alt1
- 0.7.12 -> 0.7.13.

* Mon Jun 09 2025 Stanislav Levin <slev@altlinux.org> 0.7.12-alt1
- 0.7.11 -> 0.7.12.

* Thu Jun 05 2025 Stanislav Levin <slev@altlinux.org> 0.7.11-alt1
- 0.7.7 -> 0.7.11.

* Fri May 23 2025 Stanislav Levin <slev@altlinux.org> 0.7.7-alt1
- 0.6.16 -> 0.7.7.

* Tue Apr 22 2025 Stanislav Levin <slev@altlinux.org> 0.6.16-alt1
- 0.6.14 -> 0.6.16.

* Thu Apr 10 2025 Stanislav Levin <slev@altlinux.org> 0.6.14-alt1
- 0.6.13 -> 0.6.14.

* Tue Apr 08 2025 Stanislav Levin <slev@altlinux.org> 0.6.13-alt1
- 0.6.12 -> 0.6.13.

* Fri Apr 04 2025 Stanislav Levin <slev@altlinux.org> 0.6.12-alt1
- 0.6.11 -> 0.6.12.

* Mon Mar 31 2025 Stanislav Levin <slev@altlinux.org> 0.6.11-alt1
- 0.6.10 -> 0.6.11.

* Wed Mar 26 2025 Stanislav Levin <slev@altlinux.org> 0.6.10-alt1
- 0.6.9 -> 0.6.10.

* Fri Mar 21 2025 Stanislav Levin <slev@altlinux.org> 0.6.9-alt1
- 0.6.8 -> 0.6.9.

* Wed Mar 19 2025 Stanislav Levin <slev@altlinux.org> 0.6.8-alt1
- 0.6.7 -> 0.6.8.

* Tue Mar 18 2025 Stanislav Levin <slev@altlinux.org> 0.6.7-alt1
- 0.6.6 -> 0.6.7.

* Wed Mar 12 2025 Stanislav Levin <slev@altlinux.org> 0.6.6-alt1
- 0.6.5 -> 0.6.6.

* Fri Mar 07 2025 Stanislav Levin <slev@altlinux.org> 0.6.5-alt1
- 0.6.4 -> 0.6.5.

* Tue Mar 04 2025 Stanislav Levin <slev@altlinux.org> 0.6.4-alt1
- 0.6.3 -> 0.6.4.

* Tue Feb 25 2025 Stanislav Levin <slev@altlinux.org> 0.6.3-alt1
- 0.6.2 -> 0.6.3.

* Thu Feb 20 2025 Stanislav Levin <slev@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2.

* Tue Feb 18 2025 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1.

* Mon Feb 17 2025 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.31 -> 0.6.0.

* Fri Feb 14 2025 Stanislav Levin <slev@altlinux.org> 0.5.31-alt1
- 0.5.30 -> 0.5.31.

* Tue Feb 11 2025 Stanislav Levin <slev@altlinux.org> 0.5.30-alt1
- 0.5.29 -> 0.5.30.

* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 0.5.29-alt1
- 0.5.28 -> 0.5.29.

* Wed Feb 05 2025 Stanislav Levin <slev@altlinux.org> 0.5.28-alt1
- 0.5.27 -> 0.5.28.

* Tue Feb 04 2025 Stanislav Levin <slev@altlinux.org> 0.5.27-alt1
- 0.5.26 -> 0.5.27.

* Mon Feb 03 2025 Stanislav Levin <slev@altlinux.org> 0.5.26-alt1
- 0.5.25 -> 0.5.26.

* Wed Jan 29 2025 Stanislav Levin <slev@altlinux.org> 0.5.25-alt1
- 0.5.24 -> 0.5.25.

* Fri Jan 24 2025 Stanislav Levin <slev@altlinux.org> 0.5.24-alt1
- 0.5.23 -> 0.5.24.

* Thu Jan 23 2025 Stanislav Levin <slev@altlinux.org> 0.5.23-alt1
- 0.5.22 -> 0.5.23.

* Wed Jan 22 2025 Stanislav Levin <slev@altlinux.org> 0.5.22-alt1
- 0.5.21 -> 0.5.22.

* Mon Jan 20 2025 Stanislav Levin <slev@altlinux.org> 0.5.21-alt1
- 0.5.20 -> 0.5.21.

* Thu Jan 16 2025 Stanislav Levin <slev@altlinux.org> 0.5.20-alt1
- 0.5.18 -> 0.5.20.

* Mon Jan 13 2025 Stanislav Levin <slev@altlinux.org> 0.5.18-alt1
- 0.5.16 -> 0.5.18.

* Thu Jan 09 2025 Stanislav Levin <slev@altlinux.org> 0.5.16-alt1
- 0.5.13 -> 0.5.16.

* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 0.5.13-alt1
- 0.5.12 -> 0.5.13.

* Fri Dec 27 2024 Stanislav Levin <slev@altlinux.org> 0.5.12-alt1
- 0.5.11 -> 0.5.12.

* Mon Dec 23 2024 Stanislav Levin <slev@altlinux.org> 0.5.11-alt1
- 0.5.8 -> 0.5.11.

* Thu Dec 12 2024 Stanislav Levin <slev@altlinux.org> 0.5.8-alt1
- 0.5.7 -> 0.5.8.

* Mon Dec 09 2024 Stanislav Levin <slev@altlinux.org> 0.5.7-alt1
- 0.5.6 -> 0.5.7.

* Wed Dec 04 2024 Stanislav Levin <slev@altlinux.org> 0.5.6-alt1
- 0.5.5 -> 0.5.6.

* Thu Nov 28 2024 Stanislav Levin <slev@altlinux.org> 0.5.5-alt1
- 0.5.4 -> 0.5.5.

* Thu Nov 21 2024 Stanislav Levin <slev@altlinux.org> 0.5.4-alt1
- 0.5.3 -> 0.5.4.

* Wed Nov 20 2024 Stanislav Levin <slev@altlinux.org> 0.5.3-alt1
- 0.5.2 -> 0.5.3.

* Fri Nov 15 2024 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1
- 0.5.1 -> 0.5.2.

* Mon Nov 11 2024 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.5.0 -> 0.5.1.

* Fri Nov 08 2024 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.30 -> 0.5.0.

* Wed Nov 06 2024 Stanislav Levin <slev@altlinux.org> 0.4.30-alt1
- 0.4.27 -> 0.4.30.

* Mon Oct 28 2024 Stanislav Levin <slev@altlinux.org> 0.4.27-alt1
- 0.4.26 -> 0.4.27.

* Thu Oct 24 2024 Stanislav Levin <slev@altlinux.org> 0.4.26-alt1
- 0.4.25 -> 0.4.26.

* Tue Oct 22 2024 Stanislav Levin <slev@altlinux.org> 0.4.25-alt1
- 0.4.24 -> 0.4.25.

* Mon Oct 21 2024 Stanislav Levin <slev@altlinux.org> 0.4.24-alt1
- 0.4.22 -> 0.4.24.

* Wed Oct 16 2024 Stanislav Levin <slev@altlinux.org> 0.4.22-alt1
- 0.4.21 -> 0.4.22.

* Tue Oct 15 2024 Stanislav Levin <slev@altlinux.org> 0.4.21-alt1
- 0.4.20 -> 0.4.21.

* Wed Oct 09 2024 Stanislav Levin <slev@altlinux.org> 0.4.20-alt1
- 0.4.19 -> 0.4.20.

* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 0.4.19-alt1
- 0.4.18 -> 0.4.19.

* Mon Oct 07 2024 Stanislav Levin <slev@altlinux.org> 0.4.18-alt1
- 0.4.16 -> 0.4.18.

* Wed Sep 25 2024 Stanislav Levin <slev@altlinux.org> 0.4.16-alt1
- 0.4.15 -> 0.4.16.

* Mon Sep 23 2024 Stanislav Levin <slev@altlinux.org> 0.4.15-alt1
- 0.4.12 -> 0.4.15.

* Thu Sep 19 2024 Stanislav Levin <slev@altlinux.org> 0.4.12-alt1
- 0.4.11 -> 0.4.12.

* Wed Sep 18 2024 Stanislav Levin <slev@altlinux.org> 0.4.11-alt1
- 0.4.10 -> 0.4.11.

* Mon Sep 16 2024 Stanislav Levin <slev@altlinux.org> 0.4.10-alt1
- 0.4.9 -> 0.4.10.

* Thu Sep 12 2024 Stanislav Levin <slev@altlinux.org> 0.4.9-alt1
- 0.4.3 -> 0.4.9.

* Tue Sep 03 2024 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1
- 0.2.33 -> 0.4.3.

* Fri Aug 02 2024 Stanislav Levin <slev@altlinux.org> 0.2.33-alt1
- 0.2.32 -> 0.2.33.

* Wed Jul 31 2024 Stanislav Levin <slev@altlinux.org> 0.2.32-alt1
- 0.2.31 -> 0.2.32.

* Tue Jul 30 2024 Stanislav Levin <slev@altlinux.org> 0.2.31-alt1
- 0.2.30 -> 0.2.31.

* Mon Jul 29 2024 Stanislav Levin <slev@altlinux.org> 0.2.30-alt1
- 0.2.29 -> 0.2.30.

* Thu Jul 25 2024 Stanislav Levin <slev@altlinux.org> 0.2.29-alt1
- 0.2.28 -> 0.2.29.

* Wed Jul 24 2024 Stanislav Levin <slev@altlinux.org> 0.2.28-alt1
- 0.2.27 -> 0.2.28.

* Mon Jul 22 2024 Stanislav Levin <slev@altlinux.org> 0.2.27-alt1
- 0.2.26 -> 0.2.27.

* Thu Jul 18 2024 Stanislav Levin <slev@altlinux.org> 0.2.26-alt1
- 0.2.25 -> 0.2.26.

* Tue Jul 16 2024 Stanislav Levin <slev@altlinux.org> 0.2.25-alt1
- 0.2.24 -> 0.2.25.

* Fri Jul 12 2024 Stanislav Levin <slev@altlinux.org> 0.2.24-alt1
- 0.2.23 -> 0.2.24.

* Tue Jul 09 2024 Stanislav Levin <slev@altlinux.org> 0.2.23-alt1
- 0.2.22 -> 0.2.23.

* Mon Jul 08 2024 Stanislav Levin <slev@altlinux.org> 0.2.22-alt1
- 0.2.21 -> 0.2.22.

* Wed Jul 03 2024 Stanislav Levin <slev@altlinux.org> 0.2.21-alt1
- 0.2.18 -> 0.2.21.

* Mon Jul 01 2024 Stanislav Levin <slev@altlinux.org> 0.2.18-alt1
- 0.2.17 -> 0.2.18.

* Thu Jun 27 2024 Stanislav Levin <slev@altlinux.org> 0.2.17-alt1
- 0.2.15 -> 0.2.17.

* Tue Jun 25 2024 Stanislav Levin <slev@altlinux.org> 0.2.15-alt1
- 0.2.13 -> 0.2.15.

* Thu Jun 20 2024 Stanislav Levin <slev@altlinux.org> 0.2.13-alt1
- 0.2.12 -> 0.2.13.

* Tue Jun 18 2024 Stanislav Levin <slev@altlinux.org> 0.2.12-alt1
- 0.2.11 -> 0.2.12.

* Thu Jun 13 2024 Stanislav Levin <slev@altlinux.org> 0.2.11-alt1
- 0.2.10 -> 0.2.11.

* Tue Jun 11 2024 Stanislav Levin <slev@altlinux.org> 0.2.10-alt1
- 0.2.9 -> 0.2.10.

* Fri Jun 07 2024 Stanislav Levin <slev@altlinux.org> 0.2.9-alt1
- 0.2.8 -> 0.2.9.

* Thu Jun 06 2024 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1
- 0.2.6 -> 0.2.8.

* Tue Jun 04 2024 Stanislav Levin <slev@altlinux.org> 0.2.6-alt1
- 0.2.5 -> 0.2.6.

* Wed May 29 2024 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1
- 0.2.4 -> 0.2.5.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1
- 0.2.2 -> 0.2.4.

* Fri May 24 2024 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1
- 0.1.45 -> 0.2.2.

* Tue May 21 2024 Stanislav Levin <slev@altlinux.org> 0.1.45-alt1
- 0.1.44 -> 0.1.45.

* Wed May 15 2024 Stanislav Levin <slev@altlinux.org> 0.1.44-alt1
- 0.1.43 -> 0.1.44.

* Tue May 14 2024 Stanislav Levin <slev@altlinux.org> 0.1.43-alt1
- 0.1.42 -> 0.1.43.

* Mon May 13 2024 Stanislav Levin <slev@altlinux.org> 0.1.42-alt1
- 0.1.41 -> 0.1.42.

* Wed May 08 2024 Stanislav Levin <slev@altlinux.org> 0.1.41-alt1
- 0.1.39 -> 0.1.41.

* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 0.1.39-alt1
- 0.1.38 -> 0.1.39.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 0.1.38-alt1
- Initial build for Sisyphus.
