%define _unpackaged_files_terminate_build 1
%define pypi_name pypitoken
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 7.0.1
Release: alt1
Summary: Manipulate PyPI API tokens
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pypitoken
Vcs: https://github.com/ewjoachim/pypitoken
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
PyPIToken is an open-source Python 3.8+ library for generating and manipulating
PyPI tokens.

PyPI tokens are very powerful, as that they are based on Macaroons. They allow
the bearer to add additional restrictions to an existing token. For example,
given a PyPI token that can upload releases for any project of its owner, you
can generate a token that will only allow some projects, or even a single one.

%prep
%setup
%autopatch -p1
# fix 0.0.0 version
sed -i 's/version = "0.0.0"/version = "%version"/' pyproject.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry tests
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -o=addopts='' -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 04 2024 Stanislav Levin <slev@altlinux.org> 7.0.1-alt1
- Initial build for Sisyphus.
