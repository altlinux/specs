%define _unpackaged_files_terminate_build 1

Name: glassfish-hk2-extra
Version: 3.0.0
Release: alt1

Summary: HK2 OSGi resource locator
License: EPL-2.0
Group: Development/Java
Url: https://github.com/eclipse-ee4j/glassfish-hk2-extra
Vcs: https://github.com/eclipse-ee4j/glassfish-hk2-extra.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-build-helper
BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: ee4j-parent

%description
%summary

%{?javadoc_package}

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin osgi-resource-locator
%pom_remove_plugin :osgiversion-maven-plugin osgi-resource-locator
sed -i 's/${project.osgi.version}/%{version}/' osgi-resource-locator/osgi.bundle

%build
%mvn_build -s -- -pl osgi-resource-locator

%install
%mvn_install

%files -f .mfiles-osgi-resource-locator

%changelog
* Tue Mar 24 2026 Ivan Khanas <xeno@altlinux.org> 3.0.0-alt1
- First build for ALT.
