%define _unpackaged_files_terminate_build 1

Name: jackson-dataformat-xml
Version: 2.20.1
Release: alt1

Summary: Jackson XML dataformat module
License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-dataformat-xml
Vcs: https://github.com/FasterXML/jackson-dataformat-xml.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: moditect-maven-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: jackson-core
BuildRequires: jackson-annotations
BuildRequires: jackson-databind
BuildRequires: stax2-api
BuildRequires: woodstox-core

%description
Data format extension for Jackson to serialize Java objects as XML and
deserialize XML as Java objects.

%prep
%setup

%pom_remove_parent

%pom_remove_plugin -r org.jacoco:jacoco-maven-plugin
%pom_remove_plugin -r org.cyclonedx:cyclonedx-maven-plugin
%pom_remove_plugin -r org.gradlex:gradle-module-metadata-maven-plugin
%pom_remove_plugin -r com.google.code.maven-replacer-plugin:replacer
%pom_xpath_remove -r -f "//pom:repositories"

%pom_change_dep com.fasterxml.jackson.core:jackson-core com.fasterxml.jackson.core:jackson-core:2.20.1
%pom_change_dep com.fasterxml.jackson.core:jackson-annotations com.fasterxml.jackson.core:jackson-annotations:2.19.4
%pom_change_dep com.fasterxml.jackson.core:jackson-databind com.fasterxml.jackson.core:jackson-databind:2.20.1
%pom_change_dep org.codehaus.woodstox:stax2-api org.codehaus.woodstox:stax2-api:4.2.1
%pom_change_dep com.fasterxml.woodstox:woodstox-core com.fasterxml.woodstox:woodstox-core:6.2.3

sed -e 's/@package@/com.fasterxml.jackson.dataformat.xml/g' \
    -e 's/@projectversion@/%{version}/g' \
    -e 's/@projectgroupid@/com.fasterxml.jackson.dataformat/g' \
    -e 's/@projectartifactid@/jackson-dataformat-xml/g' \
    src/main/java/com/fasterxml/jackson/dataformat/xml/PackageVersion.java.in \
    > src/main/java/com/fasterxml/jackson/dataformat/xml/PackageVersion.java

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Mon Apr 13 2026 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt1
- First build for ALT.
