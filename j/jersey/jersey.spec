%define _unpackaged_files_terminate_build 1

Name: jersey
Version: 4.0.2
Release: alt1

Summary: REST framework that provides JAX-RS Reference Implementation and more
License: EPL-2.0
Group: Development/Java
Url: https://github.com/eclipse-ee4j/jersey/wiki
Vcs: https://github.com/eclipse-ee4j/jersey.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: jackson-bom
BuildRequires: ee4j-parent
BuildRequires: maven-plugin-bundle
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-resolver
BuildRequires: jackson-parent
BuildRequires: maven-enforcer-rules
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-dependency-tree
BuildRequires: maven-lib
BuildRequires: maven-model
BuildRequires: jetty-servlet
BuildRequires: istack-commons-maven-plugin
BuildRequires: jaxb-api
BuildRequires: angus-activation
BuildRequires: jakarta-ws-rs
BuildRequires: atinject
BuildRequires: osgi-core
BuildRequires: glassfish-hk2-locator
BuildRequires: glassfish-hk2-extra-osgi-resource-locator
BuildRequires: javassist
BuildRequires: jakarta-validation-api
BuildRequires: jakarta-servlet
BuildRequires: jakarta-persistence
BuildRequires: jackson-module-jakarta-xmlbind-annotations
BuildRequires: jackson-module-jaxb-annotations
BuildRequires: jetty-server
BuildRequires: jetty-security
BuildRequires: jetty-util
BuildRequires: jetty-alpn-server
BuildRequires: jetty-http2-server

%description
Jersey is a REST framework that provides JAX-RS Reference Implementation and
more. Jersey provides its own APIs that extend the JAX-RS toolkit with
additional features and utilities to further simplify RESTful service and
client development. Jersey also exposes numerous extension SPIs so that
developers may extend Jersey to best suit their needs.

%package bom
Summary: Jersey BOM POM
Group: Development/Java
%description bom
Bill of materials POM for Jersey modules.

%package common
Summary: Jersey common core module
Group: Development/Java
%description common
Jersey core common module.

%package client
Summary: Jersey client core module
Group: Development/Java
%description client
Jersey client core module.

%package server
Summary: Jersey server core module
Group: Development/Java
%description server
Jersey server core module.

%package hk2
Summary: Jersey HK2 integration module
Group: Development/Java
%description hk2
Jersey HK2 integration module.

%package container-jdk-http
Summary: Jersey JDK HTTP container module
Group: Development/Java
%description container-jdk-http
Jersey container provider for JDK HTTP server.

%package container-servlet
Summary: Jersey servlet container module
Group: Development/Java
%description container-servlet
Jersey servlet container module.

%package container-jetty-http
Summary: Jersey Jetty HTTP container module
Group: Development/Java
%description container-jetty-http
Jersey container provider for Jetty HTTP server.

%package container-jetty-http2
Summary: Jersey Jetty HTTP/2 container module
Group: Development/Java
%description container-jetty-http2
Jersey container provider for Jetty HTTP/2 server.

%package entity-filtering
Summary: Jersey entity filtering extension
Group: Development/Java
%description entity-filtering
Jersey entity filtering extension module.

%package media-json-jackson
Summary: Jersey Jackson JSON media module
Group: Development/Java
%description media-json-jackson
Jersey media provider for Jackson JSON.

%prep
%setup

# Fix OSGi module name for module-info compilation
sed -i 's/requires static org\.osgi\.core;/requires static osgi.core;/' core-common/src/main/java/module-info.java

%pom_disable_module archetypes pom.xml
%pom_disable_module connectors pom.xml
%pom_disable_module incubator pom.xml
%pom_disable_module security pom.xml
%pom_disable_module bundles pom.xml
%pom_disable_module docs pom.xml
%pom_disable_module examples pom.xml
%pom_disable_module tests pom.xml
%pom_disable_module test-framework pom.xml

%pom_disable_module cdi2-se inject/pom.xml

%pom_disable_module glassfish containers/pom.xml
%pom_disable_module grizzly2-http containers/pom.xml
%pom_disable_module grizzly2-servlet containers/pom.xml
%pom_disable_module jetty-servlet containers/pom.xml
%pom_disable_module netty-http containers/pom.xml
%pom_disable_module helidon containers/pom.xml

%pom_disable_module bean-validation ext/pom.xml
%pom_disable_module cdi ext/pom.xml
%pom_disable_module constants ext/pom.xml
%pom_disable_module metainf-services ext/pom.xml
%pom_disable_module micrometer ext/pom.xml
%pom_disable_module mvc ext/pom.xml
%pom_disable_module mvc-bean-validation ext/pom.xml
%pom_disable_module mvc-freemarker ext/pom.xml
%pom_disable_module mvc-jsp ext/pom.xml
%pom_disable_module mvc-mustache ext/pom.xml
%pom_disable_module mvc-thymeleaf ext/pom.xml
%pom_disable_module proxy-client ext/pom.xml
%pom_disable_module rx ext/pom.xml
%pom_disable_module spring6 ext/pom.xml
%pom_disable_module wadl-doclet ext/pom.xml
%pom_disable_module microprofile ext/pom.xml

%pom_disable_module jaxb media/pom.xml
%pom_disable_module json-binding media/pom.xml
%pom_disable_module json-gson media/pom.xml
%pom_disable_module json-jettison media/pom.xml
%pom_disable_module json-processing media/pom.xml
%pom_disable_module moxy media/pom.xml
%pom_disable_module multipart media/pom.xml
%pom_disable_module sse media/pom.xml

%pom_remove_plugin org.codehaus.mojo:flatten-maven-plugin pom.xml
%pom_remove_plugin org.codehaus.mojo:flatten-maven-plugin bom/pom.xml
%pom_remove_plugin org.commonjava.maven.plugins:directory-maven-plugin pom.xml
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin pom.xml
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin pom.xml
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin pom.xml
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin bom/pom.xml
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin core-common/pom.xml
%pom_xpath_remove -f "//pom:extension[pom:groupId='org.glassfish' and pom:artifactId='findbugs']" pom.xml
%pom_remove_dep -f org.eclipse.jetty.toolchain:jetty-jakarta-servlet-api containers/jetty-http/pom.xml
%pom_remove_dep -f org.eclipse.jetty:jetty-alpn-conscrypt-server containers/jetty-http2/pom.xml
%pom_add_dep org.eclipse.jetty:jetty-alpn-server containers/jetty-http2/pom.xml

# Bundle plugin stays enabled; avoid failing on missing generated legal dir
sed -i 's|<Include-Resource>{maven-resources},${project.build.directory}/legal</Include-Resource>|<Include-Resource>{maven-resources}</Include-Resource>|' pom.xml

# OSGi module names available in ALT
%pom_add_dep org.glassfish.hk2:osgi-resource-locator core-common/pom.xml

# Do not install intermediate parent POMs with duplicate artifactId "project"
%mvn_package org.glassfish.jersey.inject:project __noinstall
%mvn_package org.glassfish.jersey.containers:project __noinstall
%mvn_package org.glassfish.jersey.ext:project __noinstall
%mvn_package org.glassfish.jersey.media:project __noinstall
%mvn_package org.glassfish.jersey:project __noinstall

# Compat alias needed by greenmail
%mvn_alias org.glassfish.jersey.containers:jersey-container-servlet org.glassfish.jersey.containers:jersey-container-servlet-core

%build
%mvn_build -s -j -f

%install
%pom_remove_parent pom.xml
%mvn_install

%files bom -f .mfiles-jersey-bom
%files common -f .mfiles-jersey-common
%files client -f .mfiles-jersey-client
%files server -f .mfiles-jersey-server
%files hk2 -f .mfiles-jersey-hk2
%files container-jdk-http -f .mfiles-jersey-container-jdk-http
%files container-servlet -f .mfiles-jersey-container-servlet
%files container-jetty-http -f .mfiles-jersey-container-jetty-http
%files container-jetty-http2 -f .mfiles-jersey-container-jetty-http2
%files entity-filtering -f .mfiles-jersey-entity-filtering
%files media-json-jackson -f .mfiles-jersey-media-json-jackson

%changelog
* Wed Mar 18 2026 Ivan Khanas <xeno@altlinux.org> 4.0.2-alt1
- Initial build for ALT.
