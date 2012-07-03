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


Name:           maven-injection-plugin
Version:        1.0.0
Release:	alt1_2jpp6
Epoch:          0
Summary:        Injection Maven Mojo
License:        LGPLv2+
URL:            http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/maven-plugins/tags/maven-injection-plugin-1.0.0
Group:          Development/Java
# svn -q export http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/maven-plugins/tags/maven-injection-plugin-1.0.0 && tar cjf maven-injection-plugin-1.0.0.tar.bz2 maven-injection-plugin-1.0.0
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
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
BuildRequires: javassist
BuildRequires: jboss-parent
BuildRequires: jpackage-utils >= 0:1.7.5
BuildArch:      noarch

%description
Provides capability to perform bytecode injection as part of build.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
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

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export M2_SETTINGS=$(pwd)/settings.xml
%{_bindir}/mvn-jpp \
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

install -m 644 target/%{name}-%{version}.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

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
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_2jpp6
- new version

