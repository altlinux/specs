Patch33: mina10-alt-drop-spring.patch
#BuildRequires: velocity15
Packager: Igor Vlasenko <viy@altlinux.ru>
%define _without_tests 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

# build with option --with tests
%define tests %{?_with_tests:1}%{!?_with_tests:%{?_without_tests:0}%{!?_without_tests:%{?_tests:%{_tests}}%{!?_tests:0}}}


%define oname mina

Summary:        A Multipurpose Infrastructure for Network Applications
Name:           mina10
Version:        1.0.2
Release:        alt5_2jpp5
Epoch:          0
Group:          Development/Java
License:        Apache 2.0 License
URL:            http://directory.apache.org/subprojects/mina/
Source0:        %{name}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/mina/tags/1.0.2/ mina-1.0.2

Source1:        directory-pom-1.0.4.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml

#Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:%{_vendor}}
#Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-default-skin
BuildRequires: maven2-plugin-antrun
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
BuildRequires: easymock
BuildRequires: easymock-classextension
BuildRequires: aopalliance
BuildRequires: backport-util-concurrent
BuildRequires: jakarta-commons-net
BuildRequires: jzlib
BuildRequires: nlog4j
BuildRequires: slf4j
BuildRequires: spring
BuildRequires: tl-netty2


Requires: backport-util-concurrent
Requires: slf4j

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
Requires: spring-beans
Requires: spring-core

%description integration-spring
%{summary}.

%package java5
Group:          Development/Java
Summary:        Java5 extensions for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: slf4j

%description java5
%{summary}.

%package demo
Group:          Development/Java
Summary:        Examples for %{name}
Requires: %{name}-filter-ssl = %{epoch}:%{version}-%{release}
Requires: %{name}-integration-spring = %{epoch}:%{version}-%{release}
Requires: nlog4j
Requires: spring-context
Requires: spring-support

%description demo
%{summary}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{oname}-%{version}
%patch33

%build
cp %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP



export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
%if ! %{tests}
        -Dmaven.test.skip=true \
%endif
        -Dmaven.test.failure.ignore=true \
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

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-build.pom
%add_to_maven_depmap org.apache.mina build %{version} JPP/%{name} build

install -m 644 core/target/%{oname}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%add_to_maven_depmap org.apache.mina mina-core %{version} JPP/%{name} core

install -m 644 filter-codec-netty/target/%{oname}-filter-codec-netty-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/filter-codec-netty-%{version}.jar
install -m 644 filter-codec-netty/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-filter-codec-netty.pom
%add_to_maven_depmap org.apache.mina mina-filter-codec-netty %{version} JPP/%{name} filter-codec-netty

install -m 644 filter-compression/target/%{oname}-filter-compression-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/filter-compression-%{version}.jar
install -m 644 filter-compression/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-filter-compression.pom
%add_to_maven_depmap org.apache.mina mina-filter-compression %{version} JPP/%{name} filter-compression

#install -m 644 example/target/%{oname}-example-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/example-%{version}.jar
#install -m 644 example/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-example.pom
#%add_to_maven_depmap org.apache.mina mina-example %{version} JPP/%{name} example

install -m 644 filter-ssl/target/%{oname}-filter-ssl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/filter-ssl-%{version}.jar
install -m 644 filter-ssl/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-filter-ssl.pom
%add_to_maven_depmap org.apache.mina mina-filter-ssl %{version} JPP/%{name} filter-ssl

install -m 644 integration-jmx/target/%{oname}-integration-jmx-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/integration-jmx-%{version}.jar
install -m 644 integration-jmx/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-integration-jmx.pom
%add_to_maven_depmap org.apache.mina mina-integration-jmx %{version} JPP/%{name} integration-jmx

#install -m 644 integration-spring/target/%{oname}-integration-spring-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/integration-spring-%{version}.jar
#install -m 644 integration-spring/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-integration-spring.pom
#%add_to_maven_depmap org.apache.mina mina-integration-spring %{version} JPP/%{name} integration-spring

install -m 644 java5/target/%{oname}-java5-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/java5-%{version}.jar
install -m 644 java5/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-java5.pom
%add_to_maven_depmap org.apache.mina mina-java5 %{version} JPP/%{name} java5


(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

pushd $RPM_BUILD_ROOT%{_javadir}
   ln -fs %{name}/core-%{version}.jar %{name}-jdk14-%{version}.jar
   ln -fs %{name}/core.jar %{name}-jdk14.jar
popd

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr core/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf target/site/apidocs*

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
cp -p core/src/main/resources/META-INF/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/core*.jar
%{_javadir}/%{name}-jdk14*.jar
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}
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

#files integration-spring
#%{_javadir}/%{name}/integration-spring*.jar

%files java5
%{_javadir}/%{name}/java5*.jar

#files demo
#%{_javadir}/%{name}/example*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt5_2jpp5
- fixed build with maven3

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt4_2jpp5
- build with velocity 15

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_2jpp5
- fixes for java6 support

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- fixed docdir ownership

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- converted from JPackage by jppimport script

