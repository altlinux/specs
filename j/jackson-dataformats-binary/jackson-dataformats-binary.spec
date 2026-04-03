%define _unpackaged_files_terminate_build 1
%def_without extra_dataformats

Name: jackson-dataformats-binary
Version: 2.20.1
Release: alt2
Summary: Jackson standard binary data format backends

License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-dataformats-binary
Vcs: https://github.com/FasterXML/jackson-dataformats-binary.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Fix-HashMap-incompareble-types-cast-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: maven-local
BuildRequires: jackson-annotations
BuildRequires: jackson-core
BuildRequires: jackson-databind
BuildRequires: jackson-bom
BuildRequires: replacer
BuildRequires: junit
BuildRequires: maven-plugin-bundle
BuildRequires: jacoco-maven-plugin
BuildRequires: apiguardian
BuildRequires: moditect-maven-plugin
%if %{with extra_dataformats}
BuildRequires: logback-classic
BuildRequires: protoparser
BuildRequires: assertj-core
BuildRequires: avro
%endif


%description
Parent pom for Jackson binary dataformats.

%if %{with extra_dataformats}
%package -n jackson-dataformat-avro
Group: Development/Java
Summary: Support for reading and writing AVRO-encoded data via Jackson abstractions

%description -n jackson-dataformat-avro
Jackson extension component for reading and writing data encoded using Apache
Avro data format. Project adds necessary abstractions on top to make things
work with other Jackson functionality. It relies on standard Avro library for
Avro Schema handling, and some parts of deserialization/serialization.

%package -n jackson-dataformat-protobuf
Group: Development/Java
Summary: Support for reading and writing protobuf-encoded data via Jackson abstractions

%description -n jackson-dataformat-protobuf
Jackson extension component for reading and writing Protobuf encoded data
(see protobuf encoding spec). This project adds necessary abstractions on top
to make things work with other Jackson functionality; mostly just low-level
Streaming components (JsonFactory, JsonParser, JsonGenerator).
%endif

%package -n jackson-dataformat-cbor
Group: Development/Java
Summary: Support for reading and writing Concise Binary Object Representation

%description -n jackson-dataformat-cbor
Jackson data format module that supports reading and writing CBOR ("Concise
Binary Object Representation") encoded data. Module extends standard Jackson
streaming API (JsonFactory, JsonParser, JsonGenerator), and as such works
seamlessly with all the higher level data abstractions (data binding, tree
model, and pluggable extensions).

%package -n jackson-dataformat-smile
Group: Development/Java
Summary: Support for reading and writing Smile encoded data using Jackson abstractions

%description -n jackson-dataformat-smile
This Jackson extension handles reading and writing of data encoded in Smile
data format ("binary JSON"). It extends standard Jackson streaming API
(JsonFactory, JsonParser, JsonGenerator), and as such works seamlessly with
all the higher level data abstractions (data binding, tree model, and
pluggable extensions).

%prep
%setup
%autopatch -p1

%if %{without extra_dataformats}
%pom_disable_module avro
%pom_disable_module protobuf
%endif

%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :cyclonedx-maven-plugin

%pom_disable_module ion

%pom_add_dep -r org.apiguardian:apiguardian-api:test

%build
%mvn_build -s -j -- -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=9 \
  #

%install
%mvn_install

%files -f .mfiles-jackson-dataformats-binary
%doc README.md release-notes/*
%doc --no-dereference LICENSE

%if %{with extra_dataformats}
%files -n jackson-dataformat-avro -f .mfiles-jackson-dataformat-avro
%doc avro/README.md avro/release-notes/*
%doc --no-dereference LICENSE

%files -n jackson-dataformat-protobuf -f .mfiles-jackson-dataformat-protobuf
%doc protobuf/README.md protobuf/release-notes/*
%doc --no-dereference LICENSE
%endif

%files -n jackson-dataformat-cbor -f .mfiles-jackson-dataformat-cbor
%doc cbor/README.md cbor/release-notes/*
%doc --no-dereference LICENSE

%files -n jackson-dataformat-smile -f .mfiles-jackson-dataformat-smile
%doc smile/README.md smile/release-notes/*
%doc --no-dereference LICENSE

%changelog
* Thu Apr 02 2026 Anton Meleshnikov <alton@altlinux.org> 2.20.1-alt2
- FTBFS fix.

* Mon Nov 10 2025 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt1
- New version.

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 2.9.8-alt1_9jpp11
- java11 build

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_3jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_4jpp8
- fc29 update

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- new version

