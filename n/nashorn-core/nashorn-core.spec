%define _unpackaged_files_terminate_build 1

Name: nashorn-core
Version: 15.7
Release: alt1

Summary: OpenJDK Nashorn JavaScript engine
License: GPL-2.0-only WITH Classpath-exception-2.0
Group: Development/Java
URL: https://github.com/openjdk/nashorn
VCS: https://github.com/openjdk/nashorn.git

Source0: %name-%version.tar
Source1: build.sh
Source2: nashorn
Source3: NashornTestsRunner.java
Patch0: %name-%version.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-11-openjdk-devel
BuildRequires: maven-local
BuildRequires: ant
BuildRequires: objectweb-asm
BuildRequires: testng
BuildRequires: beust-jcommander
BuildRequires: bsh
BuildRequires: snakeyaml
BuildRequires: slf4j

%description
Standalone OpenJDK Nashorn JavaScript engine for Java 11 and later.
Implements ECMAScript 5.1 and selected ECMAScript 6 features, JSR 223
scripting and Java interoperability. Includes the Nashorn command shell.

%prep
%setup
%autopatch -p1
cp %SOURCE1 .
cp %SOURCE3 test/nashorn/src/
cp make/nashorn/nashorn-core.pom pom.xml
sed -i -e 's/NASHORN_VERSION/%version/g' \
    -e "s/ASM_VERSION/$(rpm -q --qf '%%{VERSION}' objectweb-asm)/g" pom.xml
%mvn_file org.openjdk.nashorn:nashorn-core %name/%name

%build
bash build.sh %_jvmdir/java-11-openjdk
%mvn_artifact pom.xml build/nashorn/dist/nashorn.jar

%install
%mvn_install
install -m644 build/nashorn/dist/jjs.jar %buildroot%_javadir/%name/
install -d %buildroot%_bindir
sed 's|@JAVADIR@|%_javadir|g' %SOURCE2 >%buildroot%_bindir/nashorn
chmod 755 %buildroot%_bindir/nashorn

%files -f .mfiles
%_bindir/nashorn
%_javadir/%name/jjs.jar
%doc LICENSE ASSEMBLY_EXCEPTION ADDITIONAL_LICENSE_INFO CHANGELOG.md
%doc src/org.openjdk.nashorn/share/legal/*.md

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 15.7-alt1
- Initial build for ALT.
