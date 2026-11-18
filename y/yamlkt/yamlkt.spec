%define _unpackaged_files_terminate_build 1

Name: yamlkt
Version: 0.13.0
Release: alt1

Summary: Kotlin Multiplatform YAML parser and serializer
License: Apache-2.0
Group: Development/Java
URL: https://github.com/Him188/yamlkt
VCS: https://github.com/Him188/yamlkt.git

BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-serialization-core-jvm)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.charleskorn.kaml:kaml-jvm)
BuildRequires: mvn(org.yaml:snakeyaml)

%description
YAML parser and serializer for kotlinx.serialization, written in Kotlin.
This package provides the JVM implementation.

%prep
%setup -q
%autopatch -p1

%build
%gradle_publish -Pyamlkt.jvmOnly=true

%install
%gradle_register --artifacts=yamlkt-jvm-
%gradle_install

%check
%gradle_check --continue -Pyamlkt.jvmOnly=true

%files -f .mfiles
%doc LICENSE

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 0.13.0-alt1
- Initial build for ALT.
