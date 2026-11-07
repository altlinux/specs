%define _unpackaged_files_terminate_build 1

Name: jetbrains-markdown
Version: 0.7.18
Release: alt1

Summary: Kotlin Markdown parser and HTML generator
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/markdown
VCS: https://github.com/JetBrains/markdown.git

Source: %name-%version.tar
Patch: %name-system.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: kotlin-test
BuildRequires: junit

%description
A Kotlin library for parsing Markdown into syntax trees and rendering HTML.
This package provides the JVM implementation and common metadata.

%prep
%setup
%autopatch -p1
# Upstream buildSrc applies Dokka, whose parser depends on this library.
mv buildSrc buildSrc.upstream

%build
%gradle_publish -Psnapshot=false

%install
%gradle_register --artifacts=markdown-
%gradle_install

%check
%gradle_check -Psnapshot=false

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 0.7.18-alt1
- Initial build for ALT.
