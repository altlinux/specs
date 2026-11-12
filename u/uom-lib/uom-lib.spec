%define _unpackaged_files_terminate_build 1

Name: uom-lib
Version: 2.2
Release: alt1

Summary: Common libraries for Units of Measurement
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/unitsofmeasurement/uom-lib
VCS: https://github.com/unitsofmeasurement/uom-lib.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(tech.uom:uom-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: mvn(javax.measure:unit-api)
BuildRequires: mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)

%description
The original common utilities and parent POM from the complete upstream
uom-lib source distribution. Other modules remain in the source archive.

%package common
Summary: Units of Measurement common Java utilities
Group: Development/Java

%description common
The complete original common module of the Units of Measurement libraries.

%prep
%setup
%pom_xpath_inject pom:project "<version>%version</version>"
%pom_set_parent tech.uom:uom-parent:2.2.5
# Align the released reactor parent in all retained modules.
%pom_set_parent tech.uom.lib:uom-lib:%version assertj jackson yasson
# Preserve the genuine parent build model, not XMvn's reduced system model.
install -D -m 644 %_mavenpomdir/uom-parent/uom-parent.pom .parent/pom.xml
%pom_xpath_inject pom:parent "<relativePath>.parent/pom.xml</relativePath>"
# The complete common API bootstraps Indriya, needed by other modules.
# The common tests use JUnit assertions; no hamcrest-junit API is used.
%pom_remove_dep org.hamcrest:hamcrest-junit common
# The unused JUnit4 bridge prevents Surefire from selecting Jupiter.
%pom_remove_dep org.junit.platform:junit-platform-runner common
# Retain the original JUnit4 assertion helper without the runner bridge.
%pom_add_dep junit:junit:4.13.2:test common
%mvn_package :::sources: __noinstall
%mvn_package tech.uom.lib:uom-lib-common common

%build
%mvn_build -j -- -Dmaven.javadoc.skip=true -DfailIfNoTests=true -pl common -am

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files common -f .mfiles-common

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 2.2-alt1
- Initial build for ALT.
