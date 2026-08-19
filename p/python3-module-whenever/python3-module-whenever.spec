%define _unpackaged_files_terminate_build 1
%define pypi_name whenever
%define mod_name whenever

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.5
Release: alt1

Summary: Modern datetime library for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/whenever/
Vcs: https://github.com/ariebovenberg/whenever

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %pyproject_deps_config_name
Source3: config.toml
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-tzdata
%endif

%description
Whenever helps you write correct and type checked datetime code, using
well-established concepts from modern libraries in other languages.
It's also way faster than other third-party libraries, and usually the standard
library as well.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE3 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export TZ=UTC
%pyproject_run_pytest -vra tests -o=addopts=

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 19 2026 Anton Zhukharev <ancieg@altlinux.org> 0.10.5-alt1
- Packaged for ALT Sisyphus.
