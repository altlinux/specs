Patch33: jboss-security-xacml-alt-maven3.patch
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.0.4
%define name jboss-security-xacml
# Copyright (c) 2000-2011, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-xacml/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag %{nil}
%define namedversion %{version}
%define oname jboss-security-xacml

Name:           jboss-security-xacml
Version:        2.0.4
Release:        alt2_5jpp6
Epoch:          0
Summary:        JBoss Security XACML
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/security/security-xacml/tags/2.0.4 jboss-security-xacml-2.0.4 && tar cjf jboss-security-xacml-2.0.4.tar.bz2 jboss-security-xacml-2.0.4
Source0:        jboss-security-xacml-2.0.4.tar.bz2
Source1:        jboss-security-xacml-jpp-depmap.xml
Source2:        jboss-security-xacml-settings.xml
Source3:        jboss-security-component-info.xml
Patch0:         jboss-security-stax.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jaf_1_1_api
Requires:       jaxb_2_1_api
Requires:       jpackage-utils
Requires:       stax_1_0_api
Requires:       glassfish-jaxb
Requires:       servlet_2_5_api
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  commons-parent >= 0:9
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  junit
BuildRequires:  glassfish-jaxb
BuildRequires:  jaf_1_1_api
BuildRequires:  jaxb_2_1_api
BuildRequires:  jboss-parent
BuildRequires:  servlet_2_5_api
BuildRequires:  stax_1_0_api
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildArch:      noarch
Source44: import.info

%description
JBoss Security XACML.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{name}-%{namedversion} 
%patch0 -p0 -b .sav0
%patch33

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:aggregate

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -p -m 644 assembly/target/jbossxacml-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/jbossxacml-%{version}.jar
install -p -m 644 assembly/target/jbossxacml-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/jbossxacml-sources-%{version}.jar
install -p -m 644 jboss-sunxacml/target/jboss-sunxacml-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/jboss-sunxacml-%{version}.jar
#install -p -m 644 jboss-sunxacml/target/jboss-sunxacml-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/jboss-sunxacml-sources-%{version}.jar
install -p -m 644 jboss-xacml/target/jboss-xacml-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/jboss-xacml-%{version}.jar
#install -p -m 644 jboss-xacml/target/jboss-xacml-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/jboss-xacml-sources-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms

%add_to_maven_depmap org.jboss.security jboss-xacml-project %{namedversion} JPP/%{name} %{name}-project
install -p -m 644 parent/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{name}-project.pom

%add_to_maven_depmap org.jboss.security jbossxacml %{namedversion} JPP/%{name} jbossxacml
install -p -m 644 assembly/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jbossxacml.pom

%add_to_maven_depmap org.jboss.security jboss-xacml-main %{namedversion} JPP/%{name} %{name}-main
install -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{name}-main.pom

%add_to_maven_depmap org.jboss.security jboss-sunxacml %{namedversion} JPP/%{name} jboss-sunxacml
install -p -m 644 jboss-sunxacml/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-sunxacml.pom

%add_to_maven_depmap org.jboss.security jboss-xacml %{namedversion} JPP/%{name} jboss-xacml
install -p -m 644 jboss-xacml/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-xacml.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 %{buildroot}%{repodir}
install -d -m 755 %{buildroot}%{repodirlib}
install -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
install -d -m 755 %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
install -p -m 644 %{buildroot}%{_javadir}/%{name}/jbossxacml.jar %{buildroot}%{repodirlib}/jbossxacml.jar
install -p -m 644 %{buildroot}%{_javadir}/%{name}/jbossxacml-sources.jar %{buildroot}%{repodirlib}/jbossxacml-sources.jar
install -p -m 644 %{buildroot}%{_javadir}/%{name}/jboss-sunxacml.jar  %{buildroot}%{repodirlib}/jboss-sunxacml.jar
#install -p -m 644 %{buildroot}%{_javadir}/%{name}/jboss-sunxacml-sources.jar %{buildroot}%{repodirlib}/jboss-sunxacml-sources.jar
install -p -m 644 %{buildroot}%{_javadir}/%{name}/jboss-xacml.jar %{buildroot}%{repodirlib}/jboss-xacml.jar
#install -p -m 644 %{buildroot}%{_javadir}/%{name}/jboss-xacml-sources.jar %{buildroot}%{repodirlib}/jboss-xacml-sources.jar
install -p -m 644 %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jbossxacml.pom %{buildroot}%{repodirlib}/jbossxacml.pom
install -p -m 644 %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-xacml-main.pom %{buildroot}%{repodirlib}/jboss-security-xacml-main.pom
install -p -m 644 %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-xacml-project.pom %{buildroot}%{repodirlib}/jboss-security-xacml-project.pom
install -p -m 644 %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-sunxacml.pom %{buildroot}%{repodirlib}/jboss-sunxacml.pom
install -p -m 644 %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-xacml.pom %{buildroot}%{repodirlib}/jboss-xacml.pom
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/jbossxacml-%{version}.jar
%{_javadir}/%{name}/jbossxacml.jar
#%{_javadir}/%{name}/jbossxacml-sources-%{version}.jar
#%{_javadir}/%{name}/jbossxacml-sources.jar
%{_javadir}/%{name}/jboss-sunxacml-%{version}.jar
%{_javadir}/%{name}/jboss-sunxacml.jar
#%{_javadir}/%{name}/jboss-sunxacml-sources-%{version}.jar
#%{_javadir}/%{name}/jboss-sunxacml-sources.jar
%{_javadir}/%{name}/jboss-xacml-%{version}.jar
%{_javadir}/%{name}/jboss-xacml.jar
#%{_javadir}/%{name}/jboss-xacml-sources-%{version}.jar
#%{_javadir}/%{name}/jboss-xacml-sources.jar
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-xacml-main.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-xacml-project.pom
%{_datadir}/maven2/poms/JPP.%{name}-jbossxacml.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-sunxacml.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-xacml.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_5jpp6
- fixed build with maven3

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_5jpp6
- new jpp release

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_4jpp6
- new version

