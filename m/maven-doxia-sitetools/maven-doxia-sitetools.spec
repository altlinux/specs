Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
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

%global parent maven-doxia
%global subproj sitetools

Name:           %{parent}-%{subproj}
Version:        1.2
Release:        alt2_5jpp7
Summary:        Doxia content generation framework
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/doxia/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-%{subproj}-%{version}-source-release.zip

# Point it at the correct plexus-container-default
Source1:        maven-doxia-depmap.xml

Patch0:         0001-Remove-clirr-dependency.patch
Patch1:         0002-Remove-htmlunit-dependency.patch
Patch2:         0003-Migration-to-component-metadata.patch

BuildRequires:  itext
BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia
BuildRequires:  modello-maven-plugin
BuildRequires:  classworlds
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-configuration
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-validator
BuildRequires:  junit
BuildRequires:  jakarta-oro
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-containers-component-javadoc
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-i18n
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  velocity
BuildRequires:  %{_javadir}/javamail/mail.jar

Requires:       classworlds
Requires:       apache-commons-collections
Requires:       apache-commons-configuration
Requires:       apache-commons-logging
Requires:       apache-commons-validator
Requires:       junit
Requires:       maven-doxia
Requires:       jakarta-oro
Requires:       plexus-containers-container-default
Requires:       plexus-i18n
Requires:       plexus-utils
Requires:       plexus-velocity
Requires:       velocity
Requires:       %{_javadir}/javamail/mail.jar

Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %%{name}.

%prep
%setup -q -n doxia-%{subproj}-%{version}

%patch0 -p1

# Disable tests that need htmlunit, until we get it in Fedora
%patch1 -p1

%patch2 -p1


%build

# tests can't run because of missing deps
mvn-rpmbuild \
      -e \
      -Dmaven.local.depmap.file=%{SOURCE1} \
      -Dmaven.test.skip=true \
      install javadoc:aggregate

%install

# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

install -m 644 -p pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-sitetools.pom
install -m 644 -p doxia-decoration-model/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-decoration-model.pom
install -m 644 -p doxia-site-renderer/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-site-renderer.pom
install -m 644 -p doxia-doc-renderer/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-doc-renderer.pom

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}

install -m 644 -p doxia-decoration-model/target/doxia-decoration-model-%{version}.jar \
	$RPM_BUILD_ROOT%{_javadir}/%{parent}/decoration-model.jar
install -m 644 -p doxia-site-renderer/target/doxia-site-renderer-%{version}.jar \
	$RPM_BUILD_ROOT%{_javadir}/%{parent}/site-renderer.jar
install -m 644 -p doxia-doc-renderer/target/doxia-doc-renderer-%{version}.jar \
	$RPM_BUILD_ROOT%{_javadir}/%{parent}/doc-renderer.jar

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP.%{parent}-sitetools.pom
%add_maven_depmap JPP.%{parent}-decoration-model.pom %{parent}/decoration-model.jar
%add_maven_depmap JPP.%{parent}-site-renderer.pom %{parent}/site-renderer.jar
%add_maven_depmap JPP.%{parent}-doc-renderer.pom %{parent}/doc-renderer.jar

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%{_javadir}/%{parent}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

