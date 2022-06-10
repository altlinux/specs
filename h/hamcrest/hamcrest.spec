Epoch: 0
Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.2
%bcond_with bootstrap

%global upstream_version %(echo %{version} | tr '~' '-')

Name:           hamcrest
Version:        2.2
Release:        alt1_5jpp11
Summary:        Library of matchers for building test expressions
License:        BSD
URL:            https://github.com/hamcrest/JavaHamcrest
BuildArch:      noarch

Source0:        https://github.com/hamcrest/JavaHamcrest/archive/v%{upstream_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/hamcrest/hamcrest/%{upstream_version}/hamcrest-%{upstream_version}.pom

Patch0:         0001-Fix-build-with-OpenJDK-11.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
%endif

Provides:       hamcrest-core = %{version}-%{release}
Obsoletes:      hamcrest-core < 1.3-32
Obsoletes:      hamcrest-demo < 1.3-32
Source44: import.info

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n JavaHamcrest-%{upstream_version}
%patch0 -p1

rm -rf docs
rm -rf *gradle*
rm -rf */*.gradle

mv hamcrest/src .
rm -rf hamcrest
rm -rf hamcrest-core
rm -rf hamcrest-integration
rm -rf hamcrest-library

cp -p %{SOURCE1} pom.xml
%pom_add_dep junit:junit::test
%pom_xpath_inject pom:project '
<build>
	<plugins>
		<plugin>
		<groupId>org.apache.maven.plugins</groupId>
		<artifactId>maven-compiler-plugin</artifactId>
		<version>3.8.1</version>
		<configuration>
			<source>1.8</source>
			<target>1.8</target>
		</configuration>
		</plugin>
	</plugins>
</build>'

%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-all
%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-core
%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-library

sed -i 's/\r//' LICENSE.txt

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2-alt1_5jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.3-alt3_30jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_27jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_25jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_23jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_22jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_18jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_14jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_13jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_5jpp7
- new release

* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp7
- new version

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_21jpp7
- source and target to 1.5

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_21jpp7
- fix for arm

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_21jpp7
- fc update

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_19jpp7
- java6 build for jmock2

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_19jpp7
- fc release

* Tue Oct 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_9.2jpp6
- added OSGi manifest for eclipse

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp5
- rebuild to fix jmock2

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

