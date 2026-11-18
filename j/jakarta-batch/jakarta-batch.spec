%define _unpackaged_files_terminate_build 1

Name: jakarta-batch
Version: 2.1.1
Release: alt1

Summary: Jakarta Batch API
License: Apache-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/batch/
VCS: https://github.com/jakartaee/batch.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: cdi-api-compat4
BuildRequires: asciidoctor

%description
Jakarta Batch defines the Java programming model, job specification language
and runtime interfaces for batch processing. This package contains the
complete API, XML schemas, JPMS and OSGi metadata and all original Maven POMs.

%package javadoc
Summary: API documentation for Jakarta Batch
Group: Development/Java

%description javadoc
API documentation for Jakarta Batch.

%package manual
Summary: Jakarta Batch upstream specification draft
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
The complete specification included in the upstream API 2.1.1 source tree.
Upstream marks this document as version 2.2 DRAFT.

%prep
%setup
# Bind the provided CDI API to the genuine versioned CDI 4.1 output.
%pom_xpath_set \
    pom:properties/pom:version.jakarta.enterprise.jakarta.enterprise.cdi-api \
    4.1.0
# RPM output has no sources.jar; Javadoc is built independently by XMvn.
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :maven-javadoc-plugin api
# Keep the spec module and POM; native Asciidoctor builds complete HTML.
# The unavailable PDF backend and its document ZIP are not RPM outputs.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin spec
%pom_remove_plugin :maven-assembly-plugin spec
%mvn_file :jakarta.batch-api %name/jakarta.batch-api

%build
java -version
%mvn_build
# Preserve the upstream 2.2 DRAFT label from this stable API source tag.
asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
    -a revnumber=2.2 -a revremark=DRAFT -a imagesdir=images \
    -a idprefix= -a idseparator=- \
    -D target/manual spec/src/main/asciidoc/jakarta-batch-spec.adoc

%install
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/jakarta-batch-spec.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 2.1.1-alt1
- Initial build for ALT.
