%define _unpackaged_files_terminate_build 1

Name: jetty-version-maven-plugin
Version: 2.7
Release: alt1

Summary: Version and release management plugin for Jetty
License: EPL-1.0 or Apache-2.0
Group: Development/Java
URL: https://www.eclipse.org/jetty/
VCS: https://github.com/jetty-project/jetty-version-maven-plugin.git

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit5
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.commons:commons-text)
BuildRequires: github-api
BuildRequires: mvn(com.squareup.okhttp3:okhttp)
BuildRequires: mvn(com.squareup.okio:okio-jvm)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-test-helper)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.hamcrest:hamcrest)

%description
Maven plugin for Jetty version text generation, release information, Git tags
and release staging, including the GitHub issue resolver.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the Jetty version management Maven plugin.

%prep
%setup
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_xpath_set pom:properties/pom:github-api.version 1.330
%pom_xpath_set pom:properties/pom:okhttp3.version 5.5.1
%pom_remove_dep com.squareup.okhttp3:okhttp-urlconnection
%pom_remove_dep com.squareup.okhttp:okhttp-urlconnection
%pom_xpath_set pom:properties/pom:okio.version 3.18.2
%pom_xpath_set 'pom:dependencies/pom:dependency[pom:artifactId="okio"]/pom:artifactId' okio-jvm

%build
%mvn_build -- --fail-at-end

%install
%mvn_install
rm -f %buildroot%_javadocdir/%name/args

%files -f .mfiles
%doc LICENSE-eplv10-aslv20.html README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 17 2026 Ivan Khanas <xeno@altlinux.org> 2.7-alt1
- Initial build for ALT.
