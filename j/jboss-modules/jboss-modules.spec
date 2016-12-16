Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-modules
%define version 1.5.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-modules
Version:          1.5.2
Release:          alt1_1jpp8
Summary:          A Modular Classloading System
# XPP3 License: src/main/java/org/jboss/modules/xml/MXParser.java
#  src/main/java/org/jboss/modules/xml/XmlPullParser.java
#  src/main/java/org/jboss/modules/xml/XmlPullParserException.java
License:          ASL 2.0 and xpp
URL:              https://github.com/jbossas/jboss-modules
Source0:          https://github.com/jbossas/jboss-modules/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
%if 0%{?fedora}
BuildRequires: graphviz libgraphviz
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
%endif
Source44: import.info

%description
Ths package contains A Modular Classloading System.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Conditionally remove dependency on apiviz
if [ %{?rhel} ]; then
    %pom_remove_plugin :maven-javadoc-plugin
fi

# Unneeded task
%pom_remove_plugin :maven-source-plugin

# Use not available org.wildfly.checkstyle:wildfly-checkstyle-config:1.0.4.Final
%pom_remove_plugin :maven-checkstyle-plugin

# Tries to connect to remote host
rm src/test/java/org/jboss/modules/MavenResourceTest.java \
 src/test/java/org/jboss/modules/maven/MavenSettingsTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt XPP3-LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt XPP3-LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_0.1.Beta3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp7
- new version

