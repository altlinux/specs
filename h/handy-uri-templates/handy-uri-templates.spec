%define _unpackaged_files_terminate_build 1

Name: handy-uri-templates
Version: 2.1.8
Release: alt1

Summary: RFC 6570 URI template processor for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/damnhandy/Handy-URI-Templates
VCS: https://github.com/damnhandy/Handy-URI-Templates.git
Source0: %name-%version.tar
Patch0: handy-uri-templates-java21-collections.patch
Source1: handy-uri-templates-tests-520fdd8.tar.xz

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(junit:junit)

%description
Handy URI Templates is an RFC 6570 compliant URI template processor for
Java. It provides a fluent API, custom variable renderers, and support for
every level of URI templates.

%prep
%setup -q -a 1
%patch0 -p1
%pom_remove_parent
%pom_xpath_replace '*[local-name()="packaging"]' '<packaging>jar</packaging>'
compiler='pom:project/pom:build/pom:plugins/pom:plugin'
compiler="$compiler[pom:artifactId='maven-compiler-plugin']/pom:configuration"
%pom_xpath_set "$compiler/pom:source" 8
%pom_xpath_set "$compiler/pom:target" 8
%pom_change_dep \
    com.fasterxml.jackson.core:jackson-core \
    com.fasterxml.jackson.core:jackson-core:2.22.1
%pom_change_dep \
    com.fasterxml.jackson.core:jackson-databind \
    com.fasterxml.jackson.core:jackson-databind:2.22.1
%pom_change_dep \
    com.fasterxml.jackson.core:jackson-annotations \
    com.fasterxml.jackson.core:jackson-annotations:2.23
%pom_change_dep joda-time:joda-time joda-time:joda-time:2.14.0
%pom_change_dep junit:junit junit:junit:4.13.2
%pom_remove_dep com.ning:async-http-client
%pom_remove_dep org.apache.httpcomponents:httpclient
%pom_xpath_remove '*[local-name()="build"]/*[local-name()="extensions"]'
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin pl.project13.maven:git-commit-id-plugin
%pom_remove_plugin com.rimerosolutions.maven.plugins:wrapper-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-doap-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin
%pom_remove_plugin org.codehaus.mojo:exec-maven-plugin
%pom_remove_plugin org.apache.felix:maven-bundle-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin
# Examples use the asynchronous HTTP client to call live services.
rm -rf src/test/java/com/damnhandy/uri/template/examples

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-handy-uri-templates
%doc LICENSE.txt

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.1.8-alt1
- Initial build for ALT.
