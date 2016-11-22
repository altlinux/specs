Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-dmr
%define version 1.2.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-dmr
Version:          1.2.0
Release:          alt1_6jpp8
Summary:          JBoss DMR
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-dmr
Source0:          https://github.com/jbossas/jboss-dmr/archive/%{namedversion}.tar.gz
# pre-generated with JDK7:
# JAVA_HOME=/path/to/jdk7/ mvn clean generate-resources
# cp target/generated-sources/apt/org/jboss/dmr/* src/main/java/org/jboss/dmr/
# git add src/main/java/org/jboss/dmr/*.java
# git commit -m 'Add pre-generated Java classes' && git format-patch -1
Patch0:           0001-Add-pre-generated-Java-classes.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(com.google.code.cookcc:cookcc)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss.apiviz:apiviz:pom:)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(jdepend:jdepend)
Source44: import.info

%description
This package contains the Dynamic Model Representation.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1

%pom_remove_plugin :apt-maven-plugin
%pom_remove_plugin :maven-antrun-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_6jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp8
- java8 update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0.1.Beta2jpp7
- new release

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_9jpp7
- new release

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- fixed build

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp7
- new version

