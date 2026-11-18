%define _unpackaged_files_terminate_build 1

Name: jakarta-concurrency
Version: 3.1.1
Release: alt1

Summary: Jakarta Concurrency API
License: EPL-2.0 or GPL-2.0 with Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/concurrency/
VCS: https://github.com/jakartaee/concurrency.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(jakarta.interceptor:jakarta.interceptor-api)
BuildRequires: cdi-api-compat4
BuildRequires: mvn(junit:junit)
BuildRequires: asciidoctor

%description
Jakarta Concurrency provides application components with managed executors,
thread factories, scheduling and context propagation. This package contains
the complete API, JPMS and OSGi metadata and the original Maven POMs.

%package javadoc
Summary: API documentation for Jakarta Concurrency
Group: Development/Java

%description javadoc
API documentation for Jakarta Concurrency.

%package manual
Summary: Jakarta Concurrency upstream specification
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
The complete upstream Jakarta Concurrency specification, including its
original diagrams and DRAFT label.

%prep
%setup
# Only the external-container TCK and its distribution need unavailable
# SigTest, Arquillian JUnit5 and ShrinkWrap Resolver providers. Keep all API
# tests, test compilation and every production source and module.
%pom_disable_module tck
%pom_disable_module tck-dist
# Formatting and source cross-reference HTML are not RPM outputs.
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-jxr-plugin api
# XMvn builds independent Javadoc; RPMs have no source-classifier JARs.
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :maven-javadoc-plugin api
# This fixed release already has explicit parent/version properties; keep
# its original POM and let XMvn resolve metadata without a release flattener.
%pom_remove_plugin :flatten-maven-plugin api
# Native Asciidoctor builds complete HTML; the PDF backend is unavailable.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin specification
%pom_remove_plugin :maven-assembly-plugin specification
%mvn_file :jakarta.enterprise.concurrent-api \
    %name/jakarta.enterprise.concurrent-api
%mvn_file :jakarta.enterprise.concurrent.parent \
    %name/jakarta.enterprise.concurrent.parent
%mvn_file :concurrency-spec %name/concurrency-spec

%build
java -version
%mvn_build
asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
    -a revnumber=3.1.1 -a revremark=DRAFT -a status=DRAFT \
    -a imagesdir=images -a idprefix= -a idseparator=- \
    -D target/manual \
    specification/src/main/asciidoc/jakarta-concurrency-spec.adoc

%install
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.adoc

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/jakarta-concurrency-spec.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 3.1.1-alt1
- Initial build for ALT.
