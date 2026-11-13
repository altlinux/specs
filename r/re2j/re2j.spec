%define _unpackaged_files_terminate_build 1

Name: re2j
Version: 1.8
Release: alt1

Summary: Linear time regular expressions for Java
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/google/re2j
VCS: https://github.com/google/re2j.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.truth:truth)

%description
RE2/J is a regular expression engine with linear matching time.
It provides the complete Java Pattern and Matcher implementation.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the RE2/J regular expression library.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%install
%gradle_register
%gradle_register_javadoc
%gradle_install

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 1.8-alt1
- Initial build for ALT.
