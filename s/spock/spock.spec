Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.7
%global namedreltag  -groovy-2.0
%global namedversion %{version}%{?namedreltag}
%global nameddottag  %(echo %{?namedreltag} | tr - . )
Name:          spock
Version:       0.7
Release:       alt4_0.17.groovy.2.0jpp8
Summary:       A testing and specification framework
License:       ASL 2.0
URL:           https://github.com/spockframework/spock
Source0:       https://github.com/spockframework/spock/archive/%{name}-%{namedversion}.tar.gz
Patch0:        0001-Build-with-Gradle-local-mode.patch
Patch1:        spock-0.7-core-port-to-groovy2.4.8.patch
Patch33:       spock-0.7-groovy-2.0-alt-fix-build-with-ant.patch

BuildRequires: gradle-local
BuildRequires: apache-parent

BuildRequires: ant
BuildRequires: antlr-tool
BuildRequires: aopalliance
BuildRequires: apache-commons-cli
BuildRequires: cglib
BuildRequires: google-guice
BuildRequires: groovy >= 2.0
BuildRequires: hamcrest
BuildRequires: junit
BuildRequires: objenesis
BuildRequires: objectweb-asm

Requires:      java
BuildArch:     noarch

Obsoletes:     %{name}-javadoc < 0.7-0.5
Source44: import.info

%description
Spock is a testing and specification framework for Java and
Groovy applications.

%package core
Group: Development/Java
Summary:       Spock Framework - Core Module

%description core
Spock Framework - Core Module.

%package guice
Group: Development/Java
Summary:       Spock Framework - Guice Module

%description guice
Spock Framework - Guice Module provides support for
testing Guice 2/3 based applications.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch33 -p1
find . -name "*.class" -delete
find . -name "*.jar" -delete

sed -i "s|sourceCompatibility = 1.5|sourceCompatibility = 1.6|" build.gradle

# We don't need these modules.
rm -rf spock-maven spock-specs spock-spring spock-tapestry spock-unitils
%mvn_package ":spock-{maven,specs,spring,tapestry,unitils}" __noinstall

%build

# install task used for generate pom files
%gradle_build -s -- -x javadoc

%install
%mvn_install

%files core -f .mfiles-spock-core
%doc LICENSE NOTICE

%files guice -f .mfiles-spock-guice

%changelog
* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt4_0.17.groovy.2.0jpp8
- fixed build with new ant

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.17.groovy.2.0jpp8
- fixed build

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.14.groovy.2.0jpp8
- new fc release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.13.groovy.2.0jpp8
- new fc release

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.9.groovy.2.0jpp8
- unbootstrap build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_0.3%(echo -groovy-1.8 | tr - . )jpp7
- fixed build with new junit

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_0.3%(echo -groovy-1.8 | tr - . )jpp7
- new version

