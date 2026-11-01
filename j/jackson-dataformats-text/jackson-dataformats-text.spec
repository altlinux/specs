%define _unpackaged_files_terminate_build 1

Name: jackson-dataformats-text
Version: 2.22.4
Release: alt1

Summary: Jackson standard text-format data format backends
License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-dataformats-text
VCS: https://github.com/FasterXML/jackson-dataformats-text
BuildArch: noarch

Source: %name-%version.tar
Patch0: jflex17-skeleton.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: jflex
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.yaml:snakeyaml)

%description
Parent pom for Jackson text-format dataformats.

%package -n     jackson-dataformat-csv
Group: Development/Java
Summary: Support for reading and writing CSV-encoded data via Jackson abstractions

%description -n jackson-dataformat-csv
Jackson data format module for reading and writing CSV encoded data, either
as "raw" data (sequence of String arrays), or via data binding to/from Java
Objects (POJOs).

%package -n     jackson-dataformat-properties
Group: Development/Java
Summary: Support for reading and writing content of "Java Properties" files

%description -n jackson-dataformat-properties
Jackson data format module that supports reading and writing Java Properties
files, using naming convention to determine implied structure (by default
assuming dotted notation, but configurable from non-nested to other
separators).

%package -n     jackson-dataformat-yaml
Group: Development/Java
Summary: Support for reading and writing YAML-encoded data via Jackson abstractions

%description -n jackson-dataformat-yaml
Jackson extension component for reading and writing YAML encoded data.
SnakeYAML library is used for low-level YAML parsing. This project adds
necessary abstractions on top to make things work with other Jackson
functionality.

%package -n     jackson-dataformat-toml
Group: Development/Java
Summary: Support for reading and writing TOML data with Jackson

%description -n jackson-dataformat-toml
Jackson data format module for parsing and generating TOML documents,
including data binding to and from Java objects.

%javadoc_package

%prep
%setup

case "$(jflex --version)" in
    *"JFlex 1.7."*)
%patch0 -p1
        ;;
esac

%pom_remove_plugin :jflex-maven-plugin toml
%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :cyclonedx-maven-plugin

%mvn_file ":{*}" jackson-dataformats/@1

%build
jflex --skel toml/src/main/jflex/skeleton-toml \
    -d toml/src/main/java \
    toml/src/main/jflex/com/fasterxml/jackson/dataformat/toml/toml.jflex
# Allow recursive TOML tests to reach the nesting limit on i586.
%mvn_build -s -- -DargLine=-Xss2m

%install
%mvn_install

%files -f .mfiles-jackson-dataformats-text
%doc README.md release-notes/*
%doc LICENSE

%files -n jackson-dataformat-csv -f .mfiles-jackson-dataformat-csv
%doc csv/README.md csv/release-notes/*
%doc LICENSE

%files -n jackson-dataformat-properties -f .mfiles-jackson-dataformat-properties
%doc properties/README.md properties/release-notes/*
%doc LICENSE

%files -n jackson-dataformat-yaml -f .mfiles-jackson-dataformat-yaml
%doc yaml/README.md yaml/release-notes/*
%doc LICENSE

%files -n jackson-dataformat-toml -f .mfiles-jackson-dataformat-toml
%doc toml/README.md LICENSE

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 2.22.4-alt1
- New version.
- Build TOML support with the system JFlex generator.

* Tue Aug 11 2026 Evgeniy Serov <scala@altlinux.org> 2.22.1-alt1
- Automatically updated to 2.22.1.

* Fri Apr 03 2026 Anton Meleshnikov <alton@altlinux.org> 2.20.1-alt2
- fixed FTBFS.

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

