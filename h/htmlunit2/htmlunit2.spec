BuildRequires: maven2-plugin-enforcer
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
#def_with test
%bcond_with test

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           htmlunit2
Version:        2.8
Release:        alt3_2jpp6
Epoch:          0
Summary:        Browser for Java programs
License:        ASL 2.0
Group:          Development/Java
URL:            http://htmlunit.sourceforge.net/
# svn export http://htmlunit.svn.sourceforge.net/svnroot/htmlunit/tags/HtmlUnit-2.8/ htmlunit2-2.8 && tar cjf htmlunit2-2.8.tar.bz2 htmlunit2-2.8
# Exported revision 6155.
Source0:        htmlunit2-2.8.tar.bz2
Source1:        htmlunit2-settings.xml
Source2:        htmlunit2-jpp-depmap.xml
Patch0:         htmlunit2-no-test.patch
Patch1:         htmlunit2-attributes.patch
Patch2:         htmlunit2-apache-james.patch
Patch3:         htmlunit2-compile.patch
Patch4:         htmlunit2-no-sign-artifacts.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       apache-mime4j
Requires:       commons-codec
Requires:       commons-collections
Requires:       commons-httpclient
Requires:       jakarta-commons-io
Requires:       commons-lang
Requires:       jakarta-commons-logging
Requires:       jpackage-utils
Requires:       cssparser
Requires:       httpcomponents-client
Requires:       htmlunit-core-js >= 0:%{version}
Requires:       xalan-j2
BuildRequires:  apache-commons-parent >= 0:9
BuildRequires:  apache-mime4j >= 0:0.6
BuildRequires:  commons-codec >= 0:1.3
# XXX: lowered from 3.2.1
BuildRequires:  commons-collections >= 0:3.2
BuildRequires:  commons-httpclient >= 0:3.1
# XXX: should provide commons-io
BuildRequires:  jakarta-commons-io >= 0:1.4
BuildRequires:  commons-lang >= 0:2.4
# XXX: should provide commons-logging
BuildRequires:  jakarta-commons-logging >= 0:1.1.1
BuildRequires:  james-project
BuildRequires:  cssparser >= 0:0.9.5
BuildRequires:  httpcomponents-project
BuildRequires:  httpcomponents-client >= 0:4.0.1
BuildRequires:  htmlunit-core-js >= 0:%{version}
BuildRequires:  nekohtml >= 0:1.9.14
BuildRequires:  xalan-j2 >= 0:2.7.1
%if %with test
BuildRequires:  commons-fileupload >= 0:1.2.1
BuildRequires:  gsbase >= 0:2.0.1
BuildRequires:  jfreechart >= 0:1.0.12
BuildRequires:  junit4 >= 0:4.5
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  log4j >= 0:1.2.14
BuildRequires:  easymock2 >= 0:2.5.1
BuildRequires:  jetty6 >= 0:6.1.14
BuildRequires:  slf4j >= 0:1.4.3
%if 0
org.eclipse.equinox:common:3.3.0-v20070426:test
org.eclipse.jdt:core:3.4.2.v_883_R34x:test
org.openqa.selenium.webdriver:webdriver-firefox:0.5.524:test
org.openqa.selenium.webdriver:webdriver-htmlunit:0.5.524:test
org.openqa.selenium.webdriver:webdriver-ie:0.5.524:test
%endif
%endif
BuildRequires:  oss-parent >= 0:3
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-checkstyle
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-gpg
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-maven-plugin
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
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
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
%if %without test
%patch0 -p0 -b .sav0
%endif
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%{_bindir}/find -type f -name "*.jar"  | %{_bindir}/xargs -t %{__rm}

%{__cp} -p %{SOURCE1} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

%{__mkdir} external_repo
%{__ln_s} %{_javadir} external_repo/JPP


sed -i -e 's,<id></id>,<id>ALT</id>,' src/assembly/*.xml
sed -i 's,<move file="${basedir}/artifacts/${project.artifactId}-${project.version}.zip",<move file="${basedir}/artifacts/${project.artifactId}-${project.version}-ALT.zip",' pom.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%{__mkdir_p} ${MAVEN_REPO_LOCAL}
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/maven2-settings.xml \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.failure.ignore=true \
%if %without test
        -Dmaven.test.skip=true \
%endif
        install javadoc:javadoc

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/htmlunit-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.sourceforge.htmlunit htmlunit %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
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
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt3_2jpp6
- fixed build with java 7

* Fri Jan 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt2_2jpp6
- fixed build

* Mon Mar 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_2jpp6
- new version

