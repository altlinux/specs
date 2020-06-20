%define  modulename confluent-kafka

Name:    python3-module-%modulename
Version: 1.4.2
Release: alt1

Summary: Confluent's Kafka Python Client

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/confluentinc/confluent-kafka-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: librdkafka-devel

Source:  %modulename-%version.tar

%description
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

# Remove license file installed in weird place
rm -f  %buildroot/%_prefix/LICENSE.txt

%files
%python3_sitelibdir/confluent_kafka
%python3_sitelibdir/*.egg-info

%changelog
* Sat Jun 20 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus.
