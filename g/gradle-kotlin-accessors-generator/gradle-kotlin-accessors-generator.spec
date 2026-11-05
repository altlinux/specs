%define _unpackaged_files_terminate_build 1

Name: gradle-kotlin-accessors-generator
Version: 0.2.0
Release: alt1

Summary: Annotation processor generating Kotlin Gradle accessors
License: Apache-2.0
Group: Development/Java
URL: https://github.com/tbroyer/gradle-kotlin-accessors-generator
VCS: https://github.com/tbroyer/gradle-kotlin-accessors-generator.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-metadata-jvm)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(net.ltgt.gradle.incap:incap)
BuildRequires: mvn(net.ltgt.gradle.incap:incap-processor)
BuildRequires: mvn(com.google.auto.service:auto-service-annotations)
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.testing.compile:compile-testing)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: junit5

%description
Annotations and an annotation processor that generate Kotlin extension
accessors for Gradle model types.

%prep
%setup -q
%autopatch -p1

%build
export GRADLE_USER_HOME="$PWD/.gradle"
%gradle_publish -Pversion=%version

%install
%gradle_register --artifacts=annotations,processor
%gradle_install

%check
%gradle_check -Pversion=%version

%files -f .mfiles
%doc LICENSE LICENSE.header

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 0.2.0-alt1
- Initial build for ALT.
