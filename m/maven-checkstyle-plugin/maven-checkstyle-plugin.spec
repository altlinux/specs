Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             maven-checkstyle-plugin
Version:          2.13
Release:          alt2_6jpp8
Summary:          Plugin that generates a report regarding the code style used by the developers
License:          ASL 2.0
URL:              http://maven.apache.org/plugins/%{name}

Source0:          http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch1:           0001-Port-to-doxia-1.7.patch

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(com.puppycrawl.tools:checkstyle:7)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-integration-tools)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-plugin-descriptor)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
Source44: import.info

%description
Generates a report on violations of code style and optionally fails the build
if violations are detected.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%patch1 -p1

%pom_remove_plugin :apache-rat-plugin


sed -i -e 's,checkstyleVersion>5.7</checkstyleVersion,checkstyleVersion>7.7</checkstyleVersion,' pom.xml

%build
%mvn_build -f -- -DmavenVersion=3.2.1

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt2_6jpp8
- fixed build with new checkstyle

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_6jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt4_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_2jpp7
- new version

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_2jpp7
- complete build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

