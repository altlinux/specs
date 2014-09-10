Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             stax2-api
Version:          3.1.1
Release:          alt2_8jpp7
Summary:          Experimental API extending basic StAX implementation
License:          BSD
# NOTE. new home http://wiki.fasterxml.com/WoodstoxStax2
URL:              http://docs.codehaus.org/display/WSTX/StAX2
# NOTE. newer release available here https://github.com/FasterXML/stax2-api/
Source0:          http://repository.codehaus.org/org/codehaus/woodstox/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:          http://repository.codehaus.org/org/codehaus/woodstox/%{name}/%{version}/%{name}-%{version}.pom

BuildArch:        noarch

BuildRequires:    maven-surefire-provider-junit
BuildRequires:    bea-stax-api
BuildRequires:    maven-local
Source44: import.info

%description
StAX2 is an experimental API that is intended to extend
basic StAX specifications in a way that allows implementations
to experiment with features before they end up in the actual
StAX specification (if they do). As such, it is intended
to be freely implementable by all StAX implementations same way
as StAX, but without going through a formal JCP process.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c %{name}
# fixing incomplete source directory structure
mkdir -p src/main/java
mv -f org src/main/java/

cp %{SOURCE1} pom.xml
%pom_remove_dep javax.xml.stream:stax-api
%pom_add_dep stax:stax-api:1.0.1

%build

%mvn_file :%{name} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_4jpp7
- new version

