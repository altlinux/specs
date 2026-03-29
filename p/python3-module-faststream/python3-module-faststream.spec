%define _unpackaged_files_terminate_build 1

%def_with check
%global pypi_name faststream

Name: python3-module-%pypi_name
Version: 0.6.7
Release: alt1.1

Summary: Effortless event stream integration for your services
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch

VCS: https://github.com/airtai/FastStream
Url: https://faststream.ag2.ai/latest/
Source: %name-%version.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-uv-build
BuildRequires: /proc

%if_with check
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-dirty-equals
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-httpx
BuildRequires: python3-module-msgspec
BuildRequires: python3-module-opentelemetry-sdk
BuildRequires: python3-module-prometheus-client
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pydantic-settings
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-rerunfailures
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pyyaml
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-uvloop

BuildRequires: python3-module-anyio
BuildRequires: python3-module-fast-depends
BuildRequires: python3-module-typer
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-watchfiles
BuildRequires: python3-module-confluent-kafka
BuildRequires: python3-module-aiokafka
BuildRequires: python3-module-nats-py
BuildRequires: python3-module-aio-pika
BuildRequires: python3-module-redis
%endif

%description
FastStream simplifies the process of writing producers and consumers for message
queues,  handling  all  the  parsing, networking  and  documentation  generation
automatically.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vv -m "(slow and not connected) or not connected"

%files
%doc LICENSE README.md
%_bindir/faststream
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir_noarch/%{pep427_name %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.6.7-alt1.1
- Demodernized packaging.

* Tue Mar 03 2026 Egor Ignatov <egori@altlinux.org> 0.6.7-alt1
- New version 0.6.7.

* Tue Feb 10 2026 Egor Ignatov <egori@altlinux.org> 0.6.6-alt1
- New version 0.6.6.

* Thu Nov 06 2025 Egor Ignatov <egori@altlinux.org> 0.6.3-alt1
- New version 0.6.3.

* Thu Jul 24 2025 Egor Ignatov <egori@altlinux.org> 0.5.48-alt1
- New version 0.5.48.

* Tue Jul 15 2025 Egor Ignatov <egori@altlinux.org> 0.5.47-alt1
- New version 0.5.47.

* Tue Jul 08 2025 Egor Ignatov <egori@altlinux.org> 0.5.45-alt1
- New version 0.5.45.

* Wed Jun 25 2025 Egor Ignatov <egori@altlinux.org> 0.5.43-alt1
- New version 0.5.43.

* Fri Apr 11 2025 Egor Ignatov <egori@altlinux.org> 0.5.39-alt1
- New version 0.5.39.

* Thu Mar 27 2025 Egor Ignatov <egori@altlinux.org> 0.5.37-alt1
- New version 0.5.37.

* Tue Mar 18 2025 Egor Ignatov <egori@altlinux.org> 0.5.35-alt1
- New version 0.5.35.

* Tue Jan 14 2025 Egor Ignatov <egori@altlinux.org> 0.5.34-alt1
- New version 0.5.34.

* Sat Dec 21 2024 Egor Ignatov <egori@altlinux.org> 0.5.33-alt1
- New version 0.5.33.

* Thu Dec 05 2024 Egor Ignatov <egori@altlinux.org> 0.5.32-alt1
- New version 0.5.32.

* Thu Nov 28 2024 Egor Ignatov <egori@altlinux.org> 0.5.30-alt1
- First build for ALT.
