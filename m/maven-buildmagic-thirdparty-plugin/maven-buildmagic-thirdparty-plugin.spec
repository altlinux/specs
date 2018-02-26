Patch33: maven-buildmagic-thirdparty-plugin-2.2.0-alt-maven3.patch

Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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


Name:           maven-buildmagic-thirdparty-plugin
Version:        2.2.0
Release:	alt2_3jpp6
Epoch:          0
Summary:        JBoss Buildmagic Thirdparty Repository Maven Plugin
License:        ASL 2.0
URL:            http://www.jboss.org/community/wiki/MavenBuildmagicThirdpartyPlugin
Group:          Development/Java
# svn -q export http://anonsvn.jboss.org/repos/maven/plugins/jboss/tags/maven-buildmagic-thirdparty-plugin-2.2.0/ && tar cjf maven-buildmagic-thirdparty-plugin-2.2.0.tar.bz2 maven-buildmagic-thirdparty-plugin-2.2.0
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         maven-buildmagic-thirdparty-plugin-JBBUILD-547.patch
Requires: maven2
%if 0
FIXME:
DEBUG:   Path to dependency:                                                                                                                               
DEBUG:          1) org.apache.maven.plugins:maven-plugin-plugin:maven-plugin:2.0.7                                                                         
DEBUG:          2) org.apache.maven:maven-plugin-tools-beanshell:jar:2.1                                                                                   
DEBUG:          3) bsh:bsh:jar:1.3.0                                                                                                                       
DEBUG:          4) bsf:bsf:jar:2.3.0
%endif
BuildRequires: bsf
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-invoker
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
%if 0
DEBUG: 1) javax.mail:mail:jar:1.4                                                                                                                                                                                                            
DEBUG:   Try downloading the file manually from the project website.                                                                                                                                                                         
DEBUG:   Then, install it using the command:                                                                                                                                                                                                 
DEBUG:       mvn install:install-file -DgroupId=javax.mail -DartifactId=mail -Dversion=1.4 -Dpackaging=jar -Dfile=/path/to/file                                                                                                              
DEBUG:   Alternatively, if you host your own repository you can deploy the file there:                                                                                                                                                       
DEBUG:       mvn deploy:deploy-file -DgroupId=javax.mail -DartifactId=mail -Dversion=1.4 -Dpackaging=jar -Dfile=/path/to/file -Durl=[url] -DrepositoryId=[id]                                                                                
DEBUG:   Path to dependency:                                                                                                                                                                                                                 
DEBUG:          1) org.apache.maven.plugins:maven-plugin-plugin:maven-plugin:2.4.1                                                                                                                                                           
DEBUG:          2) org.apache.maven.reporting:maven-reporting-impl:jar:2.0                                                                                                                                                                   
DEBUG:          3) commons-validator:commons-validator:jar:1.2.0                                                                                                                                                                             
DEBUG:          4) commons-logging:commons-logging:jar:1.0.4                                                                                                                                                                                 
DEBUG:          5) log4j:log4j:jar:1.2.12                                                                                                                                                                                                    
DEBUG:          6) javax.mail:mail:jar:1.4
%endif
BuildRequires: javamail_1_4_api
BuildRequires: jboss-parent
BuildRequires: jpackage-utils >= 0:1.7.5
BuildArch:      noarch

%description
Plugin for deploying artifacts to JBoss ant/buildmagic repository, and building
a thirdparty directory from dependencies in a maven repository.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
%patch0 -p4
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%patch33

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
                -e \
                -s ${M2_SETTINGS} \
                -Dmaven2.jpp.depmap.file=%{SOURCE2} \
                -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
                -Dmaven.test.skip=true \
                install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 755 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.maven.plugins %{name} %{version} JPP %{name}

install -p -m 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_3jpp6
- fixed build with new asm

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_3jpp6
- new version

