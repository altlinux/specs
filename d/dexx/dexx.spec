%define _unpackaged_files_terminate_build 1

Name: dexx
Version: 0.7
Release: alt1

Summary: Persistent immutable collection library
License: MIT AND BSD-3-Clause
Group: Development/Java
URL: https://github.com/andrewoma/dexx
VCS: https://github.com/andrewoma/dexx.git

Source: %name-%version.tar
Patch0: 0001-Build-both-modules-with-system-Gradle.patch
Patch1: 0002-Use-explicit-types-in-Kotlin-tests.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.assertj:assertj-core)

%description
Persistent immutable collections for Java and Kotlin.

%package kollection
Summary: Kotlin API for Dexx collections
Group: Development/Java

%description kollection
Kotlin wrappers for persistent collections supplied by Dexx.

%prep
%setup -q
%autopatch -p1
%mvn_package :kollection kollection

%build
export LC_ALL=C.UTF-8
%gradle_publish

%install
%gradle_register --artifacts=collection,kollection
%gradle_install

%check
export LC_ALL=C.UTF-8
%gradle_check

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt licenses/LICENSE_Scala.txt

%files kollection -f .mfiles-kollection

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 0.7-alt1
- Initial build for ALT.
