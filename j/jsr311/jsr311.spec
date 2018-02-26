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

%define gcj_support 0


Name:           jsr311
Version:        1.0
Release:        alt1_3jpp6
Epoch:          0
Summary:        JAX-RS: Java API for RESTful Web Services
License:        CDDL
Group:          Development/Java
URL:            https://jsr311.dev.java.net/
# svn export https://jsr311.dev.java.net/svn/jsr311/tags/jsr311-api-1.0/jsr311-api/ jsr311-1.0 --username guest
# tar czf jsr311-1.0-src.tar.gz jsr311-1.0/
Source0:        jsr311-1.0-src.tar.gz
Source1:        jsr311-settings.xml
Source2:        jsr311-jpp-depmap.xml

Patch0:         jsr311-1.0-pom-xml.patch
Provides:       jsr311-api = %{epoch}:%{version}-%{release}

Buildarch:      noarch


BuildRequires: ant
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: concurrent
BuildRequires: dtdparser
BuildRequires: maven2 >= 2.0.4-10
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-plugin-surefire-report
BuildRequires: maven2-common-poms >= 1.0
#BuildRequires:  maven-wagon >= 1.0-0.1.b2
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: junit
BuildRequires: log4j

Requires(post): jpackage-utils >= 0:1.7.2
Requires(postun): jpackage-utils >= 0:1.7.2

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif


%description
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p0

cp -p %{SOURCE1} settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven.test.failure.ignore=true \
	    install

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/jsr311-api-1.0.jar \
          $RPM_BUILD_ROOT%{_javadir}/jsr311-api-1.0.jar
install -pm 644 target/jsr311-api-1.0-sources.jar \
          $RPM_BUILD_ROOT%{_javadir}/jsr311-api-1.0-sources.jar

(cd $RPM_BUILD_ROOT%{_javadir} \
    && ln -sf jsr311-api-1.0.jar jsr311.jar \
    && ln -sf jsr311-api-1.0.jar jsr311-api.jar \
    && ln -sf jsr311-api-1.0.jar %{name}-%{version}.jar )
(cd $RPM_BUILD_ROOT%{_javadir} \
    && ln -sf jsr311-api-1.0-sources.jar jsr311-sources.jar \
    && ln -sf jsr311-api-1.0-sources.jar jsr311-api-sources.jar \
    && ln -sf jsr311-api-1.0-sources.jar %{name}-%{version}-sources.jar )

# poms
%add_to_maven_depmap org.jsr311 %{name} %{version} JPP %{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/jsr311-api-1.0-javadoc.jar %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif


%files
%doc README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jsr311.jar
%{_javadir}/jsr311-api-1.0.jar
%{_javadir}/jsr311-api.jar
%{_javadir}/jsr311-api-1.0-sources.jar
%{_javadir}/jsr311-sources.jar
%{_javadir}/jsr311-api-sources.jar
%{_javadir}/%{name}-%{version}-sources.jar
%{_javadir}/%{name}-sources.jar

%{_datadir}/maven2/poms/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp6
- new version

