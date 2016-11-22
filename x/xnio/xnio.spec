Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name xnio
%define version 3.3.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             xnio
Version:          3.3.0
Release:          alt1_3jpp8
Summary:          JBoss XNIO
License:          ASL 2.0
URL:              http://www.jboss.org/xnio
Source0:          https://github.com/xnio/xnio/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local

BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools >= 1.1.0
BuildRequires:    jboss-logmanager
BuildRequires:    maven-injection-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    junit
BuildRequires:    maven-shared
BuildRequires:    jmock
BuildRequires:    byteman >= 2.0.4
Source44: import.info

%description
A simplified low-level I/O layer which can be used anywhere you are
using NIO today. It frees you from the hassle of dealing with Selectors and
the lack of NIO support for multicast sockets and non-socket I/O, while still
maintaining all the capabilities present in NIO.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n xnio-%{namedversion}

%pom_remove_plugin "org.jboss.bridger:bridger" api/pom.xml

%build
# JMock is too old in Fedora
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
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

