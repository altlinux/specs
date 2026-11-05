%define _unpackaged_files_terminate_build 1

Name: atinject
Version: 2.0.1
Release: alt2

Summary: Dependency injection specification for Java (JSR-330)
License: Apache-2.0
Group: Development/Java
URL: https://github.com/jakartaee/inject
VCS: https://github.com/jakartaee/inject.git
BuildArch: noarch

Source0: atinject-%version.tar
Patch0: atinject-%version-alt-patch.patch
Source1: injection-api-1.0.5.tar.gz
Source2: javax-inject-1.tar.gz
Source3: jakarta-inject-tck-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: rpm-build-java-osgi
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: junit
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: maven-plugin-bundle

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%package javax
Summary: Original javax.inject 1 dependency injection API
Group: Development/Java

%description javax
The original JSR-330 release 1 API in the javax.inject namespace.
It provides the genuine javax.inject:javax.inject:1 Maven artifact.

%package tck
Summary: Jakarta Dependency Injection compatibility test kit
Group: Development/Java

%description tck
The complete Jakarta Dependency Injection 2.0.1 compatibility test kit.
An injector implementation supplies the object graph to the genuine TCK.

%{?javadoc_package}

%prep
%setup -a1 -a2 -a3
%autopatch -p1

%pom_remove_parent
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file jakarta.inject:jakarta.inject-api atinject jakarta.inject-api
%mvn_file javax.inject:javax.inject javax.inject
%mvn_package javax.inject:javax.inject javax
%mvn_compat_version javax.inject:javax.inject 1 ""
%mvn_file jakarta.inject:jakarta.inject-tck jakarta.inject-tck
%mvn_package jakarta.inject:jakarta.inject-tck tck

%build
%mvn_build

# Compile the complete original API and TCK with system JUnit.
pushd javax-inject-1
mkdir -p build/classes build/tck/classes
find src -name '*.java' -print > build/api-sources
javac -g --release 8 -d build/classes @build/api-sources
find tck -name '*.java' -print > build/tck-sources
javac -g --release 8 -cp build/classes:%_javadir/junit.jar \
    -d build/tck/classes @build/tck-sources
jar cf build/javax.inject.jar -C build/classes .
popd
%mvn_artifact javax-inject-1/pom.xml \
    javax-inject-1/build/javax.inject.jar

# Build all genuine TCK classes against the API built above and system JUnit.
pushd jakarta-inject-tck-%version
mkdir -p target/classes
find src/main/java -name '*.java' -print > target/sources
javac -g --release 8 -cp ../target/classes:%_javadir/junit.jar \
    -d target/classes @target/sources
jar cf target/jakarta.inject-tck.jar -C target/classes .
popd
%mvn_artifact jakarta-inject-tck-%version/pom.xml \
    jakarta-inject-tck-%version/target/jakarta.inject-tck.jar

%install
%mvn_install

%files -n %name -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.md

%files javax -f .mfiles-javax

%files tck -f .mfiles-tck

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 2.0.1-alt2
- Build genuine javax.inject 1 and Jakarta Inject TCK artifacts.

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

