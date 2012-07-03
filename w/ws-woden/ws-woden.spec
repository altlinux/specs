Patch33: ws-woden-1.0M8_20080423-alt-drop-maven-one-plugin.patch
%define _without_online_tests 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

# If you don't want to run the online tests
# give rpmbuild option '--without online_tests'

%define with_online_tests %{!?_with_online_tests:0}%{?_with_online_tests:1}
%define without_online_tests %{?_with_online_tests:0}%{!?_with_online_tests:1}

%define namedversion    1.0M8
%define short_name      woden

Name:           ws-woden
Version:        1.0
Release:        alt3_0.m8.2jpp6
Epoch:          0
Summary:        WSDL document library
License:        Apache Software License 2.0
Url:            http://ws.apache.org/woden/
Group:          Development/Java
Source0:        woden-1.0M8_20080423.tar.gz
# svn export http://svn.apache.org/repos/asf/webservices/woden/tags/1.0M8_20080423/ woden-1.0M8_20080423

Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         %{name}-pom_xml.patch
Patch1:         %{name}-TestDescription1001.patch


BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven2 >= 2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-one
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
BuildRequires: apache-commons-parent
BuildRequires: maven-plugin-bundle
BuildRequires: jakarta-commons-logging
BuildRequires: stax_1_0_api
BuildRequires: ws-commons-XmlSchema
BuildRequires: ws-commons-axiom
BuildRequires: wsdl4j
BuildRequires: wstx
Requires: ant >= 0:1.7.1
Requires: stax_1_0_api
Requires: ws-commons-XmlSchema
Requires: ws-commons-axiom
Requires: wsdl4j
Requires: wstx

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
Source44: import.info

%description
The Woden project is an incubation subproject of the Apache
Web Services Project to develop a Java class library for
reading, manipulating, creating and writing WSDL documents,
initially to support WSDL 2.0 but with the longer term aim
of supporting past, present and future versions of WSDL.

There are two main deliverables: an API and an implementation.
The Woden API will consist of a set of Java interfaces. The
WSDL 2.0-specific portion of the Woden API will conform to the
W3C WSDL 2.0 specification. The implementation will be a high
performance implementation directly usable in other Apache
projects such as Axis2.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n woden-1.0M8_20080423/
cp %{SOURCE1} settings.xml
mkdir -p .m2/repository/JPP/maven2/default_poms/
%patch0 -b .sav
%if ! %{with_online_tests}
%patch1 -b .noonline
%endif
%patch33

%build
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
	-Dmaven.test.skip=true \
	-e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install 

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
#        install javadoc:aggregate

mkdir tmpdir
pushd tmpdir
jar xf ../woden-api/target/woden-api-%{namedversion}.jar
jar xf ../woden-dom/target/woden-impl-dom-%{namedversion}.jar
jar xf ../woden-om/target/woden-impl-om-%{namedversion}.jar
rm -rf META-INF
jar cf ../woden-%{namedversion}.jar *
popd
rm -rf tmpdir

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 woden-api/target/woden-api-%{namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -m 644 woden-dom/target/woden-impl-dom-%{namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-impl-dom-%{version}.jar
install -m 644 woden-om/target/woden-impl-om-%{namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-impl-om-%{version}.jar
install -m 644 woden-%{namedversion}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap org.apache.woden woden %{namedversion} JPP %{name}
%add_to_maven_depmap org.apache.woden woden-api %{namedversion} JPP %{name}-api
%add_to_maven_depmap org.apache.woden woden-impl-dom %{namedversion} JPP %{name}-impl-dom
%add_to_maven_depmap org.apache.woden woden-impl-om %{namedversion} JPP %{name}-impl-om

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 woden-api/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-api.pom
install -m 644 woden-dom/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-impl-dom.pom
install -m 644 woden-om/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-impl-om.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.m8.2jpp6
- dropped felix-maven2 dependency

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.m8.2jpp6
- fixed build with maven3

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.m8.2jpp6
- jpp 6.0 relese

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.m8.1jpp5
- new version

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.m7a.1jpp1.7
- converted from JPackage by jppimport script

