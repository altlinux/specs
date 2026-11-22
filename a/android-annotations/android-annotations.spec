%define _unpackaged_files_terminate_build 1

Name: android-annotations
Version: 4.1.1.4
Release: alt1

Summary: Annotations for the Google Android Platform
License: Apache-2.0
Group: Development/Java
URL: https://source.android.com/
VCS: https://android.googlesource.com/platform/frameworks/base

Source0: %name-%version.tar
Source1: annotations.pom

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

BuildArch: noarch

%description
The Android annotation library provides the annotations used by the Google
Android platform.

%package javadoc
Summary: API documentation for android-annotations
Group: Development/Documentation

%description javadoc
API documentation for the Android annotation library.

%prep
%setup -q
cp -p %SOURCE1 pom.xml
%mvn_file :annotations android-annotations/annotations

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-annotations
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 4.1.1.4-alt1
- Initial build for ALT.
