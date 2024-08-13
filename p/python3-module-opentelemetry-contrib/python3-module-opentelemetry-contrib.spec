%define pypi_name opentelemetry-contrib
%define mod_name opentelemetry
%define prerel_version 1.26.0

%def_with check

Name:    python3-module-%pypi_name
Version: 0.47b0
Release: alt1

Summary: OpenTelemetry instrumentation for Python modules
License: Apache-2.0 and BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/open-telemetry/opentelemetry-python-contrib

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-asgiref
BuildRequires: python3-module-opentelemetry-api
BuildRequires: python3-module-opentelemetry-test-utils
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest-benchmark
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%package -n python3-module-%mod_name-instrumentation
Summary: OpenTelemetry Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation
This package provides commands that help automatically instrument a program.

%package -n python3-module-%mod_name-instrumentation-asgi
Summary: OpenTelemetry ASGI Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-asgi
This library provides a ASGI middleware that can be used on any ASGI framework
(such as Django, Starlette, FastAPI or Quart) to track requests timing through
OpenTelemetry.

%package -n python3-module-%mod_name-propagator-aws-xray
Summary: OpenTelemetry Propagator for AWS X-Ray Service
Group: Development/Python3

%description -n python3-module-%mod_name-propagator-aws-xray
This library provides the propagator necessary to inject or extract a tracing
context across AWS services.

%package -n python3-module-%mod_name-propagator-ot-trace
Summary: OpenTelemetry OT Trace Propagator
Group: Development/Python3

%description -n python3-module-%mod_name-propagator-ot-trace
OpenTelemetry OT Trace Propagator.

%package -n python3-module-%mod_name-util-http
Summary: OpenTelemetry Util HTTP
Group: Development/Python3

%description -n python3-module-%mod_name-util-http
This library provides ASGI, WSGI middleware and other HTTP-related
functionality that is common to instrumented web frameworks (such as Django,
Starlette, FastAPI, etc.) to track requests timing through OpenTelemetry.

%prep
%setup -n %pypi_name-%version

%build
pushd ./%mod_name-instrumentation
    %pyproject_build
popd

pushd ./util/%mod_name-util-http
    %pyproject_build
popd

# Instrumentations pkg sources
for idir in ./instrumentation/%mod_name-instrumentation-asgi; do
    pushd $idir
        %pyproject_build
    popd
done

# Propagators pkg sources
for pdir in ./propagator/%mod_name-propagator-{aws-xray,ot-trace}; do
    pushd $pdir
        %pyproject_build
    popd
done

%install
pushd ./%mod_name-instrumentation
    %pyproject_install
popd

pushd ./util/%mod_name-util-http
    %pyproject_install
popd

# Instrumentations pkg sources
for idir in ./instrumentation/%mod_name-instrumentation-asgi; do
    pushd $idir
        %pyproject_install
    popd
done

# Propagators pkg sources
for pdir in ./propagator/%mod_name-propagator-{aws-xray,ot-trace}; do
    pushd $pdir
        %pyproject_install
    popd
done

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ./%mod_name-instrumentation
    %pyproject_run_pytest -k "not test_run.py"
popd

pushd ./util/%mod_name-util-http
    %pyproject_run_pytest
popd

# Instrumentations pkg sources
for idir in ./instrumentation/%mod_name-instrumentation-asgi; do
    pushd $idir
        %pyproject_run_pytest
    popd
done

# Propagators pkg sources
for pdir in ./propagator/%mod_name-propagator-{aws-xray,ot-trace}; do
    pushd $pdir
        %pyproject_run_pytest
    popd
done

%files -n python3-module-%mod_name-instrumentation
%doc %mod_name-instrumentation/{LICENSE,README.rst}
%_bindir/opentelemetry-bootstrap
%_bindir/opentelemetry-instrument
%python3_sitelibdir/%mod_name/instrumentation/__pycache__
%python3_sitelibdir/%mod_name/instrumentation/auto_instrumentation
%python3_sitelibdir/%mod_name/instrumentation/_semconv.py
%python3_sitelibdir/%mod_name/instrumentation/bootstrap.py
%python3_sitelibdir/%mod_name/instrumentation/bootstrap_gen.py
%python3_sitelibdir/%mod_name/instrumentation/dependencies.py
%python3_sitelibdir/%mod_name/instrumentation/distro.py
%python3_sitelibdir/%mod_name/instrumentation/environment_variables.py
%python3_sitelibdir/%mod_name/instrumentation/instrumentor.py
%python3_sitelibdir/%mod_name/instrumentation/propagators.py
%python3_sitelibdir/%mod_name/instrumentation/py.typed
%python3_sitelibdir/%mod_name/instrumentation/sqlcommenter_utils.py
%python3_sitelibdir/%mod_name/instrumentation/utils.py
%python3_sitelibdir/%mod_name/instrumentation/version.py
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation}

%files -n python3-module-%mod_name-instrumentation-asgi
%doc instrumentation/%mod_name-instrumentation-asgi/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/asgi
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-asgi}

%files -n python3-module-%mod_name-propagator-aws-xray
%doc propagator/%mod_name-propagator-aws-xray/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/propagators/aws
%python3_sitelibdir/%{mod_name}_propagator_aws_xray-1.0.1.dist-info/

%files -n python3-module-%mod_name-propagator-ot-trace
%doc propagator/%mod_name-propagator-ot-trace/README.rst LICENSE
%python3_sitelibdir/%mod_name/propagators/ot_trace
%python3_sitelibdir/%{pyproject_distinfo %mod_name-propagator-ot-trace}

%files -n python3-module-%mod_name-util-http
%doc util/%mod_name-util-http/README.rst LICENSE
%python3_sitelibdir/%mod_name/util/http
%python3_sitelibdir/%{pyproject_distinfo %mod_name-util-http}

%changelog
* Wed Aug 07 2024 Alexander Burmatov <thatman@altlinux.org> 0.47b0-alt1
- Initial build for Sisyphus.
