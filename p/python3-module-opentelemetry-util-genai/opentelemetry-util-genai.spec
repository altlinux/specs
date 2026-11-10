%define _unpackaged_files_terminate_build 1
%define pypi_name opentelemetry-util-genai
%define module_name opentelemetry/util/genai/
%define version_beta b0

# Upstream versions the wheel X.YbN; the spec keeps the beta in Release.
%define pyproject_distinfo() %{pep427_name: %1}-%version%{version_beta}.dist-info

%def_with check

Name: python3-module-%pypi_name
Version: 1.3
Release: alt2.%version_beta

Summary: OpenTelemetry GenAI utilities
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/opentelemetry-util-genai/
Vcs: https://github.com/open-telemetry/opentelemetry-python-genai
BuildArch: noarch

Source0: %name-%version.tar
Source1: scripts.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
%pyproject_configure_with_check_deps pip_reqfile test-requirements.txt
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-opentelemetry-sdk
BuildRequires: python3-module-opentelemetry-test-utils
BuildRequires: python3-module-pytest-timeout
%endif
%pyproject_configure_pypi_package

%description
The GenAI Utils package provides boilerplate and helpers to standardize
instrumentation for Generative AI: a telemetry handler for invocation
lifecycles, a structured data model for GenAI interactions, completion
hooks for uploading content to external storage and the GenAI metrics.

%prep
%setup -a1
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH="$PWD/scripts"
%pyproject_run_pytest -ra --session-timeout=600 tests

%files
%doc README.rst LICENSE
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.3-alt2.b0
- Split opentelemetry-util-genai out into a separate source package.

* Fri Nov 06 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.3-alt1.b0
- Updated to 1.3.

* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.2-alt1.b0
- Initial build for ALT Sisyphus.
