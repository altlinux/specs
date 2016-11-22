Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global api_version 2.0
%global pkg_name portlet-api_%{api_version}_spec
Name:          portlet-2.0-api
Version:       1.0
Release:       alt2_12jpp8
Summary:       Java Portlet Specification V2.0
License:       ASL 2.0
Url:           http://portals.apache.org/
# svn export http://svn.apache.org/repos/asf/portals/portlet-spec/tags/portlet-api_2.0_spec-1.0 portlet-2.0-api-1.0
# tar czf portlet-2.0-api-1.0-src-svn.tar.gz portlet-2.0-api-1.0
Source0:       %{name}-%{version}-src-svn.tar.gz

BuildRequires: mvn(org.apache.portals:portals-pom:pom:)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildArch:     noarch
Source44: import.info

%description
The Java Portlet API version 2.0 developed by the
Java Community Process JSR-286 Expert Group.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# cleanup
find . -name '*.class' -delete
find . -name '*.jar' -delete

for p in LICENSE NOTICE;do
  iconv -f iso8859-1 -t utf-8 ${p} > ${p}.conv && mv -f ${p}.conv ${p}
  sed -i 's/\r//' ${p}
done

# change apis version
sed -i "s|javax.servlet.http;version=2.4,*|javax.servlet.http;version=3.0,*|" pom.xml

# Force tomcat apis
%pom_remove_dep javax.servlet:servlet-api
%pom_add_dep org.apache.tomcat:tomcat-servlet-api::provided

%mvn_file :%{pkg_name} %{name}
%mvn_alias :%{pkg_name} javax.portlet:portlet-api

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_3jpp7
- new version

