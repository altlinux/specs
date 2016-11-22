Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-transaction-spi
%define version 7.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-transaction-spi
Version:          7.1.0
Release:          alt1_4jpp8
Summary:          JBoss Transaction SPI
License:          LGPLv2+
URL:              http://www.jboss.org
Source0:          https://github.com/jbosstm/jboss-transaction-spi/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    jboss-connector-1.7-api
BuildRequires:    jboss-logging
BuildRequires:    jboss-transaction-1.2-api
BuildRequires:    maven-local
BuildRequires:    maven-enforcer-plugin
Source44: import.info

%description
The Java Transaction SPI classes

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-transaction-spi-%{namedversion}

rm -rf .classpath
rm -rf .settings

sed -i "s|jboss-logging-spi|jboss-logging|" pom.xml
sed -i "s|>jboss-connector-api_1.5_spec<|>jboss-connector-api_1.7_spec<|" pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
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

