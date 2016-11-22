Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           apache-commons-jxpath
Version:        1.3
Release:        alt3_25jpp8
Summary:        Simple XPath interpreter
License:        ASL 2.0
URL:            http://commons.apache.org/jxpath/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/jxpath/source/commons-jxpath-%{version}-src.tar.gz

Patch0:         commons-jxpath-mockrunner.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(javax.servlet:jsp-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
Source44: import.info

%description
Defines a simple interpreter of an expression language called XPath.
JXPath applies XPath expressions to graphs of objects of all kinds:
JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-jxpath-%{version}-src
%patch0 -p1

%mvn_file ":{*}" %{name} @1
%mvn_alias : org.apache.commons:

%pom_xpath_inject 'pom:properties' \
  '<commons.osgi.import>org.apache.commons.beanutils;resolution:="optional",org.jdom*;resolution:="optional",org.w3c.dom;resolution:="optional",*</commons.osgi.import>'

%build
# we are skipping tests because we don't have com.mockrunner in repos yet
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

