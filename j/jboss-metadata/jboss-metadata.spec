Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-metadata
%define version 8.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           jboss-metadata
Version:        8.0.0
Release:        alt1_5jpp8
Summary:        JBoss Metadata
License:        LGPLv2+
URL:            https://github.com/jboss/metadata
Source0:        https://github.com/jboss/metadata/archive/%{namedversion}.tar.gz

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
#BuildRequires:  mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.ejb3:jboss-ejb3-ext-api)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.jms:jboss-jms-api_2.0_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
Source44: import.info

%description
This package contains JBoss Metadata for WildFly.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n metadata-%{namedversion}

# Fix the line ending in the license file:
dos2unix common/LICENSE.txt

# maven-checkstyle-plugin:2.12:checkstyle (check-style) on project jboss-metadata-common:
# An error has occurred in Checkstyle report generation. Failed during checkstyle configuration:
# cannot initialize module TreeWalker - Unable to instantiate RedundantThrows:
# Unable to instantiate RedundantThrowsCheck -> [Help 1]
%pom_remove_plugin :maven-checkstyle-plugin

%build
# Skip tests - no test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README
%doc common/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc common/LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:8.0.0-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:8.0.0-alt1_4jpp8
- java8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:7.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:7.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:7.0.1-alt1_3jpp7
- new version

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_0jpp6
- fixed build with java 7

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_0jpp6
- new version

