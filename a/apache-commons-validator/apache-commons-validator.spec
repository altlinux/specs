%define _unpackaged_files_terminate_build 1

Name: apache-commons-validator
Epoch: 1
Version: 1.11.0
Release: alt1

Summary: Apache Commons Validator
License: Apache-2.0
Group: Development/Java
URL: https://commons.apache.org/proper/commons-validator/
VCS: https://github.com/apache/commons-validator.git
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-digester:commons-digester)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(org.apache.commons:commons-csv)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit-pioneer:junit-pioneer)
BuildRequires: mvn(org.apache.commons:commons-lang3)

%description
Apache Commons Validator provides reusable validation components for Java
applications.

%prep
%setup -q
%pom_xpath_set pom:project/pom:parent/pom:version 107
%pom_change_dep \
    org.apache.commons:commons-lang3:3.20.0 \
    org.apache.commons:commons-lang3:3.21.0
# The startup test requires JUnit CLPTR to spawn a JVM.
%pom_remove_dep org.bitstrings.test:junit-clptr
routines=src/test/java/org/apache/commons/validator/routines
rm -f "$routines/DomainValidatorStartupTest.java"

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-commons-validator
%doc LICENSE.txt NOTICE.txt README.md

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1:1.11.0-alt1
- Initial build for ALT.
- Preserve the RPM epoch from p10.
