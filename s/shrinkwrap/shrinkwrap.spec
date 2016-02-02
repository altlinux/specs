Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name shrinkwrap
%define version 1.1.2
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
Name:          shrinkwrap
Version:       1.1.2
Release:       alt1_7jpp8
Summary:       A simple mechanism to assemble Java archives
License:       ASL 2.0
Url:           http://www.jboss.org/shrinkwrap/
Source0:       https://github.com/shrinkwrap/shrinkwrap/archive/%{namedversion}.tar.gz
# remove env.JAVA"x"_HOME
# malformed pom file, not able to use pom macros
Patch0:        %{name}-%{namedversion}-remove-enforcer-requireProperty.patch

BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
#BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-source-plugin

# required by enforcer-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

BuildArch:     noarch
Source44: import.info

%description
Shrinkwrap provides a simple mechanism to assemble archives
like JARs, WARs, and EARs with a friendly, fluent API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p0

%pom_disable_module dist
# remove env.JAVA"x"_HOME
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:executable"
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-surefire-plugin']/pom:configuration/pom:jvm" api
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:executable" api-nio2
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:executable" impl-nio2
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-surefire-plugin']/pom:configuration/pom:jvm" impl-base
%pom_xpath_remove "pom:profiles" impl-base 

# [ERROR] Failed to execute goal org.apache.maven.plugins:maven-checkstyle-plugin:2.12:check
# (checkstyle-report) on project shrinkwrap-api: Failed during checkstyle configuration:
# cannot initialize module TreeWalker - Unable to instantiate RedundantThrows:
# Unable to instantiate RedundantThrowsCheck
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-checkstyle-plugin api
%pom_remove_plugin :maven-checkstyle-plugin api-nio2
%pom_remove_plugin :maven-checkstyle-plugin impl-base
%pom_remove_plugin :maven-checkstyle-plugin impl-nio2
%pom_remove_plugin :maven-checkstyle-plugin spi


sed -i 's/\r//' LICENSE

%mvn_file :%{name}-api %{name}/api
%mvn_file :%{name}-api-nio2 %{name}/api-nio2
%mvn_file :%{name}-build-resources %{name}/build-resources
%mvn_file :%{name}-impl-base %{name}/impl-base
%mvn_file :%{name}-impl-nio2 %{name}/impl-nio2
%mvn_file :%{name}-spi %{name}/spi

%mvn_package :%{name}-api::tests:
%mvn_package :%{name}-impl-base::tests:

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_7jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

