# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:             opensaml-java-parent
Version:          4
Release:          alt1_10jpp8
Summary:          OpenSAML Java Parent
Group:            Development/Other
License:          ASL 2.0
URL:              http://www.jboss.org/jbossws
Source0:          https://build.shibboleth.net/nexus/content/groups/public/net/shibboleth/parent/%{version}/parent-%{version}.pom
Source1:          LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-dependency-plugin

%if 0%{?fedora} >= 21
BuildRequires:    jcl-over-slf4j
BuildRequires:    jul-to-slf4j
BuildRequires:    log4j-over-slf4j
%else
BuildRequires:    slf4j
%endif
Source44: import.info

%description
This package contains the OpenSAML Java Parent

%prep
cp %{SOURCE0} pom.xml
cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4-alt1_10jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 4-alt1_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4-alt1_3jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 4-alt1_1jpp7
- fc update

