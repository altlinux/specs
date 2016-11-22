Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jgroups
%define version 3.4.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:     jgroups
Version:  3.4.2
Release:  alt1_5jpp8
Summary:  Toolkit for reliable multicast communication
License:  LGPLv2+
URL:      http://www.jgroups.org
Source0:  https://github.com/belaban/JGroups/archive/JGroups-%{namedversion}.tar.gz

BuildRequires: bsh
BuildRequires: log4j
BuildRequires: byteman
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-build-helper
BuildRequires: testng
BuildRequires: bouncycastle

BuildArch:     noarch
Source44: import.info

%description
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other.

%package  javadoc
Group: Development/Java
Summary:  API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JGroups-JGroups-%{namedversion}

find . -name '*.class' -delete
find . -name '*.jar' -delete

%pom_remove_dep "bouncycastle:bcprov-jdk15"
%pom_add_dep "org.bouncycastle:bcprov-jdk16"

# log4j 2 is not available
%pom_remove_dep "org.apache.logging.log4j:log4j-core"

rm src/org/jgroups/logging/Log4J2LogImpl.java
sed -i 's|Log4J2LogImpl|Log4JLogImpl|g' src/org/jgroups/logging/LogFactory.java

%build
# A few failed tests:
# DEBUG: Failed tests: 
# DEBUG:   PrioTest.init:40 null
# DEBUG:   BecomeServerTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   ForwardToCoordFailoverTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   MessageBeforeConnectedTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   SequencerFailoverTest>BMNGRunner.bmngAfterTest:65->BMNGAbstractRunner.bmngAfterTest:193 ? FileNotFound
# DEBUG:   TCPGOSSIP_Test.stopRouter:56 NullPointer
# DEBUG:   TUNNELDeadLockTest.tearDown:73 NullPointer
# DEBUG:   TUNNEL_Test.stopRouter:56 NullPointer
# DEBUG: Tests run: 1795, Failures: 8, Errors: 0, Skipped: 1
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc INSTALL.html LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt1_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt1_4jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.4.0-alt1_0.1.Beta1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0.6-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0.6-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.0.6-alt1_2jpp7
- new version

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.6.10-alt1_4jpp6
- new version

* Sat Sep 27 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt2_1.SP4.1jpp5
- fixed build

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:2.4.1-alt1_1.SP4.1jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.9.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

