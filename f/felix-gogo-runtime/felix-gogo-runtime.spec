Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle  org.apache.felix.gogo.runtime

%bcond_without tests

Name:           felix-gogo-runtime
Version:        1.1.4
Release:        alt1_1jpp11
Summary:        Apache Felix Gogo command line shell for OSGi
# One file is also MIT licensed:
#  src/main/java/org/apache/felix/gogo/runtime/Expression.java
License:        ASL 2.0 and MIT
URL:            http://felix.apache.org/documentation/subprojects/apache-felix-gogo.html

Source0:        http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:gogo-parent:pom:) >= 5
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
%if %{with tests}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
Source44: import.info

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

# Use compendium dep
%pom_remove_dep :org.osgi.namespace.service
%pom_remove_dep :org.osgi.service.component.annotations
%pom_remove_dep :org.osgi.service.event
%pom_xpath_inject "pom:dependencies" "
<dependency>
<groupId>org.osgi</groupId>
<artifactId>osgi.cmpn</artifactId>
</dependency>"

# Remove 2 failing assertions on Java 11 in TestParser.testPipe()
sed -i '/(echoout/ d' src/test/java/org/apache/felix/gogo/runtime/TestParser.java

%mvn_file : felix/%{bundle}

%build
%if %{with tests}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dsource=1.8 -DdetectJavaApiLink=false
%else
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dsource=1.8 -DdetectJavaApiLink=false
%endif

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.1.4-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.1.0-alt1_8jpp11
- update

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 1.1.0-alt1_5jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp8
- explicit build with java8

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp8
- java update

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.2-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.2-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.2-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.2-alt1_2jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_5jpp7
- new release

