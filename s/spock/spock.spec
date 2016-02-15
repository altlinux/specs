Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name spock
%define version 0.7
%global namedreltag  -groovy-2.0
%global namedversion %{version}%{?namedreltag}
%global nameddottag  %(echo %{?namedreltag} | tr - . )
Name:          spock
Version:       0.7
Release:       alt3_0.9.groovy.2.0jpp8
Summary:       A testing and specification framework
License:       ASL 2.0
URL:           https://github.com/spockframework/spock
Source0:       https://github.com/spockframework/spock/archive/%{name}-%{namedversion}.tar.gz
Patch0:        0001-Build-with-Gradle-local-mode.patch

BuildRequires: gradle-local
BuildRequires: apache-parent

BuildRequires: ant
BuildRequires: antlr
BuildRequires: aopalliance
BuildRequires: apache-commons-cli
BuildRequires: cglib
BuildRequires: google-guice
BuildRequires: groovy >= 2.0
BuildRequires: hamcrest
BuildRequires: junit
BuildRequires: objectweb-asm
BuildRequires: objenesis

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
find . -name "*.class" -delete
find . -name "*.jar" -delete

# We don't need these modules.
rm -rf spock-maven spock-spring spock-tapestry spock-unitils

%build
gradle-local -s --offline -x javadoc install

%install
repo=$HOME/.m2/repository

for mod in core guice; do
    pom=$repo/org/spockframework/spock-$mod/%{namedversion}/spock-$mod-%{namedversion}.pom
    jar=$repo/org/spockframework/spock-$mod/%{namedversion}/spock-$mod-%{namedversion}.jar
    %mvn_artifact $pom $jar
    %mvn_package :spock-$mod $mod
done

%mvn_install

%files core -f .mfiles-core
%doc LICENSE NOTICE

%files guice -f .mfiles-guice

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.9.groovy.2.0jpp8
- unbootstrap build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_0.3%(echo -groovy-1.8 | tr - . )jpp7
- fixed build with new junit

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_0.3%(echo -groovy-1.8 | tr - . )jpp7
- new version

