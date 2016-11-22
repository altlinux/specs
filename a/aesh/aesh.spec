Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:       aesh
Version:    0.33.7
Release:    alt1_4jpp8
Summary:    Another Extendable SHell
License:    EPL
URL:        http://aeshell.github.io/
Source0:    https://github.com/aeshell/aesh/archive/%{version}.tar.gz

BuildRequires: jboss-parent
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jansi
BuildRequires: fusesource-pom
BuildRequires: junit
BuildRequires: maven-surefire-provider-junit

BuildArch: noarch
Source44: import.info

%description
A.sh is a Java library for handling console input with the goal to support most
GNU Readline features.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n aesh-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc license.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.7-alt1_4jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.33.7-alt1_3jpp8
- java 8 mass update

