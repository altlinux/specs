%define _unpackaged_files_terminate_build 1
%define pypi_name dirty-equals
%define mod_name dirty_equals

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1

Summary: Doing dirty (but extremely useful) things with equals
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dirty-equals/
Vcs: https://github.com/samuelcolvin/dirty-equals

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: dirty-equals-0.7.0-upstream-fix-pydantic-version-checking.patch
Patch1: dirty-equals-0.7.0-alt-fix-IsUrl-for-pydanticV2.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-module-pydantic
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

dirty-equals is a python library that (mis)uses the __eq__ method to make
python code (generally unit tests) more declarative and therefore easier
to read and write.

dirty-equals can be used in whatever context you like, but it comes into
its own when writing unit tests for applications where you're commonly
checking the response to API calls and the contents of a database.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
touch pytest.ini
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 13 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.7.0-alt1
- 0.4 -> 0.7.0

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 0.4-alt2
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Tue Jul 26 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4-alt1
- initial build for Sisyphus

