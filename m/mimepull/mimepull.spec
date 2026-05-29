Name:          mimepull
Version:       1.11.0
Release:       alt1
Summary:       MIME Streaming Extension
License:       BSD-3-Clause
Group:         Development/Java
Url:           https://github.com/eclipse-ee4j/metro-mimepull
Vcs:           https://github.com/eclipse-ee4j/metro-mimepull.git
BuildArch:     noarch

Source0:       %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-default
BuildRequires: ee4j-parent
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-build-helper

%description
MIME Streaming Extension offering streaming API
to access attachments parts in a MIME message.

%prep
%setup

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Fri May 29 2026 Ilfat Aminov <aminov@altlinux.org> 1.11.0-alt1
- First build for ALT.
