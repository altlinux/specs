%define _unpackaged_files_terminate_build 1
%define pypi_name openai
%define pypi_nname openai
%define mod_name openai

# too many unpackaged and dubious dependencies
%def_without check

Name: python3-module-%pypi_nname
Version: 1.65.2
Release: alt1

Summary: The official Python library for the OpenAI API
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/openai/
Vcs: https://github.com/openai/openai-python

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The OpenAI Python library provides convenient access to the
OpenAI REST API from any Python 3.8+ application. The library includes
type definitions for all request params and response fields, and
offers both synchronous and asynchronous clients powered by httpx.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.lock
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc CHANGELOG.md README.md
%_bindir/openai
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 1.65.2-alt1
- Built for ALT Sisyphus.

