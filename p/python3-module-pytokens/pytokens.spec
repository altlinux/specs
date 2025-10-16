%define _unpackaged_files_terminate_build 1
%define pypi_name pytokens
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt1
Summary: Fast, spec compliant Python 3.13+ tokenizer
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytokens
Vcs: https://github.com/tusharsadhwani/pytokens
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%endif

%description
%summary.

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
%pyproject_run_pytest -vra -o=addopts=''

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 15 2025 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- initial build for sisyphus (0.2.0).
