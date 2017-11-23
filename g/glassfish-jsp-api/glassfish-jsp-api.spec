Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global artifactId javax.servlet.jsp-api
%global jspspec 2.2
%global reltag b01


Name:       glassfish-jsp-api
Version:    2.3.2
Release:    alt1_0.8.b01jpp8
Summary:    Glassfish J2EE JSP API specification

License:    (CDDL-1.1 or GPLv2 with exceptions) and ASL 2.0
URL:        http://java.net/jira/browse/JSP
Source0:    %{artifactId}-%{version}-%{reltag}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh
Source2:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:    https://javaee.github.io/glassfish/LICENSE.html

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
%setup -q -n %{artifactId}-%{version}-%{reltag}

cp -p %{SOURCE2} LICENSE-ASL-2.0.txt
cp -p %{SOURCE3} LICENSE-CDDL+GPLv2.html

# Submited upstream: http://java.net/jira/browse/JSP-31
sed -i "/<bundle.symbolicName>/s/-api//" pom.xml

%pom_xpath_remove "pom:dependency[pom:groupId='javax.el' or pom:groupId='javax.servlet']/pom:scope"

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin

%mvn_alias : javax.servlet:jsp-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-ASL-2.0.txt LICENSE-CDDL+GPLv2.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL-2.0.txt LICENSE-CDDL+GPLv2.html


%changelog
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

