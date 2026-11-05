%define _unpackaged_files_terminate_build 1

Name: maven-shared-jarsigner
Version: 3.1.0
Release: alt1

Summary: Maven component for signing and verifying Java archives
License: Apache-2.0
Group: Development/Java
URL: https://maven.apache.org/shared/maven-jarsigner/
VCS: https://github.com/apache/maven-jarsigner.git

Source0: %name-%version.tar
Source1: LICENSE
Source2: NOTICE

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(com.google.inject:guice)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)

%description
Apache Maven Jarsigner is a component which invokes the JDK jarsigner tool
to sign and verify Java archives. It supports dependency injection for use
in Maven plugins and other Java applications.

%javadoc_package

%prep
%setup
cp -p %SOURCE1 %SOURCE2 .
# Keep upstream signed-JAR test fixtures and execute the complete unit suite.
%mvn_file : maven-shared-jarsigner

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-maven-jarsigner
%doc LICENSE NOTICE

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 3.1.0-alt1
- New version.

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_11jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_9jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_3jpp8
- new version
