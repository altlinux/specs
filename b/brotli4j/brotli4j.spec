%define _unpackaged_files_terminate_build 1

%ifarch %ix86
%define native_arch x86_32
%else
%define native_arch %_arch
%endif

Name: brotli4j
Version: 1.24.0
Release: alt2
Summary: Java Brotli compression with JNI bindings
License: Apache-2.0 AND MIT
Group: Development/Java
URL: https://github.com/hyperxpro/Brotli4j
VCS: https://github.com/hyperxpro/Brotli4j.git
Source0: %name-%version.tar
Patch0: system-native.patch
ExclusiveArch: %ix86 x86_64 aarch64

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake
BuildRequires: pkg-config
BuildRequires: pkgconfig(libbrotlienc)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(libbrotlicommon)
BuildRequires: mvn(io.netty:netty-buffer)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)

%description
Brotli4j provides Java streaming, buffer and channel APIs for Brotli compression
and decompression. The Linux JNI implementation links to system Brotli.

%package classes
Summary: Brotli4j service interfaces and common Maven metadata
Group: Development/Java
BuildArch: noarch

%description classes
Pure Java service interface, common POMs and BOM for Brotli4j.

%package native
Summary: Java Brotli API and Linux JNI bindings
Group: Development/Java

%description native
Java Brotli API with its Linux JNI implementation, dynamically
linked to system Brotli libraries.

# NativeLoader API documentation follows the selected native platform.
%package javadoc
Summary: API documentation for Brotli4j
Group: Development/Documentation

%description javadoc
API documentation for Brotli4j and its Linux native provider.

%prep
%setup
%autopatch -p1
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
# Upstream OS profiles select the current platform; retain foreign sources.
%pom_xpath_remove 'pom:project/pom:modules' natives
%mvn_package :brotli4j native
%mvn_package :service classes
%mvn_package :brotli4j-parent classes
%mvn_package :natives classes
%mvn_package :brotli4j-bom classes
%mvn_package :all classes
%mvn_package :native-linux-%native_arch native

%build
CFLAGS="%optflags" CXXFLAGS="%optflags" LDFLAGS="-Wl,-z,defs" \
    %mvn_build

%install
%mvn_install
# Expose the JNI ELF to normal dependency and debug information generators.
install -D -m755 natives/linux-%native_arch/target/libbrotli.so \
    %buildroot%_jnidir/libbrotli4j.so

%files javadoc -f .mfiles-javadoc

%files classes -f .mfiles-classes
%doc LICENSE NOTICE.txt LICENSES

%files native -f .mfiles-native
%_jnidir/libbrotli4j.so

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.24.0-alt2
- Build the Linux JNI provider for i586.
- Do not package source JARs.

* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 1.24.0-alt1
- Initial build for ALT.
