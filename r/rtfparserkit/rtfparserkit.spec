%define _unpackaged_files_terminate_build 1

Name: rtfparserkit
Version: 1.16.0
Release: alt1

Summary: Primary repository for RTF Parser Kit library
License: Apache-2.0
Group: Development/Java
Url: https://github.com/joniles/rtfparserkit
Vcs: https://github.com/joniles/rtfparserkit.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-default
BuildRequires: maven-source-plugin

%description
The idea is to provide a "kit" of components which can either be used "as-is",
for example to extract plain text or HTML from an RTF file, or can be used as a
component in a larger application which requires the capability to parse RTF
documents.

%{?javadoc_package}

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%changelog
* Wed Apr 15 2026 Ivan Khanas <xeno@altlinux.org> 1.16.0-alt1
- First build fpr ALT.

