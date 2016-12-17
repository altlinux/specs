Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          spatial4j
Version:       0.5.0
Release:       alt1_4jpp8
Summary:       A Geospatial Library for Java
License:       ASL 2.0
URL:           https://github.com/locationtech/spatial4j
Source0:       https://github.com/spatial4j/spatial4j/archive/%{name}-0.5.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.vividsolutions:jts)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.noggit:noggit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

# test deps
%if 0
BuildRequires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.slf4j:slf4j-simple)
%endif

BuildArch:     noarch
Source44: import.info

%description
Spatial4j is a general purpose spatial/geospatial Java library.
It's core capabilities are 3-fold: to provide common geospatially-aware shapes,
to provide distance calculations and other math, and to read and write the
shapes to strings.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-0.5

# Unwanted tasks
%pom_remove_plugin de.thetaphi:forbiddenapis
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

# the attach-sources execution breaks OSGi manifest generation
%pom_remove_plugin :maven-jar-plugin

%mvn_file : %{name}

%build

# Test skipped for unavailable test deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_4jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_3jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_4jpp8
- java 8 mass update

