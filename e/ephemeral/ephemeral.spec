%define _unpackaged_files_terminate_build 1

Name: ephemeral
Version: 1.5.0
Release: alt1

Summary: Ephemeral design system for desktop applications
License: Apache-2.0
Group: Development/Java
Url: https://github.com/kirill-grouchnikov/ephemeral
Vcs: https://github.com/kirill-grouchnikov/ephemeral.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: xgradle

%description
Ephemeral is a design system for building modern and elegant desktop
applications. This package builds and installs the Java Chroma module.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Thu Apr 16 2026 Ivan Khanas <xeno@altlinux.org> 1.5.0-alt1
- First build for ALT.
