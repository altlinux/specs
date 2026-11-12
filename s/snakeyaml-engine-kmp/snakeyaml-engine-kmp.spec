%define _unpackaged_files_terminate_build 1

Name: snakeyaml-engine-kmp
Version: 5.0.0
Release: alt1

Summary: YAML 1.2 processor for Kotlin Multiplatform
License: Apache-2.0 AND MIT
Group: Development/Java
URL: https://github.com/krzema12/snakeyaml-engine-kmp
VCS: https://github.com/krzema12/snakeyaml-engine-kmp.git
BuildArch: noarch

Source: %name-%version.tar
Patch: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-sam-with-receiver-compiler-plugin)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-api)
BuildRequires: mvn(com.google.devtools.ksp:symbol-processing-aa)
BuildRequires: mvn(com.squareup:kotlinpoet-jvm)
BuildRequires: mvn(com.squareup:kotlinpoet-ksp)
BuildRequires: mvn(com.squareup.okio:okio)
BuildRequires: mvn(com.squareup.okio:okio-jvm)
BuildRequires: mvn(net.thauvin.erik.urlencoder:urlencoder-lib)
BuildRequires: mvn(net.thauvin.erik.urlencoder:urlencoder-lib-jvm)

%description
SnakeYAML Engine KMP is a YAML 1.2 parser and emitter for Kotlin
Multiplatform. Includes the JVM library and genuine multiplatform
metadata. The Copy DSL processor is built from the same complete source.

%prep
%setup
%autopatch -p1
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i 's/-Xmx4g/-Xmx1g/' gradle.properties
fi

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk --no-configuration-cache

%install
%gradle_register --artifacts=snakeyaml-engine-kmp
%gradle_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 5.0.0-alt1
- Initial build for ALT.
