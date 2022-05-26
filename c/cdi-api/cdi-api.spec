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
%bcond_with bootstrap

Name:           cdi-api
Version:        2.0.2
Release:        alt1_3jpp11
Summary:        CDI API
License:        ASL 2.0
URL:            https://github.com/eclipse-ee4j/cdi
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/cdi/archive/%{version}.tar.gz

Patch1:         0001-Remove-dependency-on-glassfish-el.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  %{?module_prefix}mvn(jakarta.inject:jakarta.inject-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
Source44: import.info

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%{?javadoc_package}

%prep
%setup -q -n cdi-%{version}

%pom_remove_parent
%pom_remove_parent api
%pom_disable_module spec
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_dep :jakarta.el-api api
%pom_remove_dep :jakarta.interceptor-api api
rm -rf api/src/main/java/javax/enterprise/{context/,inject/spi/,inject/se/,inject/Model.java,inject/New.java}

%mvn_alias :jakarta.enterprise.cdi-api javax.enterprise:cdi-api

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

ln -s jakarta.enterprise.cdi-api.jar %buildroot%_javadir/%name/%{name}.jar

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt
%_javadir/%name/%{name}.jar

%changelog
* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 2.0.2-alt1_3jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.0-alt1_2jpp11
- new version

* Mon May 31 2021 Igor Vlasenko <viy@altlinux.org> 1.2-alt2_12jpp8
- build w/o asciidoc (python2)

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_12jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp8
- new jpp release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13jpp8
- added osgi provides

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12jpp8
- fixed osgi provides

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_12jpp8
- added osgi provides

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11jpp8
- java 8 mass update

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9.SP4jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6.SP4jpp7
- fc update

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4.SP4jpp7
- new version

