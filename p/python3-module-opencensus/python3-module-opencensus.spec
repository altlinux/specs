%define pypi_name opencensus

%def_with check

Name:    python3-module-%pypi_name
Version: 0.11.4
Release: alt1

Summary: A stats collection and distributed tracing framework
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/census-instrumentation/opencensus-python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
BuildRequires: python3-module-google-api-core
BuildRequires: python3-module-mock
BuildRequires: python3-module-opencensus-context
BuildRequires: python3-module-django
BuildRequires: python3-module-flask
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-retrying
BuildRequires: python3-module-pyramid
BuildRequires: python3-module-azure-core
BuildRequires: python3-module-prometheus_client
%endif

Requires: python3-module-opencensus-context

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: use-correct-assertion-methods.patch

%description
OpenCensus for Python. OpenCensus provides a framework to measure a server's
resource usage and collect performance stats. This repository contains Python
related utilities and supporting software needed by OpenCensus.

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install
# add ext infrastructure
mkdir %buildroot%python3_sitelibdir/opencensus/ext/
cp %buildroot%python3_sitelibdir/opencensus/__init__* %buildroot%python3_sitelibdir/opencensus/ext
[ -e %buildroot%python3_sitelibdir/opencensus/__pycache* ] && cp -r %buildroot%python3_sitelibdir/opencensus/__pycache* %buildroot%python3_sitelibdir/opencensus/ext


%check
%pyproject_run_pytest tests/unit

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 24 2024 Alexander Burmatov <thatman@altlinux.org> 0.11.4-alt1
- Initial build for Sisyphus (thx toni@).
