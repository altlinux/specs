%define _unpackaged_files_terminate_build 1

Name: streamex
Version: 0.9.0
Release: alt1

Summary: Enhancing Java 8 Streams
License: Apache-2.0
Group: Development/Java
URL: https://github.com/amaembo/streamex
VCS: https://github.com/amaembo/streamex

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)

BuildArch: noarch

%description
StreamEx is an enhancement library for Java streams, adding convenient
operations while preserving compatibility with the Java 8 Stream API.

%package javadoc
Summary: API documentation for StreamEx
Group: Development/Documentation

%description javadoc
API documentation for the StreamEx Java library.

%prep
%setup -q
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.eluder.coveralls:coveralls-maven-plugin
%pom_remove_plugin org.jreleaser:jreleaser-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_xpath_replace \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.apache.maven.plugins'] and *[local-name()='artifactId' and text()='maven-enforcer-plugin']]/*[local-name()='executions']/*[local-name()='execution'][*[local-name()='goals']/*[local-name()='goal' and text()='enforce']]" \
    "<execution><id>enforce-java</id><phase>validate</phase><goals><goal>enforce</goal></goals><configuration><rules><requireJavaVersion><version>17</version></requireJavaVersion></rules></configuration></execution>"
%pom_xpath_set \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.apache.maven.plugins'] and *[local-name()='artifactId' and text()='maven-enforcer-plugin']]/*[local-name()='version']" \
    3.5.0
%pom_xpath_set \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.codehaus.mojo'] and *[local-name()='artifactId' and text()='build-helper-maven-plugin']]/*[local-name()='version']" \
    3.6.1
%pom_xpath_set \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.apache.maven.plugins'] and *[local-name()='artifactId' and text()='maven-compiler-plugin']]/*[local-name()='version']" \
    3.14.0
%pom_xpath_set \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.apache.maven.plugins'] and *[local-name()='artifactId' and text()='maven-javadoc-plugin']]/*[local-name()='version']" \
    3.12.0
%pom_xpath_set \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.apache.maven.plugins'] and *[local-name()='artifactId' and text()='maven-source-plugin']]/*[local-name()='version']" \
    3.2.1
%pom_xpath_set \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.apache.maven.plugins'] and *[local-name()='artifactId' and text()='maven-jar-plugin']]/*[local-name()='version']" \
    3.2.2
%pom_xpath_set \
    "//*[local-name()='plugin'][*[local-name()='groupId' and text()='org.apache.maven.plugins'] and *[local-name()='artifactId' and text()='maven-surefire-plugin']]/*[local-name()='version']" \
    3.5.6
%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
