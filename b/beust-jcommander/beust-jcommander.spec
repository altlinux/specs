Group: Development/Java
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
%bcond_with bootstrap

Name:           beust-jcommander
Version:        1.78
Release:        alt1_7jpp11
Summary:        Java framework for parsing command line parameters
License:        ASL 2.0
URL:            http://jcommander.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# Adapted from earlier version that still shipped poms. It uses kobalt for building now
Source1:        %{name}.pom
# Cleaned up bundled jars whose licensing cannot be easily verified
Source2:        generate-tarball.sh

Patch0:         0001-ParseValues-NullPointerException-patch.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.testng:testng)
%endif
Source44: import.info

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the %{summary}.

%prep
%setup -q
%patch0 -p1

chmod -x license.txt
cp -p %SOURCE1 pom.xml
sed -i 's/@VERSION@/%{version}/g' pom.xml

%build
%mvn_file : %{name}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc license.txt notice.md README.markdown

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.78-alt1_7jpp11
- update

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 1.78-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_6jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_3jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.65-alt1_1jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_4jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

