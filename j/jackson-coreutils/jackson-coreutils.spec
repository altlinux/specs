%define _unpackaged_files_terminate_build 1

Name: jackson-coreutils
Version: 2.0
Release: alt1

Summary: JSON Pointer and numeric equality for Jackson
License: Apache-2.0 or LGPL-3.0-or-later
Group: Development/Java
URL: https://github.com/java-json-tools/jackson-coreutils
VCS: https://github.com/java-json-tools/jackson-coreutils.git
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
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.mockito:mockito-core)

%description
JSON Pointer (RFC 6901) support and numeric equality utilities for Jackson.
Includes the upstream Guava equivalence integration.

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
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 2.0-alt1
- Initial build for ALT.
