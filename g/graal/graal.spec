Name: graal
Version: 25.5.5.0.3
Release: alt1

Summary: GraalVM SDK, Truffle runtime and regular expression engine
License: UPL-1.0 and GPL-2.0-only WITH Classpath-exception-2.0 and BSD-3-Clause and Unicode-3.0 and Apache-2.0 and 0BSD and MIT
Group: Development/Java
Url: https://github.com/oracle/graal

Source0: %name-%version.tar
Source1: graal-mx.py
Source2: shading-sources.tar.xz
Source3: graal-mx-deps.tar.xz

Patch0: graal-icu79.patch
Patch1: graal-test-fixtures.patch
Patch2: graal-i586.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: mx >= 7.87.0
# The 32-bit JDK has no JVMCI. Build the SDK libraries on this target.
%ifarch %ix86
%define graal_suite sdk
%define graal_mx -p %graal_suite --java-home %_jvmdir/java-21-openjdk
BuildRequires: java-21-openjdk-devel
BuildRequires: java-21-openjdk-jmods
%else
%define graal_suite regex
%define graal_mx -p %graal_suite
BuildRequires: java-25-openjdk-devel
BuildRequires: java-25-openjdk-jmods
%endif
BuildRequires: ninja-build
BuildRequires: python3-module-ninja_syntax
BuildRequires: gcc-c++ zlib-devel
# JLINE3 and LAUNCHER_COMMON are not built: jline4-terminal-ffm cannot
# currently be built consistently as noarch because JDK 22+ is unavailable
# on i586.
BuildRequires: icu4j = 1:79.1
BuildRequires: icu4j-charset = 1:79.1
BuildRequires: objectweb-asm = 9.11.1
BuildRequires: xz-java = 1.10
BuildRequires: guava
BuildRequires: jimfs = 1.3.2
BuildRequires: jopt-simple = 5.0.4
BuildRequires: mvn(org.antlr:antlr4-runtime)
BuildRequires: junit hamcrest

%description
GraalVM SDK APIs, Truffle language framework and runtime, its language
implementation tools, and the TRegex regular expression engine. All these
modules are built from the same Graal source release.

%package nativeimage-sdk
BuildArch: noarch
Summary: GraalVM Native Image SDK
Group: Development/Java

%description nativeimage-sdk
Native Image APIs and annotations, with the Word API they depend on.

%prep
%setup
%autopatch -p1
tar -xf %SOURCE2
tar -xf %SOURCE3
python3 %SOURCE1 %graal_suite

%ifarch %ix86
# These eight-thread stress tests exhaust the heap of the 32-bit JVM.
sed -i -e '/public void largeMultiThreadedHeap()/i\    @org.junit.Ignore' \
       -e '/public void largeMultiThreadedPool()/i\    @org.junit.Ignore' \
    sdk/src/org.graalvm.collections.test/src/org/graalvm/collections/test/LockFreePrefixTreeTest.java
%endif

%build
%mvn_package org.graalvm.sdk:nativeimage nativeimage-sdk
%mvn_package org.graalvm.sdk:word nativeimage-sdk
python3 rpm-mx/mx.py %graal_mx build --build-logs=silent --dependencies="$(cat rpm-build-targets)"
python3 rpm-mx/mx.py %graal_mx rpm-export
while IFS="$(printf '\t')" read -r pom jar; do
    %mvn_artifact "$pom" "$jar"
done < rpm-artifacts/artifacts.tsv

%check
python3 rpm-mx/mx.py %graal_mx unittest --suite sdk
%ifnarch %ix86
python3 rpm-mx/mx.py -p regex unittest --suite truffle
python3 rpm-mx/mx.py -p regex unittest --suite regex
%endif

%install
%mvn_install
cp -p sdk/LICENSE.md LICENSE-sdk.md
cp -p truffle/LICENSE.md LICENSE-truffle.md

%files -f .mfiles
%doc LICENSE-sdk.md LICENSE-truffle.md

%files nativeimage-sdk -f .mfiles-nativeimage-sdk
%doc LICENSE-sdk.md

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 25.5.5.0.3-alt1
- Initial build for ALT.
