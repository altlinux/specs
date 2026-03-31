%define _unpackaged_files_terminate_build 1

Name: atinject
Version: 2.0.1
Release: alt1

Summary: Dependency injection specification for Java (JSR-330)
License: Apache-2.0
Group: Development/Java
Url: https://github.com/eclipse-ee4j/injection-api
BuildArch: noarch

Source0: atinject-%version.tar
Patch0: atinject-%version-alt-patch.patch
Source1: injection-api-1.0.5.tar.gz

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-plugin-bundle

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%{?javadoc_package}

%prep
%setup -a1
%autopatch -p1

%pom_remove_parent
%pom_remove_plugin :maven-javadoc-plugin

%mvn_alias : javax.inject:javax.inject jakarta.inject:jakarta.inject-api:1.0.5

%mvn_file : atinject jakarta.inject-api

%build
%mvn_build

%install
%mvn_install

%files -n %name -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.md

%changelog
* Tue Mar 24 2026 Ivan Khanas <xeno@altlinux.org> 2.0.1-alt1
- Upgrade to 2.0.1 with dual javax.inject + jakarta.inject support.

* Tue Oct 21 2025 Ivan Khanas <xeno@altlinux.org> 0:1.0.5-alt2
- Create jakarta.inject-api symlink.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.0.5-alt1_3jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:1.0.3-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1-alt7_35.20100611svn86jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_32.20100611svn86jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_30.20100611svn86jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_29.20100611svn86jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_28.20100611svn86jpp8
- java fc28+ update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_27.20100611svn86jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_25.20100611svn86jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_24.20100611svn86jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_22.20100611svn86jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt7_21.20100611svn86jpp8
- added osgi provides

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt6_21.20100611svn86jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_13.20100611svn86jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_10.20100611svn86jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_8.20100611svn86jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt4_6.20100611svn86jpp7
- fc release

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt3_8jpp6
- added fc compat symlink %{_javadir}/atinject.jar

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt2_8jpp6
- target 5 build

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_8jpp6
- new jpp relase

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_2.20100611svn86jpp6
- fixed build

