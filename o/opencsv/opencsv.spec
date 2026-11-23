%define _unpackaged_files_terminate_build 1
%define _without_javadoc 1

Name: opencsv
Version: 5.12.0
Release: alt1

Summary: Easy-to-use CSV parser library for Java
License: Apache-2.0
Group: Development/Java
URL: https://opencsv.sourceforge.net/
VCS: https://git.code.sf.net/p/opencsv/source

Source: %name-%version.tar
Patch0: 0001-Use-the-current-Mockito-matchers.patch
Patch1: 0002-Accept-the-numeric-daylight-time-name-in-German-CSV-tests.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.commons:commons-text)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(org.apache.commons:commons-collections4)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires: mvn(org.apache.groovy:groovy)
BuildRequires: mvn(org.spockframework:spock-core)
BuildRequires: mvn(cglib:cglib-nodep)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.vintage:junit-vintage-engine)

%description
OpenCSV is an easy-to-use CSV parser library for Java applications.

%prep
%setup -q
%autopatch -p1
%pom_xpath_set pom:properties/pom:dep.plugin.maven-surefire.version 3.5.6
%pom_xpath_set pom:properties/pom:dep.plugin.jacoco.version 0.8.14
%pom_xpath_set pom:properties/pom:dep.plugin.maven-jar.version 3.2.2
%pom_xpath_set pom:properties/pom:dep.plugin.maven-compiler.version 3.14.0
%pom_xpath_set pom:properties/pom:dep.commons-lang3.version 3.21.0
%pom_xpath_set pom:properties/pom:dep.commons-collections4.version 4.6.0
%pom_xpath_set pom:properties/pom:dep.junit.version 5.14.4
%pom_xpath_set pom:properties/pom:dep.junit.platform.version 1.14.4
%pom_xpath_set pom:properties/pom:dep.commons-text.version 1.15.0
%pom_xpath_set pom:properties/pom:dep.mockito.core.version 5.24.0
%pom_xpath_set pom:properties/pom:dep.plugin.gmavenplus.version 5.1.0
%pom_xpath_set pom:properties/pom:dep.groovy.version 6.0.0
%pom_xpath_set pom:properties/pom:dep.spock.core.version 2.5-groovy-6.0
%pom_xpath_set \
    'pom:plugin[pom:artifactId="gmavenplus-plugin"]//pom:dependency/pom:groupId' \
    org.apache.groovy
%pom_xpath_inject \
    'pom:plugin[pom:artifactId="gmavenplus-plugin"]/pom:configuration' \
    '<targetBytecode>17</targetBytecode>'
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

%build
# Upstream documents exception-count discrepancies on high-core systems.
JAVA_TOOL_OPTIONS='-XX:ActiveProcessorCount=4' %mvn_build -s

%install
%mvn_install

%files -f .mfiles-opencsv
%doc LICENSE NOTICE_Modifications

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 5.12.0-alt1
- Initial build for ALT.
