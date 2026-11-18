%define _unpackaged_files_terminate_build 1

Name: jetty-parent
Version: 32
Release: alt1

Summary: Parent POM for Eclipse Jetty projects
License: Apache-2.0 or EPL-2.0
Group: Development/Java
URL: https://jetty.org/
VCS: https://github.com/jetty/jetty.parent.git

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-enforcer-plugin

%description
Shared Maven build configuration for Eclipse Jetty projects and build tools.

%prep
%setup

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 32-alt1
- Initial build for ALT.
