Name: cbi-plugins
Version: 1.1.7
Release: alt2.1

Summary: A set of helpers for Eclipse CBI
License: EPL-1.0
Group: Development/Java

Url: https://git.eclipse.org/c/cbi/org.eclipse.cbi.git/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

# https://git.eclipse.org/c/cbi/org.eclipse.cbi.git/snapshot/org.eclipse.cbi_maven-plugin-parent_%version.tar.gz
Source: org.eclipse.cbi_maven-plugin-parent_%version.tar

BuildRequires: /proc
BuildRequires: auto-value
BuildRequires: java-devel >= 11.0.0
BuildRequires: maven-plugin-plugin
BuildRequires: rpm-build-java
BuildRequires: tycho

%description
A set of helpers for Eclipse CBI

%package javadoc
Summary: Javadoc for %name
Group: Development/Java
BuildArch: noarch

%description javadoc
API documentation for %name.

%prep
%setup -n org.eclipse.cbi_maven-plugin-parent_%version

%pom_disable_module eclipse-macsigner-plugin maven-plugins
%pom_disable_module eclipse-winsigner-plugin maven-plugins
%pom_disable_module eclipse-jarsigner-plugin maven-plugins
%pom_disable_module eclipse-dmg-packager maven-plugins
%pom_disable_module eclipse-flatpak-packager maven-plugins
%pom_disable_module common maven-plugins

%pom_remove_parent maven-plugins

# Disable plugins not needed for RPM builds
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin

%build
%mvn_build -f -- -f maven-plugins/pom.xml -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Oct 18 2021 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt2.1
- NMU: Rebuild with java-11-openjdk.

* Sat Mar 06 2021 Nazarov Denis <nenderus@altlinux.org> 1.1.7-alt2
- Fix build

* Thu Mar 04 2021 Nazarov Denis <nenderus@altlinux.org> 1.1.7-alt1
- Initial build for ALT Linux
