Patch33: taglib-maven2-plugin-alt-maven3.patch
BuildRequires: servletapi4
Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define altname maven-taglib-plugin

Name:           taglib-maven2-plugin
Version:        2.3.1
Release:        alt4_2jpp5
Epoch:          0
Summary:        Taglib Maven plugin
License:        Artistic License
Url:            http://dtddoc.sourceforge.net/
Group:          Development/Java
Source0:        maven-taglib-plugin-2.3.1.tar.gz
# svn export http://maven-taglib.svn.sourceforge.net/svnroot/maven-taglib/m2-taglib-plugin/tags/maven-taglib-plugin-2.3.1/
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         maventaglib-TagreferenceMojo.patch
Patch1:         maventaglib-pom.patch
Patch2:         maventaglib-ValidateRenderer.patch

BuildRequires: jpackage-utils >= 1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
#BuildRequires: maven-embedder
BuildRequires: maven-surefire-plugin
BuildRequires: tlddoc
BuildRequires: tomcat5-servlet-2.4-api
BuildRequires: tomcat5-jsp-2.0-api

Requires: tlddoc
Requires: tomcat5-servlet-2.4-api
Requires: tomcat5-jsp-2.0-api

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif


%description
Taglib maven plugin.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q -n %{altname}-%{version}
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch33

%build
cp %{SOURCE1} maven2-settings.xml

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
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.skip=true \
        install 

#       -Dmaven.test.failure.ignore=true \

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        javadoc:javadoc

%install
%{__rm} -fr %{buildroot}
%{__install} -d -m 755 %{buildroot}%{_datadir}/maven2/poms
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 pom.xml \
             %{buildroot}%{_datadir}/maven2/poms/JPP-taglib-maven2-plugin.pom
%add_to_maven_depmap net.sourceforge.maven-taglib maven-taglib-plugin %{version} JPP %{name}

%{__install} -m 644 target/%{altname}-%{version}.jar \
             %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

%{__install} -d -m 755 %{buildroot}%{_datadir}/maven2/plugins
pushd ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
    ln -sf %{_javadir}/%{name}-%{version}.jar maven-taglib-plugin.jar
popd

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_datadir}/maven2/plugins/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%{_javadocdir}/%{name}

%changelog
* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt4_2jpp5
- dropped maven-embedder dependency

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt3_2jpp5
- fixed build with maven3

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt2_2jpp5
- fixed build

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_2jpp5
- new version

