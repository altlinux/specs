%define _unpackaged_files_terminate_build 1

Name: jakarta-resource-api
Version: 2.1.0
Release: alt1

Summary: Jakarta Connectors API
License: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/connectors/
VCS: https://github.com/jakartaee/connectors.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(jakarta.transaction:jakarta.transaction-api)
BuildRequires: cdi-api-compat4
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: asciidoctor

%description
Jakarta Connectors defines a standard architecture for Jakarta EE
application components to connect to Enterprise Information Systems.
This package contains the complete Connectors API and its parent POM.

%package javadoc
Summary: API documentation for Jakarta Connectors
License: Eclipse Foundation Specification License v1.0
Group: Development/Java

%description javadoc
API documentation for Jakarta Connectors.

%package manual
Summary: Jakarta Connectors specification
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
The complete upstream Jakarta Connectors specification in HTML format.

%prep
%setup
%mvn_file :jakarta.resource-api %name/jakarta.resource-api

%build
java -version
%mvn_build
# The spec is outside the upstream Maven reactor. Use native Asciidoctor
# for its complete HTML output; the Maven/PDF providers are unavailable.
asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
    -a revnumber=2.1 -a revdate=2022-04-21 -a revremark= \
    -a idprefix= -a idseparator=- \
    -D target/manual spec/src/main/asciidoc/jakarta-connectors-spec.adoc

%install
# Generated Javadoc source links and compiler arguments are build inputs.
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/jakarta-connectors-spec.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
