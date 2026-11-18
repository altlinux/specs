%define _unpackaged_files_terminate_build 1

Name: jackson3-dataformats-text
Version: 3.3.0
Release: alt1

Summary: Jackson standard text-format data format backends
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-dataformats-text
VCS: https://github.com/FasterXML/jackson-dataformats-text.git

Source0: %name-%version.tar
Patch0: jflex17-skeleton.patch
Patch1: 0001-Use-system-AssertJ-module-name.patch
Patch2: 0002-Build-independent-TOML-tests-without-corpus-provider.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(tools.jackson:jackson-base:pom:)
BuildRequires: mvn(tools.jackson.core:jackson-core)
BuildRequires: mvn(tools.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: jflex
BuildRequires: replacer
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.snakeyaml:snakeyaml-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.assertj:assertj-core)

BuildArch: noarch

%description
Parent pom for Jackson text-format dataformats.

%package -n jackson3-dataformat-csv
Group: Development/Java
Summary: Support for reading and writing CSV-encoded data via Jackson abstractions

%description -n jackson3-dataformat-csv
Jackson data format module for reading and writing CSV encoded data, either
as "raw" data (sequence of String arrays), or via data binding to/from Java
Objects (POJOs).

%package -n jackson3-dataformat-properties
Group: Development/Java
Summary: Support for reading and writing content of "Java Properties" files

%description -n jackson3-dataformat-properties
Jackson data format module that supports reading and writing Java Properties
files, using naming convention to determine implied structure (by default
assuming dotted notation, but configurable from non-nested to other
separators).

%package -n jackson3-dataformat-yaml
Group: Development/Java
Summary: Support for reading and writing YAML-encoded data via Jackson abstractions

%description -n jackson3-dataformat-yaml
Jackson extension component for reading and writing YAML encoded data.
SnakeYAML library is used for low-level YAML parsing. This project adds
necessary abstractions on top to make things work with other Jackson
functionality.

%package -n jackson3-dataformat-toml
Group: Development/Java
Summary: Support for reading and writing TOML data with Jackson

%description -n jackson3-dataformat-toml
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
%patch1 -p1
%patch2 -p1

# Only the two TOML corpus classes require this unavailable test provider.
%pom_remove_dep at.yawk.toml.test:toml-test-for-java toml

%pom_remove_plugin :jflex-maven-plugin toml
%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :cyclonedx-maven-plugin

%mvn_file ":{*}" %name/@1

%build
jflex --skel toml/src/main/jflex/skeleton-toml \
    -d toml/src/main/java/tools/jackson/dataformat/toml \
    toml/src/main/jflex/tools/jackson/dataformat/toml/toml.jflex
%mvn_build -s

%install
%mvn_install
install -Dm644 LICENSE %buildroot%_docdir/%name-%version/LICENSE
for module in csv properties yaml toml; do
    install -Dm644 "$module/src/main/resources/META-INF/NOTICE" \
        %buildroot%_docdir/%name-%version/$module-NOTICE
done

%files -f .mfiles-jackson-dataformats-text
%doc %_docdir/%name-%version

%files -n jackson3-dataformat-csv -f .mfiles-jackson-dataformat-csv

%files -n jackson3-dataformat-properties -f .mfiles-jackson-dataformat-properties

%files -n jackson3-dataformat-yaml -f .mfiles-jackson-dataformat-yaml

%files -n jackson3-dataformat-toml -f .mfiles-jackson-dataformat-toml

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
