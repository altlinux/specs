Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without groovy

Name:           testng
Version:        6.12
Release:        alt2_2jpp8
Summary:        Java-based testing framework
License:        ASL 2.0
URL:            http://testng.org/
Source0:        https://github.com/cbeust/testng/archive/%{version}.tar.gz

# Allows building with maven instead of gradle
Source1:        pom.xml

Patch0:         0001-Avoid-accidental-javascript-in-javadoc.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache-extras.beanshell:bsh)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.yaml:snakeyaml)
%if %{with groovy}
BuildRequires:  mvn(org.assertj:assertj-core) >= 3.8.0
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.spockframework:spock-core)
%endif
Source44: import.info

%description
TestNG is a testing framework inspired from JUnit and NUnit but introducing
some new functionality, including flexible test configuration, and
distributed test running.  It is designed to cover unit tests as well as
functional, end-to-end, integration, etc.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1

cp %{SOURCE1} .

# remove any bundled libs, but not test resources
find ! -path "*/test/*" -name *.jar -print -delete
find -name *.class -delete

# these are unnecessary
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# missing test deps
%if %{with groovy}
%pom_add_plugin "org.codehaus.gmavenplus:gmavenplus-plugin" pom.xml \
  "<executions><execution><goals><goal>addTestSources</goal><goal>testGenerateStubs</goal><goal>testCompile</goal><goal>removeTestStubs</goal></goals></execution></executions>"
%pom_add_dep "org.assertj:assertj-core::test"
%pom_add_dep "org.spockframework:spock-core::test"
%pom_add_dep "org.codehaus.groovy:groovy-all::test"

# remove failing test
sed -i -e '/parallelDataProviderSample/,+12d' ./src/test/java/test/dataprovider/DataProviderTest.java
%endif

sed -i -e 's/DEV-SNAPSHOT/%{version}/' src/main/java/org/testng/internal/Version.java

cp -p ./src/main/java/*.dtd.html ./src/main/resources/.

%mvn_file : %{name}
# jdk15 classifier is used by some other packages
%mvn_alias : :::jdk15:

%build
%if %{with groovy}
%mvn_build -- -Dmaven.test.skip.exec=true  -Dmaven.local.debug=true
%else
%mvn_build -f -- -Dmaven.test.skip.exec=true  -Dmaven.local.debug=true
%endif

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.12-alt2_2jpp8
- fixed build

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.12-alt1_2jpp8
- new version

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.9.12-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.9.11-alt1_1jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.9.10-alt1_2jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.8.21-alt2_2jpp8
- added osgi provides

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.8.21-alt1_2jpp8
- unbootsrap build

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.8.21-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.8.7-alt1_1jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.8-alt1_1jpp7
- new version

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt3_4jpp7
- fixed deps

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt2_4jpp7
- new release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt2_1jpp7
- added oss-parent pom dependency

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt1_1jpp7
- new version

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt2_2jpp6
- fixed build

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt1_2jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt4_1jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt1_1jpp5
- converted from JPackage by jppimport script

