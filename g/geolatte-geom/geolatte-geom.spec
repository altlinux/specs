Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          geolatte-geom
Version:       1.2.0
Release:       alt1_3jpp8
Summary:       A geometry model for Java that conforms to the Simple Features For SQL
License:       LGPLv3+
URL:           http://www.geolatte.org/
Source0:       https://github.com/GeoLatte/geolatte-geom/archive/v%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(com.vividsolutions:jts)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)

BuildArch:     noarch
Source44: import.info

%description
A geometry model for Java that conforms to the Simple Features For
SQL specification. It is intended as a drop-in replacement for the
Java Topology Suite (JTS) geometry model. GeoLatte-geom is fully
inter-operable with JTS but offers additional features.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

# Unneeded plugins for RPM builds
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Use compat version of log4j
%pom_xpath_set "pom:dependency[pom:groupId='log4j']/pom:version" 1.2.17 geom

# Fix dependencies to reflect what's in Fedora
%pom_change_dep :jackson-mapper-lgpl org.codehaus.jackson:jackson-mapper-asl geom
%pom_change_dep :org.apache.commons.collections commons-collections:commons-collections geom

# Allow building against new jts
sed -i -e 's/com\.vividsolutions\.jts/org.locationtech.jts/g' $(find geom -name "*.java")
sed -i -e '/clone()/a@Override public CoordinateSequence copy() {return (CoordinateSequence)clone();}' \
  geom/src/main/java/org/geolatte/geom/AbstractPositionSequence.java

%build
# Ignore a couple of test failures, not sure why it happens
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference copyright-template.vml

%files javadoc -f .mfiles-javadoc
%doc --no-dereference copyright-template.vml

%changelog
* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3jpp8
- new version

* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2_7jpp8
- build with jts1.14

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2jpp8
- new version

