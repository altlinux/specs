%define _unpackaged_files_terminate_build 1

Name: jakarta-ejb
Version: 4.0.1
Release: alt1

Summary: Jakarta Enterprise Beans API and specifications
License: EPL-2.0 or GPL-2.0 with Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/enterprise-beans/
VCS: https://github.com/jakartaee/enterprise-beans.git
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
BuildRequires: mvn(jakarta.transaction:jakarta.transaction-api)
# Keep the genuine CDI4 provider selected through Transactions metadata.
BuildRequires: cdi-api-compat4
BuildRequires: asciidoctor

%description
Jakarta Enterprise Beans defines the architecture and API for component-based
business applications. This package contains the complete API, JPMS and OSGi
metadata, and the original upstream Maven POMs.

%package javadoc
Summary: API documentation for Jakarta Enterprise Beans
Group: Development/Java

%description javadoc
API documentation for Jakarta Enterprise Beans.

%package manual
Summary: Jakarta Enterprise Beans core and optional specifications
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
Complete core and optional feature specifications from the stable API 4.0.1
source tree, with their original upstream 4.0 DRAFT labels preserved.

%prep
%setup
# Build the complete API and both specification documents. XMvn builds
# independent Javadoc; RPM output has no source-classifier JARs.
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin api
# Native Asciidoctor replaces the HTML/PDF distribution assembly.
# The unavailable PDF backend is not an RPM output.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin spec
%pom_remove_plugin :maven-assembly-plugin spec
%pom_remove_plugin :maven-assembly-plugin
%mvn_file :jakarta.ejb-api %name/jakarta.ejb-api
%mvn_file :jakarta.ejb-parent %name/jakarta.ejb-parent
%mvn_file :jakarta.ejb-spec %name/jakarta.ejb-spec

%build
java -version
%mvn_build
for part in core opt; do
    asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
        -a revnumber=4.0 -a revremark=DRAFT -a status=DRAFT \
        -a imagesdir=images -a idprefix= -a idseparator=- \
        -D target/manual \
        spec/src/main/asciidoc/enterprise-beans-spec-$part.adoc
done

%install
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/enterprise-beans-spec-core.html
%doc target/manual/enterprise-beans-spec-opt.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 4.0.1-alt1
- Initial build for ALT.
