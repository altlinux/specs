Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          maven-jaxb2-plugin
Version:       0.13.0
Release:       alt1_2jpp8
Summary:       Provides the capability to generate java sources from schemas
License:       BSD and ASL 2.0
URL:           http://java.net/projects/maven-jaxb2-plugin/pages/Home
Source0:       https://github.com/highsource/maven-jaxb2-plugin/archive/%{version}.tar.gz
# Don't try to use an internal bundled resolver, as this is not available in
# Fedora:
Patch0:        %{name}-0.13.0-dont-use-internal-resolver.patch
# Adapt for Maven 3:
Patch1:        %{name}-0.13.0-adapt-for-maven-3.patch
# Remove the enconding option as the version of the XJC compiler that we build
# in Fedora doesn't have it:
Patch2:        %{name}-0.13.0-remove-enconding-option.patch

BuildArch:     noarch
BuildRequires: java-headless
BuildRequires: maven-local
BuildRequires: mvn(com.sun.codemodel:codemodel)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(xml-resolver:xml-resolver)
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

# use glassfish-jaxb = 2.0.5
%pom_disable_module plugin-2.0
# use glassfish-jaxb = 2.1.13
%pom_disable_module plugin-2.1

# Add dependency on codemodel:
# because org.glassfish.jaxb:codemodel:2.2.11 have missing classes use @ runtime by these plugins:
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin-2.2

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
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.13.0-alt1_2jpp8
- new version

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

