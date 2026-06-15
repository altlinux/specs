%define _unpackaged_files_terminate_build 1
%define pypi_name backports-zstd
%define ns_name backports
%define mod_name zstd

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.0
Release: alt1
Summary: Backport of compression.zstd
License: PSF-2.0
Group: Development/Python3
Url: https://pypi.org/project/backports-zstd
Vcs: https://github.com/rogdham/backports.zstd
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
# prepared with https://git.altlinux.org/people/slev/public/updater_submodules.git
Source2: modules.tar
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libzstd-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
%summary.

%prep
%setup -a2
# use system zstd, remove the bundled one just in case
rm -r src/c/zstd/
# workaround for generating zstd license (see setup.py for details)
mkdir src/c/zstd && touch src/c/zstd/LICENSE
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
# https://github.com/rogdham/backports.zstd?tab=readme-ov-file#can-i-use-the-libzstd-version-installed-on-my-system
%pyproject_build --backend-config-settings='{"--build-option": ["--system-zstd"]}'

%install
%pyproject_install

%check
export BACKPORTSZSTD_SKIP_EXTENSION_TEST=1
%pyproject_run_unittest discover tests -v

%files
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 15 2026 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.5.0 -> 1.6.0

* Thu May 14 2026 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.3.0 -> 1.5.0.

* Thu Jan 15 2026 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Mon Dec 08 2025 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Wed Nov 26 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.0 -> 1.1.0.

* Thu Oct 30 2025 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1
- Initial build for sisyphus.
