Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-common-artifact-filters
Version:        3.0.1
Release:        alt1_6jpp8
Summary:        Maven Common Artifact Filters
License:        ASL 2.0
URL:            http://maven.apache.org/shared/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Remove-Maven-3.0-specific-code.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
Source44: import.info

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1

# We don't want to support legacy Maven versions (older than 3.1)
%pom_remove_dep org.sonatype.sisu:
%pom_remove_dep org.sonatype.aether:
find -name SonatypeAether\*.java -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_6jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt5_16jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_11jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_3jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

