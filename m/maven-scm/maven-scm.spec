Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

Name:           maven-scm
Version:        1.9.5
Release:        alt1_6jpp8
Summary:        Common API for doing SCM operations
License:        ASL 2.0
URL:            http://maven.apache.org/scm
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/maven/scm/%{name}-%{version}-source-release.zip

# Patch to migrate to new plexus default container
# This has been sent upstream: https://issues.apache.org/jira/browse/SCM-731
Patch1:         0001-Port-maven-scm-to-latest-version-of-plexus-default-c.patch
# Workaround upstream's workaround for a modello bug, see: https://issues.apache.org/jira/browse/SCM-518
Patch2:         0002-Fix-vss-modello-config.patch
# Compatibility with JGit 4.x, not yet forwarded
Patch3:         0003-Compatibility-with-JGit-4.0.0.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.sonatype.plexus:plexus-sec-dispatcher)
Source44: import.info

%description
Maven SCM supports Maven plugins (e.g. maven-release-plugin) and other
tools (e.g. Continuum) in providing them a common API for doing SCM operations.

%package test
Group: Development/Java
Summary:        Tests for %{name}
Requires:       maven-scm = %{?epoch:%epoch:}%{version}-%{release}

%description test
Tests for %{name}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1

# Remove unnecessary animal sniffer
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_remove_plugin :maven-enforcer-plugin

# Remove providers-integrity from build (we don't have mks-api)
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-integrity maven-scm-providers/maven-scm-providers-standard
%pom_disable_module maven-scm-provider-integrity maven-scm-providers

# Partially remove cvs support for removal of netbeans-cvsclient
# It still works with cvsexe provider
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-cvsjava maven-scm-client
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-cvsjava maven-scm-providers/maven-scm-providers-standard
%pom_disable_module maven-scm-provider-cvsjava maven-scm-providers/maven-scm-providers-cvs
sed -i s/cvsjava.CvsJava/cvsexe.CvsExe/ maven-scm-client/src/main/resources/META-INF/plexus/components.xml

# Tests are skipped anyways, so remove dependency on mockito.
%pom_remove_dep org.mockito: maven-scm-providers/maven-scm-provider-jazz
%pom_remove_dep org.mockito: maven-scm-providers/maven-scm-provider-accurev

# Don't use deprecated "descriptorId" configuration parameter of Maven
# Assembly Plugin, which was removed in version 3.0.0.
%pom_xpath_replace "pom:plugin[pom:artifactId='maven-assembly-plugin']/pom:configuration/pom:descriptorId" "
    <descriptorRefs>
      <descriptorRef>jar-with-dependencies</descriptorRef>
    </descriptorRefs>" maven-scm-client

# Put TCK tests into a separate sub-package
%mvn_package :%{name}-provider-cvstest test
%mvn_package :%{name}-provider-gittest test
%mvn_package :%{name}-provider-svntest test
%mvn_package :%{name}-test test

%build
# Don't build and unit run tests because
# * accurev tests need porting to a newer hamcrest
# * vss tests fail with the version of junit in fedora
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files test -f .mfiles-test
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.5-alt1_6jpp8
- java fc28+ update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.5-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.5-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt1_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt1_2jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt4_6jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_6jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_3jpp7
- new release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_4jpp7
- applied repocop patches

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_4jpp7
- restored maven-scm-cvsjava (reverted to rel4)

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_5jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp6
- new jpp relase

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- fixed build

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_2jpp5
- fixed modello plugin dep

* Sat Oct 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- added missing symlink in maven2/plugins

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b3.2jpp1.7
- converted from JPackage by jppimport script

