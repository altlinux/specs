Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          geolatte-geom
Version:       0.14
Release:       alt1_4jpp8
Summary:       A geometry model for Java that conforms to the Simple Features For SQL
License:       LGPLv3+
URL:           http://www.geolatte.org/
Source0:       https://github.com/GeoLatte/geolatte-geom/archive/v%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.vividsolutions:jts)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(jaxen:jaxen)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)

BuildArch:     noarch
Source44: import.info

%description
This geoLatte-geom library offers a geometry model
that conforms to the OGC Simple Features for SQL
specification.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%pom_xpath_set "pom:dependency[pom:groupId='log4j']/pom:version" 1.2.17
%pom_xpath_set "pom:dependency[pom:groupId='org.codehaus.jackson']/pom:artifactId" jackson-mapper-asl

%pom_remove_dep org.apache.directory.studio:org.apache.commons.collections
%pom_add_dep commons-collections:commons-collections:3.2.1:test

%mvn_file org.geolatte:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc copyright-template.vml

%files javadoc -f .mfiles-javadoc
%doc copyright-template.vml

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_2jpp8
- new version

