Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: jetty6-servlet-2.5-api
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without maven

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           htmlunit
Version:        1.14
Release:        alt5_4jpp6
Epoch:          0
Summary:        Browser for Java programs
License:        ASL 2.0
Group:          Development/Java
URL:            http://htmlunit.sourceforge.net/
# svn export http://htmlunit.svn.sourceforge.net/svnroot/htmlunit/tags/HtmlUnit-1dot14/ htmlunit-1.14
Source0:        htmlunit-1.14.tar.gz
Source1:        htmlunit-settings.xml
Source2:        htmlunit-jpp-depmap.xml
Patch0:         htmlunit-1.14-pom.patch
Patch1:         htmlunit-1.14-Stylesheet.patch
Patch2:         htmlunit-1.14-build.patch
Patch3:         htmlunit-1.14-rhino.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: cssparser >= 0:0.9.4
Requires: jakarta-commons-codec >= 0:1.3
Requires: jakarta-commons-collections >= 0:3.2
Requires: jakarta-commons-httpclient >= 0:3.1
Requires: jakarta-commons-io >= 0:1.3.1
Requires: commons-lang >= 0:2.3
Requires: jakarta-commons-logging >= 0:1.1
Requires: jaxen >= 0:1.1.1
Requires: nekohtml >= 0:0.9.5
Requires: rhino16 >= 0:1.6-0.R7
Requires: xerces-j2 >= 0:2.6.2
Requires: xml-commons-jaxp-1.3-apis
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit >= 0:3.8.2
%if %with maven
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
%endif
BuildRequires: cssparser
BuildRequires: excalibur-avalon-framework >= 0:4.1.3
BuildRequires: gsbase >= 0:2.0.1
BuildRequires: jakarta-commons-codec >= 0:1.3
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-fileupload >= 0:1.2.1
BuildRequires: jakarta-commons-httpclient >= 0:3.0.1
BuildRequires: jakarta-commons-io >= 0:1.3.1
BuildRequires: commons-lang
BuildRequires: jakarta-commons-logging >= 0:1.1
BuildRequires: jakarta-commons-parent
BuildRequires: jaxen >= 0:1.1
BuildRequires: jetty6
BuildRequires: nekohtml >= 0:0.9.5
BuildRequires: rhino16
BuildRequires: sac
%if 0
BuildRequires: servlet_2_4_api
%else
# XXX: for pom
BuildRequires: geronimo-servlet-2.4-api
%endif
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
HtmlUnit is a "browser for Java programs". It models the HTML
documents and provides an API that allows you to invoke pages,
fill forms, click links, etc. just like you do in your
"normal" browser.

It has fairly good JavaScript support (which gets continuously
improved) and is able to work even with quite complex AJAX
libraries simulating either Firefox or Internet Explorer
depending on the configuration you want to use. 
It is typically used for testing purposes or to retrieve 
information from web sites. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
find . -name "*.jar"  | xargs -t rm

cp -p %{SOURCE1} settings.xml

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3

%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}

%if %with maven
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.test.skip=true \
        install javadoc:javadoc
%else
export CLASSPATH=$(build-classpath \
commons-codec \
commons-collections \
commons-fileupload \
commons-httpclient \
commons-io \
commons-lang \
commons-logging \
cssparser \
gsbase \
jaxen \
jetty6/jetty6 \
jetty6/jetty6-util \
js16 \
sac \
servlet_2_4_api \
nekohtml \
xerces-j2 \
xml-commons-jaxp-1.3-apis  \
)
CLASSPATH=$CLASSPATH:ant-target/classes:ant-target/test-classes
export LANG=en_US.UTF-8
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -d -Dbuild.sysclasspath=only javadoc
%endif

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
%if %with maven
install -p -m 644 target/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
%else
install -p -m 644 ant-target/distrib/HtmlUnit.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
%endif
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%else
cp -pr ant-target/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Thu May 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt5_4jpp6
- fixed build

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt4_4jpp6
- build with velocity15

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt3_4jpp6
- build with new jakarta-commons-lang

* Wed Nov 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt2_4jpp6
- added BR: jetty6-servlet-2.5-api

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_4jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_3jpp5
- full build

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt0.1jpp
maven 2.0.7 bootstrap

