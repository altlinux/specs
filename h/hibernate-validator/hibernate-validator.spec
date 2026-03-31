%define _unpackaged_files_terminate_build 1

Name: hibernate-validator
Version: 9.1.0
Release: alt1

Summary: Jakarta Validation reference implementation
License: Apache-2.0
Group: Development/Java
Url: https://hibernate.org/validator
Vcs: https://github.com/hibernate/hibernate-validator.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-resources-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-failsafe-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: sisu-mojos
BuildRequires: jacoco-maven-plugin
BuildRequires: moditect-maven-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: jakarta-validation-api
BuildRequires: jboss-logging
BuildRequires: jboss-logging-tools
BuildRequires: java-classmate
BuildRequires: jakarta-el-api
BuildRequires: jakarta-persistence
BuildRequires: joda-time
BuildRequires: money-api
BuildRequires: paranamer

%description
Hibernate Validator is the reference implementation of Jakarta Validation.

%package annotation-processor
Summary: Hibernate Validator annotation processor
Group: Development/Java

%description annotation-processor
Annotation processor for detecting incorrect usage of Jakarta Validation
constraints at compile time.

%package bom
Summary: Hibernate Validator BOM
Group: Development/Java

%description bom
Bill of materials POM for Hibernate Validator artifacts.

%package parent
Summary: Hibernate Validator parent POM
Group: Development/Java

%description parent
Parent POM for Hibernate Validator modules.

%package public-parent
Summary: Hibernate Validator public parent POM
Group: Development/Java

%description public-parent
Public parent POM for Hibernate Validator modules.

%prep
%setup
%autopatch -p1

rm -f .mvn/extensions.xml .mvn/develocity.xml

%pom_disable_module parents/internal
%pom_disable_module build/build-config
%pom_disable_module build/enforcer
%pom_disable_module build/reports
%pom_disable_module test-utils
%pom_disable_module tck-runner
%pom_disable_module cdi
%pom_disable_module performance
%pom_disable_module integrationtest/wildfly
%pom_disable_module integrationtest/java/modules/simple
%pom_disable_module integrationtest/java/modules/no-el
%pom_disable_module integrationtest/java/modules/test-utils
%pom_disable_module integrationtest/java/modules/cdi

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-surefire-report-plugin
%pom_remove_plugin -r :maven-wrapper-plugin
%pom_remove_plugin -r org.codehaus.mojo:flatten-maven-plugin
%pom_remove_plugin -r org.codehaus.mojo:versions-maven-plugin
%pom_remove_plugin -r org.sonarsource.scanner.maven:sonar-maven-plugin
%pom_remove_plugin -r org.jboss.maven.plugins:maven-injection-plugin
%pom_remove_plugin -r com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r de.thetaphi:forbiddenapis
%pom_remove_plugin -r com.github.siom79.japicmp:japicmp-maven-plugin
%pom_remove_plugin -r com.buschmais.jqassistant:jqassistant-maven-plugin

%pom_remove_dep org.openjfx:javafx-base engine
%pom_remove_dep :hibernate-validator-test-utils annotation-processor

%pom_add_plugin :maven-compiler-plugin engine \
  '<configuration><excludes>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/ListPropertyValueExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/MapPropertyKeyExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/MapPropertyValueExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/ObservableValueValueExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/ReadOnlyListPropertyValueExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/ReadOnlyMapPropertyKeyExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/ReadOnlyMapPropertyValueExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/ReadOnlySetPropertyValueExtractor.java</exclude>\
    <exclude>org/hibernate/validator/internal/engine/valueextraction/SetPropertyValueExtractor.java</exclude>\
  </excludes></configuration>'

%build
%mvn_build -s -f -j -- -DdisableDocumentationBuild=true \
  -DdisableDistributionBuild=true \
  -Denforcer.skip=true \
  -Dmdep.skip=true \
  #

%install
%mvn_install

%files -f .mfiles-hibernate-validator
%doc license.txt
%doc README.md AUTHORS.txt

%files annotation-processor -f .mfiles-hibernate-validator-annotation-processor
%files bom -f .mfiles-hibernate-validator-bom
%files parent -f .mfiles-hibernate-validator-parent
%files public-parent -f .mfiles-hibernate-validator-public-parent

%changelog
* Wed Mar 25 2026 Ivan Khanas <xeno@altlinux.org> 9.1.0-alt1
- Initial build for ALT Linux.
