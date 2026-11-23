%define _unpackaged_files_terminate_build 1
%define java_source %name-java-%version

Name: cucumber-tag-expressions
Version: 11.0.1
Release: alt1

Summary: Java parser for Cucumber tag expressions
License: MIT
Group: Development/Java
URL: https://github.com/cucumber/tag-expressions
VCS: https://github.com/cucumber/tag-expressions.git

Source: %java_source.tar
Source1: testdata.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(io.cucumber:cucumber-parent:pom:)
BuildRequires: mvn(com.google.errorprone:error_prone_core)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.assertj:assertj-bom:pom:)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit:junit-bom:pom:)
BuildRequires: mvn(org.yaml:snakeyaml)

%description
A Java parser and evaluator for boolean tag expressions used by Cucumber.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation

%description javadoc
API documentation for the Cucumber tag expression parser.

%prep
%setup -q -c -a 1
cd %java_source
%pom_xpath_set pom:parent/pom:version 5.8.0
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_add_plugin org.apache.maven.plugins:maven-site-plugin:3.12.1
%pom_add_plugin org.apache.maven.plugins:maven-deploy-plugin:3.1.4
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test
%mvn_package :tag-expressions %name

%build
cd %java_source
%mvn_build -s

%install
cd %java_source
%mvn_install

%files -f %java_source/.mfiles-%name
%doc %java_source/LICENSE

%files javadoc -f %java_source/.mfiles-javadoc

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 11.0.1-alt1
- Initial build for ALT.
