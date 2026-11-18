%define _unpackaged_files_terminate_build 1

Name: barchart-udt
Version: 2.3.0
Release: alt1

Summary: Java UDT sockets, NIO channels and native transport
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/barchart/barchart-udt
VCS: https://github.com/barchart/barchart-udt.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: gcc-c++
BuildRequires: maven-plugin-bundle
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)

%description
Barchart UDT supplies Java socket and selector APIs, its genuine native UDT
transport, the bundle artifact and an example application.


%package archon
Summary: Parent POM for Barchart UDT modules
Group: Development/Java
BuildArch: noarch

%description archon
Parent POM for Barchart UDT modules.

%package bundle
Summary: OSGi bundle for Barchart UDT
Group: Development/Java
BuildArch: noarch

%description bundle
OSGi bundle for Barchart UDT.

%package demo
Summary: Java examples for Barchart UDT
Group: Development/Java
BuildArch: noarch

%description demo
Java examples for Barchart UDT.

%package tools
Summary: Native UDT client, server and file transfer examples
Group: Networking/Other

%description tools
The upstream native UDT examples built with the same patched transport.

%package testlib
Summary: Upstream test helpers for Barchart UDT
Group: Development/Java
BuildArch: noarch
Requires: %name = %EVR
Requires: mvn(junit:junit)
Requires: mvn(commons-io:commons-io)

%description testlib
The genuine upstream unit-test classes and helpers for Barchart UDT.

%javadoc_package

%prep
%setup
# The OSGi bundle loads the JNI library shipped by the core module.
%pom_add_dep com.barchart.udt:barchart-udt-core:%version:runtime barchart-udt-bundle
%mvn_package :barchart-udt __noinstall
%mvn_package :barchart-udt-it __noinstall
%mvn_package :barchart-udt-it-01-bundle __noinstall
%mvn_package :barchart-udt-it-02-bundle-test __noinstall
%mvn_package :barchart-udt-core:jar:tests: testlib
%mvn_package :barchart-udt-core
%mvn_package :barchart-udt-archon archon
%mvn_package :barchart-udt-bundle bundle
%mvn_package :barchart-udt-demo demo
%mvn_file :{*} barchart-udt/@1

%build
CXXFLAGS="%optflags" LDFLAGS="%optflags" \
    %mvn_build -s -- -Dnative.jdk.include=%_jvmdir/java-21-openjdk/include

%install
%mvn_install
install -Dm755 barchart-udt-core/target/native/libbarchart-udt-core-%version-SNAPSHOT.so \
    %buildroot%_jnidir/libbarchart-udt-core-%version-SNAPSHOT.so
install -d %buildroot%_bindir
install -m755 barchart-udt-core/target/native-tools/barchart-udt-* \
    %buildroot%_bindir/

%files -f .mfiles
%doc barchart-udt-core/src/main/c++/udt/LICENSE.txt
%doc barchart-udt-core/src/main/c++/jni/JNIHelpers.h
%_jnidir/libbarchart-udt-core-%version-SNAPSHOT.so

%files archon -f .mfiles-archon

%files bundle -f .mfiles-bundle

%files demo -f .mfiles-demo

%files testlib -f .mfiles-testlib

%files tools
%_bindir/barchart-udt-*

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 2.3.0-alt1
- Initial build for ALT.
