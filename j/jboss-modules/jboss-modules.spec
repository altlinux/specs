%define _unpackaged_files_terminate_build 1

Name: jboss-modules
Version: 2.3.0
Release: alt1

Summary: Modular classloading implementation for Java
License: Apache-2.0
Group: Development/Java
Url: http://jboss-modules.github.io/jboss-modules
Vcs: https://github.com/jboss-modules/jboss-modules.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: jboss-parent
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-surefire-plugin

%description
JBoss Modules is a standalone implementation of a modular classloader and
module system for Java.

%prep
%setup

%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin org.jboss.bridger:bridger
%pom_remove_dep org.jboss.shrinkwrap:shrinkwrap-impl-base
%pom_remove_dep junit:junit

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md XPP3-LICENSE.txt

%changelog
* Tue Mar 31 2026 Ivan Khanas <xeno@altlinux.org> 2.3.0-alt1
- First build for ALT.
