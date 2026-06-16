%global _unpackaged_files_terminate_build 1
%define pypi_name litellm

# needs fsspec>=2023.5.0
%def_without check

%def_without proxy-extras

Name: litellm
Version: 1.89.0
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
Source2: litellm.service
Source3: litellm.config.yaml
Source4: litellm.sysconfig

%add_pyproject_deps_runtime_filter azure-storage-blob
%add_pyproject_deps_runtime_filter litellm-enterprise
%add_pyproject_deps_runtime_filter litellm-proxy-extras
%add_pyproject_deps_runtime_filter mangum
%add_pyproject_deps_runtime_filter polars
%add_pyproject_deps_runtime_filter pyroscope-io
%add_pyproject_deps_runtime_filter semantic-router
%add_pyproject_deps_runtime_filter granian
%pyproject_runtimedeps_metadata_extra proxy

BuildRequires(pre): rpm-build-pyproject
BuildRequires: rpm-macros-systemd
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter fastapi-offline
%add_pyproject_deps_check_filter langfuse
%add_pyproject_deps_check_filter opentelemetry-exporter-otlp
%add_pyproject_deps_check_filter pytest-postgresql
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-huggingface-hub
%endif

%description
CLI and proxy service utilities for running LiteLLM as a centralized
AI Gateway for a team or organization.

%package -n python3-module-%{pypi_name}
Summary: Python SDK for unified integration with LLM providers
Group: Development/Python3
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
%pyproject_runtimedeps_metadata_extra caching

%description -n python3-module-%{pypi_name}
LiteLLM Python SDK provides a single interface for 100+ LLM providers
(OpenAI, Anthropic, Gemini, Bedrock, Azure, etc.) via OpenAI format.
Use it for direct library integration in Python applications.

%if_with proxy-extras
%package proxy-extras
Summary: Additional files for the LiteLLM Proxy
Group: Development/Python3
AutoReq: yes, nopython3

%add_pyproject_deps_runtime_filter a2a-sdk
%add_pyproject_deps_runtime_filter google-cloud-iam
%add_pyproject_deps_runtime_filter google-cloud-kms
#%%add_pyproject_deps_runtime_filter prisma
%add_pyproject_deps_runtime_filter redisvl
%add_pyproject_deps_runtime_filter resend
%pyproject_runtimedeps_metadata_extra extra-proxy

%description proxy-extras
Additional files for the proxy. Reduces the size of the main litellm package.
Currently, only stores the migration.sql files for litellm-proxy
%endif

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%if_with proxy-extras
pushd litellm-proxy-extras
%pyproject_build
popd
%endif

%install
%pyproject_install

%if_with proxy-extras
pushd litellm-proxy-extras
%pyproject_install
popd
%endif

# Exclude enterprise sources from OSS package payload.
rm -rf %{buildroot}%{python3_sitelibdir}/enterprise

install -Dpm644 %SOURCE2 %buildroot%_unitdir/litellm.service
install -Dpm644 %SOURCE3 %buildroot%_sysconfdir/litellm/config.yaml
install -Dpm600 %SOURCE4 %buildroot%_sysconfdir/sysconfig/litellm

%post
%post_service litellm

%preun
%preun_service litellm

%check
%tox_check_pyproject

%files
%doc README.md LICENSE ARCHITECTURE.md security.md
%_bindir/litellm
%_bindir/litellm-proxy
%_unitdir/litellm.service
%dir %_sysconfdir/litellm
%config(noreplace) %_sysconfdir/litellm/config.yaml
%config(noreplace) %attr(600,root,root) %_sysconfdir/sysconfig/litellm

%files -n python3-module-%{pypi_name}
%python3_sitelibdir/litellm
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%if_with proxy-extras
%files proxy-extras
%python3_sitelibdir/litellm_proxy_extras
%python3_sitelibdir/litellm_proxy_extras-*.dist-info
%endif

%changelog
* Mon Jun 15 2026 Egor Ignatov <egori@altlinux.org> 1.89.0-alt1
- New version 1.89.0.

* Wed Jun 10 2026 Egor Ignatov <egori@altlinux.org> 1.88.1-alt1
- New version 1.88.1.
- Add litellm.service systemd unit with default config (closes: #59001).

* Fri May 08 2026 Egor Ignatov <egori@altlinux.org> 1.81.13-alt2
- Fix build and runtime dependencies (closes: #59002)

* Thu Apr 02 2026 Matvey Pyanov <sen@altlinux.org> 1.81.13-alt1
- Initial build for ALT Linux.
