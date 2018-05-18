Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Allow conditionally building extra data format modules
# that require additional external dependencies
%bcond_with extra_dataformats
# Extra formats are disabled for now because deps in
# Fedora are not uptodate enough

Name:          jackson-dataformats-binary
Version:       2.9.4
Release:       alt1_3jpp8
Summary:       Jackson standard binary data format backends
# One file is BSD licensed: protobuf/src/main/resources/descriptor.proto
License:       ASL 2.0 and BSD
URL:           https://github.com/FasterXML/jackson-dataformats-binary
Source0:       https://github.com/FasterXML/jackson-dataformats-binary/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%if %{with extra_dataformats}
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.squareup:protoparser)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.apache.avro:avro)
%endif

BuildArch:      noarch
Source44: import.info

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

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
# Obsoletes standalone jackson-dataformat-* packages since F28
Obsoletes: jackson-dataformat-cbor-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-cbor-javadoc = %{version}-%{release}
Obsoletes: jackson-dataformat-smile-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-smile-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p ion/LICENSE .
cp -p ion/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%if %{without extra_dataformats}
%pom_disable_module avro
%pom_disable_module protobuf
%endif

# Test dep lombok is not in Fedora
%pom_remove_dep org.projectlombok:lombok avro

# Deps are not available in Fedora for this module
%pom_disable_module ion

%mvn_file ":{*}" jackson-dataformats/@1

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-dataformats-binary
%doc README.md release-notes/*
%doc --no-dereference LICENSE NOTICE

%if %{with extra_dataformats}
%files -n jackson-dataformat-avro -f .mfiles-jackson-dataformat-avro
%doc avro/README.md avro/release-notes/*
%doc --no-dereference LICENSE NOTICE

%files -n jackson-dataformat-protobuf -f .mfiles-jackson-dataformat-protobuf
%doc protobuf/README.md protobuf/release-notes/*
%doc --no-dereference LICENSE NOTICE
%endif

%files -n jackson-dataformat-cbor -f .mfiles-jackson-dataformat-cbor
%doc cbor/README.md cbor/release-notes/*
%doc --no-dereference LICENSE NOTICE

%files -n jackson-dataformat-smile -f .mfiles-jackson-dataformat-smile
%doc smile/README.md smile/release-notes/*
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- new version

