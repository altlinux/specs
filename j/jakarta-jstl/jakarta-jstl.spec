%define _unpackaged_files_terminate_build 1

Name: jakarta-jstl
Version: 3.0.2
Release: alt2

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
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(jakarta.servlet.jsp:jakarta.servlet.jsp-api)
BuildRequires: tomcat-jsp-2.3-api
BuildRequires: tomcat-el-3.0-api
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(jakarta.el:jakarta.el-api)
BuildRequires: mvn(xalan:xalan)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
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

%package ee8-api
Summary: Java EE Standard Tag Library API for Servlet 4
Group: Development/Java

%description ee8-api
The original JSTL 1.2 API with the javax.servlet.jsp.jstl namespace.

%package ee8-impl
Summary: GlassFish Standard Tag Library implementation for Servlet 4
Group: Development/Java

%description ee8-impl
The Java EE implementation of the core, formatting, SQL and XML tag libraries.

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

%mvn_file :jakarta.servlet.jsp.jstl-api:3.0.2 %name/jakarta.servlet.jsp.jstl-api
%mvn_file org.glassfish.web:jakarta.servlet.jsp.jstl:3.0.1 \
    %name/jakarta.servlet.jsp.jstl
%mvn_file org.glassfish.web:tagsdoc %name/tagsdoc
%mvn_file org.glassfish.web:jstl %name/jstl
%mvn_file jakarta.stl:jakarta-stl-spec %name/jakarta-stl-spec
%mvn_package :jakarta.servlet.jsp.jstl-api:3.0.2
%mvn_package org.glassfish.web:jstl
%mvn_package jakarta.stl:jakarta-stl-spec
%mvn_package org.glassfish.web:jakarta.servlet.jsp.jstl:3.0.1 impl
%mvn_package :jakarta.servlet.jsp.jstl-api:1.2.7 ee8-api
%mvn_package org.glassfish.web:jakarta.servlet.jsp.jstl:1.2.6 ee8-impl
%mvn_compat_version :jakarta.servlet.jsp.jstl-api:1.2.7 1.2.7
%mvn_compat_version org.glassfish.web:jakarta.servlet.jsp.jstl:1.2.6 1.2.6
%mvn_file :jakarta.servlet.jsp.jstl-api:1.2.7 \
    %name-ee8-api/jakarta.servlet.jsp.jstl-api
%mvn_file org.glassfish.web:jakarta.servlet.jsp.jstl:1.2.6 \
    %name-ee8-impl/jakarta.servlet.jsp.jstl
%mvn_package org.glassfish.web:tagsdoc tagsdoc

%build
# XMvn aggregate Javadoc mixes source-path and module-source-path for this
# modular API and the two classpath modules. Generate all three separately.
%mvn_build -s -j -- -Ptlddocs
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

%files ee8-api -f .mfiles-ee8-api

%files ee8-impl -f .mfiles-ee8-impl
%doc compat/ee8-impl/NOTICE.md

%files tagsdoc -f .mfiles-tagsdoc
%_bindir/%name-tagsdoc

%files javadoc
%_javadocdir/%name

%files manual
%doc target/manual/*.html
%doc impl/target/tlddoc

%changelog
* Thu Nov 19 2026 Ivan Khanas <xeno@altlinux.org> 3.0.2-alt2
- Package the Java EE 8 JSTL API and implementation.

* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 3.0.2-alt1
- Initial build for ALT.
