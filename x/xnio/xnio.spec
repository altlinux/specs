Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.4.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             xnio
Version:          3.4.0
Release:          alt1_4jpp8
Summary:          JBoss XNIO
# LGPLv2+ ./api/src/main/java/org/xnio/ObjectProperties.java
License:          ASL 2.0 and LGPLv2+
URL:              http://www.jboss.org/xnio
Source0:          https://github.com/xnio/xnio/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(java_cup:java_cup)
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
BuildRequires:    mvn(org.jboss.byteman:byteman)
BuildRequires:    mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires:    mvn(org.jboss.byteman:byteman-install)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires:    mvn(org.jmock:jmock)
BuildRequires:    mvn(org.jmock:jmock-junit4)
BuildRequires:    mvn(org.wildfly.common:wildfly-common)
Source44: import.info

%description
A simplified low-level I/O layer which can be used anywhere you are
using NIO today. It frees you from the hassle of dealing with Selectors and
the lack of NIO support for multicast sockets and non-socket I/O, while still
maintaining all the capabilities present in NIO.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin "org.jboss.bridger:bridger" api
%pom_remove_plugin -r :maven-source-plugin

#  @ random fails in koji (arm) builder
rm nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioSslTcpConnectionTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/NioSslTcpChannelTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/NioSslTcpConnectionTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/NioStartTLSTcpChannelTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/NioStartTLSTcpConnectionTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioSslTcpChannelTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioStartTLSTcpConnectionTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioStartTLSTcpChannelTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/NioTcpConnectionTestCase.java \
 nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioTcpConnectionTestCase.java
 
%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_2jpp8
- java 8 mass update

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt3_6jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_3jpp7
- new version

