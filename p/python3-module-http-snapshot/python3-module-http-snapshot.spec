%define _unpackaged_files_terminate_build 1
%define pypi_name http-snapshot
%define mod_name http_snapshot

%def_with check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 0.1.9
Release: alt1

Summary: pytest plugin that snapshots requests made with popular Python HTTP clients
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/http-snapshot/
Vcs: https://github.com/karpetrosyan/http-snapshot

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra httpx
%pyproject_builddeps_metadata_extra requests
%pyproject_builddeps_check
%endif

%description
http-snapshot is a pytest plugin that captures and snapshots HTTP
requests/responses made with popular Python HTTP clients like httpx and
requests. It uses inline-snapshot to store HTTP interactions as JSON files,
enabling fast and reliable HTTP testing without making actual network calls.

%add_python_extra httpx
%add_python_extra requests

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
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 10 2026 Anton Zhukharev <ancieg@altlinux.org> 0.1.9-alt1
- Packaged for ALT Sisyphus.
