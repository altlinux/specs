%define _unpackaged_files_terminate_build 1

Name: airline
Version: 0.9
Release: alt1

Summary: Annotation-based command line parser for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/airlift/airline
VCS: https://github.com/airlift/airline.git

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire-provider-testng
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.assertj:assertj-core)

%description
Airline provides annotation-based parsing, command groups, option conversion
and generated usage text for Java command line applications.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for Airline.

%prep
%setup
# Replace unavailable build-only parent with explicit original coordinates.
%pom_remove_parent
%pom_xpath_inject pom:project '<groupId>io.airlift</groupId>'
%pom_xpath_inject pom:properties '<maven.compiler.source>8</maven.compiler.source><maven.compiler.target>8</maven.compiler.target>'
%pom_xpath_inject 'pom:dependencies/pom:dependency[pom:artifactId="javax.inject"]' '<version>1</version>'
%pom_xpath_inject 'pom:dependencies/pom:dependency[pom:artifactId="jsr305"]' '<version>3.0.2</version>'
%pom_xpath_inject 'pom:dependencies/pom:dependency[pom:artifactId="guava"]' '<version>33.8.0-jre</version>'
%pom_xpath_inject 'pom:dependencies/pom:dependency[pom:artifactId="testng"]' '<version>7.8.0</version>'
%pom_xpath_inject 'pom:dependencies/pom:dependency[pom:artifactId="assertj-core"]' '<version>3.27.3</version>'

%build
%mvn_build

%install
%mvn_install
rm -f %buildroot%_javadocdir/%name/args

%files -f .mfiles
%doc license.txt notice.md

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 0.9-alt1
- Initial build for ALT.
