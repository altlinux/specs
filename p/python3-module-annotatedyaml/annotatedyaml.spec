Name: python3-module-annotatedyaml
Version: 1.0.2
Release: alt1

Summary: Annotated YAML that supports secrets
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/annotatedyaml/
VCS: https://github.com/home-assistant-libs/annotatedyaml

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o=addopts= tests

# extensions built against stable API, drop versioned ABI req
%filter_from_requires /%python3_ABI_dep/d

%files
%python3_sitelibdir/annotatedyaml
%python3_sitelibdir/annotatedyaml-%version.dist-info

%changelog
* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released
