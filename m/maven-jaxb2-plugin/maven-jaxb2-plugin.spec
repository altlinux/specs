Epoch: 0
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          maven-jaxb2-plugin
Version:       0.8.1
Release:       alt3_11jpp7
Summary:       Provides the capability to generate java sources from schemas
License:       BSD and ASL 2.0
URL:           http://java.net/projects/maven-jaxb2-plugin/pages/Home
# svn export https://svn.java.net/svn/maven-jaxb2-plugin~svn/tags/0.8.1/ maven-jaxb2-plugin-0.8.1
# tar -zcvf maven-jaxb2-plugin-0.8.1.tar.gz maven-jaxb2-plugin-0.8.1
Source0:       %{name}-%{version}.tar.gz
# Don't try to use an internal bundled resolver, as this is not available in
# Fedora:
Patch0:        %{name}-dont-use-internal-resolver.patch
# Adapt for Maven 3:
Patch1:        %{name}-adapt-for-maven-3.patch
# Remove the enconding option as the version of the XJC compiler that we build
# in Fedora doesn't have it:
Patch2:        %{name}-remove-enconding-option.patch

BuildArch:     noarch
BuildRequires: maven-local
BuildRequires: xml-commons-resolver
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-anno-plugin
BuildRequires: glassfish-jaxb
BuildRequires: codemodel
Source44: import.info

%description
This Maven 2 plugin wraps the JAXB 2.x XJC compiler and provides the capability
to generate Java sources from XML Schemas.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
The API documentation of %{name}.

%prep
%setup -q
%patch0 -p1
# Build only version 2.2
%pom_disable_module plugin-2.0
%pom_disable_module plugin-2.1
%pom_disable_module plugin
%pom_disable_module testing
%patch1 -p1
# Add dependency on codemodel:
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin-2.2
%patch2 -p1

%build

%mvn_file :maven-jaxb22-plugin %{name}
%mvn_file :%{name}-core %{name}-core
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt3_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt3_9jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt3_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt1_7jpp7
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.6.1-alt1_1jpp5
- new version

