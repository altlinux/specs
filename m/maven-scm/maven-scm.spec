BuildRequires: maven-plugin-plugin
Epoch: 0
# BEGIN SourceDeps(oneline):
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

Name:           maven-scm
Version:        1.7
Release:        alt3_3jpp7
Summary:        Common API for doing SCM operations
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/scm

Source0:        http://repo1.maven.org/maven2/org/apache/maven/scm/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-jpp-depmap.xml

# fix modello configuration in vss provider pom and the cast as above
Patch0:         005_maven-scm_fix-vss-provider-pom.patch
# replace plexus-maven-plugin for plexus-component-metadata
Patch1:         007_maven-scm_migration-to-component-metadata.patch
# plexus-maven-plugin -> plexus-component-metadata
Patch5:         012-plexus-component-metadata.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven2-common-poms >= 0:1.0-21
BuildRequires:  modello >= 1.1
BuildRequires:  plexus-utils >= 1.5.6
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  maven-doxia-sitetools
BuildRequires:  plexus-interpolation
BuildRequires:  bzr
BuildRequires:  subversion
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-classworlds

Requires:       junit >= 3.8.2
Requires:       apache-commons-collections >= 3.1
Requires:       modello >= 1.0-0.a8
Requires:       jakarta-oro >= 2.0.8
Requires:       plexus-utils >= 1.2
Requires:       velocity >= 1.4
Requires:       maven
Source44: import.info

%description
Maven SCM supports Maven plugins (e.g. maven-release-plugin) and other
tools (e.g. Continuum) in providing them a common API for doing SCM operations.

%package test
Summary:        Tests for %{name}
Group:          Development/Java
Requires:       maven-scm = %{?epoch:%epoch:}%{version}-%{release}

%description test
Tests for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch5 -p1

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin maven-scm-plugin

# remove providers-integrity from build (we don't have mks-api)
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-integrity maven-scm-providers/maven-scm-providers-standard
%pom_disable_module maven-scm-provider-integrity maven-scm-providers

# Partially remove cvs support for removal of netbeans-cvsclient
# It still works with cvsexe provider
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-cvsjava maven-scm-client
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-cvsjava maven-scm-providers/maven-scm-providers-standard
%pom_disable_module maven-scm-provider-cvsjava maven-scm-providers/maven-scm-providers-cvs


%build
# we don't have all test dependencies to run full testsuite anyway
mvn-rpmbuild -Dproject.build.sourceEncoding=ISO-8859-1 \
        -Dmaven.test.skip=true \
        -Dmaven.local.depmap.file=%{SOURCE1} \
        install javadoc:aggregate

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}

for jar in `find . -type f -name "*.jar" | grep -E "target/.*.jar$"`; do
        newname=`basename $jar`
        newname=${newname/maven-scm-/}
        versionless_jar=${newname/-%{version}/}
        install -pm 644 $jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$versionless_jar
done

#remove maven-scm CLI jar-with-dependencies created by maven-assembly-plugin
rm $RPM_BUILD_ROOT%{_javadir}/%{name}/client-jar-with-dependencies.jar

#poms (exclude the svn/cvs test poms. They are unnecessary)
# ignore
#  1) poms in target/ (they are either copies, or temps)
#  2) poms in src/test/ (they are poms needed for tests only)
for i in `find . -name pom.xml | grep -v \\\./pom.xml | \
   grep -v target | grep -v src/test`; do
        artifactname=`basename \`dirname $i\``
        jarname=`echo $artifactname | sed -e s:^maven-scm-::g`
        cp -p $i $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.$artifactname.pom
        %add_to_maven_depmap org.apache.maven.scm $artifactname %{version} JPP/%{name} $jarname
done
cp -p pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.maven-scm-scm.pom
%add_to_maven_depmap org.apache.maven.scm maven-scm %{version} JPP/maven-scm scm

%add_to_maven_depmap org.apache.maven.plugins maven-scm-plugin %{version} JPP/maven-scm plugin

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/api*
%{_javadir}/%{name}/client*
%{_javadir}/%{name}/manager-plexus*
%{_javadir}/%{name}/plugin*
%{_javadir}/%{name}/provider-*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files test
%{_javadir}/%{name}/provider-cvstest*
%{_javadir}/%{name}/provider-svntest*
%{_javadir}/%{name}/test*

%files javadoc
%{_javadocdir}/*

%changelog
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

