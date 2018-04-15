Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        An open source data binding framework for Java
Name:           castor
Version:        1.3.3
Release:        alt1_8jpp8
# Older source files are BSD licensed and newer ones are ASL licensed
License:        BSD and ASL 2.0
URL:            http://castor-data-binding.github.io/castor/
# Hash sum of source will not match upstream because bundled jars have been removed
Source0:        http://dist.codehaus.org/castor/%{version}/castor-%{version}-src.tgz
Patch0:         castor-1.3.2-fix-unmappable-chars.patch

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(ant:ant)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(edu.umd.cs:multithreadedtc)
BuildRequires:  mvn(jakarta-regexp:jakarta-regexp)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(ldapsdk:ldapsdk)
BuildRequires:  mvn(log4j:log4j:1.2.16)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.castor:castor-xml)
BuildRequires:  mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires:  mvn(org.codehaus.mojo:castor-maven-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.springframework:spring-context)
BuildRequires:  mvn(org.springframework:spring-test)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(velocity:velocity)
BuildRequires:  mvn(xmlunit:xmlunit)
Obsoletes:      castor-demo < 1.3.2
Obsoletes:      castor-test < 1.3.2
Obsoletes:      castor-xml < 1.3.2
Obsoletes:      castor-doc < 1.3.2
Source44: import.info

%description
Castor is an open source data binding framework for Java. It's basically
the shortest path between Java objects, XML documents and SQL tables.
Castor provides Java to XML binding, Java to SQL persistence, and more.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%patch0 -p0 -b .orig

# Disable uneeded modules
%pom_disable_module anttask
%pom_disable_module xmlctf-framework
%pom_disable_module maven-plugins
%pom_disable_module xml-annotations

# Disable integration test suites
%pom_disable_module cpactf
%pom_disable_module jpa-extensions-it
%pom_disable_module xmlctf

# Remove test deps that are not in Fedora
%pom_remove_dep tyrex:tyrex
%pom_remove_dep tyrex:tyrex cpa
%pom_xpath_remove "pom:build/pom:extensions"

# Fix dep on cglib
sed -i 's@cglib-nodep@cglib@g' pom.xml cpa/pom.xml

# Fix dep on mtc
sed -i 's@edu.umd.cs.mtc@edu.umd.cs@g' pom.xml xml/pom.xml

# These APIs are provided by modern JREs
%pom_remove_dep "javax.xml.stream:stax-api" . xml
%pom_remove_dep "stax:stax" . xml

%build
%mvn_build -- -Dgpg.skip=true -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles
%doc src/doc/license.txt src/doc/new-license.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc src/doc/license.txt src/doc/new-license.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_2jpp8
- unbootsrap build

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_6jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_3jpp7
- new version

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt3_4jpp5
- fixed build

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt2_4jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt1_4jpp5
- new version

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

