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

%define reltag Beta1
%define namedversion %{version}.%{reltag}

Name:           jboss-aspects-test
Version:        1.0.0
Release:        alt2_0.b1.2jpp6
Epoch:          0
Summary:        JBoss Aspects Test
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn export http://anonsvn.jboss.org/repos/jbossas/projects/jboss-aspects/tags/jboss-aspects-test-1.0.0.Beta1/
Source0:        jboss-aspects-test-1.0.0.Beta1.tar.gz
Source1:        jboss-aspects-test-jpp-depmap.xml
Source2:        jboss-aspects-test-settings.xml
# FIXME: (dwalluck): do not bundle this
Source3:        jboss-aspects-build-1.0.1.CR5.pom
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: ant-junit
Requires: gnu-trove
Requires: jboss-aop2
Requires: jboss-aspects-common
Requires: jboss-test
Requires: junit
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-jboss-deploy-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: ant-junit
BuildRequires: gnu-trove
BuildRequires: jboss-aop2
BuildRequires: jboss-parent >= 0:3
BuildRequires: jboss-test
BuildRequires: junit
BuildArch:      noarch

%description
JBoss aspects test.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{namedversion}

cp -p %{SOURCE2} maven2-settings.xml

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
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp -p %{SOURCE3} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.jboss.aspects-jboss-aspects-build.pom
install -Dm644 %{SOURCE3} $MAVEN_REPO_LOCAL/org/jboss/aspects/jboss-aspects-build/1.0.0.Beta1/jboss-aspects-build-1.0.0.Beta1.pom
# FIXME: (dwalluck): do not skip tests
%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.test.skip=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.aspects %{name} %{namedversion} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_0.b1.2jpp6
- fixed build with new jboss-test

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_0.b1.2jpp6
- new version

