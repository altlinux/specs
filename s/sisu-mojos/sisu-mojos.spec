Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           sisu-mojos
Version:        0.3.1
Release:        alt1_5jpp8
Summary:        Sisu plugin for Apache Maven
License:        EPL
URL:            http://www.eclipse.org/sisu
BuildArch:      noarch

Source0:        http://git.eclipse.org/c/sisu/org.eclipse.sisu.mojos.git/snapshot/releases/%{version}.tar.bz2#/%{name}-%{version}.tar.bz2

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

Obsoletes:      sisu-maven-plugin < 1:0.1
Source44: import.info

%description
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -c
mv releases/%{version}/* .
# Animal Sniffer is not useful in Fedora
%pom_remove_plugin :animal-sniffer-maven-plugin
%mvn_alias : org.sonatype.plugins:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_5jpp8
- fc27 update

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

