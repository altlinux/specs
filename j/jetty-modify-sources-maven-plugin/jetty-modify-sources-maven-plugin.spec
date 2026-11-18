%define _unpackaged_files_terminate_build 1

Name: jetty-modify-sources-maven-plugin
Version: 1.0.15
Release: alt1

Summary: Maven source and resource transformation plugin for Jetty
License: Apache-2.0 or EPL-2.0
Group: Development/Java
URL: https://github.com/jetty-project/jetty-modify-sources-maven-plugin
VCS: https://github.com/jetty-project/jetty-modify-sources-maven-plugin.git

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: jetty-parent
BuildRequires: maven-filtering
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-testing
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire-provider-testng
BuildRequires: mvn(com.github.javaparser:javaparser-core)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.commons:commons-text)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.apache.groovy:groovy)

%description
Maven plugin used by Jetty to transform Jakarta EE source, service-loader
files and resources into the Java EE 8 javax namespace. Includes the resource
filters used for configuration and module files.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the Jetty source and resource transformation plugin.

%prep
%setup
sed -n '1,/^$/p' \
    src/main/java/org/eclipse/jetty/toolchain/modifysources/ModFilesFiltering.java \
    > LICENSE

%build
%mvn_build -- -Dmaven.source.skip=true \
    -Dinvoker.mavenExecutable=/usr/bin/xmvn -Dinvoker.offline=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 1.0.15-alt1
- Initial build for ALT.
