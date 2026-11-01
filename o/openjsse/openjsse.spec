%define _unpackaged_files_terminate_build 1

Name: openjsse
Version: 1.1.14
Release: alt1

Summary: TLS 1.3 JSSE provider for Java 8
License: GPL-2.0-only WITH Classpath-exception-2.0 AND BSD-2-Clause
Group: Development/Java
Url: https://github.com/openjsse/openjsse
VCS: https://github.com/openjsse/openjsse.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
OpenJSSE provides TLS 1.3 and RSASSA-PSS support for Java 8 applications.
It is based on the OpenJDK JSSE implementation and exposes the provider
under the org.openjsse namespace.

%package javadoc
Summary: API documentation for OpenJSSE
Group: Development/Documentation

%description javadoc
API documentation for OpenJSSE.

%prep
%setup -q
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin com.google.code.maven-replacer-plugin:maven-replacer-plugin
sed -e 's/\$VERSION\$/%version/g' \
    -e 's/\$BUILD_TIME\$/reproducible ALT build/g' \
    src/main/java/org/openjsse/Version.java.template \
    > src/main/java/org/openjsse/Version.java
sed -e 's/\$VERSION\$/%version/g' \
    -e 's/\$BUILD_TIME\$/reproducible ALT build/g' \
    src/main/templates/VERSION.template > src/main/resources/VERSION

# Upstream keeps the BSD notices in source headers, outside LICENSE.
sed -n '1,/^ \*\//p' src/main/java/org/openjsse/Version.java.template \
    > LICENSE-BSD
sed -n '1,/^ \*\//p' \
    src/main/java/org/openjsse/sun/security/ssl/CertificateAuthorityExtension.java \
    >> LICENSE-BSD

%build
# Maven plugins need JDK 21; the provider needs JDK 8 internal APIs.
%mvn_build -j -- \
    -Dmaven.compiler.fork=true \
    -Dmaven.compiler.executable=%_jvmdir/java-1.8.0-openjdk/bin/javac \
    -Dbuild.bootclasspath=%_jvmdir/java-1.8.0-openjdk/jre/lib/resources.jar:%_jvmdir/java-1.8.0-openjdk/jre/lib/rt.jar:%_jvmdir/java-1.8.0-openjdk/jre/lib/jce.jar
# Match upstream's public API documentation, using the matching JDK 8 tool.
%_jvmdir/java-1.8.0-openjdk/bin/javadoc \
    -quiet -notimestamp -Xdoclint:none -d target/site/apidocs \
    -sourcepath src/main/java:src/main/java1.8 -classpath target/classes \
    -subpackages org.openjsse.javax:org.openjsse.java

%install
%mvn_install

%files -f .mfiles
%doc LICENSE LICENSE-BSD README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 1.1.14-alt1
- Initial build for ALT.
