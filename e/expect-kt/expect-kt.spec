%define _unpackaged_files_terminate_build 1

Name: expect-kt
Version: 1.0.1
Release: alt1

Summary: Readable test assertions in Kotlin
License: Apache-2.0
Group: Development/Java
URL: https://github.com/nhaarman/expect.kt
VCS: https://github.com/nhaarman/expect.kt.git

Source: %name-%version.tar
Patch: %name-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(io.reactivex.rxjava3:rxjava)
BuildRequires: mvn(junit:junit)

%description
Expect.kt provides readable assertions for Kotlin tests, including matchers
for values, collections, strings, numbers, errors and RxJava observers.

%prep
%setup
%patch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=expect.kt
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
