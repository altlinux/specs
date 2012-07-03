BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 3.1.0
%define name hibernate3-commons-annotations
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

%define namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:           hibernate3-commons-annotations
Version:        3.1.0
Release:	alt1_4jpp6
Epoch:          0
Summary:        Hibernate annotations
License:        LGPLv2+
Group:          Databases
URL:            http://www.hibernate.org/
# svn export http://anonsvn.jboss.org/repos/hibernate/commons-annotations/tags/3.1.0.GA/ hibernate3-commons-annotations-3.1.0.GA
Source0:        hibernate3-commons-annotations-3.1.0.GA.tar.gz
Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml
Patch0:         hibernate3-commons-annotations-pom.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       jpackage-utils
Requires:       slf4j
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  commons-parent
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  slf4j
BuildArch:      noarch
Source44: import.info

%description
Following the DRY (Don't Repeat Yourself) principle, 
Hibernate Validator let's you express your domain 
constraints once (and only once) and ensure their 
compliance at various level of your system 
automatically.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n hibernate3-commons-annotations-%{namedversion}
%patch0 -p0 -b .sav0

cp -p %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file:`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file:`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file:`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:%{_datadir}/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:%{_datadir}/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export M2SETTINGS=`pwd`/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
export MAVEN_OPTS="-Xmx384m"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}
install -p -m 644 target/hibernate-commons-annotations-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{namedversion}||g"`; done)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.hibernate hibernate-commons-annotations %{namedversion} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%files
%doc lgpl.txt
%{_javadir}/%{name}-%{namedversion}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_4jpp6
- new jpp release

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_3jpp6
- new version

