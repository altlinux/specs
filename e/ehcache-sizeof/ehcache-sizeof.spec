%define _unpackaged_files_terminate_build 1
%define test_jvm %_jvmdir/java-1.8.0-openjdk/bin/java

Name: ehcache-sizeof
Version: 0.4.4
Release: alt1

Summary: Ehcache object graph size measurement engine
License: Apache-2.0
Group: Development/Java
URL: https://github.com/ehcache/sizeof
VCS: https://github.com/ehcache/sizeof.git

Source: %name-%version.tar
Patch0: 0001-Build-the-embedded-agent-with-Ant.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.ow2.asm:asm)

%description
Ehcache object graph size measurement engine.

%javadoc_package

%prep
%setup -q
%autopatch -p1
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
# The upstream SLF4J 1.7 API needs a matching test logging implementation.
%pom_change_dep ch.qos.logback:logback-classic org.slf4j:slf4j-simple:1.7.36
%pom_change_dep junit:junit:4.12 junit:junit:4.13.2
%pom_change_dep org.hamcrest:hamcrest-library:1.3 org.hamcrest:hamcrest:3.0
%pom_change_dep org.ow2.asm:asm:6.0 org.ow2.asm:asm:9.11.1
# Upstream Azure CI used JDK 8 for verify before extraction to shared templates
# (3dfac22). Keep Maven on the system JDK; run unchanged tests in that runtime.
%pom_xpath_inject \
    'pom:plugin[pom:artifactId="maven-surefire-plugin"]/pom:configuration' \
    '<jvm>%test_jvm</jvm>'
%pom_xpath_inject \
    'pom:plugin[pom:artifactId="maven-failsafe-plugin"]' \
    '<configuration><jvm>%test_jvm</jvm></configuration>'

%mvn_package :*::sources: __noinstall

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 0.4.4-alt1
- Initial build for ALT.
