%define _unpackaged_files_terminate_build 1

Name: lombok-patcher
Version: 0.56
Release: alt2

Summary: Bytecode patching library used by Lombok
License: MIT
Group: Development/Java
URL: https://github.com/rzwitserloot/lombok.patcher
VCS: https://github.com/rzwitserloot/lombok.patcher.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name.pom
Patch0: %name-system-dependencies.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: ant
BuildRequires: ivy-local
BuildRequires: ivyplusplus
BuildRequires: ecj
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-logging
BuildRequires: httpcomponents-client
BuildRequires: httpcomponents-core
BuildRequires: objectweb-asm
BuildRequires: jna
BuildRequires: java-17-openjdk-devel

%description
lombok.patcher is a bytecode patching library used by Project Lombok.

%prep
%setup
%autopatch -p1

IVY_JAR='%_javadir/ivyplusplus.jar'
sed -i \
  -e "s#<get src=\"[^\"]*/ivyplusplus.jar\"#<copy file=\"$IVY_JAR\"#" \
  -e 's# usetimestamp="true"##' \
  -e 's#dest="lib/ivyplusplus.jar"#tofile="lib/ivyplusplus.jar"#' \
  -e 's# file="buildScripts/ivysettings.xml"##' \
  -e '/https:\/\/projectlombok.org\/downloads\/ivyplusplus.jar/d' \
  build.xml

HTTP_CP='%_javadir/commons-logging.jar:'
HTTP_CP="${HTTP_CP}%_javadir/commons-codec.jar:"
HTTP_CP="${HTTP_CP}%_javadir/httpcomponents/httpclient.jar:"
HTTP_CP="${HTTP_CP}%_javadir/httpcomponents/httpcore.jar"
IVYPLUSPLUS_CP="lib/ivyplusplus.jar:${HTTP_CP}"
IVYPLUSPLUS_CP="${IVYPLUSPLUS_CP}:%_javadir/apache-ivy/ivy.jar"
IVYPLUSPLUS_CP="${IVYPLUSPLUS_CP}:%_javadir/ecj/ecj.jar"
sed -i \
  -e "s#classpath=\"lib/ivyplusplus.jar\"#classpath=\"$IVYPLUSPLUS_CP\"#" \
  build.xml

sed -i \
  -e '/projectlombok.org.*jsch-ant-fixed/d' \
  -e '/com.jcraft.*jsch/d' \
  buildScripts/ivy.xml

# Preserve the exact upstream MIT license embedded in its source header.
sed -n '2,/^ \*\//p' src/patcher/lombok/patcher/ClassRootFinder.java | \
sed -e '$d' -e 's/^ \* \?//' > LICENSE

%build
%ant -Divy.mode=local -DskipTests=true dist

sed 's/@VERSION@/%version/g' %SOURCE1 > build/lombok.patcher-%version.pom

%install
%mvn_file org.projectlombok:lombok.patcher %name
%mvn_artifact \
  build/lombok.patcher-%version.pom \
  dist/lombok.patcher-%version.jar
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 0.56-alt2
- Support current ECJ and use system ASM and JNA.

* Thu Apr 09 2026 Ivan Khanas <xeno@altlinux.org> 0.56-alt1
- First build for ALT.
