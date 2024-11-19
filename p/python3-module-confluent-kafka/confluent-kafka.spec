%define  modulename confluent-kafka

%def_with check

Name:    python3-module-%modulename
Version: 2.6.1
Release: alt1

Summary: Confluent's Kafka Python Client

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/confluentinc/confluent-kafka-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: librdkafka-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-trivup
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-avro
BuildRequires: python3-module-fastavro
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-google-api-core
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-pyrsistent
BuildRequires: python3-module-pyflakes
BuildRequires: python3-module-pyflakes-tests
%endif

Source:  %name-%version.tar

%add_python3_self_prov_path %buildroot%python3_sitelibdir/confluent_kafka/kafkatest/verifiable_client.py

%description
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# test_alter_consumer_group_offsets_api causes segault
# https://github.com/confluentinc/confluent-kafka-python/issues/1797
%pyproject_run_pytest --ignore=tests/integration \
    -k 'not test_alter_consumer_group_offsets_api'

%files
%doc *.md LICENSE
%python3_sitelibdir/confluent_kafka
%python3_sitelibdir/%{pyproject_distinfo confluent_kafka}

%changelog
* Tue Nov 19 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.1-alt1
- Automatically updated to 2.6.1.
- Built with check.

* Sat Oct 12 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1
- Automatically updated to 2.6.0.

* Thu Sep 19 2024 Grigory Ustinov <grenka@altlinux.org> 2.5.3-alt1
- Automatically updated to 2.5.3.

* Thu Jul 11 2024 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Automatically updated to 2.5.0.

* Fri May 10 2024 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Automatically updated to 2.4.0.

* Mon Oct 30 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Automatically updated to 2.3.0.

* Wed Jul 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Automatically updated to 2.2.0.

* Fri May 05 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.

* Tue Apr 25 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.

* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Automatically updated to 2.0.2.

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.9.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Aug 18 2022 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt1
- Automatically updated to 1.9.2.

* Fri Jun 17 2022 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Automatically updated to 1.9.0.

* Thu May 26 2022 Grigory Ustinov <grenka@altlinux.org> 1.8.2-alt1
- Automatically updated to 1.8.2.

* Sat Jun 20 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus.
