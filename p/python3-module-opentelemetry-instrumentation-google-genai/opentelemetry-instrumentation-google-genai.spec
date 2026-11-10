%define _unpackaged_files_terminate_build 1
%define pypi_name opentelemetry-instrumentation-google-genai
%define module_name opentelemetry/instrumentation/google_genai
%define version_beta b0

# Upstream versions the wheel X.YbN; the spec keeps the beta in Release.
%define pyproject_distinfo() %{pep427_name: %1}-%version%{version_beta}.dist-info

%def_with check

Name: python3-module-%pypi_name
Version: 1.3
Release: alt2.%version_beta

Summary: OpenTelemetry Google GenAI instrumentation
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/opentelemetry-instrumentation-google-genai/
Vcs: https://github.com/open-telemetry/opentelemetry-python-genai
BuildArch: noarch

Source0: %name-%version.tar
# Upstream pytest plugin for the GenAI suites (not on PyPI), tests only.
Source1: test-util-genai-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
%pyproject_configure_without_autodiscovery
%pyproject_configure_with_check_deps pip_reqfile tests/requirements.latest.txt
# The tox test_deps and pytest_deps plus the deps of the test-util
# plugin; tox.ini lives in the monorepo root, outside this tarball.
BuildRequires: python3-module-fsspec
BuildRequires: python3-module-opentelemetry-sdk
BuildRequires: python3-module-opentelemetry-test-utils
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-vcr
BuildRequires: python3-module-yaml
BuildRequires: python3-module-pytest-timeout
%endif
%pyproject_configure_pypi_package

%description
This library adds instrumentation to the Google GenAI SDK library to emit
telemetry data following the Semantic Conventions for GenAI systems: trace
spans for GenAI operations, events/logs for prompts and responses and
metrics describing the GenAI operations in aggregate.

%pyproject_configure_pypi_subpackage instruments

%prep
%setup -a1
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH="$PWD/test-util-genai/src"
# Replay the recorded cassettes only: hasher has no network, and the
# fixtures switch to fake credentials just in that mode.
# test_conformance.py drives the external OpenTelemetry Weaver binary.
%pyproject_run_pytest -ra --vcr-record=none tests \
	--session-timeout=600 \
	--ignore tests/test_conformance.py

%files
%doc README.rst LICENSE
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.3-alt2.b0
- Split opentelemetry-instrumentation-google-genai out into a separate
  source package.

* Fri Nov 06 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.3-alt1.b0
- Updated to 1.3.

* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.2-alt1.b0
- Initial build for ALT Sisyphus.
