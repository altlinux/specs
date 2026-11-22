%define _unpackaged_files_terminate_build 1

Name: jackson-jr-objects
Version: 3.3.0
Release: alt1

Summary: Lightweight Java data binding on Jackson streaming API
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-jr
VCS: https://github.com/FasterXML/jackson-jr

Source0: jackson-jr-%version.tar
Source1: jackson-jr-generate-package-version.py

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: python3
BuildRequires: maven-local
BuildRequires: mvn(tools.jackson:jackson-base:pom:)
BuildRequires: mvn(tools.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.codehaus.gmavenplus:gmavenplus-plugin)

BuildArch: noarch

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description
Jackson-jr Objects provides lightweight Java data binding and builder-style
content generation on top of the Jackson streaming API.

%description javadoc
API documentation for %name.

%prep
%setup -q -n jackson-jr-3.3.0
mkdir -p tools
cp %SOURCE1 tools/generate-package-version.py
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.gradlex:gradle-module-metadata-maven-plugin \
    jr-objects/pom.xml
%pom_remove_plugin com.google.code.maven-replacer-plugin:replacer \
    jr-objects/pom.xml
%pom_remove_plugin com.google.code.maven-replacer-plugin:replacer \
    jr-stree/pom.xml
%pom_remove_plugin com.google.code.maven-replacer-plugin:replacer \
    jr-annotation-support/pom.xml
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin jr-objects/pom.xml
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin jr-stree/pom.xml
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin \
    jr-annotation-support/pom.xml
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin \
    jr-extension-javatime/pom.xml
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin jr-retrofit2/pom.xml
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="gmaven-plugin"]/pom:groupId' \
    org.codehaus.gmavenplus jr-objects/pom.xml
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="gmaven-plugin"]/pom:artifactId' \
    gmavenplus-plugin jr-objects/pom.xml
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="gmavenplus-plugin"]/pom:version' \
    5.1.0 jr-objects/pom.xml
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="gmavenplus-plugin"]/pom:executions/pom:execution/pom:goals/pom:goal' \
    compileTests jr-objects/pom.xml
%mvn_package tools.jackson.jr:jackson-jr-parent:pom:3.3.0 default
%mvn_package tools.jackson.jr:jackson-jr-objects default

%build
python3 tools/generate-package-version.py
%mvn_build -s -- -pl jr-objects -am

%install
%mvn_install

%files -f .mfiles-default
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
