%define pypi_name opentelemetry

%def_with check
%def_with tests

Name:    python3-module-%pypi_name
Version: 1.41.0
Release: alt1

Summary: OpenTelemetry Python API and SDK

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/opentelemetry-sdk
VCS:     https://github.com/open-telemetry/opentelemetry-python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-deprecated
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-flaky
BuildRequires: python3-module-googleapis-common-protos
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-protobuf
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-requests
BuildRequires: python3-module-responses
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-jsonschema
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
%py3_provides %pypi_name.propagators

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
%py3_provides %pypi_name.semconv._incubating.attributes

%description -n python3-module-%pypi_name-semantic-conventions
This library contains generated code for the semantic conventions defined by
the OpenTelemetry specification.

%package -n python3-module-%pypi_name-exporter-otlp-proto-common
Summary: OpenTelemetry Python Protobuf Encoding
Group: Development/Python3

%description -n python3-module-%pypi_name-exporter-otlp-proto-common
This library is provided as a convenience to encode to Protobuf.
Currently used by:

* opentelemetry-exporter-otlp-proto-grpc
* opentelemetry-exporter-otlp-proto-http

%package -n python3-module-%pypi_name-exporter-otlp-proto-grpc
Summary: OpenTelemetry Python Collector Protobuf over gRPC Explorer
Group: Development/Python3

%description -n python3-module-%pypi_name-exporter-otlp-proto-grpc
This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over gRPC.

%package -n python3-module-%pypi_name-exporter-otlp-proto-http
Summary: OpenTelemetry Python Collector Protobuf over HTTP Explorer
Group: Development/Python3

%description -n python3-module-%pypi_name-exporter-otlp-proto-http
This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over HTTP.

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
# Root project pkg sources
for dir in ./%pypi_name-{api,proto,sdk,semantic-conventions}; do
    pushd $dir
        %pyproject_build
    popd
done

# Exporters pkg sources
for edir in ./exporter/%pypi_name-exporter-otlp-proto-{common,grpc,http}; do
    pushd $edir
        %pyproject_build
    popd
done

%if_with tests
pushd tests/%pypi_name-test-utils
    %pyproject_build
popd
%endif

%install
# Root project pkg sources
for dir in ./%pypi_name-{api,proto,sdk,semantic-conventions}; do
    pushd $dir
        %pyproject_install
    popd
done

# Exporters pkg sources
for edir in ./exporter/%pypi_name-exporter-otlp-proto-{common,grpc,http}; do
    pushd $edir
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

# Turn off a couple of broken tests
# TODO: check out next release
pushd ./exporter/%pypi_name-exporter-otlp-proto-grpc
        %pyproject_run_pytest --ignore=benchmarks/test_benchmark_trace_exporter.py
popd

for edir in ./exporter/%pypi_name-exporter-otlp-proto-{common,http}; do
    pushd $edir
        %pyproject_run_pytest
    popd
done

%files -n python3-module-%pypi_name-api
%doc %pypi_name-api/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/_events/
%python3_sitelibdir/%pypi_name/_logs/
%python3_sitelibdir/%pypi_name/attributes/
%python3_sitelibdir/%pypi_name/baggage/
%python3_sitelibdir/%pypi_name/context/
%python3_sitelibdir/%pypi_name/metrics
%python3_sitelibdir/%pypi_name/propagate/
%python3_sitelibdir/%pypi_name/propagators/
%python3_sitelibdir/%pypi_name/trace/
%python3_sitelibdir/%pypi_name/util/
%python3_sitelibdir/%pypi_name/environment_variables/
%python3_sitelibdir/%pypi_name/version/
%python3_sitelibdir/%pypi_name/py.typed
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

%files -n python3-module-%pypi_name-exporter-otlp-proto-common
%doc exporter/%pypi_name-exporter-otlp-proto-common/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/exporter/otlp/proto/common
%python3_sitelibdir/%{pypi_name}_exporter_otlp_proto_common-%version.dist-info

%files -n python3-module-%pypi_name-exporter-otlp-proto-grpc
%doc exporter/%pypi_name-exporter-otlp-proto-grpc/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/exporter/otlp/proto/grpc
%python3_sitelibdir/%{pypi_name}_exporter_otlp_proto_grpc-%version.dist-info

%files -n python3-module-%pypi_name-exporter-otlp-proto-http
%doc exporter/%pypi_name-exporter-otlp-proto-http/{LICENSE,README.rst}
%python3_sitelibdir/%pypi_name/exporter/otlp/proto/http
%python3_sitelibdir/%{pypi_name}_exporter_otlp_proto_http-%version.dist-info

%if_with tests
%files -n python3-module-%pypi_name-test-utils
%doc tests/%pypi_name-test-utils/README.rst LICENSE
%python3_sitelibdir/%pypi_name/test
%python3_sitelibdir/%{pypi_name}_test_utils-*.dist-info
%endif

%files doc
%doc *.md LICENSE docs/examples

%changelog
* Mon Apr 13 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.41.0-alt1
- New version.

* Thu Mar 05 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.40.0-alt1
- New version.

* Tue Dec 23 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.39.1-alt1
- New version.

* Thu Dec 04 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.39.0-alt1
- New version.

* Wed Oct 22 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.38.0-alt1
- New version.

* Tue Jun 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.34.1-alt1
- New version.

* Wed May 14 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.33.0-alt1
- New version.
- Added semconv._incubating.attributes as provides.

* Fri Mar 07 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.30.0-alt1
- New version.

* Mon Sep 02 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.27.0-alt1
- New version

* Thu Aug 08 2024 Alexander Burmatov <thatman@altlinux.org> 1.26.0-alt2
- Fix provides.

* Thu Aug 01 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.26.0-alt1
- New version

* Wed Jul 24 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.24.0-alt2
- Additional subpackages exporter-otlp-{common,grpc,http}

* Tue Jul 23 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.24.0-alt1
- Initial build for Sisyphus.
