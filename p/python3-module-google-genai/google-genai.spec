%define _unpackaged_files_terminate_build 1
%define pypi_name google-genai
%define module_name google/genai

%def_with check

Name: python3-module-google-genai
Version: 2.29.0
Release: alt1

Summary: GenAI Python SDK
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/google-genai/
VCS: https://github.com/googleapis/python-genai

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# pillow is only a conditional (local-tokenizer extra) runtime dependency
# upstream, but the scoped tests import PIL unconditionally.
BuildRequires: python3-module-pillow
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The Google Gen AI Python SDK provides an interface for developers
to build applications using Google's Gemini models and Vertex AI
services.

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
# The remaining suites replay recorded API sessions kept outside the
# release tarball (or record them against the live API), so only the
# offline transformer and type tests can run in hasher.
%pyproject_run_pytest %module_name/tests/transformers %module_name/tests/types

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.29.0-alt1
- Initial build for ALT Sisyphus.
