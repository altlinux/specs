%define _unpackaged_files_terminate_build 1

Name: jakarta-authorization
Version: 3.0.0
Release: alt1

Summary: Jakarta Authorization API
License: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/authorization/
VCS: https://github.com/jakartaee/authorization.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: jakarta-servlet
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: asciidoctor

%description
Jakarta Authorization defines a low-level SPI for authorization modules
and permissions for Jakarta Servlet and Enterprise Beans containers.
This package contains the complete API, JPMS and OSGi metadata, and the
original API, specification and parent Maven POMs.

%package javadoc
Summary: API documentation for Jakarta Authorization
Group: Development/Java

%description javadoc
API documentation for Jakarta Authorization.

%package manual
Summary: Jakarta Authorization specification and TCK user guide
License: Eclipse Foundation Specification License v1.1 AND EPL-2.0
Group: Documentation

%description manual
The complete Jakarta Authorization specification and TCK user's guide
in HTML format.

%prep
%setup
# RPM output has no sources.jar; Javadoc is built independently by XMvn.
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :maven-javadoc-plugin api
# Central publication flattening is unnecessary for genuine XMvn POMs.
%pom_remove_plugin org.codehaus.mojo:flatten-maven-plugin api
# Keep the spec module and POM. Native Asciidoctor builds complete HTML;
# the unavailable PDF backend and its document ZIP are not RPM outputs.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin spec
%pom_remove_plugin :maven-assembly-plugin spec
%mvn_file :jakarta.authorization-api %name/jakarta.authorization-api

%build
java -version
%mvn_build
asciidoctor -b html5 -d book -a data-uri -a toc=left -a sectanchors \
    -a revnumber=3.0 -a revdate=2024-05-13 -a revremark= \
    -a idprefix= -a idseparator=- \
    -D target/manual spec/src/main/asciidoc/authorization-spec.adoc
# The guide is ordinary AsciiDoc preceded by JBake page metadata.
mkdir -p target/tck-guide-src target/tck-userguide
cp -a tck-dist/userguide/src/main/jbake/content/. target/tck-guide-src/
cp -a tck-dist/userguide/src/main/jbake/assets/img target/tck-guide-src/
for page in target/tck-guide-src/*.adoc; do
    sed -i '1,/^~~~~~~$/d' "$page"
done
asciidoctor -b html5 -a data-uri -a compat-mode -a toc=left \
    -D target/tck-userguide target/tck-guide-src/*.adoc

%install
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/authorization-spec.html
%doc target/tck-userguide

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 3.0.0-alt1
- Initial build for ALT.
