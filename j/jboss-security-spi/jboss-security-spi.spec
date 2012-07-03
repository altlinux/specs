BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.0.3
%define name jboss-security-spi
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

%define repodir %{_javadir}/repository.jboss.com/jboss/jboss-security-spi/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define reltag SP1
%define namedversion %{version}.%{reltag}
%define oname jboss-security-spi

Name:           jboss-security-spi
Version:        2.0.3
Release:        alt2_2.SP1.2jpp6
Epoch:          1
Summary:        JBoss Security SPI
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/jbossas/projects/security/security-spi/tags/2.0.3.SP1/ jboss-security-spi-2.0.3 && tar cjf jboss-security-spi-2.0.3.tar.bz2 jboss-security-spi-2.0.3
Source0:        jboss-security-spi-2.0.3.tar.bz2
Source1:        jboss-security-spi-jpp-depmap.xml
Source2:        jboss-security-spi-settings.xml
Source3:        jboss-security-spi-component-info.xml
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jaspi_1_0_api
Requires:       jpackage-utils
Requires:       servlet_2_5_api
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  jboss-parent
BuildRequires:  jboss-test
BuildRequires:  junit
BuildRequires:  jaspi_1_0_api
BuildRequires:  servlet_2_5_api
BuildArch:      noarch
Source44: import.info

%description
JBoss Security SPI.

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
%setup -q -n %{oname}-%{version}

cp -p %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

#sed -i -e 's,<assembly>,<assembly><id>ALT</id>,' jboss-security-spi-as4/bin.xml assembly/bin.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/maven2-brew

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
	install \
         javadoc:aggregate

find maven2-brew \! -path '*/org/jboss/security/*' -type f -print -delete ||:
find maven2-brew -exec rmdir -p {} \; 2>/dev/null ||:


%install

pushd maven2-brew

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
cp -p org/jboss/security/acl-spi/%{namedversion}/acl-spi-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/acl-spi/%{namedversion}/acl-spi-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/authorization-spi/%{namedversion}/authorization-spi-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/authorization-spi/%{namedversion}/authorization-spi-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/identity-spi/%{namedversion}/identity-spi-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/identity-spi/%{namedversion}/identity-spi-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/jboss-security-spi/%{namedversion}/jboss-security-spi-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/jboss-security-spi/%{namedversion}/jboss-security-spi-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/jboss-security-spi-as4/%{namedversion}/jboss-security-spi-as4-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/jboss-security-spi-as4/%{namedversion}/jboss-security-spi-as4-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/jboss-security-spi-bare/%{namedversion}/jboss-security-spi-bare-%{namedversion}-sources.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/jboss/security/jboss-security-spi-bare/%{namedversion}/jboss-security-spi-bare-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{namedversion}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} -e "s|-%{namedversion}||g"`; done)

# poms
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p org/jboss/security/acl-spi/%{namedversion}/acl-spi-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-acl-spi.pom
cp -p org/jboss/security/authorization-spi/%{namedversion}/authorization-spi-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-authorization-spi.pom
cp -p org/jboss/security/identity-spi/%{namedversion}/identity-spi-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-identity-spi.pom
cp -p org/jboss/security/jboss-security-spi/%{namedversion}/jboss-security-spi-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi.pom
cp -p org/jboss/security/jboss-security-spi-as4/%{namedversion}/jboss-security-spi-as4-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-as4.pom
cp -p org/jboss/security/jboss-security-spi-bare/%{namedversion}/jboss-security-spi-bare-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-bare.pom
cp -p org/jboss/security/jboss-security-spi-parent/%{namedversion}/jboss-security-spi-parent-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-parent.pom
cp -p org/jboss/security/jboss-security-spi-pom/%{namedversion}/jboss-security-spi-pom-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-pom.pom

popd

# depmaps
%add_to_maven_depmap org.jboss.security acl-spi %{namedversion} JPP/%{name} acl-spi
%add_to_maven_depmap org.jboss.security authorization-spi %{namedversion} JPP/%{name} authorization-spi
%add_to_maven_depmap org.jboss.security identity-spi %{namedversion} JPP/%{name} identity-spi
%add_to_maven_depmap org.jboss.security jboss-security-spi %{namedversion} JPP/%{name} jboss-security-spi
%add_to_maven_depmap org.jboss.security jboss-security-spi-as4 %{namedversion} JPP/%{name} jboss-security-spi-as4
%add_to_maven_depmap org.jboss.security jboss-security-spi-bare %{namedversion} JPP/%{name} jboss-security-spi-bare
%add_to_maven_depmap org.jboss.security jboss-security-spi-parent %{namedversion} JPP/%{name} jboss-security-spi-parent
%add_to_maven_depmap org.jboss.security jboss-security-spi-pom %{namedversion} JPP/%{name} jboss-security-spi-pom

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
mkdir -p %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
pushd maven2-brew
cp -pr * %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
popd
mkdir -p %{buildroot}%{repodir}
mkdir -p %{buildroot}%{repodirlib}
cp -p %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
mkdir -p %{buildroot}%{repodirsrc}
cp -p %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{SOURCE1} %{buildroot}%{repodirsrc}
cp -p %{SOURCE2} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}/jboss-security-spi-%{namedversion}.jar %{buildroot}%{repodirlib}/jboss-security-spi.jar
%endif

%files
%dir %{_javadir}*/%{name}
%exclude %dir %{_javadocdir}/%{name}
%{_javadir}*/%{name}/acl-spi-%{namedversion}-sources.jar
%{_javadir}*/%{name}/acl-spi-sources.jar
%{_javadir}*/%{name}/acl-spi-%{namedversion}.jar
%{_javadir}*/%{name}/acl-spi.jar
%{_javadir}*/%{name}/authorization-spi-%{namedversion}-sources.jar
%{_javadir}*/%{name}/authorization-spi-sources.jar
%{_javadir}*/%{name}/authorization-spi-%{namedversion}.jar
%{_javadir}*/%{name}/authorization-spi.jar
%{_javadir}*/%{name}/identity-spi-%{namedversion}-sources.jar
%{_javadir}*/%{name}/identity-spi-sources.jar
%{_javadir}*/%{name}/identity-spi-%{namedversion}.jar
%{_javadir}*/%{name}/identity-spi.jar
%{_javadir}*/%{name}/jboss-security-spi-%{namedversion}-sources.jar
%{_javadir}*/%{name}/jboss-security-spi-sources.jar
%{_javadir}*/%{name}/jboss-security-spi-%{namedversion}.jar
%{_javadir}*/%{name}/jboss-security-spi.jar
%{_javadir}*/%{name}/jboss-security-spi-as4-%{namedversion}-sources.jar
%{_javadir}*/%{name}/jboss-security-spi-as4-sources.jar
%{_javadir}*/%{name}/jboss-security-spi-as4-%{namedversion}.jar
%{_javadir}*/%{name}/jboss-security-spi-as4.jar
%{_javadir}*/%{name}/jboss-security-spi-bare-%{namedversion}-sources.jar
%{_javadir}*/%{name}/jboss-security-spi-bare-sources.jar
%{_javadir}*/%{name}/jboss-security-spi-bare-%{namedversion}.jar
%{_javadir}*/%{name}/jboss-security-spi-bare.jar
%{_datadir}/maven2/poms/JPP.%{name}-acl-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-authorization-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-identity-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-as4.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-bare.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-jboss-security-spi-pom.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt2_2.SP1.2jpp6
- fixed build with maven3

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt1_2.SP1.2jpp6
- new jpp release

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1:2.0.3-alt1_2.SP1.1jpp6
- new version

