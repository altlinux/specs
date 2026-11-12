%define _unpackaged_files_terminate_build 1
%define asm_ver 9.11.1

Name: lombok
Version: 1.18.44
Release: alt2

Summary: Java annotation processor library
License: MIT
Group: Development/Java
URL: https://projectlombok.org
VCS: https://github.com/projectlombok/lombok.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: lombok-java11.patch
Patch1: lombok-system-dependencies.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-codec
BuildRequires: ivy-local
BuildRequires: ivyplusplus
BuildRequires: cmdreader
BuildRequires: lombok-patcher
BuildRequires: objectweb-asm
BuildRequires: ecj

%description
Project Lombok is a Java library that reduces boilerplate code by providing
annotation-driven code generation.

%prep
%setup
%autopatch -p1

IVY_JAR='%_javadir/ivyplusplus.jar'
IVYPLUSPLUS_CP="lib/ivyplusplus.jar:%_javadir/apache-ivy/ivy.jar:%_javadir/ecj/ecj.jar"

sed -i \
  -e "s#<get src=\"[^\"]*/ivyplusplus.jar\"#<copy file=\"$IVY_JAR\"#" \
  -e 's# usetimestamp="true"##' \
  -e 's#dest="lib/ivyplusplus.jar"#tofile="lib/ivyplusplus.jar"#' \
  -e "s#classpath=\"lib/ivyplusplus.jar\"#classpath=\"$IVYPLUSPLUS_CP\"#" \
  -e '/Full eclipse testing requires downloading a native SWT binding/d' \
  -e 's#<ivy:configure file="buildScripts/ivysettings.xml" />#<ivy:configure />#' \
  -e 's/conf="ecj8,build"/conf="ecj8,build,stripe"/' \
  -e '/pathid="cp.build" conf="build"/a\
\t\t<ivy:cachepath pathid="cp.stripe" conf="stripe" />' \
  buildScripts/setup.ant.xml

sed -i \
  -e 's/name="cmdreader" rev="1.2"/name="cmdreader" rev="1.5"/' \
  -e '/name="cmdreader".*conf="build,stripe->/a\
\t\t<dependency org="org.ow2.asm" name="asm" rev="%asm_ver" conf="build,stripe->default" />\
\t\t<dependency org="org.ow2.asm" name="asm-tree" rev="%asm_ver" conf="build,stripe->default" />\
\t\t<dependency org="org.ow2.asm" name="asm-commons" rev="%asm_ver" conf="build,stripe->default" />\
\t\t<dependency org="org.ow2.asm" name="asm-analysis" rev="%asm_ver" conf="build,stripe->default" />\
\t\t<dependency org="org.ow2.asm" name="asm-util" rev="%asm_ver" conf="build,stripe->default" />' \
  -e 's/name="cmdreader" rev="1.5" conf="build,stripe->runtime"/name="cmdreader" rev="1.5" conf="build,stripe->default"/' \
  buildScripts/ivy.xml


%build
ant -Divy.mode=local dist
sed 's/@VERSION@/%version/g' doc/maven-pom.xml > build/lombok-%version.pom

%install
%mvn_file : %name
%mvn_artifact build/lombok-%version.pom dist/lombok-%version.jar
%mvn_install

%files -f .mfiles
%doc LICENSE AUTHORS

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.18.44-alt2
- Support current ECJ and use system runtime dependencies.

* Thu Apr 09 2026 Ivan Khanas <xeno@altlinux.org> 1.18.44-alt1
- First build for ALT.
