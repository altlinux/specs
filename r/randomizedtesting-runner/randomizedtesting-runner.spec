%define _unpackaged_files_terminate_build 1

Name: randomizedtesting-runner
Version: 2.9.2
Release: alt1
Summary: JUnit runner for reproducible randomized tests
License: Apache-2.0
Group: Development/Java
URL: https://github.com/randomizedtesting/randomizedtesting
VCS: https://github.com/randomizedtesting/randomizedtesting.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(de.thetaphi:forbiddenapis)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(com.carrotsearch.thirdparty:simple-xml-safe)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.dom4j:dom4j)
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)

%description
RandomizedTesting provides a JUnit runner with reproducible random seeds,
thread leak detection and test execution controls. This package contains
the runner, Ant task and Maven plugin with their genuine Maven metadata.

%package -n randomizedtesting-ant
Summary: Ant integration for RandomizedTesting
Group: Development/Java

%description -n randomizedtesting-ant
Ant task for running reproducible randomized JUnit tests.

%package -n randomizedtesting-maven-plugin
Summary: Maven integration for RandomizedTesting
Group: Development/Java

%description -n randomizedtesting-maven-plugin
Maven plugin for running reproducible randomized JUnit tests.

%javadoc_package

%prep
%setup
%autopatch -p1
%pom_disable_module examples/maven
%pom_disable_module examples/ant
%pom_disable_module examples/security-manager
# Site descriptor attachments are not needed for the runner API package.
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
# XMvn generates the packaged API documentation.
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin randomized-runner
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin junit4-ant
# Use ordinary system dependencies instead of an obfuscated fat JAR.
%pom_remove_plugin com.pyx4me:proguard-maven-plugin junit4-ant
%pom_xpath_remove "//pom:includeGroupIds" junit4-ant
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin junit4-ant
%pom_xpath_set "pom:dependencies/pom:dependency/pom:scope" compile junit4-ant

%mvn_package :randomizedtesting-parent randomizedtesting-runner
%mvn_package :randomizedtesting-runner randomizedtesting-runner
%mvn_package :junit4-ant ant
%mvn_package :junit4-maven-plugin maven-plugin
%mvn_package :junit4-maven-plugin-tests __noinstall
%mvn_file :randomizedtesting-runner randomizedtesting-runner

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-randomizedtesting-runner
%doc LICENSE.txt CHANGES.txt

%files -n randomizedtesting-ant -f .mfiles-ant

%files -n randomizedtesting-maven-plugin -f .mfiles-maven-plugin

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 2.9.2-alt1
- Initial build for ALT.
