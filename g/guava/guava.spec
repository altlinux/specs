Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora}
%bcond_without testlib
%endif

Name:           guava
Version:        18.0
Release:        alt2_11jpp8
Summary:        Google Core Libraries for Java
License:        ASL 2.0
URL:            https://github.com/google/guava
BuildArch:      noarch

Source0:        https://github.com/google/guava/archive/v%{version}.tar.gz

Patch0:         %{name}-java8.patch
Patch1:         guava-jdk8-HashMap-testfix.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
%if %{with testlib}
BuildRequires:  mvn(com.google.truth:truth)
BuildRequires:  mvn(junit:junit)
%endif
Source44: import.info

%description
Guava is a suite of core and expanded libraries that include
utility classes, Googlea.'s collections, io classes, and much
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%if %{with testlib}
%package testlib
Group: Development/Java
Summary:        The guava-testlib subartefact

%description testlib
guava-testlib provides additional functionality for conveinent unit testing
%endif

%prep
%setup -q
%patch0 -p1
%patch1 -p1
find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%if %{without testlib}
%pom_disable_module guava-testlib
%endif
%pom_remove_plugin -r :animal-sniffer-maven-plugin 
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_dep jdk:srczip guava
%pom_remove_dep :caliper guava-tests
%mvn_package :guava-parent guava
%mvn_package :guava-tests __noinstall

# javadoc generation fails due to strict doclint in JDK 1.8.0_45
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_xpath_inject /pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:instructions "<_nouses>true</_nouses>" guava/pom.xml

%build

%mvn_file :%{name} %{name}
%mvn_alias :%{name} com.google.collections:google-collections com.google.guava:guava-jdk5
# Tests fail on Koji due to insufficient memory,
# see https://bugzilla.redhat.com/show_bug.cgi?id=1332971
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-guava
%doc AUTHORS CONTRIBUTORS README*
%doc COPYING

%files javadoc -f .mfiles-javadoc
%doc COPYING

%if %{with testlib}
%files testlib -f .mfiles-guava-testlib
%endif

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_11jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_10jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_8jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_4jpp8
- added osgi provides

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt1_4jpp8
- unbootsrap build

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_1jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

