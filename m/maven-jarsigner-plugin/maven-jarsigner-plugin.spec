%define _unpackaged_files_terminate_build 1

Name: maven-jarsigner-plugin
Version: 3.1.0
Release: alt1

Summary: Maven plugin to sign and verify Java archives
License: Apache-2.0
Group: Development/Java
URL: https://maven.apache.org/plugins/maven-jarsigner-plugin/
VCS: https://github.com/apache/maven-jarsigner-plugin.git

Source0: %name-%version.tar
Source1: LICENSE
Source2: NOTICE

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-settings)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires: mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires: mvn(org.apache.maven.shared:maven-jarsigner)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)

%description
This Maven plugin signs or verifies a project artifact and its attachments
using the JDK jarsigner tool. It supports signature verification, archive
selection and timestamp authority configuration.

%javadoc_package

%prep
%setup
cp -p %SOURCE1 %SOURCE2 .
%mvn_file : maven-jarsigner-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-maven-jarsigner-plugin
%doc LICENSE NOTICE

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 3.1.0-alt1
- New version.

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_10jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_8jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- complete build

