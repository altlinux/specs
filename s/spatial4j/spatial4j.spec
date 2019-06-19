Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          spatial4j
Version:       0.7
Release:       alt1_3jpp8
Summary:       A Geospatial Library for Java
License:       ASL 2.0
URL:           https://projects.eclipse.org/projects/locationtech.spatial4j
Source0:       https://github.com/locationtech/spatial4j/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.locationtech.jts:jts-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.noggit:noggit)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

BuildArch:     noarch
Source44: import.info

%description
Spatial4j is a general purpose spatial/geospatial Java library.
It's core capabilities are 3-fold: to provide common geospatially-aware shapes,
to provide distance calculations and other math, and to read and write the
shapes to strings.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Unwanted tasks
%pom_remove_plugin de.thetaphi:forbiddenapis
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

# Backward compatibility aliases
%mvn_alias org.locationtech.spatial4j:spatial4j com.spatial4j:spatial4j

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md FORMATS.md
%doc --no-dereference asl-v20.txt notice.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference asl-v20.txt notice.md

%changelog
* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3jpp8
- new version

* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_7jpp8
- build with jts1.14

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_4jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_3jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_4jpp8
- java 8 mass update

