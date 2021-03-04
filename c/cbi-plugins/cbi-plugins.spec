Name: cbi-plugins
Version: 1.1.7
Release: alt1

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
BuildRequires: java-devel
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
%pom_disable_module eclipse-dmg-packager maven-plugins
%pom_disable_module eclipse-flatpak-packager maven-plugins

# Disable plugins not needed for RPM builds
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin

# Build the common module
%pom_xpath_inject pom:modules "<module>../common/</module>" maven-plugins
%pom_remove_dep org.eclipse.cbi:checkstyle common

# Remove separate annotations requirement of auto
%pom_remove_dep :auto-value-annotations . common maven-plugins/common

# Parent pom and common module are "released" independently, but actually nothing changed yet since last releases
sed -i -e 's/1\.0\.6-SNAPSHOT/1.0.5/' pom.xml
sed -i -e 's/1\.2\.4-SNAPSHOT/1.2.3/' common/pom.xml

# Make dep on guava more forgiving
sed -i -e 's/>28.0-jre</>20.0</' pom.xml

# Don't use static analysis annotations
sed -i -e 's/@Nonnull//' -e '/javax.annotation.Nonnull/d' common/src/main/java/org/eclipse/cbi/common/security/*.java

%build
%mvn_build -f -- -f maven-plugins/pom.xml -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Mar 04 2021 Nazarov Denis <nenderus@altlinux.org> 1.1.7-alt1
- Initial build for ALT Linux
