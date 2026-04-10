%define _unpackaged_files_terminate_build 1

Name: lombok-patcher
Version: 0.56
Release: alt1

Summary: Bytecode patching library used by Lombok
License: MIT
Group: Development/Java
Url: https://github.com/rzwitserloot/lombok.patcher
Vcs: https://github.com/rzwitserloot/lombok.patcher.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
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
BuildRequires: jpackage-default

%description
lombok.patcher is a bytecode patching library used by Project Lombok.

%prep
%setup

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
sed -i \
  -e "s#classpath=\"lib/ivyplusplus.jar\"#classpath=\"$IVYPLUSPLUS_CP\"#" \
  build.xml

sed -i \
  -e '/projectlombok.org.*jsch-ant-fixed/d' \
  -e '/com.jcraft.*jsch/d' \
  buildScripts/ivy.xml

%build
%ant -Divy.mode=local -DskipTests=true dist

cat > build/lombok.patcher-%version.pom <<'POM'
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.projectlombok</groupId>
  <artifactId>lombok.patcher</artifactId>
  <version>%version</version>
  <packaging>jar</packaging>
  <name>lombok.patcher</name>
</project>
POM

%install
%mvn_file org.projectlombok:lombok.patcher %name
%mvn_artifact \
  build/lombok.patcher-%version.pom \
  dist/lombok.patcher-%version.jar
%mvn_install

%files -f .mfiles
%doc README.markdown

%changelog
* Thu Apr 09 2026 Ivan Khanas <xeno@altlinux.org> 0.56-alt1
- First build for ALT.
