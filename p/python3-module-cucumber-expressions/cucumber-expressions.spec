%define _unpackaged_files_terminate_build 1
%define pypi_name cucumber-expressions
%define mod_name cucumber_expressions

%def_with check

Name: python3-module-%pypi_name
Version: 18.0.1
Release: alt1
Summary: A simpler alternative to Regular Expressions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cucumber-expressions
Vcs: https://github.com/cucumber/cucumber-expressions
BuildArch: noarch
Source: %name-%version.tar
Source1: testdata.tar
Source2: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Cucumber Expressions is an alternative to Regular Expressions with a more
intuitive syntax.

%prep
%setup
# to make tests data available (see python/tests/definitions.py)
%setup -D -T -b1
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 18.0.1-alt1
- Initial build for Sisyphus.
