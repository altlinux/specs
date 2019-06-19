%define oldname geolatte-geom
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          geolatte-geom0.14
Version:       0.14
Release:       alt3_7jpp8
Summary:       A geometry model for Java that conforms to the Simple Features For SQL
License:       LGPLv3+
URL:           http://www.geolatte.org/
Source0:       https://github.com/GeoLatte/geolatte-geom/archive/v%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.vividsolutions:jts:1.14.0)
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
Summary:       Javadoc for %{oldname}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{oldname}.

%prep
%setup -q -n %{oldname}-%{version}

%pom_xpath_set "pom:dependency[pom:groupId='log4j']/pom:version" 1.2.17
%pom_xpath_set "pom:dependency[pom:groupId='org.codehaus.jackson']/pom:artifactId" jackson-mapper-asl

%pom_remove_dep org.apache.directory.studio:org.apache.commons.collections
%pom_add_dep commons-collections:commons-collections:3.2.1:test

%mvn_file org.geolatte:%{oldname} %{oldname}
%pom_change_dep com.vividsolutions:jts:1.13 com.vividsolutions:jts:1.14.0
%mvn_compat_version : 0.13 %{version}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference copyright-template.vml

%files javadoc -f .mfiles-javadoc
%doc --no-dereference copyright-template.vml

%changelog
* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3_7jpp8
- compat package

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

