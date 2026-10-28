%define _unpackaged_files_terminate_build 1
%define pypi_name pydantic-handlebars
%define module_name pydantic_handlebars

%def_with check

Name: python3-module-pydantic-handlebars
Version: 0.2.1
Release: alt1

Summary: Handlebars template engine for composing LLM prompts, built on Pydantic
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/pydantic-handlebars/
VCS: https://github.com/pydantic/pydantic-handlebars

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-pytest-examples
BuildRequires: python3-module-hypothesis
%pyproject_builddeps_metadata
%pyproject_builddeps_check
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
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.2.1-alt1
- Initial build for ALT Sisyphus.
