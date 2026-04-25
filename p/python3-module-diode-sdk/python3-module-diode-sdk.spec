%define pypi_name diode-sdk
%define mod_name diode
%define upstream_name netboxlabs

%def_with check

Name:    python3-module-%pypi_name
Version: 1.11.0
Release: alt1

Summary: Diode SDK Python
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/netboxlabs/diode-sdk-python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-protobuf
BuildRequires: python3-module-grpcio
BuildRequires: python3-module-certifi
BuildRequires: python3-module-requests
BuildRequires: python3-module-sentry-sdk
BuildRequires: python3-module-opentelemetry-proto
BuildRequires: python3-module-grpcio-status
%endif

%add_python3_req_skip opentelemetry.proto.collector.logs.v1
%add_python3_req_skip opentelemetry.proto.logs.v1
Requires: python3-module-opentelemetry-proto

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Diode SDK Python is a Python library for interacting with the Diode ingestion
service utilizing gRPC.

%prep
%setup -n %pypi_name-%version
sed -i 's/^version = "0.0.1"/version = "1.11.0"/' pyproject.toml
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/diode-replay-dryrun
%python3_sitelibdir/%upstream_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %upstream_name-%pypi_name}

%changelog
* Tue Apr 21 2026 Alexander Burmatov <thatman@altlinux.org> 1.11.0-alt1
- Initial build for Sisyphus.
