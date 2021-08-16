# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jmock
Version:        2.12.0
Release:        alt1_4jpp11
Summary:        Java library for testing code with mock objects
License:        BSD

URL:            http://www.jmock.org/
Source0:        https://github.com/jmock-developers/jmock-library/archive/%{version}/%{name}-%{version}.tar.gz
# Adapt to junit 4.13
# See https://github.com/jmock-developers/jmock-library/pull/200
Patch0:         %{name}-junit4.13.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(com.google.auto.service:auto-service)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(javax.xml.ws:jaxws-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apache-extras.beanshell:bsh)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm)

# required for some unit tests
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
Source44: import.info

%description
Mock objects help you design and test the interactions between the objects in
your programs.
The jMock library:
  * makes it quick and easy to define mock objects, so you don't break the
    rhythm of programming.
  * lets you precisely specify the interactions between your objects, reducing
    the brittleness of your tests.
  * works well with the auto-completion and re-factoring features of your IDE
  * plugs into your favorite test framework
  * is easy to extend.


%package example
Group: Development/Java
Summary:        jMock Examples

%description example
jMock Examples.


%package imposters
Group: Development/Java
Summary:        jMock imposters

%description imposters
jMock imposters.


%package junit3
Group: Development/Java
Summary:        jMock JUnit 3 Integration

%description junit3
jMock JUnit 3 Integration.


%package junit4
Group: Development/Java
Summary:        jMock JUnit 4 Integration

%description junit4
jMock JUnit 4 Integration.


%package junit5
Group: Development/Java
Summary:        jMock JUnit 5 Integration

%description junit5
jMock JUnit 5 Integration.


%package legacy
Group: Development/Java
Summary:        jMock Legacy Plugins

%description legacy
Plugins that make it easier to use jMock with legacy code.


%package parent
Group: Development/Java
Summary:        jMock Parent POM

%description parent
jMock Parent POM.


%package testjar
Group: Development/Java
Summary:        jMock Test Jar

%description testjar
Source for JAR files used in jMock Core tests.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n %{name}-library-%{version}
%patch0 -p1


# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove maven plugins that are not required for RPM builds
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin -r :versions-maven-plugin
%pom_remove_plugin :maven-gpg-plugin testjar

# use correct maven artifact for @javax.annotations.Nullable
%pom_change_dep com.google.code.findbugs:annotations com.google.code.findbugs:jsr305 testjar

# don't install imposters-tests package
%mvn_package org.jmock:jmock-imposters-tests __noinstall


%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.test.failure.ignore=true


%install
%mvn_install


%files           -f .mfiles-%{name}
%doc README*
%doc --no-dereference LICENSE.txt

%files example   -f .mfiles-%{name}-example
%files imposters -f .mfiles-%{name}-imposters
%files junit3    -f .mfiles-%{name}-junit3
%files junit4    -f .mfiles-%{name}-junit4
%files junit5    -f .mfiles-%{name}-junit5
%files legacy    -f .mfiles-%{name}-legacy

%files parent    -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE.txt

%files testjar   -f .mfiles-%{name}-testjar
%doc --no-dereference LICENSE.txt

%files javadoc   -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt


%changelog
* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 0:2.12.0-alt1_4jpp11
- fixed build

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.12.0-alt1_3jpp11
- jvm11 build, added unzip BR

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.12.0-alt1_2jpp11
- new version

* Fri May 14 2021 Igor Vlasenko <viy@altlinux.org> 0:2.8.2-alt4_10jpp8
- fixed build

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 0:2.8.2-alt3_10jpp8
- new version

* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt3_7jpp8
- fixed build

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt2_7jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt2_6jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt2_5jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt2_4jpp8
- fixed build

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt1_2jpp8
- new version

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_2jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_1jpp7
- fc update

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt4_3jpp6
- build with objectweb-asm

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_3jpp6
- new jpp release

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_2jpp5
- fixed build; use cglib21 (with old asm)

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_1jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

