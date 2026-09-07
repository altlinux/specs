%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-mypyc
%define mod_name hatch_mypyc

%def_with check

Name: python3-module-%pypi_name
Version: 0.16.0
Release: alt1
Summary: Hatch build hook plugin for Mypyc
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-mypyc
Vcs: https://github.com/ofek/hatch-mypyc
# mypyc is not built for i586
ExcludeArch: %ix86
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# mypyc is subpackaged from mypy
Requires: python3-module-mypyc
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# assumed to be installed by 'build'
BuildRequires: python3-module-mypyc
BuildRequires: python3-module-charset-normalizer
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_hatch hatch.toml default
%endif

%build
%pyproject_build

%install
%pyproject_install

# synthetically arch specific
%if "%python3_sitelibdir" != "%python3_sitelibdir_noarch"
mkdir -p %buildroot%python3_sitelibdir
mv -fT %buildroot%python3_sitelibdir_noarch %buildroot%python3_sitelibdir
%endif

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Mar 05 2026 Stanislav Levin <slev@altlinux.org> 0.16.0-alt1
- Initial build for sisyphus.
