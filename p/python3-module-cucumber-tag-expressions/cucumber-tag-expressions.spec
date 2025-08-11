%define _unpackaged_files_terminate_build 1
%define pypi_name cucumber-tag-expressions
%define mod_name cucumber_tag_expressions

%def_with check

Name: python3-module-%pypi_name
Version: 6.2.0
Release: alt1
Summary: A tag-expression parser and evaluation logic for cucumber/behave
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cucumber-tag-expressions
Vcs: https://github.com/cucumber/tag-expressions
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
Cucumber tag-expressions provide readable boolean expressions to select features
and scenarios marked with tags in Gherkin files in an easy way.

%prep
%setup
# to make tests data available
%setup -D -T -b1
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile py.requirements/testing.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 08 2025 Stanislav Levin <slev@altlinux.org> 6.2.0-alt1
- Initial build for Sisyphus.
