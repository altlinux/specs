%define _unpackaged_files_terminate_build 1

%ifarch %ix86
%define native_classifier linux-x86
%else
%ifarch aarch64
%define native_classifier linux-aarch_64
%else
%define native_classifier linux-x86_64
%endif
%endif

Name: conscrypt
Version: 2.8.0
Release: alt1

Summary: OpenJDK security provider backed by BoringSSL
License: Apache-2.0 and ISC
Group: Development/Java
Url: https://conscrypt.org
VCS: https://github.com/google/conscrypt.git

Source0: %name-%version.tar
# BoringSSL 0.20261020.0 LICENSE, outside the Conscrypt upstream archive.
Source1: LICENSE.boringssl
Patch0: conscrypt-system-build.patch

ExclusiveArch: %ix86 x86_64 aarch64

BuildRequires(pre): rpm-macros-gradle
BuildRequires: boringssl-devel
BuildRequires: gcc-c++
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle

%description
Conscrypt is a Java Security Provider that uses BoringSSL for TLS and
cryptographic operations. This package contains the OpenJDK library and
native JNI implementation for the host Linux architecture, including its
Maven classifier artifact. It does not contain the universal multi-platform
uber JAR or Android libraries.

%prep
%setup -q
%autopatch -p1
%ifarch %ix86
# The upstream 4 GiB heap cannot fit a 32-bit JVM address space.
sed -i 's/-Xmx4g/-Xmx2g/' gradle.properties
%endif
cp %SOURCE1 LICENSE.boringssl

%build
CXXFLAGS="%optflags" \
%gradle_publish \
    -PnativeClassifier=%native_classifier \
    -PboringsslLibDir=%_libdir/boringssl \
    -PboringsslVersion="$(rpm -q --qf '%%{VERSION}' boringssl-devel)"

%install
%gradle_register --artifacts=conscrypt-openjdk-
%mvn_artifact org.conscrypt:conscrypt-openjdk:jar:%native_classifier:%version \
    %_mavenrepolocal/repository/org/conscrypt/conscrypt-openjdk/%version/conscrypt-openjdk-%version-%native_classifier.jar
%mvn_package org.conscrypt:conscrypt-openjdk:jar:%native_classifier:%version
%mvn_file org.conscrypt:conscrypt-openjdk:jar:%native_classifier:%version \
    %name/conscrypt-openjdk-%native_classifier
%gradle_install
%gradle_register_javadoc --artifacts=conscrypt-openjdk-
# Also provide the native library through the standard JVM library path.
install -Dm755 build/native/libconscrypt_openjdk_jni-%native_classifier.so \
    %buildroot%_libdir/libconscrypt_openjdk_jni-%native_classifier.so

%files -f .mfiles
%doc LICENSE NOTICE README.md licenses LICENSE.boringssl
%_libdir/libconscrypt_openjdk_jni-%native_classifier.so
%_javadocdir/%name

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 2.8.0-alt1
- Initial build for ALT.
