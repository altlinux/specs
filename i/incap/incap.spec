%define _unpackaged_files_terminate_build 1

Name: incap
Version: 1.0.0
Release: alt1

Summary: Helpers for building incremental Java annotation processors
License: Apache-2.0
Group: Development/Java
Url: https://github.com/tbroyer/gradle-incap-helper
VCS: https://github.com/tbroyer/gradle-incap-helper.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: offline-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-21-openjdk-devel
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.testing.compile:compile-testing)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(junit:junit)

%description
Library annotations and processor generating Gradle incremental annotation
processor descriptors. Includes the incap and incap-processor Maven artifacts.

%prep
%setup
%autopatch -p1

%build
%gradle_publish --no-daemon --max-workers=2

%install
%gradle_register --artifacts=incap-
%gradle_install

%check
%gradle_check --no-daemon --max-workers=2

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- Initial build for ALT.
