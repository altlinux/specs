%define _unpackaged_files_terminate_build 1

Name: jboss-vfs
Version: 3.3.2
Release: alt1

Summary: JBoss virtual file system library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/wildfly/jboss-vfs
VCS: https://github.com/wildfly/jboss-vfs.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-system.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(junit:junit)

%description
JBoss VFS provides a virtual file system over directories and archives.

%javadoc_package

%prep
%setup
%autopatch -p1
# Source archives are retained; Java source classifiers are not binary outputs.
%mvn_package ::sources __noinstall
%mvn_file : %name

%build
%mvn_build -s -- -Dmaven.compiler.release=11 -Dmaven.compiler.proc=full

%install
%mvn_install

%files -f .mfiles-jboss-vfs
%doc LICENSE.txt

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 3.3.2-alt1
- Initial build for ALT.
