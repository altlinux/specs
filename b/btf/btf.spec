%define _unpackaged_files_terminate_build 1

Name: btf
Version: 1.3
Release: alt1

Summary: Builder and freeze/thaw interfaces
License: Apache-2.0 or LGPL-3.0-or-later
Group: Development/Java
URL: https://github.com/java-json-tools/btf
VCS: https://github.com/java-json-tools/btf.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-system-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: aqute-bnd
BuildRequires: mvn(com.google.code.findbugs:jsr305)

%description
Generic interfaces for the builder and freeze/thaw design patterns.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_install

%files -f .mfiles
%doc LICENSE ASL-2.0.txt LGPL-3.0.txt

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.3-alt1
- Initial build for ALT.
