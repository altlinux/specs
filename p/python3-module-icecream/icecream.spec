%define _unpackaged_files_terminate_build 1
%define pypi_name icecream
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 2.1.3
Release: alt1
Summary: Never use print() to debug again
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/icecream
Vcs: https://github.com/gruns/icecream
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Never use print() to debug again; inspect variables, expressions, and program
execution with a single, simple function call.

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
# upstream still sits on dead nose

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 26 2023 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus.
