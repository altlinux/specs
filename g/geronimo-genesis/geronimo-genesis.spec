Patch32: geronimo-genesis-1.3-alt-maven3-bootstrap.patch
Patch33: geronimo-genesis-1.3-alt-maven3-fix.patch
BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:           geronimo-genesis
Version:        1.3
Release:        alt4_2jpp6
Epoch:          0
Summary:        Geronimo Genesis
License:        ASL 2.0
Group:          Development/Java
URL:            http://geronimo.apache.org/
# Steps to reproduce
# svn export http://svn.apache.org/repos/asf/geronimo/server/tags/2.1.1/ geronimo-server-2.1.1
Source0:        %{name}-%{version}.tar.gz
Patch0:         geronimo-genesis-tools-maven-plugin-pom.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:       ant
Requires:       jakarta-commons-lang
Requires:       jpackage-utils
Requires:       plugin-support
Requires:       plexus-utils
BuildRequires:  apache-jar-resource-bundle
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant
BuildRequires:  maven2
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-plugin
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-remote-resources
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin
BuildRequires:  plugin-support
BuildRequires:  jakarta-commons-jexl >= 0:1.1
BuildArch:      noarch
Source44: import.info

%description
Genesis.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
  mv $f $f.no
done

%patch0 -p0 -b .sav0

cp -a config config.bootstrap
pushd config.bootstrap
%patch32 -p1
popd
%patch33
#sed -i '/relativePath/d' `grep -rl relativePath . | grep pom.xml`

%build
export MAVEN_REPO_LOCAL=`pwd`/.m2/repository
pushd config.bootstrap
#config/checkstyle-config/
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e -Dmaven.repo.local=${MAVEN_REPO_LOCAL} install
popd
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e -Dmaven.repo.local=${MAVEN_REPO_LOCAL} install javadoc:aggregate

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/plugins

%add_to_maven_depmap org.apache.geronimo.genesis.config project-config %{version} JPP/%{name} project-config
cp -p config/project-config/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-project-config.pom

%add_to_maven_depmap org.apache.geronimo.genesis genesis %{version} JPP/%{name} genesis
cp -p pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-genesis.pom

%add_to_maven_depmap org.apache.geronimo.genesis legal-bundle %{version} JPP/%{name} legal-bundle
cp -p legal-bundle/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-legal-bundle.pom
cp -p legal-bundle/target/legal-bundle-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/legal-bundle-%{version}.jar

%add_to_maven_depmap org.apache.geronimo.genesis.config config %{version} JPP/%{name} config
cp -p config/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-config.pom

%add_to_maven_depmap org.apache.geronimo.genesis.config checkstyle-config %{version} JPP/%{name} checkstyle-config
cp -p config/checkstyle-config/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-checkstyle-config.pom
cp -p config/checkstyle-config/target/checkstyle-config-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/checkstyle-config-%{version}.jar

%add_to_maven_depmap org.apache.geronimo.genesis.config geronimo-skin %{version} JPP/%{name} geronimo-skin
cp -p config/geronimo-skin/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-geronimo-skin.pom
cp -p config/geronimo-skin/target/geronimo-skin-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/geronimo-skin-%{version}.jar

%add_to_maven_depmap org.apache.geronimo.genesis.config logging-config %{version} JPP/%{name} logging-config
cp -p config/logging-config/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-logging-config.pom
cp -p config/logging-config/target/logging-config-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/logging-config-%{version}.jar


%add_to_maven_depmap org.apache.geronimo.genesis.plugins tools-maven-plugin %{version} JPP/%{name} tools-maven-plugin
%add_to_maven_depmap org.apache.geronimo.genesis.plugins maven-maven-plugin %{version} JPP/%{name} maven-maven-plugin
%add_to_maven_depmap org.apache.geronimo.genesis.plugins plugins %{version} JPP/%{name} plugins
cp -p plugins/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-plugins.pom
install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
cp -p plugins/tools-maven-plugin/target/tools-maven-plugin-%{version}.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/tools-maven-plugin-%{version}.jar
cp -p plugins/tools-maven-plugin/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tools-maven-plugin.pom
cp -p plugins/maven-maven-plugin/target/maven-maven-plugin-%{version}.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-maven-plugin-%{version}.jar
cp -p plugins/maven-maven-plugin/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-maven-maven-plugin.pom
pushd ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
    ln -sf %{_javadir}/%{name}/tools-maven-plugin-%{version}.jar tools-maven-plugin.jar
    ln -sf %{_javadir}/%{name}/maven-maven-plugin-%{version}.jar maven-maven-plugin.jar
popd

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc *.txt
%{_javadir}/%{name}
%{_datadir}/maven2/poms/*
%{_datadir}/maven2/plugins/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4_2jpp6
- fixed build with maven3

* Tue Jan 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_2jpp6
- jpp6 build

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_1jpp5
- fixed build

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp5
- fixes for java6 support

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp5
- first build

