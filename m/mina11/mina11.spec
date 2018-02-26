BuildRequires: jmock
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat jakarta-commons-net14
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


%define gcj_support 0


%define oname   mina

Summary:        A Multipurpose Infrastructure for Network Applications
Name:           mina11
Version:        1.1.4
Release:        alt5_2jpp5
Epoch:		0
Group:          Development/Java
License:        Apache 2.0 License
URL:            http://directory.apache.org/subprojects/mina/
Source0:        %{oname}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/mina/tags/1.1.4/ mina-1.1.4

Source1:        directory-pom-1.0.4.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-default-skin
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven-jxr
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin

BuildRequires: junit
BuildRequires: easymock
BuildRequires: easymock-classextension
BuildRequires: aopalliance
BuildRequires: slf4j
BuildRequires: tl-netty2
BuildRequires: jzlib
BuildRequires: spring2-beans
BuildRequires: spring2-core
BuildRequires: spring2-context
BuildRequires: spring-support

Requires: slf4j
Obsoletes:	mina-java5 <= 0:1.0.2
Provides:	mina-java5

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
MINA (Multipurpose Infrastructure for Network Applications) is a
network application framework which helps users develop high
performance and high scalability network applications easily.

%package filter-codec-netty
Group:          Development/Java
Summary:        Netty2 filter for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: tl-netty2

%description filter-codec-netty
%{summary}.

%package filter-compression
Group:          Development/Java
Summary:        JZlib compression filter for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jzlib

%description filter-compression
%{summary}.

%package filter-ssl
Group:          Development/Java
Summary:        SSL filter for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: slf4j

%description filter-ssl
%{summary}.

%package integration-jmx
Group:          Development/Java
Summary:        JMX integration for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}

%description integration-jmx
%{summary}.

%package integration-spring
Group:          Development/Java
Summary:        Spring integration for %{name}
Requires: %{name}-filter-ssl = %{epoch}:%{version}-%{release}
Requires: slf4j
Requires: spring2-beans
Requires: spring2-core

%description integration-spring
%{summary}.

%package demo
Group:          Development/Java
Summary:        Examples for %{name}
Requires: %{name}-filter-ssl = %{epoch}:%{version}-%{release}
Requires: %{name}-integration-spring = %{epoch}:%{version}-%{release}
Requires: nlog4j
Requires: spring2-context
Requires: spring-support

%description demo
%{summary}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}

%description manual
%{summary}.

%prep
%setup -q -n %{oname}-%{version}


%build
cp %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir -p m2_repo/repository/JPP/maven2/default_poms
cp %{SOURCE1} m2_repo/repository/JPP/maven2/default_poms/org.apache.directory-build.pom
cp pom.xml m2_repo/repository/JPP/maven2/default_poms/org.apache.mina-build.pom

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
export MAVEN_OPTS="-Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.jpp.mode=true -Dmaven.test.failure.ignore=true -Djava.awt.headless=true"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install 

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        javadoc:javadoc

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -N \
        site


%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-build.pom
%add_to_maven_depmap org.apache.mina build %{version} JPP/mina11 build

install -m 644 core/target/%{oname}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-core.pom
%add_to_maven_depmap org.apache.mina mina-core %{version} JPP/mina11 core

install -m 644 filter-codec-netty/target/%{oname}-filter-codec-netty-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/filter-codec-netty-%{version}.jar
install -m 644 filter-codec-netty/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-filter-codec-netty.pom
%add_to_maven_depmap org.apache.mina mina-filter-codec-netty %{version} JPP/mina11 filter-codec-netty

install -m 644 filter-compression/target/%{oname}-filter-compression-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/filter-compression-%{version}.jar
install -m 644 filter-compression/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-filter-compression.pom
%add_to_maven_depmap org.apache.mina mina-filter-compression %{version} JPP/mina11 filter-compression

install -m 644 example/target/%{oname}-example-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/example-%{version}.jar
install -m 644 example/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-example.pom
%add_to_maven_depmap org.apache.mina mina-example %{version} JPP/mina11 example

install -m 644 filter-ssl/target/%{oname}-filter-ssl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/filter-ssl-%{version}.jar
install -m 644 filter-ssl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-filter-ssl.pom
%add_to_maven_depmap org.apache.mina mina-filter-ssl %{version} JPP/mina11 filter-ssl

install -m 644 integration-jmx/target/%{oname}-integration-jmx-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/integration-jmx-%{version}.jar
install -m 644 integration-jmx/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-integration-jmx.pom
%add_to_maven_depmap org.apache.mina mina-integration-jmx %{version} JPP/mina11 integration-jmx

install -m 644 integration-spring/target/%{oname}-integration-spring-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/integration-spring-%{version}.jar
install -m 644 integration-spring/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.mina11-integration-spring.pom
%add_to_maven_depmap org.apache.mina mina-integration-spring %{version} JPP/mina11 integration-spring

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

pushd $RPM_BUILD_ROOT%{_javadir}
   ln -fs %{name}/core-%{version}.jar %{name}-jdk14-%{version}.jar
   ln -fs %{name}/core.jar %{name}-jdk14.jar
popd

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf target/site/apidocs*

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
cp -p core/src/main/resources/META-INF/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}/core*.jar
%{_javadir}/%{name}-jdk14*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/core-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files filter-codec-netty
%{_javadir}/%{name}/filter-codec-netty*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/filter-codec-netty-%{version}.jar.*
%endif

%files filter-compression
%{_javadir}/%{name}/filter-compression*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/filter-compression-%{version}.jar.*
%endif

%files filter-ssl
%{_javadir}/%{name}/filter-ssl*.jar

%files integration-jmx
%{_javadir}/%{name}/integration-jmx*.jar

%files integration-spring
%{_javadir}/%{name}/integration-spring*.jar

%files demo
%{_javadir}/%{name}/example*.jar

#files javadoc
#%doc %{_javadocdir}/%{name}-%{version}
#%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt5_2jpp5
- fixed build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt4_2jpp5
- fixed build with java 7

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt3_2jpp5
- build with velocity 15

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt2_2jpp5
- rebuild with compat jakarta-commons-net14

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_2jpp5
- new version

