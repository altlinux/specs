%define _unpackaged_files_terminate_build 1

Name: jakarta-security
Version: 4.0.0
Release: alt1

Summary: Jakarta Security API
License: EPL-2.0 or GPL-2.0 with Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/security/
VCS: https://github.com/jakartaee/security.git
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
BuildRequires: jakarta-servlet
BuildRequires: jakarta-servlet-javax
BuildRequires: mvn(jakarta.interceptor:jakarta.interceptor-api)
BuildRequires: mvn(jakarta.authentication:jakarta.authentication-api)
BuildRequires: mvn(jakarta.authorization:jakarta.authorization-api)
BuildRequires: jakarta-el-api
BuildRequires: jakarta-json-api
BuildRequires: cdi-api-compat4
BuildRequires: mvn(junit:junit)
BuildRequires: asciidoctor

%description
Jakarta Security defines APIs for authentication, identity stores, security
contexts and OpenID Connect. This package contains the complete API, JPMS
and OSGi metadata and original Maven POMs.

%package javadoc
Summary: API documentation for Jakarta Security
Group: Development/Java

%description javadoc
API documentation for Jakarta Security.

%package manual
Summary: Jakarta Security specification and upstream TCK guide
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
The complete specification from the stable API 4.0.0 source tree, preserving
its upstream 4.0.0-SNAPSHOT DRAFT label. The included TCK guide retains its
original upstream Security 3.0 and May 2022 labels.

%prep
%setup
# Keep the complete root API/spec reactor and normal test lifecycle.
# Copyright checking does not generate API classes or legal resources.
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin api
# Fixed upstream release coordinates are resolved by XMvn directly.
%pom_remove_plugin :flatten-maven-plugin api
# Independent XMvn Javadoc replaces the upstream documentation JAR.
%pom_remove_plugin :maven-javadoc-plugin api
# Native Asciidoctor builds complete HTML; the PDF backend is unavailable.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin spec
%pom_remove_plugin :maven-assembly-plugin spec
%mvn_file :jakarta.security.enterprise-api %name/jakarta.security.enterprise-api
%mvn_file :security.enterprise-api-parent %name/security.enterprise-api-parent
%mvn_file :security-spec %name/security-spec

%build
java -version
%mvn_build
asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
    -a revnumber=4.0.0-SNAPSHOT -a revremark=DRAFT -a status=DRAFT \
    -a imagesdir=images -a idprefix= -a idseparator=- \
    -D target/manual spec/src/main/asciidoc/security-spec.adoc

# Strip only JBake front matter; preserve every original guide chapter,
# include and version attribute for standalone native HTML generation.
guide=tck-dist/userguide/src/main/jbake/content
mkdir -p target/tck-guide-src
cp "$guide"/*.inc "$guide"/attributes.conf target/tck-guide-src/
for page in "$guide"/*.adoc; do
    sed '1,/^~~~~~~$/d' "$page" \
        > target/tck-guide-src/$(basename "$page")
done
asciidoctor -b html5 -a data-uri -a toc=left -a sectanchors \
    -D target/tck-guide target/tck-guide-src/*.adoc

%install
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/security-spec.html
%doc target/tck-guide

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 4.0.0-alt1
- Initial build for ALT.
