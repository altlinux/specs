%define _unpackaged_files_terminate_build 1
%def_without fuzz

Name: lz4-java
Version: 1.14.0
Release: alt1

Summary: Java implementations and JNI bindings of LZ4 and xxHash
License: Apache-2.0
Group: Development/Java
URL: https://github.com/yawkat/lz4-java
VCS: https://github.com/yawkat/lz4-java.git

Source0: %name-%version.tar
Patch0: system-jvm.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: gcc
BuildRequires: liblz4-devel
BuildRequires: lz4
BuildRequires: libxxhash-devel
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(biz.aQute.bnd:biz.aQute.bnd.ant)
BuildRequires: mvn(org.mvel:mvel2)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.junit.vintage:junit-vintage-engine)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.junit.platform:junit-platform-commons)
BuildRequires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
%if_with fuzz
BuildRequires: mvn(com.code-intelligence:jazzer-junit)
%endif

Requires: liblz4 >= 1:1.9.4

%description
LZ4 Java provides complete Java implementations and JNI bindings for LZ4
and xxHash. The Linux JNI implementation links to the system libraries.

%javadoc_package

%prep
%setup
%autopatch -p1
rm -f .mvn/extensions.xml
%pom_xpath_set 'pom:project/pom:version' '%version'
%pom_remove_plugin org.gradlex:gradle-module-metadata-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
# Main remains Java7 bytecode; upstream tests genuinely require Java21.
%pom_xpath_inject '//pom:jdkToolchain/..' '
<executable>%_jvmdir/java-17-openjdk/bin/javac</executable>'
%pom_xpath_remove '//pom:jdkToolchain'
%if_without fuzz
# All ordinary tests run; the separate Jazzer fuzz profile needs its SDK.
%pom_remove_dep com.code-intelligence:jazzer-junit
%pom_xpath_inject '//pom:plugin[pom:artifactId="maven-compiler-plugin"]' '
<configuration>
  <testExcludes><testExclude>net/jpountz/fuzz/**</testExclude></testExcludes>
</configuration>'
%endif
%mvn_file : lz4-java

%build
CFLAGS="%optflags" LDFLAGS="-Wl,-z,defs" \
    %mvn_build -j
# Parse Java7 sources with the current documentation tool, without recompiling.
xmvn --batch-mode --offline \
    -Dmaven.compiler.source=8 org.fedoraproject.xmvn:xmvn-mojo:javadoc

%install
%mvn_install
install -d %buildroot%_jnidir
find target/classes/net/jpountz/util -name liblz4-java.so \
    -exec install -m755 '{}' %buildroot%_jnidir/ ';'
test -f %buildroot%_jnidir/liblz4-java.so

%files -f .mfiles
%doc LICENSE.txt
%_jnidir/liblz4-java.so

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.14.0-alt1
- Initial build for ALT.
