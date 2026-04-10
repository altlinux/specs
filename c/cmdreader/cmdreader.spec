%define _unpackaged_files_terminate_build 1

Name: cmdreader
Version: 1.5
Release: alt1

Summary: Command line parser for Java
License: MIT
Group: Development/Java
Url: https://github.com/rzwitserloot/com.zwitserloot.cmdreader
Vcs: https://github.com/rzwitserloot/com.zwitserloot.cmdreader.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: ant
BuildRequires: ivy-local
BuildRequires: apache-ivy
BuildRequires: apache-commons-logging
BuildRequires: ivyplusplus
BuildRequires: maven-local
BuildRequires: jpackage-default

%description
CmdReader is a Java library for declarative command line parsing.

%prep
%setup

# Use system ivyplusplus + ivy-local (XMvn), no network downloads.
sed -i \
  -e 's#<target name="ensure-ipp" depends="load-ipp, checkver-ipp" />#<target name="ensure-ipp" depends="load-ipp" />#' \
  -e 's#classpath="lib/ivyplusplus.jar"#classpath="lib/ivyplusplus.jar:lib/commons-logging.jar"#' \
  -e 's#<ivy:configure file="buildScripts/ivysettings.xml" />#<ivy:configure />#' \
  -e 's/depends="compile, -test.quiet, -test, javadoc"/depends="compile, javadoc"/' \
  -e 's/source="1.5" target="1.5"/source="1.8" target="1.8"/g' \
  -e 's/target="1.5" source="1.5"/target="1.8" source="1.8"/g' \
  build.xml

%build
IPP_JAR=%_javadir/ivyplusplus.jar
CLOG_JAR=%_javadir/commons-logging.jar

[ -f "$IPP_JAR" ] || IPP_JAR=$(find %_javadir -type f -name 'ivyplusplus*.jar' | sort | head -n1)
[ -f "$CLOG_JAR" ] || CLOG_JAR=$(find %_javadir -type f -name 'commons-logging*.jar' | sort | head -n1)

test -n "$IPP_JAR" -a -f "$IPP_JAR"
test -n "$CLOG_JAR" -a -f "$CLOG_JAR"

mkdir -p lib
cp -f "$IPP_JAR" lib/ivyplusplus.jar
cp -f "$CLOG_JAR" lib/commons-logging.jar

%ant -Divy.mode=local -Dversion=%version dist

cat > build/cmdreader-%version.pom <<'POM'
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>zwitserloot.com</groupId>
  <artifactId>cmdreader</artifactId>
  <version>%version</version>
  <packaging>jar</packaging>
  <name>CmdReader</name>
</project>
POM

%install
%mvn_file zwitserloot.com:cmdreader %name
%mvn_artifact build/cmdreader-%version.pom dist/com.zwitserloot.cmdreader-%version.jar
%mvn_install

%files -f .mfiles
%doc README.markdown LICENSE

%changelog
* Fri Apr 10 2026 Ivan Khanas <xeno@altlinux.org> 1.5-alt1
- First build for ALT.
