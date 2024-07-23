%define pypi_name opentelemetry

%def_with check
%def_with tests

Name:    python3-module-%pypi_name
Version: 1.24.0
Release: alt1

Summary: OpenTelemetry Python API and SDK

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/opentelemetry-sdk
VCS:     https://github.com/open-telemetry/opentelemetry-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-deprecated
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-flaky
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-pytest
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-pytest-benchmark
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%package -n python3-module-%pypi_name-api
Summary: OpenTelemetry Python API
Group: Development/Python3
# PyPI name(dash, underscore)
%py3_provides %pypi_name
%py3_provides %pypi_name.util

%description -n python3-module-%pypi_name-api
OpenTelemetry Python API for the OpenTelemetry Project.

%package -n python3-module-%pypi_name-proto
Summary: OpenTelemetry Python Proto
Group: Development/Python3

%description -n python3-module-%pypi_name-proto
OpenTelemetry Python Proto for the OpenTelemetry Project.

%package -n python3-module-%pypi_name-sdk
Summary: OpenTelemetry Python SDK
Group: Development/Python3
Requires: python3-module-%pypi_name-api = %EVR
Requires: python3-module-%pypi_name-semantic-conventions = %EVR
%py3_provides %pypi_name.sdk

%description -n python3-module-%pypi_name-sdk
OpenTelemetry Python SDK for the OpenTelemetry Project.

%package -n python3-module-%pypi_name-semantic-conventions
Summary: OpenTelemetry Python Semantic Conventions
Group: Development/Python3

%description -n python3-module-%pypi_name-semantic-conventions
This library contains generated code for the semantic conventions defined by
the OpenTelemetry specification.

%if_with tests
%package -n python3-module-%pypi_name-test-utils
Summary: OpenTelemetry Python Test Utilities
Group: Development/Python3
Requires: python3-module-%pypi_name-api = %EVR
Requires: python3-module-%pypi_name-sdk = %EVR

%description -n python3-module-%pypi_name-test-utils
This package provides internal testing utilities for the OpenTelemetry Python
project and provides no stability or quality guarantees.
%endif

%package doc
Summary: Documentation and examples for python-opentelemetry
Group: Development/Python3

%description doc
This package provides documentation and examples for python-opentelemetry.

%prep
%setup

%build
for dir in ./%pypi_name-{api,proto,sdk,semantic-conventions}; do
    pushd $dir
        %pyproject_build
    popd
done
%if_with tests
pushd tests/%pypi_name-test-utils
    %pyproject_build
popd
%endif

%install
for dir in ./%pypi_name-{api,proto,sdk,semantic-conventions}; do
    pushd $dir
        %pyproject_install
    popd
done
%if_with tests
pushd tests/%pypi_name-test-utils
    %pyproject_install
popd
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
for dir in ./%pypi_name-{api,proto,sdk,semantic-conventions}; do
    pushd $dir
        %pyproject_run_pytest
    popd
done

%files -n python3-module-%pypi_name-api
%doc %pypi_name-api/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/_logs/
%python3_sitelibdir/%pypi_name/__pycache__/
%python3_sitelibdir/%pypi_name/attributes/
%python3_sitelibdir/%pypi_name/baggage/
%python3_sitelibdir/%pypi_name/context/
%python3_sitelibdir/%pypi_name/metrics
%python3_sitelibdir/%pypi_name/propagate/
%python3_sitelibdir/%pypi_name/propagators/
%python3_sitelibdir/%pypi_name/trace/
%python3_sitelibdir/%pypi_name/util/
%python3_sitelibdir/%pypi_name/environment_variables.py
%python3_sitelibdir/%pypi_name/py.typed
%python3_sitelibdir/%pypi_name/version.py
%python3_sitelibdir/%{pypi_name}_api-%version.dist-info

%files -n python3-module-%pypi_name-proto
%doc %pypi_name-proto/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/proto
%python3_sitelibdir/%{pypi_name}_proto-%version.dist-info

%files -n python3-module-%pypi_name-sdk
%doc %pypi_name-sdk/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/sdk
%python3_sitelibdir/%{pypi_name}_sdk-%version.dist-info

%files -n python3-module-%pypi_name-semantic-conventions
%doc %pypi_name-sdk/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/semconv
%python3_sitelibdir/%{pypi_name}_semantic_conventions-*.dist-info

%if_with tests
%files -n python3-module-%pypi_name-test-utils
%doc tests/%pypi_name-test-utils/README.rst LICENSE
%python3_sitelibdir/%pypi_name/test
%python3_sitelibdir/%{pypi_name}_test_utils-*.dist-info
%endif

%files doc
%doc *.md LICENSE docs/examples

%changelog
* Tue Jul 23 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.24.0-alt1
- Initial build for Sisyphus.
