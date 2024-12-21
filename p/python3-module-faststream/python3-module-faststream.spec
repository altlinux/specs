%define _unpackaged_files_terminate_build 1

%def_with check
%global pypi_name faststream

Name: python3-module-%pypi_name
Version: 0.5.33
Release: alt1

Summary: Effortless event stream integration for your services
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch

VCS: https://github.com/airtai/FastStream
Url: https://faststream.airt.ai/latest/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-fast-depends
BuildRequires: python3-module-typer
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-pydantic-settings
BuildRequires: python3-module-opentelemetry-sdk
BuildRequires: python3-module-dirty-equals
BuildRequires: python3-module-prometheus_client
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-watchfiles
BuildRequires: python3-module-yaml
BuildRequires: python3-module-httpx

BuildRequires: python3-module-aio-pika
BuildRequires: python3-module-kafka
BuildRequires: python3-module-confluent-kafka
BuildRequires: python3-module-aiokafka
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-nats-py
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
%pyproject_run -- pytest tests -m "(slow and (not nats and not kafka and not confluent and not rabbit and not redis)) or (not nats and not kafka and not confluent and not rabbit and not redis)"

%files
%doc LICENSE README.md
%_bindir/faststream
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir_noarch/%{pep427_name %pypi_name}

%changelog
* Sat Dec 21 2024 Egor Ignatov <egori@altlinux.org> 0.5.33-alt1
- New version 0.5.33.

* Thu Dec 05 2024 Egor Ignatov <egori@altlinux.org> 0.5.32-alt1
- New version 0.5.32.

* Thu Nov 28 2024 Egor Ignatov <egori@altlinux.org> 0.5.30-alt1
- First build for ALT.
