Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
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

%global dependency_analyzer_version 1.2
%global downloader_version 1.2

%global invoker_version 2.0.12
%global osgi_version 0.3.0
%global plugin_testing_harness_version 1.2

#this model is not included in parent pom
%global reporting_api_version 3.0

%global reporting_impl_version 2.1
%global repository_builder_version 1.0

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
Release:        alt9_28jpp7
License:        ASL 2.0
Group:          Development/Java

# svn export \
# http://svn.apache.org/repos/asf/maven/shared/tags/maven-shared-components-15/
# tar czf maven-shared-components-15.tar.gz maven-shared-components-15
Source0:        maven-shared-components-%{version}.tar.gz
Source1:        %{name}-jpp-depmap.xml
Patch: maven-dependency-analyzer-pom.xml.patch


BuildRequires:  ant
BuildRequires:  aqute-bnd
BuildRequires:  dom4j
BuildRequires:  easymock2
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  junit
BuildRequires:  maven
BuildRequires:  maven-artifact-manager
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-doxia
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-doxia-tools
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-model
BuildRequires:  maven-monitor
BuildRequires:  maven-plugin-cobertura
BuildRequires:  maven-plugin-testing-tools
BuildRequires:  maven-profile
BuildRequires:  maven-project
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-shared-file-management
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-site-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-report-plugin
BuildRequires:  maven-test-tools
BuildRequires:  maven-wagon
BuildRequires:  modello
BuildRequires:  objectweb-asm
BuildRequires:  plexus-component-api
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-digest
BuildRequires:  plexus-utils
BuildRequires:  saxon
BuildRequires:  saxon-scripts


Requires:       ant
Requires:       aqute-bnd
Requires:       dom4j
Requires:       jpackage-utils
Requires:       maven
Requires:       maven-wagon
Requires:       objectweb-asm
Requires:       plexus-digest
Requires:       plexus-utils
Requires:       plexus-utils
Requires:       saxon
Requires:       saxon-scripts

BuildArch:      noarch

# Obsoleting retired subpackages
Obsoletes:      maven-shared-ant < 1.0-27
Obsoletes:      maven-shared-model-converter < 2.3-27
Obsoletes:      maven-shared-ruhntime < 1.0-27
Source44: import.info

%description
Maven Shared Components

%package file-management
Summary:        Maven Shared File Management API
Group:          Development/Java
Version:        %{file_management_version}
Requires:  %{name}
Requires:  %{name}-io >= 0:%{io_version}
Requires:  maven
Requires:  plexus-containers-container-default
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
Requires:  plexus-containers-container-default

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
License:        ASL 2.0 and BSD and MIT
Requires:  %{name}
Requires:  junit

%description verifier
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Provides:       %{name}-file-management-javadoc = %{epoch}:%{file_management_version}-%{release}
Obsoletes:      %{name}-file-management-javadoc < %{epoch}:%{file_management_version}-%{release}
Provides:       %{name}-plugin-testing-harness-javadoc = %{epoch}:%{plugin_testing_harness_version}-%{release}
Obsoletes:      %{name}-plugin-testing-harness-javadoc < %{epoch}:%{plugin_testing_harness_version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

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


%prep
%setup -q -n %{name}-components-%{shared_components_version}
chmod -R go=u-w *

# Disable plugins that are not needed or are packaged separately
%pom_disable_module maven-ant
%pom_disable_module maven-archiver
%pom_disable_module maven-artifact-resolver
%pom_disable_module maven-dependency-tree
%pom_disable_module maven-doxia-tools
%pom_disable_module maven-filtering
%pom_disable_module maven-model-converter
%pom_disable_module maven-runtime

# Adding maven-reporting-api because otherwise it wouldn't build
%pom_xpath_inject pom:modules '<module>maven-reporting-api</module>'

# Adding missing dependencies to poms
%pom_add_dep org.apache.maven:maven-core:3.0.3              maven-downloader/pom.xml
%pom_add_dep org.apache.maven:maven-compat:3.0.3            maven-downloader/pom.xml
%pom_add_dep org.apache.maven:maven-compat:3.0.3            maven-repository-builder/pom.xml
%pom_add_dep org.apache.maven:maven-compat:3.0.3            maven-shared-io/pom.xml
%pom_add_dep org.codehaus.plexus:plexus-container-default   maven-shared-jar/pom.xml

# Replace plexus-maven-plugin with plexus-component-metadata
find -name 'pom.xml' -exec sed \
    -i 's/<artifactId>plexus-maven-plugin<\/artifactId>/<artifactId>plexus-component-metadata<\/artifactId>/' '{}' ';'
find -name 'pom.xml' -exec sed \
    -i 's/<goal>descriptor<\/goal>/<goal>generate-metadata<\/goal>/' '{}' ';'

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

%patch -p1

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

install -pm 644 maven-invoker/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-invoker.pom
install -p -m 0644 maven-invoker/target/maven-invoker-%{invoker_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/invoker.jar
%add_maven_depmap -f invoker JPP.%{name}-invoker.pom %{name}/invoker.jar

install -pm 644 maven-osgi/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-osgi.pom
install -p -m 0644 maven-osgi/target/maven-osgi-%{osgi_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/osgi.jar
%add_maven_depmap -f osgi JPP.%{name}-osgi.pom %{name}/osgi.jar

install -pm 644 file-management/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-file-management.pom
install -p -m 0644 file-management/target/file-management-%{file_management_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/file-management.jar
%add_maven_depmap -f file-management JPP.%{name}-file-management.pom %{name}/file-management.jar

install -pm 644 maven-reporting-api/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-shared-reporting-api.pom
install -p -m 0644 maven-reporting-api/target/maven-reporting-api-%{reporting_api_version}-SNAPSHOT.jar \
        $RPM_BUILD_ROOT%{_javadir}/maven-shared/reporting-api.jar
%add_maven_depmap -f reporting-api -a "org.apache.maven.reporting:maven-reporting-api" JPP.%{name}-reporting-api.pom %{name}/reporting-api.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc LICENSE.txt NOTICE.txt
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

%files dependency-analyzer
%{_javadir}/%{name}/dependency-analyzer.jar
%{_mavenpomdir}/JPP.%{name}-dependency-analyzer.pom
%{_mavendepmapfragdir}/%{name}-dependency-analyzer

%files downloader
%{_javadir}/%{name}/downloader.jar
%{_mavenpomdir}/JPP.%{name}-downloader.pom
%{_mavendepmapfragdir}/%{name}-downloader

%files invoker
%{_javadir}/%{name}/invoker.jar
%{_mavenpomdir}/JPP.%{name}-invoker.pom
%{_mavendepmapfragdir}/%{name}-invoker

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

%files reporting-api
%{_javadir}/%{name}/reporting-api.jar
%{_mavenpomdir}/JPP.%{name}-reporting-api.pom
%{_mavendepmapfragdir}/%{name}-reporting-api

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_28jpp7
- update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_24jpp7
- new fc release

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_23jpp7
- dropped versioned requires

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt8_23jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

