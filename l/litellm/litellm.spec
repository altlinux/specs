%global _unpackaged_files_terminate_build 1
%define pypi_name litellm

%def_with check

Name: litellm
Version: 1.81.13
Release: alt1

Summary: LiteLLM CLI and AI Gateway (Proxy Server) utilities
Group: Development/Other
License: MIT
Url: https://pypi.org/project/litellm/
VCS: https://github.com/BerriAI/litellm

BuildArch: noarch
Requires: python3-module-%{pypi_name} = %version-%release

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject

%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter fastapi-sso
%add_pyproject_deps_check_filter mangum
%add_pyproject_deps_check_filter polars
%add_pyproject_deps_check_filter semantic-router
%add_pyproject_deps_check_filter litellm
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pyyaml
%endif

%description
CLI and proxy service utilities for running LiteLLM as a centralized
AI Gateway for a team or organization.

%package -n python3-module-%{pypi_name}
Summary: Python SDK for unified integration with LLM providers
Group: Development/Python3
AutoReq: yes, nopython3
AutoProv: yes
%add_pyproject_deps_runtime_filter fastapi-sso
%add_pyproject_deps_runtime_filter mangum
%add_pyproject_deps_runtime_filter polars
%add_pyproject_deps_runtime_filter semantic-router
%pyproject_runtimedeps_metadata

%description -n python3-module-%{pypi_name}
LiteLLM Python SDK provides a single interface for 100+ LLM providers
(OpenAI, Anthropic, Gemini, Bedrock, Azure, etc.) via OpenAI format.
Use it for direct library integration in Python applications.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
# Exclude enterprise sources from OSS package payload.
rm -rf %{buildroot}%{python3_sitelibdir}/enterprise

%check
%if_with check
cd %{_builddir}/%name-%{version}
# Upstream suite has many provider/integration tests requiring network
# and external credentials. Run stable offline unit tests only.
%pyproject_run_pytest -v -l --tb=short --maxfail=1 \
    tests/test_litellm/test_uuid_helper.py \
    tests/test_litellm/test_exception_exports.py
%endif

%files
%doc README.md LICENSE ARCHITECTURE.md security.md
%_bindir/litellm
%_bindir/litellm-proxy

%files -n python3-module-%{pypi_name}
%python3_sitelibdir/litellm/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Apr 02 2026 Matvey Pyanov <sen@altlinux.org> 1.81.13-alt1
- Initial build for ALT Linux.
