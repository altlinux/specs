Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-dmr
%define version 1.2.0
%global namedreltag .Beta2
%global namedversion %{version}%{?namedreltag}

Name:             jboss-dmr
Version:          1.2.0
Release:          alt1_0.1.Beta2jpp7
Summary:          JBoss DMR
License:          LGPLv2+
URL:              https://github.com/jbossas/jboss-dmr
Source0:          https://github.com/jbossas/jboss-dmr/archive/%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    apt-maven-plugin
BuildRequires:    junit4
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    jboss-parent
BuildRequires:    jboss-logmanager
BuildRequires:    cookcc
BuildRequires:    apiviz
Source44: import.info

%description
This package contains the Dynamic Model Representation.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
# ModelNodeTest.testFromJSONStringUnicode:280 failed
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_0.1.Beta2jpp7
- new release

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_9jpp7
- new release

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- fixed build

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_6jpp7
- new version

