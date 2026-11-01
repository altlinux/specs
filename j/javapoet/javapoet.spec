%define _unpackaged_files_terminate_build 1

Name: javapoet
Version: 1.13.0
Release: alt1

Summary: A Java API for generating .java source files
License: Apache-2.0
Group: Development/Java
Url: https://github.com/square/javapoet
VCS: https://github.com/square/javapoet.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-tests.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(com.google.testing.compile:compile-testing)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.eclipse.jdt:ecj)
BuildRequires: mvn(org.mockito:mockito-core)
%description
A utility class which aids in generating Java source files.

%package javadoc
Group: Development/Java
Summary: Javadoc for JavaPoet

%description javadoc
This package contains javadoc for JavaPoet.

%prep
%setup
%autopatch -p1
%pom_remove_parent
%pom_remove_plugin :maven-checkstyle-plugin
%pom_xpath_remove 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:dependencies'
%pom_xpath_remove 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:compilerId'
%pom_add_dep com.google.code.findbugs:jsr305:3.0.2:test
%mvn_file : javapoet

%build
%mvn_build -s -- -Dmaven.compiler.release=8 -Dmaven.javadoc.source=8

%install
%mvn_install

%files -f .mfiles-javapoet
%doc CHANGELOG.md README.md LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 1.13.0-alt1
- New version.

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.7.0-alt1_12jpp11
- fc34 update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_5jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_4jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_3jpp8
- new version

