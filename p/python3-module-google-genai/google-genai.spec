%define _unpackaged_files_terminate_build 1
%define pypi_name google-genai
%define module_name google/genai

%def_with check

Name: python3-module-google-genai
Version: 3.0.0
Release: alt1

Summary: GenAI Python SDK
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/google-genai/
VCS: https://github.com/googleapis/python-genai

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

# Sisyphus has no python3-module-google-auth+requests subpackage yet, so
# google-auth[requests] is required as the plain google-auth; requests is
# a direct dependency anyway.
%pyproject_configure_with_runtime_filter 'google-auth$'
Requires: python3-module-google-auth

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
# Upstream has no test dependency source: requirements.txt is a pinned
# development lock, not a list of the test requirements.
%pyproject_configure_without_autodiscovery
%pyproject_configure_with_check_filter 'google-auth$'
BuildRequires: python3-module-google-auth
BuildRequires: python3-module-pytest-timeout
# pillow is only a conditional (local-tokenizer extra) runtime dependency
# upstream, but the scoped tests import PIL unconditionally.
BuildRequires: python3-module-pillow
%endif
%pyproject_configure_pypi_package

%description
The Google Gen AI Python SDK provides an interface for developers
to build applications using Google's Gemini models and Vertex AI
services.

%pyproject_configure_pypi_subpackage aiohttp
%pyproject_configure_pypi_subpackage httpx
%pyproject_configure_pypi_subpackage httpx2
%pyproject_configure_pypi_subpackage local-tokenizer
%pyproject_configure_pypi_subpackage pyopenssl

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
# The remaining suites replay recorded API sessions kept outside the
# release tarball (or record them against the live API), so only the
# offline transformer and type tests can run in hasher.
%pyproject_run_pytest --session-timeout=600 %module_name/tests/transformers %module_name/tests/types

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0.

* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.29.0-alt1
- Initial build for ALT Sisyphus.
