%define _unpackaged_files_terminate_build 1

Name: maven-war-plugin
Version: 3.4.0
Release: alt2

Summary: Apache Maven WAR Plugin
License: Apache-2.0
Group: Development/Java
Url: https://maven.apache.org/plugins/maven-war-plugin/
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: maven
BuildRequires: maven-parent
BuildRequires: jpackage-17-compat
BuildRequires: maven-archiver
BuildRequires: maven-filtering
BuildRequires: maven-mapping
BuildRequires: maven-plugin-annotations
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resolver
BuildRequires: maven-shared-utils
BuildRequires: apache-commons-io
BuildRequires: plexus-archiver
BuildRequires: plexus-interpolation
BuildRequires: plexus-utils
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: atinject

%description
Apache Maven WAR Plugin builds web application archives (WAR files)
from project output and dependencies.

%{?javadoc_package}

%prep
%setup

# Integration tests require extra tooling and are not needed for RPM artifact build.
%pom_remove_plugin :maven-invoker-plugin

%mvn_file : %name

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Thu May 21 2026 Ilfat Aminov <aminov@altlinux.org> 3.4.0-alt2
- fix sisu dependency

* Fri Apr 03 2026 Ivan Khanas <xeno@altlinux.org> 3.4.0-alt1
- Initial build for ALT.
