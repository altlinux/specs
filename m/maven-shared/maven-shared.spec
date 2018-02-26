%def_with artifact_resolver
Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global shared_components_version 15
%global file_management_version 1.2.2
%global ant_version 1.0

%global artifact_resolver_version 1.1

%global common_artifact_filters_version 1.3
%global dependency_analyzer_version 1.2
%global dependency_tree_version 1.3
%global downloader_version 1.2


%global invoker_version 2.0.12
%global model_converter_version 2.3
%global osgi_version 0.3.0
%global plugin_testing_harness_version 1.2

#this model is not included in parent pom
%global reporting_api_version 3.0

%global reporting_impl_version 2.1
%global repository_builder_version 1.0

%global runtime_version 1.0

%global io_version 1.2
%global jar_version 1.1
%global monitor_version 1.0
### disabled by pom.xml default
#%global script_ant_version 2.1
#%global script_beanshell_version 2.1
#%global test_tools_version 1.0
#%global toolchain_version 1.0
%global verifier_version 1.3

Summary:        Maven Shared Components
URL:            http://maven.apache.org/shared/
Name:           maven-shared
Version:        15
Release:        alt9_23jpp7
License:        ASL 2.0
Group:          Development/Java

# svn export \
# http://svn.apache.org/repos/asf/maven/shared/tags/maven-shared-components-15/
# tar czf maven-shared-components-15.tar.gz maven-shared-components-15
Source0:        maven-shared-components-%{version}.tar.gz
Source1:        %{name}-jpp-depmap.xml

Patch0:        %{name}-pom.patch
Patch1:        %{name}-maven3.patch
Patch2:        %{name}-maven-model-v3-removal.patch
Patch3:        %{name}-migration-to-component-metadata.patch
Patch6:         maven-runtime-XMLMavenRuntimeVisitor.patch
Patch7:         maven-shared-Add-container-default-to-shared-jar.patch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-report-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-doxia-tools
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-shared-file-management
BuildRequires:  maven-plugin-testing-tools
BuildRequires:  maven-test-tools
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-component-api
BuildRequires:  maven-plugin-cobertura
BuildRequires:  junit
BuildRequires:  saxon
BuildRequires:  saxon-scripts
BuildRequires:  plexus-utils
BuildRequires:  plexus-digest
BuildRequires:  modello
BuildRequires:  easymock2
BuildRequires:  objectweb-asm
BuildRequires:  dom4j
BuildRequires:  aqute-bnd
BuildRequires:  maven-wagon
BuildRequires:  maven-artifact-manager
BuildRequires:  maven-project
BuildRequires:  maven-profile
#BuildRequires:  maven-plugin-registry
BuildRequires:  maven-monitor
BuildRequires:  maven-model


Requires:       ant
Requires:       maven
Requires:       plexus-utils
Requires:       saxon
Requires:       saxon-scripts
Requires:       plexus-utils
Requires:       plexus-digest
Requires:       objectweb-asm
Requires:       dom4j
Requires:       aqute-bnd
Requires:       maven-wagon

BuildArch:      noarch
Source44: import.info

%description
Maven Shared Components

%package file-management
Summary:        Maven Shared File Management API
Group:          Development/Java
Version:        %{file_management_version}
Requires:  %{name}
Requires:  %{name}-io
Requires:  maven
Requires:  plexus-container-default
Requires:  plexus-utils

%description file-management
API to collect files from a given directory using
several include/exclude rules.

%package osgi
Summary:        Maven OSGi
Group:          Development/Java
Version:        %{osgi_version}
Requires:  %{name}
Requires:  aqute-bnd
Requires:  maven-project

%description osgi
Library for Maven-OSGi integration

%package ant
Summary:        Maven Ant
Group:          Development/Java
Version:        %{ant_version}
Requires:  %{name}
Requires:  ant
Requires:  plexus-containers-container-default
Requires:  maven-project
Requires:  maven

%description ant
Runs ant scripts embedded in the POM.

%package common-artifact-filters
Summary:        Maven Common Artifact Filters
Group:          Development/Java
Version:        %{common_artifact_filters_version}
Requires:  %{name}
Requires:  %{name}-test-tools
Requires:  junit
Requires:  plexus-container-default
Requires:  plexus-utils
Requires:  maven-project
Requires:  maven

%description common-artifact-filters
%{summary}.

%package dependency-tree
Summary:        Maven Dependency Tree
Group:          Development/Java
Version:        %{dependency_tree_version}
Requires:  %{name}
Requires:  %{name}-plugin-testing-harness
Requires:  maven
Requires:  maven-project

%description dependency-tree
%{summary}.

%package downloader
Summary:        Maven Downloader
Group:          Development/Java
Version:        %{downloader_version}
Requires:  %{name}
Requires:  maven
Requires:  maven-artifact-manager

%description downloader
Provide a super simple interface for downloading a
single artifact.

%package dependency-analyzer
Summary:        Maven Dependency Analyzer
Group:          Development/Java
Version:        %{dependency_analyzer_version}
Requires:  %{name}
Requires:  maven
Requires:  maven-project
Requires:  objectweb-asm
Requires:  plexus-utils

%description dependency-analyzer
%{summary}.

%package invoker
Summary:        Maven Process Invoker
Group:          Development/Java
Version:        %{invoker_version}
Requires:  %{name}
Requires:  %{name}-monitor
Requires:  maven
Requires:  plexus-utils

%description invoker
%{summary}.

%package model-converter
Summary:        Maven Model Converter
Group:          Development/Java
Version:        %{model_converter_version}
Requires:  %{name}
Requires:  dom4j
Requires:  maven
Requires:  maven-model
Requires:  plexus-container-default
Requires:  plexus-utils

%description model-converter
Converts between version 3.0.0 and version 4.0.0 models.

%package reporting-impl
Summary:        Maven Reporting Implementation
Group:          Development/Java
Version:        %{reporting_impl_version}
Requires:  %{name}
Requires:  apache-commons-validator
Requires:  jakarta-oro
Requires:  maven
Requires:  maven-project
Requires:  maven-doxia
Requires:  apache-commons-validator
Requires:  plexus-utils

%description reporting-impl
%{summary}.

%package repository-builder
Summary:        Maven Repository Builder
Group:          Development/Java
Version:        %{repository_builder_version}
Requires:  %{name}
Requires:  %{name}-common-artifact-filters
Requires:  maven
Requires:  maven-artifact-manager
Requires:  maven-project

%description repository-builder
%{summary}.

%package io
Summary:        Maven Shared I/O API
Group:          Development/Java
Version:        %{io_version}
Requires:  %{name}
Requires:  maven
Requires:  maven-artifact-manager
Requires:  maven-wagon
Requires:  plexus-utils
Requires:  plexus-container-default

%description io
%{summary}.

%package jar
Summary:        Maven Shared Jar
Group:          Development/Java
Version:        %{jar_version}
Requires:  %{name}
Requires:  maven
Requires:  plexus-digest
Requires:  bcel
Requires:  apache-commons-collections

%description jar
Utilities that help identify the contents of a JAR,
including Java class analysis and Maven metadata
analysis.

%package monitor
Summary:        Maven Shared Monitor API
Group:          Development/Java
Version:        %{monitor_version}
Requires:  %{name}
Requires:  maven
Requires:  plexus-containers-container-default

%description monitor
%{summary}.

%package verifier
Summary:        Maven Verifier Component
Group:          Development/Java
Version:        %{verifier_version}
Requires:  %{name}
Requires:  junit

%description verifier
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Provides:       %{name}-file-management-javadoc = %{epoch}:%{file_management_version}-%{release}
Obsoletes:      %{name}-file-management-javadoc < %{epoch}:%{file_management_version}-%{release}
Provides:       %{name}-plugin-testing-harness-javadoc = %{epoch}:%{plugin_testing_harness_version}-%{release}
Obsoletes:      %{name}-plugin-testing-harness-javadoc < %{epoch}:%{plugin_testing_harness_version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%if_with artifact_resolver
%package artifact-resolver
Summary:        Maven Artifact Resolution API
Group:          Development/Java
Version:        %{artifact_resolver_version}
Requires:  %{name}
Requires:  ant
Requires:  maven
Requires:  maven-artifact-manager
Requires:  maven-project
%endif #artifact_resolver

%if_with artifact_resolver
%description artifact-resolver
Provides a component for plugins to easily resolve project dependencies.
%endif #artifact_resolver

%package reporting-api
Summary:        Maven Reporting API
Group:          Development/Java
Version:        %{reporting_api_version}
Requires:  %{name}
Requires:  ant
Requires:  maven
Requires:  maven-doxia

%description reporting-api
Maven Reporting API.

%package runtime
Summary:        Maven Runtime
Group:          Development/Java
Version:        %{runtime_version}
Requires:  %{name}
Requires:  ant
Requires:  maven
Requires:  maven-project

%description runtime
Maven Runtime allows introspection of Maven project metadata at runtime.  Basic artifact information or full Maven
project metadata can be obtained for all projects within a given class loader, optionally sorted into dependency
order, and also for a given class within a project.

%prep
%setup -q -n %{name}-components-%{shared_components_version}
chmod -R go=u-w *
%patch0 -b .sav0
%patch1 -p1 -b .sav1
%patch6 -b .sav6
%patch2 -p1
%patch3 -p1
%patch7 -p1

# Fix aqute-bnd dependency
sed -i "s|<artifactId>bndlib|<artifactId>bnd|g" maven-osgi/pom.xml

# need namespace for new version modello
sed -i "s|<model>|<model xmlns=\"http://modello.codehaus.org/MODELLO/1.3.0\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://modello.codehaus.org/MODELLO/1.3.0 http://modello.codehaus.org/xsd/modello-1.3.0.xsd\" xml.namespace=\"..\" xml.schemaLocation=\"..\" xsd.namespace=\"..\" xsd.targetNamespace=\"..\">|" file-management/src/main/mdo/fileset.mdo

sed -i "s|<groupId>ant|<groupId>org.apache.ant|g" maven-ant/pom.xml
# Remove test that needs junit-addons until that makes it into Fedora
rm -f maven-reporting-impl/src/test/java/org/apache/maven/reporting/AbstractMavenReportRendererTest.java

# Remove tests that need jmock (for now)
rm -f maven-dependency-analyzer/src/test/java/org/apache/maven/shared/dependency/analyzer/InputStreamConstraint.java
rm -f maven-dependency-analyzer/src/test/java/org/apache/maven/shared/dependency/analyzer/ClassFileVisitorUtilsTest.java
rm -f maven-dependency-analyzer/src/test/java/org/apache/maven/shared/dependency/analyzer/AbstractFileTest.java

%build
export MAVEN_OPTS="-XX:MaxPermSize=256m"
mvn-rpmbuild \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install

# main package infrastructure
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven-shared
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}

# poms and jars
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-components-parent.pom
%add_maven_depmap JPP.%{name}-components-parent.pom

install -pm 644 maven-downloader/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-downloader.pom
install -p -m 0644 maven-downloader/target/maven-downloader-%{downloader_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/downloader.jar
%add_maven_depmap -f downloader JPP.%{name}-downloader.pom %{name}/downloader.jar

install -pm 644 maven-dependency-analyzer/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-dependency-analyzer.pom
install -p -m 0644 maven-dependency-analyzer/target/maven-dependency-analyzer-%{dependency_analyzer_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/dependency-analyzer.jar
%add_maven_depmap -f dependency-analyzer JPP.%{name}-dependency-analyzer.pom %{name}/dependency-analyzer.jar

install -pm 644 maven-dependency-tree/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-dependency-tree.pom
install -p -m 0644 maven-dependency-tree/target/maven-dependency-tree-%{dependency_tree_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/dependency-tree.jar
%add_maven_depmap -f dependency-tree JPP.%{name}-dependency-tree.pom %{name}/dependency-tree.jar

install -pm 644 maven-verifier/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-verifier.pom
install -p -m 0644 maven-verifier/target/maven-verifier-%{verifier_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/verifier.jar
%add_maven_depmap -f verifier JPP.%{name}-verifier.pom %{name}/verifier.jar

install -pm 644 maven-shared-monitor/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-monitor.pom
install -p -m 0644 maven-shared-monitor/target/maven-shared-monitor-%{monitor_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/monitor.jar
%add_maven_depmap -f monitor JPP.%{name}-monitor.pom %{name}/monitor.jar

install -pm 644 maven-shared-io/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-io.pom
install -p -m 0644 maven-shared-io/target/maven-shared-io-%{io_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/io.jar
%add_maven_depmap -f io JPP.%{name}-io.pom %{name}/io.jar

install -pm 644 maven-shared-jar/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-jar.pom
install -p -m 0644 maven-shared-jar/target/maven-shared-jar-%{jar_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/jar.jar
%add_maven_depmap -f jar JPP.%{name}-jar.pom %{name}/jar.jar

install -pm 644 maven-repository-builder/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-repository-builder.pom
install -p -m 0644 maven-repository-builder/target/maven-repository-builder-%{repository_builder_version}-alpha-3-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/repository-builder.jar
%add_maven_depmap -f repository-builder JPP.%{name}-repository-builder.pom %{name}/repository-builder.jar

install -pm 644 maven-reporting-impl/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-reporting-impl.pom
install -p -m 0644 maven-reporting-impl/target/maven-reporting-impl-%{reporting_impl_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/reporting-impl.jar
%add_maven_depmap -f reporting-impl JPP.%{name}-reporting-impl.pom %{name}/reporting-impl.jar

install -pm 644 maven-model-converter/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-model-converter.pom
install -p -m 0644 maven-model-converter/target/maven-model-converter-%{model_converter_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/model-converter.jar
%add_maven_depmap -f model-converter JPP.%{name}-model-converter.pom %{name}/model-converter.jar

install -pm 644 maven-invoker/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-invoker.pom
install -p -m 0644 maven-invoker/target/maven-invoker-%{invoker_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/invoker.jar
%add_maven_depmap -f invoker JPP.%{name}-invoker.pom %{name}/invoker.jar

install -pm 644 maven-common-artifact-filters/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-common-artifact-filters.pom
install -p -m 0644 maven-common-artifact-filters/target/maven-common-artifact-filters-%{common_artifact_filters_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/common-artifact-filters.jar
%add_maven_depmap -f common-artifact-filters JPP.%{name}-common-artifact-filters.pom %{name}/common-artifact-filters.jar

install -pm 644 maven-ant/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-ant.pom
install -p -m 0644 maven-ant/target/maven-ant-%{ant_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/ant.jar
%add_maven_depmap -f ant JPP.%{name}-ant.pom %{name}/ant.jar

install -pm 644 maven-osgi/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-osgi.pom
install -p -m 0644 maven-osgi/target/maven-osgi-%{osgi_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/osgi.jar
%add_maven_depmap -f osgi JPP.%{name}-osgi.pom %{name}/osgi.jar

install -pm 644 file-management/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-file-management.pom
install -p -m 0644 file-management/target/file-management-%{file_management_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/file-management.jar
%add_maven_depmap -f file-management JPP.%{name}-file-management.pom %{name}/file-management.jar

install -pm 644 maven-artifact-resolver/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-artifact-resolver.pom
install -p -m 0644 maven-artifact-resolver/target/maven-artifact-resolver-%{artifact_resolver_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/artifact-resolver.jar
%add_maven_depmap -f artifact-resolver JPP.%{name}-artifact-resolver.pom %{name}/artifact-resolver.jar

install -pm 644 maven-reporting-api/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-reporting-api.pom
install -p -m 0644 maven-reporting-api/target/maven-reporting-api-%{reporting_api_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/reporting-api.jar
%add_maven_depmap -f reporting-api -a "org.apache.maven.reporting:maven-reporting-api" JPP.%{name}-reporting-api.pom %{name}/reporting-api.jar

install -pm 644 maven-runtime/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-runtime.pom
install -p -m 0644 maven-runtime/target/maven-runtime-%{runtime_version}-alpha-3-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/runtime.jar
%add_maven_depmap -f runtime JPP.%{name}-runtime.pom %{name}/runtime.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%dir %{_javadir}/%{name}
%{_mavenpomdir}/JPP.%{name}-components-parent.pom
%{_mavendepmapfragdir}/%{name}

%files file-management
%{_javadir}/%{name}/file-management.jar
%{_mavenpomdir}/JPP.%{name}-file-management.pom
%{_mavendepmapfragdir}/%{name}-file-management

%files osgi
%{_javadir}/%{name}/osgi.jar
%{_mavenpomdir}/JPP.%{name}-osgi.pom
%{_mavendepmapfragdir}/%{name}-osgi

%files ant
%{_javadir}/%{name}/ant.jar
%{_mavenpomdir}/JPP.%{name}-ant.pom
%{_mavendepmapfragdir}/%{name}-ant

%files common-artifact-filters
%{_javadir}/%{name}/common-artifact-filters.jar
%{_mavenpomdir}/JPP.%{name}-common-artifact-filters.pom
%{_mavendepmapfragdir}/%{name}-common-artifact-filters

%files dependency-analyzer
%{_javadir}/%{name}/dependency-analyzer.jar
%{_mavenpomdir}/JPP.%{name}-dependency-analyzer.pom
%{_mavendepmapfragdir}/%{name}-dependency-analyzer

%files dependency-tree
%{_javadir}/%{name}/dependency-tree.jar
%{_mavenpomdir}/JPP.%{name}-dependency-tree.pom
%{_mavendepmapfragdir}/%{name}-dependency-tree

%files downloader
%{_javadir}/%{name}/downloader.jar
%{_mavenpomdir}/JPP.%{name}-downloader.pom
%{_mavendepmapfragdir}/%{name}-downloader

%files invoker
%{_javadir}/%{name}/invoker.jar
%{_mavenpomdir}/JPP.%{name}-invoker.pom
%{_mavendepmapfragdir}/%{name}-invoker

%files model-converter
%{_javadir}/%{name}/model-converter.jar
%{_mavenpomdir}/JPP.%{name}-model-converter.pom
%{_mavendepmapfragdir}/%{name}-model-converter

%files reporting-impl
%{_javadir}/%{name}/reporting-impl.jar
%{_mavenpomdir}/JPP.%{name}-reporting-impl.pom
%{_mavendepmapfragdir}/%{name}-reporting-impl

%files repository-builder
%{_javadir}/%{name}/repository-builder.jar
%{_mavenpomdir}/JPP.%{name}-repository-builder.pom
%{_mavendepmapfragdir}/%{name}-repository-builder

%files io
%{_javadir}/%{name}/io.jar
%{_mavenpomdir}/JPP.%{name}-io.pom
%{_mavendepmapfragdir}/%{name}-io

%files jar
%{_javadir}/%{name}/jar.jar
%{_mavenpomdir}/JPP.%{name}-jar.pom
%{_mavendepmapfragdir}/%{name}-jar

%files monitor
%{_javadir}/%{name}/monitor.jar
%{_mavenpomdir}/JPP.%{name}-monitor.pom
%{_mavendepmapfragdir}/%{name}-monitor

%files verifier
%{_javadir}/%{name}/verifier.jar
%{_mavenpomdir}/JPP.%{name}-verifier.pom
%{_mavendepmapfragdir}/%{name}-verifier

%if_with artifact_resolver
%files artifact-resolver
%{_javadir}/%{name}/artifact-resolver.jar
%{_mavenpomdir}/JPP.%{name}-artifact-resolver.pom
%{_mavendepmapfragdir}/%{name}-artifact-resolver
%endif #artifact_resolver

%files reporting-api
%{_javadir}/%{name}/reporting-api.jar
%{_mavenpomdir}/JPP.%{name}-reporting-api.pom
%{_mavendepmapfragdir}/%{name}-reporting-api

%files runtime
%{_javadir}/%{name}/runtime.jar
%{_mavenpomdir}/JPP.%{name}-runtime.pom
%{_mavendepmapfragdir}/%{name}-runtime

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_23jpp7
- dropped versioned requires

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt8_23jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

