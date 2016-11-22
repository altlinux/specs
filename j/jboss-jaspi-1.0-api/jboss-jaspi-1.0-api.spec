Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaspi-1.0-api
%define version 1.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaspi-1.0-api
Version:          1.0.1
Release:          alt2_11jpp8
Summary:          JBoss Java Authentication SPI for Containers 1.0 API
Group:            Development/Other
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-jaspi-api_spec.git
# cd jboss-jaspi-api_spec/ && git archive --format=tar --prefix=jboss-jaspi-1.0-api/ jboss-jaspi-api_1.0_spec-1.0.1.Final | xz > jboss-jaspi-1.0-api-1.0.1.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    jboss-logging
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-local

BuildArch:        noarch
Source44: import.info

%description
The Java Authentication SPI for Containers 1.0 API classes

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaspi-1.0-api

# Fixing JDK7 ASCII issues
files='
src/main/java/javax/security/auth/message/callback/PasswordValidationCallback.java
src/main/java/javax/security/auth/message/config/AuthConfigFactory.java
src/main/java/javax/security/auth/message/config/AuthConfigProvider.java
src/main/java/javax/security/auth/message/config/ClientAuthConfig.java
src/main/java/javax/security/auth/message/config/ServerAuthConfig.java
src/main/java/javax/security/auth/message/module/ClientAuthModule.java
src/main/java/javax/security/auth/message/module/ServerAuthModule.java
'

for f in ${files}; do
  native2ascii -encoding UTF8 ${f} ${f}
done

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE README

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_10jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_3jpp7
- new version

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt4_2jpp6
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt3_2jpp6
- build w/o jms-1.1-api

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt2_2jpp6
- built with patched assembly plugin

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.1-alt1_2jpp6
- new version

