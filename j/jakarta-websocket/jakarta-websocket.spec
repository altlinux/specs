%define _unpackaged_files_terminate_build 1

Name: jakarta-websocket
Version: 2.2.0
Release: alt1

Summary: Jakarta WebSocket client and server APIs
License: EPL-2.0 or GPL-2.0 with Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/websocket/
VCS: https://github.com/jakartaee/websocket.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: asciidoctor

%description
Jakarta WebSocket defines the API for WebSocket applications. This package
contains both complete client and server APIs, their JPMS and OSGi metadata
and the original Maven POMs.


%package client-api
Summary: Jakarta WebSocket client API
Group: Development/Java

%description client-api
Jakarta WebSocket client API.

%package javadoc
Summary: API documentation for Jakarta WebSocket
Group: Development/Java

%description javadoc
API documentation for Jakarta WebSocket.

%package manual
Summary: Jakarta WebSocket upstream specification
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
The complete upstream Jakarta WebSocket specification included in the
stable 2.2.0 API source tree. Its upstream DRAFT label is preserved.

%prep
%setup
# RPM outputs have no sources.jar; XMvn builds Javadoc independently.
for module in api api/client api/server; do
    %pom_remove_plugin :maven-source-plugin "$module"
    %pom_remove_plugin :maven-javadoc-plugin "$module"
    # This unbound copyright checker is not part of API generation.
    %pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin "$module"
done
# Preserve the specification POM and build its HTML with native Asciidoctor.
# The unavailable PDF backend and its document ZIP are not RPM outputs.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin spec
%pom_remove_plugin :maven-assembly-plugin spec
%mvn_package :jakarta.websocket-client-api client-api
%mvn_package :jakarta.websocket-api
%mvn_package :jakarta.websocket-all
%mvn_package :websocket-parent
%mvn_package :websocket-spec manual
%mvn_file :jakarta.websocket-client-api %name/jakarta.websocket-client-api
%mvn_file :jakarta.websocket-api %name/jakarta.websocket-api
%mvn_file :jakarta.websocket-all %name/jakarta.websocket-all
%mvn_file :websocket-parent %name/websocket-parent
%mvn_file :websocket-spec %name/websocket-spec

%build
java -version
%mvn_build -s
asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
    -a revnumber=2.2 -a revremark=DRAFT -a status=DRAFT \
    -a idprefix= -a idseparator=- \
    -D target/manual spec/src/main/asciidoc/websocket-spec.adoc

%install
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files client-api -f .mfiles-client-api

%files javadoc -f .mfiles-javadoc

%files manual -f .mfiles-manual
%doc target/manual/websocket-spec.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 2.2.0-alt1
- Initial build for ALT.
