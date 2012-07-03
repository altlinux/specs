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


Name:           jboss-maven-utils
Version:        1.0.0
Release:        alt2_1jpp6
Epoch:          0
Summary:        Various Maven utilities hosted by JBoss
License:        LGPLv2+
URL:            http://jboss.org/
Group:          Development/Java
# svn -q export http://anonsvn.jboss.org/repos/maven/utils/tags/jboss-maven-utils-1.0.0 && tar cjf jboss-maven-utils-1.0.0.tar.bz2 jboss-maven-utils-1.0.0
Source0:        jboss-maven-utils-1.0.0.tar.bz2
Source1:        jboss-maven-utils-settings.xml
Source2:        jboss-maven-utils-jpp-depmap.xml
Requires: jboss-parent >= 0:3
Requires: maven2
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: jboss-parent
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-default-skin
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: mojo-maven2-plugin-taglist
%if 0
FIXME
DEBUG:   Path to dependency:                                                                                                                                                                                                                 
DEBUG:          1) org.apache.maven.plugins:maven-plugin-plugin:maven-plugin:2.0.7                                                                                                                                                           
DEBUG:          2) org.apache.maven:maven-plugin-tools-beanshell:jar:2.1                                                                                                                                                                     
DEBUG:          3) bsh:bsh:jar:1.3.0                                                                                                                                                                                                         
DEBUG:          4) bsf:bsf:jar:2.3.0
%endif
BuildRequires: bsf
BuildArch:      noarch

%description
Various Maven utilities hosted by JBoss.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q

%{__cp} -p %{SOURCE1} settings.xml
%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

%{__mkdir_p} external_repo
%{__ln_s} %{_javadir} external_repo/JPP

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mkdir -p ${MAVEN_REPO_LOCAL}/JPP/maven2/default_poms
export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s ${M2_SETTINGS} \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.skip=true \
        install javadoc:javadoc 
	#site

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/jboss-maven-utils-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p target/jboss-maven-utils-%{version}-sources.jar %{buildroot}%{_javadir}/%{name}-sources-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.maven.util jboss-maven-utils %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
#%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
#%{__cp} -pr target/site/* %{buildroot}%{_docdir}/%{name}-%{version}
#%{__rm} -r %{buildroot}%{_docdir}/%{name}-%{version}/apidocs

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-sources-%{version}.jar
%{_javadir}/%{name}-sources.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

#%files manual
#%doc %{_docdir}/%{name}-%{version}

%changelog
* Sat Apr 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_1jpp6
- fixed build with new plexus-containers

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_1jpp6
- new version
