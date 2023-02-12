%define  modulename confluent-kafka

# needs pyflakes.test, but it can be removed but also
# ImportError: cannot import name 'builder' from 'google.protobuf.internal'
# in 2 tests
%def_without check

Name:    python3-module-%modulename
Version: 2.0.2
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
BuildRequires: python3-module-pyflakes
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

# Remove license file installed in weird place
rm -f  %buildroot/%_prefix/LICENSE.txt

%check
%tox_check_pyproject

%files
%doc *.md LICENSE.txt
%python3_sitelibdir/confluent_kafka
%python3_sitelibdir/%{pyproject_distinfo confluent_kafka}

%changelog
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
