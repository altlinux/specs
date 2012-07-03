BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%define short_name  neethi

Name:           ws-commons-neethi
Version:        2.0.4
Release:        alt4_2jpp6
Epoch:          0
Summary:        Apache Neethi WS-Policy implementation 
License:        ASL 2.0
Group:          Development/Java
URL:            http://ws.apache.org/commons/neethi/index.html
# svn -q export http://svn.apache.org/repos/asf/webservices/commons/tags/neethi/2.0.4/ neethi && tar cjf neethi-2.0.4.tar.bz2 neethi
Source0:        %{short_name}-%{version}.tar.bz2
Source1:        %{name}-setting.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-build.xml
Patch0:         %{name}-pom_xml.patch
Patch1:         %{name}-site_xml.patch
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  jdepend
BuildRequires:  junit >= 0:3.8.2
%if %with maven
BuildRequires:  maven2 >= 2.0.8
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-one
BuildRequires:  maven2-plugin-project-info-reports
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-site
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven2-default-skin
BuildRequires:  maven-jxr
BuildRequires:  maven-release
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  mojo-maven2-plugin-jdepend
%endif
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
BuildRequires:  ws-commons-axiom >= 0:1.2.3
BuildRequires:  wstx
BuildRequires:  stax_1_0_api
BuildRequires:  apache-commons-logging
BuildRequires:  wsdl4j >= 0:1.6.2

Requires:       jpackage-utils >= 0:1.7.5
Requires:       ws-commons-axiom >= 0:1.2.3
Requires:       wstx
Requires:       stax_1_0_api
Requires:       apache-commons-logging
Requires:       wsdl4j >= 0:1.6.2

# ws-commons-policy has NOT been renamed to neethi
Provides:   neethi = %{epoch}:%{version}-%{release}
Obsoletes:  neethi <= 0:1.0.1
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
Apache Neethi provides an implementation of WS-Policy specification.It
provides a convenient model to process any policy information at
runtime. In other words, it allows you to convert any policy to an
object (which is its runtime representation) and play with it as you
like.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}
cp -p %{SOURCE1} settings.xml
cp -p %{SOURCE3} build.xml

%build
%if %with maven
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
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc 
	#site
%else
export OPT_JAR_LIST=
export CLASSPATH=$(build-classpath \
stax_1_0_api \
ws-commons-axiom-api \
ws-commons-axiom-impl \
wstx/wstx-asl \
)
CLASSPATH=$CLASSPATH:target/classes:target/test-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar test javadoc
%endif

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap org.apache.neethi neethi %{version} JPP %{name}

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
ln -s %{name}.jar %{short_name}.jar
)

# poms
%if %with maven
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
%endif

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p *.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
#cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/*
%{_javadir}/*.jar
%{_datadir}/maven2/poms/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt4_2jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt3_2jpp6
- new jpp relase

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt3_1jpp6
- build with velocity 15

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_1jpp6
- build with wstx 3.2.8

* Wed Sep 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_1jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt4_4jpp5
- new jpp release

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt4_3jpp5
- fixed build

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_3jpp5
- fixed build with maven 2.0.7

* Mon Oct 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_2jpp5
- fixed build with velocity

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt2_2jpp5
- rebuild with velocity14

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

