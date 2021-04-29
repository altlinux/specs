Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global artifactId javax.servlet.jsp-api

Name:       glassfish-jsp-api
Version:    2.3.3
Release:    alt1_2jpp11
Summary:    Glassfish J2EE JSP API specification
License:    (CDDL-1.1 or GPLv2 with exceptions) and ASL 2.0

URL:        https://github.com/javaee/javaee-jsp-api
Source0:    %{url}/archive/%{artifactId}-%{version}.tar.gz
Source1:    http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
Source44: import.info

%description
This project provides a container independent specification of JSP
2.2. Note that this package doesn't contain implementation of this
specification. See glassfish-jsp for one of implementations

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n javaee-jsp-api-%{artifactId}-%{version}

cp -p %{SOURCE1} LICENSE-ASL-2.0.txt

pushd api
# Submited upstream: http://java.net/jira/browse/JSP-31
sed -i "/<bundle.symbolicName>/s/-api//" pom.xml

%pom_xpath_remove "pom:dependency[pom:groupId='javax.el' or pom:groupId='javax.servlet']/pom:scope"

%pom_remove_plugin :maven-gpg-plugin
# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin

%mvn_alias : javax.servlet:jsp-api
popd

%build
pushd api
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%doc --no-dereference LICENSE-ASL-2.0.txt LICENSE

%files javadoc -f api/.mfiles-javadoc
%doc --no-dereference LICENSE-ASL-2.0.txt LICENSE


%changelog
* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.11.b01jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.10.b01jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.9.b01jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.8.b01jpp8
- new fc release

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.7.b01jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.5.b01jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.4.b01jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_0.3.b01jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_6jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_4jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_4jpp7
- fc update

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2jpp7
- full version

