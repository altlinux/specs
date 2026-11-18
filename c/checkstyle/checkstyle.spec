%define _unpackaged_files_terminate_build 1

Name: checkstyle
Version: 14.4.0
Release: alt1

Summary: Java source code style checker
License: LGPL-2.1-or-later
Group: Development/Java
URL: https://checkstyle.org/
VCS: https://github.com/checkstyle/checkstyle.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: checkstyle-module-names.patch
Patch1: checkstyle-xvfb-tests.patch
Patch2: checkstyle-ant-xmvn.patch
Patch3: checkstyle-test-resources.patch
Patch4: checkstyle-ant-javadoc-regex.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(info.picocli:picocli)
BuildRequires: mvn(org.antlr:antlr4-runtime)
BuildRequires: mvn(org.antlr:antlr4-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.reflections:reflections)
BuildRequires: mvn(net.sf.saxon:Saxon-HE)
BuildRequires: mvn(org.checkerframework:checker-qual)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.itsallcode:junit5-system-extensions)
BuildRequires: mvn(org.junit-pioneer:junit-pioneer)
BuildRequires: mvn(com.tngtech.archunit:archunit-junit5)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(nl.jqno.equalsverifier:equalsverifier)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires: mvn(org.jacoco:org.jacoco.agent::runtime:)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(de.thetaphi:forbiddenapis)
BuildRequires: xvfb-run
BuildRequires: fonts-ttf-dejavu
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)

%description
Checkstyle is a development tool that helps programmers write Java code
that adheres to a coding standard. This package provides the Checkstyle
library and Maven metadata for use by other Java projects.

%javadoc_package

%prep
%setup
%autopatch -p1
# Run GUI tests on the real platform AWT toolkit with Xvfb instead of cacio.
%pom_xpath_remove '//pom:profile[pom:id="cacio-tta-pre-jdk25"]'
%pom_xpath_remove '//pom:profile[pom:id="cacio-tta-jdk25"]'
%pom_xpath_remove '//pom:systemPropertyVariables/pom:awt.toolkit'
%pom_xpath_remove '//pom:systemPropertyVariables/pom:java.awt.graphicsenv'
# One parser input uses the unavailable test-only FEST annotation.
# Retain its source and functional test; omit only Java fixture compilation.
%pom_xpath_inject \
    '//pom:execution[pom:id="default-testCompile"]/pom:configuration' \
    '<testExcludes><testExclude>**/InputAnnotatedDeclarationVisibilityMultipleConfigured.java</testExclude></testExcludes>'
# module-info directly uses JSR-305; Guava no longer supplies it transitively.
%pom_add_dep com.google.code.findbugs:jsr305::provided
# Metadata XML is shipped upstream; omit the unavailable documentation
# generator.
%pom_xpath_remove '//pom:execution[pom:id="run-checkstyle-files-generator"]'
%pom_xpath_remove \
    '//pom:dependency[pom:artifactId="checkstyle-files-generator"]'
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
# Omit offline publishing, analysis and documentation-site goals.
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin
%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:xml-maven-plugin
%pom_remove_plugin org.codehaus.mojo:tidy-maven-plugin
%pom_remove_plugin org.gaul:modernizer-maven-plugin
%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin org.openrewrite.maven:rewrite-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin
%pom_remove_plugin edu.illinois:nondex-maven-plugin
%pom_remove_plugin com.groupon.maven.plugin.json:json-schema-validator
%pom_remove_plugin io.fluxzero:lychee-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin
%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-eclipse-plugin
# Mockito 5 enables inline mocking in mockito-core itself.
%pom_change_dep org.mockito:mockito-inline org.mockito:mockito-core
%mvn_file : checkstyle

%build
xvfb-run -a %mvn_build -s

%install
%mvn_install

%files -f .mfiles-checkstyle
%doc LICENSE LICENSE.apache20 RIGHTS.antlr

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 14.4.0-alt1
- New version.
