Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.0
%global namedreltag -alpha-9
%global namedversion %{version}%{?namedreltag}

Name:          shrinkwrap-descriptors
Version:       2.0.0
Release:       alt3_0.19.alpha9jpp8
Summary:       ShrinkWrap sub-project for creating Archive Descriptors
# Some file are without license headers
# reported @ https://github.com/shrinkwrap/descriptors/issues/106
License:       ASL 2.0
Url:           http://arquillian.org/modules/descriptors-shrinkwrap/
Source0:       https://github.com/shrinkwrap/descriptors/archive/%{namedversion}.tar.gz

# Related to SHRINKDESC-137
Patch0:        shrinkwrap-descriptors-2.0.0-alpha-8-saxon9.4.patch

BuildArch:     noarch

BuildRequires: graphviz libgraphviz
BuildRequires: maven-local
BuildRequires: mvn(com.sun.codemodel:codemodel)
BuildRequires: mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires: mvn(com.thoughtworks.qdox:qdox)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(jdepend:jdepend)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.saxon:saxon)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-testutil)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
#BuildRequires: mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(xmlunit:xmlunit)
Source44: import.info

%description
ShrinkWrap sub-project for creating Archive Descriptors

This package contains the ShrinkWrap Descriptors API Base.
API Base for Client View of the ShrinkWrap Descriptors Project.

%package ant
Group: Development/Java
Summary:       ShrinkWrap Descriptors Ant Extension

%description ant
Extension module for ShrinkWrap Descriptors Ant Tasks.

%package api-javaee
Group: Development/Java
Summary:       ShrinkWrap Descriptors Generated Java EE API

%description api-javaee
Client View of the ShrinkWrap Descriptors Project.

%package api-javaee-prototype
Group: Development/Java
Summary:       ShrinkWrap Descriptors Prototype Java EE API

%description api-javaee-prototype
Client View of the ShrinkWrap Descriptors Project.

%package api-jboss
Group: Development/Java
Summary:      ShrinkWrap Descriptors Generated JBoss API

%description api-jboss
Client View of the JBoss related ShrinkWrap Descriptors Project.

%package api-misc
Group: Development/Java
Summary:      ShrinkWrap Descriptors Generated Misc API

%description api-misc
Client View of the ShrinkWrap Descriptors Project.

%package bom
Group: Development/Java
Summary:      ShrinkWrap Descriptors Bill of Materials

%description bom
Centralized dependency Management for the
ShrinkWrap Descriptors Project.

%package build-resources
Group: Development/Java
Summary:      Shrinkwrap Descriptors Build Resources

%description build-resources
Shrinkwrap Descriptors Build Resources.

%package depchain
Group: Development/Java
Summary:      ShrinkWrap Descriptors Dependency Chain

%description depchain
Single-POM Definition to export the ShrinkWrap Descriptors
artifacts in proper scope.

%package gen
Group: Development/Java
Summary:       ShrinkWrap Descriptors Source Generator

%description gen
Generates various deployment descriptors via XSLT transformation.

%package impl-base
Group: Development/Java
Summary:       ShrinkWrap Descriptors Implementation
# LGPLv2: ./impl-base/src/main/java/org/jboss/shrinkwrap/descriptor/impl/base/Strings.java
License:       ASL 2.0 and LGPLv2+

%description impl-base
Implementation of the ShrinkWrap Descriptors Project.

%package impl-javaee
Group: Development/Java
Summary:       ShrinkWrap Descriptors Generated Java EE Implementation

%description impl-javaee
Generated Implementation of the ShrinkWrap Descriptors Project.

%package impl-javaee-prototype
Group: Development/Java
Summary:       ShrinkWrap Descriptors Prototype Java EE Implementation

%description impl-javaee-prototype
Prototype Implementation of the ShrinkWrap Descriptors Project.

%package impl-jboss
Group: Development/Java
Summary:       ShrinkWrap Descriptors Generated JBoss Implementation

%description impl-jboss
Generated JBoss Implementation of the ShrinkWrap Descriptors Project.

%package impl-misc
Group: Development/Java
Summary:       ShrinkWrap Descriptors Generated Misc Implementation

%description impl-misc
Generated JBoss Implementation of the ShrinkWrap Descriptors Project.

%package metadata-parser
Group: Development/Java
Summary:       ShrinkWrap Descriptors Metadata Parser

%description metadata-parser
XSD and DTD parser for the ShrinkWrap Descriptors.

%package metadata-parser-test
Group: Development/Java
Summary:       ShrinkWrap Descriptors Metadata Parser Tests

%description metadata-parser-test
Hand-coded Tests for the generated descriptors via metadata plugin.

%package parent
Group: Development/Java
Summary:       ShrinkWrap Descriptors Aggregator POM

%description parent
ShrinkWrap Descriptors Aggregator POM.

%package spi
Group: Development/Java
Summary:       ShrinkWrap Descriptors SPI

%description spi
Service Provider Interface of the ShrinkWrap Descriptors Project.

%package test-util
Group: Development/Java
Summary:       ShrinkWrap Descriptors Test Utilities

%description test-util
Commonly used custom assertions.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n descriptors-%{namedversion}
%patch0 -p1
rm -r gen/doc/*

%pom_remove_plugin -r :maven-checkstyle-plugin

# saxon-dom is built in saxon in Fedora
%pom_remove_dep :saxon-dom metadata-parser
# Unavailable test dep
%pom_remove_dep -r org.easytesting:fest-assert

# Do not build test module, which is only for tests
%pom_disable_module test

# java.lang.NoClassDefFoundError: org/apache/maven/execution/MavenExecutionResult
%pom_add_dep org.apache.maven:maven-core::test metadata-parser

# Remove classpath in MANIFEST files
%pom_xpath_set -r "pom:addClasspath" false ant metadata-parser

# testConfiguration(org.jboss.shrinkwrap.descriptor.metadata.mojo.MetadataParserMojoTest)  Time elapsed: 1.212 sec  <<< ERROR!
# org.codehaus.plexus.component.repository.exception.ComponentLookupException: 
#java.util.NoSuchElementException
#      role: org.apache.maven.repository.RepositorySystem
rm metadata-parser/src/test/java/org/jboss/shrinkwrap/descriptor/metadata/mojo/MetadataParserMojoTest.java


%mvn_package :%{name}-impl-base::tests: %{name}-impl-base

%build

export JAVA5_HOME=%{_jvmdir}/java
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}-api-base
%doc LICENSE

%files ant -f .mfiles-%{name}-ant
%files api-javaee -f .mfiles-%{name}-api-javaee
%files api-javaee-prototype -f .mfiles-%{name}-api-javaee-prototype
%files api-jboss -f .mfiles-%{name}-api-jboss
%files api-misc -f .mfiles-%{name}-api-misc

%files bom -f .mfiles-%{name}-bom
%doc LICENSE

%files build-resources -f .mfiles-%{name}-build-resources
%doc LICENSE

%files depchain -f .mfiles-%{name}-depchain
%doc LICENSE

%files gen -f .mfiles-%{name}-gen
%doc gen/readme.txt
%doc LICENSE

%files impl-base -f .mfiles-%{name}-impl-base
%files impl-javaee -f .mfiles-%{name}-impl-javaee
%files impl-javaee-prototype -f .mfiles-%{name}-impl-javaee-prototype
%files impl-jboss -f .mfiles-%{name}-impl-jboss
%files impl-misc -f .mfiles-%{name}-impl-misc
%files metadata-parser -f .mfiles-%{name}-metadata-parser
%files metadata-parser-test -f .mfiles-%{name}-metadata-parser-test

%files parent -f .mfiles-%{name}-parent
%doc LICENSE

%files spi -f .mfiles-%{name}-spi

%files test-util -f .mfiles-%{name}-test-util
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.19.alpha9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.18.alpha9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.17.alpha9jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.16.alpha9jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.11.alpha2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.7.alpha2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.4.alpha2jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3_0.2.alpha2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2_0.2.alpha2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.2.alpha2jpp7
- new version

