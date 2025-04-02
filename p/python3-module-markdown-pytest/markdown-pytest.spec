%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name markdown-pytest
%define module_name markdown_pytest

Name: python3-module-%pypi_name
Version: 0.3.2
Release: alt1

Summary: A simple module to test your documentation examples with pytest
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/markdown-pytest/
Vcs: https://github.com/mosquito/markdown-pytest

BuildArch: noarch

Source0: %name-%version.tar
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
The markdown-pytest plugin is a pytest plugin that allows you to run tests
directly from Markdown files.
With this plugin, you can write your tests inside Markdown files, making it
easy to read, understand and maintain your documentation samples. The tests
are executed just like any other Pytest tests.

%prep
%setup
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
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%module_name.py
%python3_sitelibdir/__pycache__/%module_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.2-alt1
- Initial build for ALT Sisyphus.

