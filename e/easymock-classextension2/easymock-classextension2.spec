BuildRequires: maven2-plugin-antrun maven2-plugin-source
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

%define base_name easymockclassextension

Name:           easymock-classextension2
Version:        2.5.2
Release:	alt2_1jpp6
Epoch:          0
Summary:        EasyMock class extension

Group:          Development/Java
License:        MIT
URL:            http://www.easymock.org/
Source0:        easymock-classextension2-2.5.2.tar.bz2
#  svn -q export https://easymock.svn.sourceforge.net/svnroot/easymock/tags/easymock-classextension-2.5.2 easymock-classextension2-2.5.2 && tar cjf easymock-classextension2-2.5.2.tar.bz2 easymock-classextension2-2.5.2
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml
Source4:        apache-jar-resource-bundle-1.3.jar
Patch0:         easymock-classextension2-pom.patch

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-eclipse
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-remote-resources
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-surefire-provider-junit4
BuildRequires: cglib
BuildRequires: easymock2
BuildRequires: objenesis

Provides:  easymockclassextension2 = %{epoch}:%{version}-%{release}
Obsoletes: easymockclassextension2 < %{epoch}:%{version}-%{release}

Requires: cglib
Requires: easymock2
Requires: objenesis

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Source44: import.info

%description
This extension allows generating Mock Objects for classes. 
It has been contributed by Joel Shellman, Henri Tremblay 
and Chad Woolley. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q 
%patch0 -b .sav0
cp -p %{SOURCE3} maven2-settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mkdir -p ${MAVEN_REPO_LOCAL}/org/apache/apache-jar-resource-bundle/1.3/
cp %{SOURCE4} ${MAVEN_REPO_LOCAL}/org/apache/apache-jar-resource-bundle/1.3/apache-jar-resource-bundle-1.3.jar
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
	-Dmaven.test.skip=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install javadoc:javadoc


%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 target/%{base_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/easymockclassextension2.jar
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.easymock %{base_name} %{version} JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_1jpp6
- fixed build with maven3

* Mon Mar 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt1_1jpp6
- new version

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp5
- new jpp release

