Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 22
Name:          maven-jaxb2-plugin
Version:       0.12.3
Release:       alt1_2jpp8
Summary:       Provides the capability to generate java sources from schemas
License:       BSD and ASL 2.0
URL:           http://java.net/projects/maven-jaxb2-plugin/pages/Home
Source0:       https://github.com/highsource/maven-jaxb2-plugin/archive/%{version}.tar.gz
# Don't try to use an internal bundled resolver, as this is not available in
# Fedora:
Patch0:        %{name}-0.12.3-dont-use-internal-resolver.patch
# Adapt for Maven 3:
Patch1:        %{name}-0.12.3-adapt-for-maven-3.patch
# Remove the enconding option as the version of the XJC compiler that we build
# in Fedora doesn't have it:
Patch2:        %{name}-0.12.3-remove-enconding-option.patch

BuildArch:     noarch
BuildRequires: maven-local
BuildRequires: xml-commons-resolver
BuildRequires: maven-enforcer-plugin
BuildRequires: junit
BuildRequires: glassfish-jaxb
BuildRequires: codemodel
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.slf4j:slf4j-api)
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
%patch1 -p1
%patch2 -p1

# Build only version 2.2
%pom_disable_module plugin-2.0
%pom_disable_module plugin
%pom_disable_module testing


# Add dependency on codemodel:
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin-2.2

sed -i "s|MavenProjectBuilder.ROLE|org.apache.maven.project.MavenProjectHelper.ROLE|" \
 plugin-2.1/src/test/java/org/jvnet/mjiip/v_2_1/JAXBGenerateTest.java

%if %{?fedora} <= 21
# use glassfish-jaxb >= 2.2.7
%pom_disable_module plugin-2.2
%mvn_file :maven-jaxb21-plugin %{name}
%else
# use glassfish-jaxb >= 2.1.14
%pom_disable_module plugin-2.1
%mvn_file :maven-jaxb22-plugin %{name}
%endif

%mvn_file :%{name}-core %{name}-core

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.12.3-alt1_2jpp8
- new version

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

