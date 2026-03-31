%define _unpackaged_files_terminate_build 1

Name: jboss-logmanager
Version: 3.2.2
Release: alt1

Summary: Java Util Logging implementation used by JBoss projects
License: Apache-2.0
Group: Development/Java
Url: https://github.com/jboss-logging/jboss-logmanager
Vcs: https://github.com/jboss-logging/jboss-logmanager.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: jpackage-17-compat
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: dmlloyd-module-info
BuildRequires: jboss-modules
BuildRequires: jakarta-json-api
BuildRequires: parsson
BuildRequires: smallrye-common
BuildRequires: smallrye-common-constraint
BuildRequires: smallrye-common-cpu
BuildRequires: smallrye-common-expression
BuildRequires: smallrye-common-net
BuildRequires: smallrye-common-os
BuildRequires: smallrye-common-ref

%description
JBoss Log Manager is an implementation of java.util.logging.LogManager used
by JBoss and WildFly based projects.

%prep
%setup

%pom_remove_parent
%pom_remove_plugin :formatter-maven-plugin
%pom_remove_plugin :impsort-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :maven-surefire-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin io.github.dmlloyd.maven:module-services-plugin
%pom_remove_plugin org.codehaus.mojo:exec-maven-plugin
%pom_remove_dep org.jboss.byteman:byteman-bmunit5

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt README.adoc

%changelog
* Fri Mar 27 2026 Ivan Khanas <xeno@altlinux.org> 3.2.2-alt1
- First build for ALT.
