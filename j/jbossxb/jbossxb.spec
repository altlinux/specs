Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jbossxb
Version:        2.0.3
Release:        alt2_10jpp8
Summary:        JBoss XML Binding

License:        LGPLv2+
URL:            http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/common/jbossxb/tags/2.0.3.GA/ jbossxb-2.0.3
# tar cJf jbossxb-2.0.3.tar.xz jbossxb-2.0.3/
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.wutka:dtdparser)
BuildRequires:  mvn(org.jboss:jboss-common-core)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss:jboss-reflect)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.spec.javax.xml.bind:jboss-jaxb-api_2.2_spec)
BuildRequires:  mvn(stax:stax)
# Required by stax-ri but not resolved
BuildRequires:  mvn(stax:stax-api)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
Source44: import.info

%description
JBoss XML Binding.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# can't compile stuff in the test dir...missing deps: jboss-test
rm -rf src/test

find -type f -name *.jar -delete
find -type f -name *.class -delete

%pom_change_dep org.jboss.logging:jboss-logging-spi org.jboss.logging:jboss-logging
%pom_add_dep stax:stax
%pom_add_dep org.jboss.spec.javax.xml.bind:jboss-jaxb-api_2.2_spec
%pom_remove_dep sun-jaxb:jaxb-api
%pom_remove_dep javax.activation:activation
%pom_remove_dep org.jboss.test:jboss-test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt2_10jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt2_9jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt2_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt1_1jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt3_3.SP3.9jpp5
- updated repolib

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt2_3.SP3.9jpp5
- rebuild with new xerces repolib

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0.0-alt1_3.SP3.9jpp5
- new jpp release

