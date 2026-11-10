%define _unpackaged_files_terminate_build 1

Name: felix-prefs
Version: 1.1.0
Release: alt1

Summary: Apache Felix OSGi Preferences service
License: Apache-2.0
Group: Development/Java
URL: https://felix.apache.org/
VCS: https://github.com/apache/felix-dev.git

ExcludeArch: %ix86

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: javapackages-local
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: felix-parent
BuildRequires: maven-plugin-bundle

# Compile-time OSGi APIs and Commons Codec.
BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: osgi-annotation
BuildRequires: apache-commons-codec

# Maven lifecycle plugins needed for offline XMvn builds.
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)

Requires: apache-commons-codec

%description
Apache Felix Preferences implements persistent preferences for OSGi bundles.
This package includes the Preferences service OSGi bundle and Maven metadata.

%package javadoc
Summary: API documentation for Apache Felix Preferences
Group: Development/Documentation

%description javadoc
Java API documentation for the Apache Felix OSGi Preferences service.

%prep
%setup

%pom_change_dep org.osgi:org.osgi.core org.osgi:org.osgi.core:8.0.0
%pom_change_dep org.osgi:org.osgi.service.prefs org.osgi:osgi.cmpn:7.0.0

%pom_change_dep junit:junit junit:junit:4.13.2:test
%pom_change_dep org.mockito:mockito-all org.mockito:mockito-all:1.10.19:test

%pom_xpath_set pom:project/pom:properties/pom:felix.java.version 8

%build
%mvn_build -f -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc
%_datadir/javadoc/%name/

%changelog
* Thu Oct 22 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.1.0-alt1
- Initial build.
