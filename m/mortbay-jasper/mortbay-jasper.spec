%define _unpackaged_files_terminate_build 1

Name: mortbay-jasper
Version: 9.0.119
Release: alt1

Summary: Apache Tomcat Jasper and EL libraries for Jetty EE8
License: Apache-2.0
Group: Development/Java
URL: https://github.com/jetty-project/jasper-jsp
VCS: https://github.com/jetty-project/jasper-jsp.git

Source0: %name-%version.tar
Patch0: system-maven.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.eclipse.jetty:jetty-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.eclipse.jdt:ecj)
BuildRequires: mvn(org.eclipse.jetty.toolchain:jetty-schemas)
# Select the current Servlet metadata alongside the Servlet 4 API.
BuildRequires: jakarta-servlet
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: tomcat-lib
BuildRequires: tomcat-el-3.0-api
BuildRequires: tomcat-jsp-2.3-api
BuildRequires: tomcat-servlet-4.0-api

%description
Common Maven parent for the Jasper JSP and Expression Language libraries
rebundled for use with Jetty EE8.

%package el
Summary: Expression Language API and implementation for Jetty EE8
Group: Development/Java

%description el
The javax.el API and the Apache EL implementation bundled for Jetty EE8.

%package jsp
Summary: Jasper JSP API and implementation for Jetty EE8
Group: Development/Java

%description jsp
The javax.servlet.jsp API and the Apache Jasper JSP compiler bundled for
Jetty EE8.

%prep
%setup
%autopatch -p1

# Use the qualified Tomcat 9 update for the binaries consumed by Shade.
%pom_xpath_set "/pom:project/pom:properties/pom:tomcat.version" 9.0.121
%pom_xpath_set "/pom:project/pom:properties/pom:ecj.version" 3.46.100

# Sources are unpacked upstream for the documentation and sources artifacts.
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_package :jasper-jsp
%mvn_package ":apache-el" el
%mvn_package ":mortbay-apache-el" el
%mvn_package ":apache-jsp" jsp
%mvn_package ":mortbay-apache-jsp" jsp
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files el -f .mfiles-el

%files jsp -f .mfiles-jsp

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 9.0.119-alt1
- Initial build for ALT.
