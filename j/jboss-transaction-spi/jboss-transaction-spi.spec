Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-transaction-spi
%define version 7.3.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-transaction-spi
Version:       7.3.0
Release:       alt1_1jpp8
Summary:       JBoss Transaction SPI
License:       LGPLv2+
URL:           https://github.com/jbosstm/jboss-transaction-spi
Source0:       https://github.com/jbosstm/jboss-transaction-spi/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
# https://issues.jboss.org/browse/JBTM-2698
Patch0:        https://github.com/jbosstm/jboss-transaction-spi/commit/7aa203f7fd6b182f9b7b47118af91f126e4e11fe.patch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)

BuildArch:     noarch
Source44: import.info

%description
The Java Transaction SPI classes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

# Replace jboss-connector-api_1.5_spec https://issues.jboss.org/browse/JBTM-2663
%pom_change_dep org.jboss.spec.javax.resource: :jboss-connector-api_1.7_spec

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 7.3.0-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_4jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_3jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_4jpp7
- new version

