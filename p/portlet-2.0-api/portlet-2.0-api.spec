Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global api_version 2.0
%global pkg_name portlet-api_%{api_version}_spec
Name:          portlet-2.0-api
Version:       1.0
Release:       alt3_24jpp11
Summary:       Java Portlet Specification V2.0
License:       ASL 2.0
Url:           http://portals.apache.org/
# svn export http://svn.apache.org/repos/asf/portals/portlet-spec/tags/portlet-api_2.0_spec-1.0 portlet-2.0-api-1.0
# tar czf portlet-2.0-api-1.0-src-svn.tar.gz portlet-2.0-api-1.0
Source0:       %{name}-%{version}-src-svn.tar.gz

BuildRequires: mvn(org.apache.portals:portals-pom:pom:)
#BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: tomcat-servlet-4.0-api
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildArch:     noarch
AutoProv: yes,noosgi-fc
AutoReq: yes,noosgi-fc
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

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%mvn_file :%{pkg_name} %{name}
%mvn_alias :%{pkg_name} javax.portlet:portlet-api

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Tue Apr 18 2023 Igor Vlasenko <viy@altlinux.org> 1.0-alt3_24jpp11
- update

* Sat May 21 2022 Igor Vlasenko <viy@altlinux.org> 1.0-alt3_22jpp11
- fixed build with new maven-parent

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.0-alt2_22jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_19jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_17jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_14jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_13jpp8
- new jpp release

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

