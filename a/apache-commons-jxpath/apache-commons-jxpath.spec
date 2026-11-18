%define _unpackaged_files_terminate_build 1

Name: apache-commons-jxpath
Version: 1.4.0
Release: alt1

Summary: Simple XPath interpreter
License: Apache-2.0
Group: Development/Java
URL: https://commons.apache.org/proper/commons-jxpath/
VCS: https://github.com/apache/commons-jxpath.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.mockito:mockito-bom:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(org.jdom:jdom)
BuildRequires: jakarta-servlet-javax
BuildRequires: jakarta-servlet
BuildRequires: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(commons-io:commons-io)

BuildArch: noarch

%description
Defines a simple interpreter of an expression language called XPath.
JXPath applies XPath expressions to graphs of objects of all kinds:
JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
This package contains the API documentation for %name.

%prep
%setup

%pom_change_dep javax.servlet:servlet-api javax.servlet:javax.servlet-api:4.0.1
%pom_change_dep javax.servlet:jsp-api \
    org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec:1.0.1.Final
%pom_remove_dep com.mockrunner:mockrunner-jdk1.3-j2ee1.3
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin . \
    '<configuration><testExcludes><testExclude>**/JXPathServletContextTest.java</testExclude></testExcludes></configuration>'

%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%mvn_file : %name commons-jxpath

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 1.4.0-alt1
- New version.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.3-alt3_43jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.3-alt3_40jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.3-alt3_37jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_34jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_32jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_30jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_29jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_28jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_26jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_25jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_24jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_17jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_15jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_11jpp7
- rebuild with maven-local

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_11jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_9jpp7
- fixed build

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_9jpp7
- fc release

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_5jpp6
- new version

