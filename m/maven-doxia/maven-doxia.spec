BuildRequires: maven-plugin-plugin
BuildRequires: bouncycastle-tsp
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

Name:           maven-doxia
Version:        1.2
Release:        alt4_4jpp7
Epoch:          0
Summary:        Content generation framework
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/doxia/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip

# Point it at the correct plexus-container-default
Source1:        %{name}-depmap.xml


# TODO: push upstream
Patch0:         0001-Use-plexus-component-metadata.patch
# TODO: push upstream
# abstract class should not be annotated as component because maven
# will pick it up and try to instantiate
Patch1:         0002-doxia-core-remove-plexus-component-annotation.patch

Patch2:         0003-remove-clirr.patch
# Build against iText 2.x
# http://jira.codehaus.org/browse/DOXIA-53
Patch3:         0004-Fix-itext-dependency.patch


BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant ant-nodeps
BuildRequires:  itext
BuildRequires:  plexus-cli
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shared-reporting-impl
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-doxia-tools
BuildRequires:  modello-maven-plugin
BuildRequires:  servlet25
BuildRequires:  classworlds
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-validator
BuildRequires:  apache-commons-configuration
BuildRequires:  junit
BuildRequires:  jakarta-oro
BuildRequires:  plexus-i18n
BuildRequires:  plexus-utils
BuildRequires:  plexus-velocity
BuildRequires:  plexus-build-api
BuildRequires:  velocity
BuildRequires:	fop
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-containers-component-javadoc
BuildRequires:  plexus-containers-container-default
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-project
BuildRequires:  xmlgraphics-commons
BuildRequires:  avalon-framework
BuildRequires:  geronimo-parent-poms
BuildRequires:  geronimo-jms
BuildRequires:  javamail



Requires:       classworlds
Requires:       apache-commons-collections
Requires:       apache-commons-logging
Requires:       apache-commons-validator
Requires:       junit
Requires:       jakarta-oro
Requires:       plexus-container-default
Requires:       plexus-i18n
Requires:       plexus-utils
Requires:       plexus-velocity
Requires:       velocity
Requires:	fop
Requires:       httpcomponents-client
Requires:       httpcomponents-project
Requires:       geronimo-jms
Requires:       javamail
# should be in geronimo-jms but that would pull maven even for ant use
# of library so we don't add it there
Requires:       geronimo-parent-poms

Requires:         jpackage-utils
Source44: import.info

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n doxia-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
# tests disabled because some use old plexus-container and don't work
# with new
mvn-rpmbuild \
	-e \
	-Dmaven.local.depmap.file=%{SOURCE1} \
	-Dmaven.test.skip=true \
	install javadoc:aggregate

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

for targetdir in `find -type d -name target`; do

    targetdir=`echo $targetdir | sed -e s:^\./::g`

    modulename=`echo $targetdir | awk -F / '{print $(NF-1)}'`
    strippedmodulename=`echo $modulename | sed -e s:^doxia-::g`

    # Skip parent pom
    if [ ! -z $strippedmodulename ]; then
        cp -p $targetdir/../pom.xml \
                $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-$strippedmodulename.pom

    fi

    # Does the module have a jar?
    if [ -f $targetdir/$modulename-%{version}.jar ]; then
        cp -p $targetdir/$modulename-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}/$strippedmodulename.jar
        %add_maven_depmap JPP.%{name}-$strippedmodulename.pom %{name}/$strippedmodulename.jar
    else
        %add_maven_depmap JPP.%{name}-$strippedmodulename.pom
    fi

done

# Install parent pom
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-doxia-doxia.pom
%add_maven_depmap JPP.maven-doxia-doxia.pom
install -pm 644 doxia-modules/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.maven-doxia-modules.pom
%add_maven_depmap JPP.maven-doxia-modules.pom

install -d -m 0755 %{buildroot}/%{_datadir}/maven2/lib
ln -s %{_javadir}/maven-doxia/logging-api.jar $RPM_BUILD_ROOT/%{_datadir}/maven2/lib/maven-doxia_logging-api.jar

# javadoc (all javadocs are contained in the main module docs dir used below)
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/%{name}
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}
%{_datadir}/maven2/lib/*

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_4jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_4jpp7
- fixed build

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp7
- use fc geronimo

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

