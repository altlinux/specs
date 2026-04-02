Name:           jackson-dataformats-text
Version:        2.20.1
Release:        alt1.1

Summary:        Jackson standard text-format data format backends
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/FasterXML/jackson-dataformats-text
VCS:            https://github.com/FasterXML/jackson-dataformats-text

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(org.yaml:snakeyaml)
BuildRequires:  mvn(org.jetbrains:annotations)

BuildArch:      noarch

%description
Parent pom for Jackson text-format dataformats.

%package -n jackson-dataformat-csv
Group:          Development/Java
Summary:        Support for reading and writing CSV-encoded data via Jackson abstractions

%description -n jackson-dataformat-csv
Jackson data format module for reading and writing CSV encoded data, either
as "raw" data (sequence of String arrays), or via data binding to/from Java
Objects (POJOs).

%package -n jackson-dataformat-properties
Group:          Development/Java
Summary:        Support for reading and writing content of "Java Properties" files

%description -n jackson-dataformat-properties
Jackson data format module that supports reading and writing Java Properties
files, using naming convention to determine implied structure (by default
assuming dotted notation, but configurable from non-nested to other
separators).

%package -n jackson-dataformat-yaml
Group:          Development/Java
Summary:        Support for reading and writing YAML-encoded data via Jackson abstractions

%description -n jackson-dataformat-yaml
Jackson extension component for reading and writing YAML encoded data.
SnakeYAML library is used for low-level YAML parsing. This project adds
necessary abstractions on top to make things work with other Jackson
functionality.

%javadoc_package

%prep
%setup

# TODO: needed for TOML
%pom_remove_plugin :jflex-maven-plugin toml

%pom_disable_module toml
# can help compile without jflex-maven-plugin
# jflex --skel toml/src/main/jflex/skeleton-toml -d toml/src/main/java toml/src/main/jflex/com/fasterxml/jackson/dataformat/toml/toml.jflex

%mvn_file ":{*}" jackson-dataformats/@1

%build
%mvn_build -- \
    -Dmaven.compiler.source=1.8 \
    -Dmaven.compiler.target=1.8 \
    -Dmaven.javadoc.source=1.8 \
    -Dmaven.compiler.release=8 \

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE

%files -n jackson-dataformat-csv
%doc csv/README.md csv/release-notes/*
%doc LICENSE

%files -n jackson-dataformat-properties
%doc properties/README.md properties/release-notes/*
%doc LICENSE

%files -n jackson-dataformat-yaml
%doc yaml/README.md yaml/release-notes/*
%doc LICENSE

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.20.1-alt1.1
- Cosmetic fixes.

* Sat Dec 27 2025 Evgeniy Serov <scala@altlinux.org> 2.20.1-alt1
- fixed FTBFS
- new version 2.20.1 (without toml)
- removed import.info

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

