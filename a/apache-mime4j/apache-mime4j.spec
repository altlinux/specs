%define _unpackaged_files_terminate_build 1

Name: apache-mime4j
Version: 0.8.15
Release: alt1

Summary: Streaming MIME parser and message object model for Java
License: Apache-2.0
Group: Development/Java
URL: https://james.apache.org/mime4j/
VCS: https://github.com/apache/james-mime4j.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: apache-parent
BuildRequires: maven-plugin-bundle
BuildRequires: javacc-maven-plugin
BuildRequires: apache-commons-io
BuildRequires: apache-commons-logging
BuildRequires: guava
BuildRequires: junit
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:slf4j-api)

%description
Apache James Mime4j parses MIME and RFC 822 messages, provides a message
object model, streaming codecs, storage backends and an mbox iterator.

%package core
Summary: Streaming MIME parser and codecs
Group: Development/Java

%description core
Streaming MIME parser and codecs for Apache James Mime4j.

%package dom
Summary: MIME message object model
Group: Development/Java

%description dom
MIME message object model for Apache James Mime4j.

%package storage
Summary: MIME storage backends
Group: Development/Java

%description storage
MIME storage backends for Apache James Mime4j.

%package mbox-iterator
Summary: Mbox message iterator
Group: Development/Java

%description mbox-iterator
Mbox message iterator for Apache James Mime4j.

%package james-utils
Summary: MIME utility library
Group: Development/Java

%description james-utils
MIME utility library for Apache James Mime4j.

%package examples
Summary: MIME usage examples
Group: Development/Java

%description examples
MIME usage examples for Apache James Mime4j.

%prep
%setup
# Benchmarks and distribution assembly are not production libraries.
%pom_disable_module benchmark
%pom_disable_module assemble
%pom_remove_plugin org.apache.rat:apache-rat-plugin
# Keep reactor test fixtures available to dependent module tests.
%mvn_package ":*:jar:tests" __noinstall

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-%name-project
%doc LICENSE NOTICE

%files core -f .mfiles-%name-core
%files dom -f .mfiles-%name-dom
%files storage -f .mfiles-%name-storage
%files mbox-iterator -f .mfiles-%name-mbox-iterator
%files james-utils -f .mfiles-%name-james-utils
%files examples -f .mfiles-%name-examples

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 0.8.15-alt1
- Initial build for ALT.
