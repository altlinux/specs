%define _unpackaged_files_terminate_build 1

Name: jakarta-data
Version: 1.0.2
Release: alt1

Summary: Jakarta Data API
License: Apache-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/data/
VCS: https://github.com/jakartaee/data.git
BuildArch: noarch

Source: %name-%version.tar
# Original HTML from the official upstream TCK distribution.
Source1: data-tck-reference-guide-%version.html

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(org.junit:junit-bom:pom:)
BuildRequires: junit5
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: asciidoctor

%description
Jakarta Data standardizes repository interfaces and data access APIs.
This package contains the complete API with JPMS and OSGi metadata and
original Maven coordinates.

%package javadoc
Summary: API documentation for Jakarta Data
Group: Development/Java

%description javadoc
API documentation for Jakarta Data.

%package manual
Summary: Jakarta Data specifications and TCK reference guide
License: Eclipse Foundation Specification License v1.0 and Eclipse Foundation Technology Compatibility Kit License
Group: Documentation

%description manual
The complete Jakarta Data specification, Query by Method Name Extension,
and original TCK reference guide in HTML. Upstream version labels are kept.

%prep
%setup
# Separate container TCK needs unavailable Arquillian, SigTest and NoSQL
# providers. Keep the full API, its ordinary tests and spec reactor.
%pom_disable_module tck
%pom_disable_module tck-dist
%pom_remove_dep org.jboss.arquillian:arquillian-bom
%pom_remove_dep org.jboss.arquillian.jakarta:arquillian-jakarta-bom
%pom_remove_dep org.jboss.shrinkwrap:shrinkwrap-bom
%pom_remove_dep org.jboss.shrinkwrap.resolver:shrinkwrap-resolver-bom
# Formatting, release-only sources and optional CI mutation checks.
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin org.apache.rat:apache-rat-plugin
%pom_remove_plugin org.pitest:pitest-maven
%pom_remove_plugin :maven-source-plugin
# Independent XMvn Javadoc preserves API documentation without a JAR.
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin api
# Native Asciidoctor preserves complete HTML; PDF backend is unavailable.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin spec
%mvn_file :jakarta.data-api %name/jakarta.data-api
%mvn_file :jakarta.data-parent %name/jakarta.data-parent
%mvn_file :jakarta.data-spec %name/jakarta.data-spec

%build
java -version
%mvn_build
asciidoctor -b html5 -d book -a data-uri -a revnumber=1.0 \
    -a revremark=Draft -a source-highlighter! \
    -D target/manual spec/src/main/asciidoc/jakarta-data.adoc \
    spec/src/main/asciidoc/method-query.asciidoc
# The guide generator requires a compiled container TCK. Use the genuine
# released versioned HTML, including its original generated tables.
cp -p %SOURCE1 target/manual/data-tck-reference-guide-%version.html

%install
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.adoc

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/*.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
