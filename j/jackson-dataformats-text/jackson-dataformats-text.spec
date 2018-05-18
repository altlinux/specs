Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-dataformats-text
Version:       2.9.4
Release:       alt1_3jpp8
Summary:       Jackson standard text-format data format backends
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-dataformats-text
Source0:       https://github.com/FasterXML/jackson-dataformats-text/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.yaml:snakeyaml)

BuildArch:      noarch
Source44: import.info

%description
Parent pom for Jackson text-format dataformats.

%package -n jackson-dataformat-csv
Group: Development/Java
Summary: Support for reading and writing CSV-encoded data via Jackson abstractions

%description -n jackson-dataformat-csv
Jackson data format module for reading and writing CSV encoded data, either
as "raw" data (sequence of String arrays), or via data binding to/from Java
Objects (POJOs).

%package -n jackson-dataformat-properties
Group: Development/Java
Summary: Support for reading and writing content of "Java Properties" files

%description -n jackson-dataformat-properties
Jackson data format module that supports reading and writing Java Properties
files, using naming convention to determine implied structure (by default
assuming dotted notation, but configurable from non-nested to other
separators).

%package -n jackson-dataformat-yaml
Group: Development/Java
Summary: Support for reading and writing YAML-encoded data via Jackson abstractions

%description -n jackson-dataformat-yaml
Jackson extension component for reading and writing YAML encoded data.
SnakeYAML library is used for low-level YAML parsing. This project adds
necessary abstractions on top to make things work with other Jackson
functionality.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
# Obsoletes standalone jackson-dataformat-* packages since F28
Obsoletes: jackson-dataformat-csv-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-csv-javadoc = %{version}-%{release}
Obsoletes: jackson-dataformat-properties-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-properties-javadoc = %{version}-%{release}
Obsoletes: jackson-dataformat-yaml-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-yaml-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p yaml/src/main/resources/META-INF/{NOTICE,LICENSE} .
sed -i 's/\r//' LICENSE NOTICE

%mvn_file ":{*}" jackson-dataformats/@1

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-dataformats-text
%doc README.md release-notes/*
%doc --no-dereference LICENSE NOTICE

%files -n jackson-dataformat-csv -f .mfiles-jackson-dataformat-csv
%doc csv/README.md csv/release-notes/*
%doc --no-dereference LICENSE NOTICE

%files -n jackson-dataformat-properties -f .mfiles-jackson-dataformat-properties
%doc properties/README.md properties/release-notes/*
%doc --no-dereference LICENSE NOTICE

%files -n jackson-dataformat-yaml -f .mfiles-jackson-dataformat-yaml
%doc yaml/README.md yaml/release-notes/*
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- new version

