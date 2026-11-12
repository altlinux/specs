%define _unpackaged_files_terminate_build 1

Name: json-patch
Version: 1.13
Release: alt1

Summary: JSON Patch and JSON Merge Patch for Jackson
License: Apache-2.0 or LGPL-3.0-or-later
Group: Development/Java
URL: https://github.com/java-json-tools/json-patch
VCS: https://github.com/java-json-tools/json-patch.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-system-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: aqute-bnd
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.github.java-json-tools:msg-simple)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.github.java-json-tools:jackson-coreutils)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(com.google.guava:guava)

%description
An implementation of JSON Patch (RFC 6902) and JSON Merge Patch (RFC 7386)
using Jackson.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE ASL-2.0.txt LGPL-3.0.txt

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.13-alt1
- Initial build for ALT.
