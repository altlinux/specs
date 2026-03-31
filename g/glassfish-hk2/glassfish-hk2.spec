%define _unpackaged_files_terminate_build 1

Name: glassfish-hk2
Version: 3.1.1
Release: alt1

Summary: A light-weight and dynamic dependency injection framework
License: EPL-2.0
Group: Development/Java
Url: https://eclipse-ee4j.github.io/glassfish-hk2
Vcs: https://github.com/eclipse-ee4j/glassfish-hk2.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: ee4j-parent
BuildRequires: maven-dependency-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-plugin-annotations
BuildRequires: maven-osgi
BuildRequires: jboss-logging
BuildRequires: easymock
BuildRequires: aopalliance
BuildRequires: atinject
BuildRequires: glassfish-hk2-extra
BuildRequires: google-guice
BuildRequires: javassist
BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: osgi-annotation
BuildRequires: objectweb-asm
BuildRequires: junit
BuildRequires: jakarta-validation-api
BuildRequires: hibernate-validator
BuildRequires: jaxb-api
BuildRequires: jaxb-runtime
BuildRequires: protobuf-java
BuildRequires: jakarta-json
BuildRequires: java-classmate
BuildRequires: parsson
BuildRequires: jakarta-el-api
BuildRequires: jakarta-el

%description
%summary

%package api
Summary: HK2 API module
Group: Development/Java
%description api
HK2 API module

%package locator
Summary: ServiceLocator Default Implementation
Group: Development/Java
%description locator
ServiceLocator Default Implementation

%package utils
Summary: HK2 Implementation Utilities
Group: Development/Java
%description utils
HK2 Implementation Utilities

%package core
Summary: HK2 core module
Group: Development/Java
%description core
HK2 core module

%package runlevel
Summary: Run Level Service
Group: Development/Java
%description runlevel
HK2 Run Level Service

%package junitrunner
Summary: HK2 JUnit Runner
Group: Development/Java
%description junitrunner
HK2 JUnit Runner

%package extras
Summary: HK2 extras module
Group: Development/Java
%description extras
HK2 extras module

%package bundle
Summary: HK2 module of HK2 itself (bundle)
Group: Development/Java
%description bundle
HK2 module of HK2 itself - convenience OSGi bundle

%package class-model
Summary: Class Model for HK2
Group: Development/Java
%description class-model
Class Model for HK2

%package osgi-adapter
Summary: HK2 OSGi Adapter
Group: Development/Java
%description osgi-adapter
HK2 OSGi Adapter

%package guice-bridge
Summary: HK2 Guice Bridge
Group: Development/Java
%description guice-bridge
HK2 Guice Bridge

%package jmx
Summary: HK2 JMX module
Group: Development/Java
%description jmx
HK2 JMX module

%package configuration-hub
Summary: HK2 Configuration Hub
Group: Development/Java
%description configuration-hub
HK2 Configuration Hub

%package configuration-integration
Summary: HK2 Configuration Integration
Group: Development/Java
%description configuration-integration
HK2 Configuration Integration

%package property-file
Summary: HK2 Configuration Property File Reader
Group: Development/Java
%description property-file
HK2 Configuration Property File Reader

%package aopalliance-repackaged
Summary: aopalliance repackaged as OSGi bundle
Group: Development/Java
%description aopalliance-repackaged
aopalliance repackaged as OSGi bundle

%package metadata-generator
Summary: HK2 Metadata Generator
Group: Development/Java
%description metadata-generator
HK2 Metadata Generator

%package metadata-generator-test1
Summary: HK2 Metadata Generator Test One
Group: Development/Java
%description metadata-generator-test1
HK2 Metadata Generator Test One

%package inhabitant-generator
Summary: HK2 Inhabitant Generator Maven plugin
Group: Development/Java
%description inhabitant-generator
HK2 Inhabitant Generator Maven plugin

%package consolidatedbundle-plugin
Summary: HK2 Consolidated Bundle Maven plugin
Group: Development/Java
%description consolidatedbundle-plugin
HK2 Consolidated Bundle Maven plugin

%package osgiversion-plugin
Summary: OSGiVersion Maven Plugin
Group: Development/Java
%description osgiversion-plugin
OSGiVersion Maven Plugin

%package xml
Summary: HK2 XML module
Group: Development/Java
%description xml
HK2 XML module for binding XML configuration to HK2 beans.

%package xml-schema
Summary: HK2 XML schema module
Group: Development/Java
%description xml-schema
HK2 XML schema module for HK2 XML integration.

%package pbuf
Summary: HK2 PBUF module
Group: Development/Java
%description pbuf
HK2 PBUF serialization support module.

%package json
Summary: HK2 JSON module
Group: Development/Java
%description json
HK2 JSON binding module.

%package external
Summary: HK2 external dependencies parent POM
Group: Development/Java
%description external
POM metadata for HK2 external dependencies module.

%package bom
Summary: HK2 BOM POM
Group: Development/Java
%description bom
Bill of materials POM for HK2 components.

%package configuration
Summary: HK2 configuration parent POM
Group: Development/Java
%description configuration
Parent POM for HK2 configuration modules.

%package configuration-persistence
Summary: HK2 configuration persistence parent POM
Group: Development/Java
%description configuration-persistence
Parent POM for HK2 configuration persistence modules.

%package metadata-generator-parent
Summary: HK2 metadata generator parent POM
Group: Development/Java
%description metadata-generator-parent
Parent POM for HK2 metadata generator modules.

%package parent
Summary: HK2 parent POM
Group: Development/Java
%description parent
Parent POM for GlassFish HK2 artifacts.

%package testing
Summary: HK2 testing parent POM
Group: Development/Java
%description testing
Parent POM for HK2 testing modules.

%package xml-parent
Summary: HK2 XML parent POM
Group: Development/Java
%description xml-parent
Parent POM for HK2 XML modules.

%package maven-plugins
Summary: HK2 Maven plugins parent POM
Group: Development/Java
%description maven-plugins
Parent POM for HK2 Maven plugin modules.

%package osgi
Summary: HK2 OSGi parent POM
Group: Development/Java
%description osgi
Parent POM for HK2 OSGi modules.

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :findbugs-maven-plugin

# Disable examples, test utilities, and modules with unavailable deps (Spring)
%pom_disable_module examples
%pom_disable_module spring-bridge

# hk2-xml submodules with unavailable deps
%pom_disable_module integration-test hk2-configuration/persistence/hk2-xml
%pom_disable_module test1 hk2-configuration/persistence/hk2-xml

# Keep only hk2-junitrunner from hk2-testing; disable other test utilities
%pom_disable_module ant hk2-testing
%pom_disable_module hk2-locator-extras hk2-testing
%pom_disable_module hk2-testng hk2-testing
%pom_disable_module hk2-runlevel-extras hk2-testing
%pom_disable_module hk2-locator-no-proxies hk2-testing
%pom_disable_module hk2-locator-no-proxies2 hk2-testing
%pom_disable_module interceptor-events hk2-testing
%pom_disable_module hk2-mockito hk2-testing
%pom_disable_module collections hk2-testing
%pom_disable_module jersey hk2-testing
%pom_disable_module adapter-tests osgi

# aopalliance-repackaged only embeds classes into final JAR via bundle plugin,
# but hk2-api needs them at compile time directly
%pom_add_dep aopalliance:aopalliance hk2-api

%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations::provided maven-plugins/osgiversion-maven-plugin
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations::provided maven-plugins/consolidatedbundle-maven-plugin
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations::provided maven-plugins/hk2-inhabitant-generator

# osgi.enterprise not in ALT; class-model only uses org.osgi.framework (in osgi-core)
%pom_change_dep org.osgi:osgi.enterprise org.osgi:osgi.core class-model

# felix-bundlerepository not in ALT; remove OBR-dependent source files
rm osgi/adapter/src/main/java/org/jvnet/hk2/osgiadapter/ObrHandler.java
rm osgi/adapter/src/main/java/org/jvnet/hk2/osgiadapter/OSGiObrBasedRepository.java
rm osgi/adapter/src/main/java/org/jvnet/hk2/osgiadapter/OSGiObrModuleImpl.java
rm osgi/adapter/src/main/java/org/jvnet/hk2/osgiadapter/OSGiObrModulesRegistryImpl.java

%build
%mvn_build -s -j -f

%install
%mvn_install

%files
%doc --no-dereference LICENSE.md NOTICE.md README.md

%files api -f .mfiles-hk2-api
%files locator -f .mfiles-hk2-locator
%files utils -f .mfiles-hk2-utils
%files core -f .mfiles-hk2-core
%files runlevel -f .mfiles-hk2-runlevel
%files junitrunner -f .mfiles-hk2-junitrunner
%files extras -f .mfiles-hk2-extras
%files bundle -f .mfiles-hk2
%files class-model -f .mfiles-class-model
%files osgi-adapter -f .mfiles-osgi-adapter
%files guice-bridge -f .mfiles-guice-bridge
%files jmx -f .mfiles-hk2-jmx
%files configuration-hub -f .mfiles-hk2-configuration-hub
%files configuration-integration -f .mfiles-hk2-configuration-integration
%files property-file -f .mfiles-hk2-property-file
%files aopalliance-repackaged -f .mfiles-aopalliance-repackaged
%files metadata-generator -f .mfiles-hk2-metadata-generator
%files metadata-generator-test1 -f .mfiles-hk2-metadata-generator-test1
%files inhabitant-generator -f .mfiles-hk2-inhabitant-generator
%files consolidatedbundle-plugin -f .mfiles-consolidatedbundle-maven-plugin
%files osgiversion-plugin -f .mfiles-osgiversion-maven-plugin
%files xml -f .mfiles-hk2-xml
%files xml-schema -f .mfiles-hk2-xml-schema
%files pbuf -f .mfiles-hk2-pbuf
%files json -f .mfiles-hk2-json
%files external -f .mfiles-external
%files bom -f .mfiles-hk2-bom
%files configuration -f .mfiles-hk2-configuration
%files configuration-persistence -f .mfiles-hk2-configuration-persistence
%files metadata-generator-parent -f .mfiles-hk2-metadata-generator-parent
%files parent -f .mfiles-hk2-parent
%files testing -f .mfiles-hk2-testing
%files xml-parent -f .mfiles-hk2-xml-parent
%files maven-plugins -f .mfiles-maven-plugins
%files osgi -f .mfiles-osgi

%changelog
* Tue Mar 24 2026 Ivan Khanas <xeno@altlinux.org> 3.1.1-alt1
- First build for ALT.
