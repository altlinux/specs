Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.2.3
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
Name:          shrinkwrap
Version:       1.2.3
Release:       alt1_4jpp8
Summary:       A simple mechanism to assemble Java archives
# Some file are without license headers
# reported @ https://issues.jboss.org/browse/SHRINKWRAP-501
License:       ASL 2.0
Url:           http://arquillian.org/modules/shrinkwrap-shrinkwrap/
Source0:       https://github.com/shrinkwrap/shrinkwrap/archive/%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(jdepend:jdepend)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
Shrinkwrap provides a simple mechanism to assemble archives
like JARs, WARs, and EARs with a friendly, fluent API.

%package api-nio2
Group: Development/Java
Summary:       ShrinkWrap NIO.2 API

%description api-nio2
ShrinkWrap NIO.2 API.

%package bom
Group: Development/Java
Summary:       ShrinkWrap Bill of Materials

%description bom
Centralized dependencyManagement for the ShrinkWrap Project.

%package build-resources
Group: Development/Java
Summary:       Shrinkwrap Build Resources

%description build-resources
Shrinkwrap Build Resources.

%package depchain
Group: Development/Java
Summary:       ShrinkWrap Dependency Chain

%description depchain
Single-POM Definition to export the
ShrinkWrap artifacts in proper scope.

%package depchain-java7
Group: Development/Java
Summary:       ShrinkWrap Dependency Chain for Java7 Environments

%description depchain-java7
Single-POM Definition to export the
ShrinkWrap artifacts in proper scope
for Java 7 Environments.

%package impl-base
Group: Development/Java
Summary:       ShrinkWrap Implementation Base
# Public Domain:
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/InvalidHeaderException.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarArchive.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarBuffer.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarEntry.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarGzOutputStream.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarHeader.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarInputStream.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarOutputStream.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarOutputStreamImpl.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarProgressDisplay.java
# ./impl-base/src/main/java/org/jboss/shrinkwrap/impl/base/io/tar/TarTransFileTyper.java
License:       ASL 2.0 and Public Domain

%description impl-base
Common Base for Implementations of the ShrinkWrap Project.

%package impl-nio2
Group: Development/Java
Summary:       ShrinkWrap NIO.2 Implementation

%description impl-nio2
ShrinkWrap NIO.2 Implementation.

%package parent
Group: Development/Java
Summary:       ShrinkWrap Aggregator and Build Parent

%description parent
ShrinkWrap Aggregator POM.

%package spi
Group: Development/Java
Summary:       ShrinkWrap SPI

%description spi
Generic Service Provider Contract of the ShrinkWrap Project.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_disable_module dist

# remove env.JAVA"x"_HOME
%pom_xpath_remove "pom:requireProperty"
# Option UseSplitVerifier support was removed in 8.0
# <argLine>-XX:-UseSplitVerifier</argLine>
%pom_xpath_remove "pom:configuration/pom:argLine" 
%pom_xpath_remove "pom:configuration/pom:jvm" api
%pom_xpath_remove "pom:configuration/pom:jvm" impl-base
%pom_xpath_remove "pom:profiles" impl-base 

%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r org.eclipse.m2e:lifecycle-mapping

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' LICENSE
touch -r LICENSE.orig LICENSE
rm LICENSE.orig

%mvn_package :%{name}-api::tests: %{name}-api
%mvn_package :%{name}-impl-base::tests: %{name}-impl-base

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}-api
%doc LICENSE

%files api-nio2 -f .mfiles-%{name}-api-nio2
%files impl-base -f .mfiles-%{name}-impl-base
%files impl-nio2 -f .mfiles-%{name}-impl-nio2
%files spi -f .mfiles-%{name}-spi

%files bom -f .mfiles-%{name}-bom
%doc LICENSE

%files build-resources -f .mfiles-%{name}-build-resources
%doc LICENSE

%files depchain -f .mfiles-%{name}-depchain
%doc LICENSE

%files depchain-java7 -f .mfiles-%{name}-depchain-java7
%doc LICENSE

%files parent -f .mfiles-%{name}-parent
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_7jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

