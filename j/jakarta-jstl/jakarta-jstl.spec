%define _unpackaged_files_terminate_build 1

Name: jakarta-jstl
Version: 3.0.2
Release: alt1

Summary: Jakarta Standard Tag Library
License: (EPL-2.0 or GPL-2.0 with Classpath-exception-2.0) and BSD-3-Clause
Group: Development/Java
URL: https://jakarta.ee/specifications/tags/
VCS: https://github.com/jakartaee/tags.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: jakarta-servlet
BuildRequires: jakarta-servlet-javax
BuildRequires: jakarta-server-pages-api
BuildRequires: mvn(jakarta.el:jakarta.el-api)
BuildRequires: mvn(xalan:xalan)
BuildRequires: junit5
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: asciidoctor

%description
Complete Jakarta Standard Tag Library API with JPMS and OSGi metadata.
The original API and implementation versions and coordinates are retained.

%package impl
Summary: Jakarta Standard Tag Library implementation
Group: Development/Java

%description impl
The full Jakarta Standard Tag Library implementation, including core,
formatting, SQL and XML tags, using system Xalan.

%package tagsdoc
Summary: Jakarta tag library documentation generator
License: BSD-3-Clause
Group: Development/Java

%description tagsdoc
The original TLDDoc-based Jakarta tag library documentation generator.

%package javadoc
Summary: API documentation for Jakarta Standard Tag Library
Group: Development/Java

%description javadoc
Independent Javadoc for the Jakarta Standard Tag Library modules.

%package manual
Summary: Jakarta Standard Tag Library specification and tag reference
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
The complete HTML specification and generated reference for the five
Jakarta Standard Tag Library tag libraries.

%prep
%setup
# No sources or documentation classifier JARs; retain independent Javadoc.
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
# Optional legacy CI reporting, not an upstream test execution.
%pom_remove_plugin -r org.codehaus.mojo:findbugs-maven-plugin
# Native Asciidoctor preserves complete HTML without the PDF-only backend.
%pom_remove_plugin org.asciidoctor:asciidoctor-maven-plugin spec
%pom_remove_plugin :maven-assembly-plugin spec

%mvn_file :jakarta.servlet.jsp.jstl-api %name/jakarta.servlet.jsp.jstl-api
%mvn_file org.glassfish.web:jakarta.servlet.jsp.jstl \
    %name/jakarta.servlet.jsp.jstl
%mvn_file org.glassfish.web:tagsdoc %name/tagsdoc
%mvn_file org.glassfish.web:jstl %name/jstl
%mvn_file jakarta.stl:jakarta-stl-spec %name/jakarta-stl-spec
%mvn_package org.glassfish.web:jakarta.servlet.jsp.jstl impl
%mvn_package org.glassfish.web:tagsdoc tagsdoc

%build
# XMvn aggregate Javadoc mixes source-path and module-source-path for this
# modular API and the two classpath modules. Generate all three separately.
%mvn_build -j -- -Ptlddocs
mkdir -p target/javadoc
jstl_javadoc_cp=$(build-classpath jakarta-servlet/jakarta.servlet-api \
    jakarta-server-pages/jakarta.servlet.jsp-api jakarta-el/jakarta.el-api)
find api/src/main/java -name '*.java' -print > target/api-javadoc-sources
javadoc -quiet -Xdoclint:none -encoding UTF-8 -d target/javadoc/api \
    --module-path "$jstl_javadoc_cp" @target/api-javadoc-sources
find impl/src/main/java -name '*.java' -print > target/impl-javadoc-sources
javadoc -quiet -Xdoclint:none -encoding UTF-8 -d target/javadoc/impl \
    -classpath "$jstl_javadoc_cp:$(build-classpath xalan-j2):api/target/jakarta.servlet.jsp.jstl-api-3.0.2.jar" \
    @target/impl-javadoc-sources
find tagsdoc/src/main/java -name '*.java' -print > target/tagsdoc-javadoc-sources
javadoc -quiet -Xdoclint:none -encoding UTF-8 -d target/javadoc/tagsdoc \
    @target/tagsdoc-javadoc-sources
asciidoctor -b html5 -d book -a data-uri -a revnumber=3.0-SNAPSHOT \
    -a status=DRAFT -a revremark=DRAFT -a source-highlighter! \
    -D target/manual spec/src/main/asciidoc/jakarta-stl-spec.adoc

%install
%mvn_install
install -d %buildroot%_javadocdir/%name
cp -a target/javadoc/* %buildroot%_javadocdir/%name/
%jpackage_script com.sun.tlddoc.TLDDoc "" "" %name/tagsdoc %name-tagsdoc

%files -f .mfiles
%doc LICENSE.md NOTICE.md tagsdoc/LICENSE

%files impl -f .mfiles-impl

%files tagsdoc -f .mfiles-tagsdoc
%_bindir/%name-tagsdoc

%files javadoc
%_javadocdir/%name

%files manual
%doc target/manual/*.html
%doc impl/target/tlddoc

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 3.0.2-alt1
- Initial build for ALT.
