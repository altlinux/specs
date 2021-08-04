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
%bcond_without tests

Name:		classloader-leak-test-framework
Version:	1.1.1
Release:	alt1_16jpp11
Summary:	Detection and verification of Java ClassLoader leaks
License:	ASL 2.0
URL:		https://github.com/mjiderhamn/classloader-leak-prevention/tree/master/%{name}
Source0:	https://github.com/mjiderhamn/classloader-leak-prevention/archive/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.bcel:bcel)
Source44: import.info

%description
Stand-alone test framework for detecting and/or verifying the existence or
non-existence of Java ClassLoader leaks. It is also possible to test leak
prevention mechanisms to confirm that the leak really is avoided. The framework
is an built upon JUnit.

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n classloader-leak-prevention-%{name}-%{version}

rm -r classloader-leak-prevention
cp -r %{name}/* .

%pom_remove_dep com.sun.faces:jsf-api
%pom_remove_dep com.sun.faces:jsf-impl
%pom_remove_dep javax.el:el-api

%pom_remove_plugin -r :maven-javadoc-plugin

%build
%if %{with tests}
%mvn_build --xmvn-javadoc -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
%else
%mvn_build -f --xmvn-javadoc -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
%endif

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.1.1-alt1_16jpp11
- update

* Wed Dec 16 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_13jpp8
- build w/o mojarra

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_8jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_4jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp8
- new jpp release

