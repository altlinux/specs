%define _unpackaged_files_terminate_build 1

Name: idw-gpl
Version: 1.7.2
Release: alt1

Summary: InfoNode Docking Windows
Group: Development/Java
License: GPL-2.0
Url: https://github.com/REC-SPb-ETU/idw-gpl.git
Vcs: https://github.com/REC-SPb-ETU/idw-gpl.git

Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-source-plugin

%{?javadoc_package}

%description
InfoNode Docking Windows is a pure Java Swing based docking windows framework.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_remove "pom:properties/pom:maven.compiler.source" pom.xml
%pom_xpath_remove "pom:properties/pom:maven.compiler.target" pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Apr 20 2026 Arseniy Kostevich <faux@altlinux.org> 1.7.2-alt1
- Initial build for ALT.
