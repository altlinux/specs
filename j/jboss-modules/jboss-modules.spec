Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-modules
%define version 1.3.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-modules
Version:          1.3.3
Release:          alt1_3jpp8
Summary:          A Modular Classloading System
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-modules
Source0:          https://github.com/jbossas/jboss-modules/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
%if 0%{?fedora}
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
# Missing apiviz dep ...
BuildRequires: graphviz libgraphviz
BuildRequires:    mvn(jdepend:jdepend)
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
%setup -q -n jboss-modules-%{namedversion}

%pom_remove_plugin "org.jboss.seven2six:seven2six"

# Conditionally remove dependency on apiviz
if [ %{?rhel} ]; then
    %pom_remove_plugin :maven-javadoc-plugin
fi

# Tries to connect to remote host
rm src/test/java/org/jboss/modules/MavenResourceTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
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

