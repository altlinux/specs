%define _unpackaged_files_terminate_build 1

Name: msg-simple
Version: 1.2
Release: alt1

Summary: Lightweight UTF-8 message bundles
License: Apache-2.0 or LGPL-3.0-or-later
Group: Development/Java
URL: https://github.com/java-json-tools/msg-simple
VCS: https://github.com/java-json-tools/msg-simple.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-system-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: aqute-bnd
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.github.java-json-tools:btf)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.mockito:mockito-core)

%description
Message bundles with UTF-8 resources, locale selection and printf formatting.

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
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.2-alt1
- Initial build for ALT.
