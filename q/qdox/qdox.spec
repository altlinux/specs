Patch33: qdox-disable-xsite.patch
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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


Name:           qdox
Version:        1.12
Release:        alt2_2jpp6
Summary:        Extract class/interface/method definitions from sources
Epoch:          1
License:        Apache-style Software License
URL:            http://qdox.codehaus.org/
Group:          Development/Java
# svn export http://svn.codehaus.org/qdox/tags/qdox-1.12/ && tar cjf qdox-1.12.tar.bz2 qdox-1.12
# Exported revision 1031.
Source0:        qdox-1.12.tar.bz2
Source1:        qdox-build.xml
Source2:        qdox-settings.xml
Source3:        qdox-jpp-depmap.xml
Patch0:         qdox-pom.patch
Requires:       annotation_1_0_api
Requires:       jpackage-utils
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit >= 0:3.8.2
BuildRequires:  byaccj
BuildRequires:  java-cup
BuildRequires:  jflex
%if %with maven
BuildRequires:  maven2 >= 2.0.8
BuildRequires:  maven2-plugin-ant
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-changes
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-dependency
BuildRequires:  maven2-plugin-deploy
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven2-common-poms >= 1.0
BuildRequires:  maven2-default-skin
BuildRequires:  mojo-maven2-plugin-cobertura
BuildRequires:  jflex-maven-plugin
BuildRequires:  jmock >= 0:1.0
%endif
BuildRequires:  annotation_1_0_api
BuildRequires:  excalibur-avalon-framework
BuildRequires:  excalibur-avalon-logkit
BuildRequires:  jakarta-slide-webdavclient
BuildRequires:  xmlrpc
#BuildRequires:  xsite
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif
Source44: import.info

%description
QDox is a high speed, small footprint parser 
for extracting class/interface/method definitions 
from source files complete with JavaDoc @tags. 
It is designed to be used by active code 
generators or documentation tools. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q 
%patch0 -p0 -b .sav0
%patch33

rm bootstrap/yacc.linux
ln -s /usr/bin/byaccj bootstrap/yacc.linux
ln -s $(build-classpath jflex) bootstrap
ln -s $(build-classpath java_cup) bootstrap
cp -p %{SOURCE1} build.xml
cp -p %{SOURCE2} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml

%if %without maven
perl -pi -e 's/\@VERSION\@/%{version}/g;' build.xml
%endif

%build
%if %with maven
mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

# XXX: huh?
mkdir -p target/generated-site
cp -pr src/site/* target/generated-site

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s settings.xml \
        -Dproject.build.directory=$(pwd)/target \
        -Dmaven2.jpp.depmap.file=%{SOURCE3} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.build.timestamp=$(date "+%Y-%m-%d") \
        ant:ant install javadoc:javadoc 
%else
mkdir -p src/java/com/thoughtworks/qdox/parser/impl
export CLASSPATH=$(build-classpath jmock jflex java_cup):target/classes:target/test-classes
%{java} JFlex.Main \
    -d src/java/com/thoughtworks/qdox/parser/impl \
    src/grammar/lexer.flex
pushd src
byaccj \
    -Jnorun \
    -Jnoconstruct \
    -Jclass=Parser \
    -Jsemantic=Value \
    -Jpackage=com.thoughtworks.qdox.parser.impl \
    grammar/parser.y
popd
mv src/Parser.java src/java/com/thoughtworks/qdox/parser/impl
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar test javadoc
%endif

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p target/%{name}-%{version}.jar \
      %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap qdox qdox %{version} JPP %{name}
%add_to_maven_depmap com.thoughtworks.qdox qdox %{version} JPP %{name}

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt %{buildroot}%{_docdir}/%{name}-%{version}
cp -p README.txt %{buildroot}%{_docdir}/%{name}-%{version}
%if %with maven
#cp -pr target/site/* %{buildroot}%{_docdir}/%{name}-%{version}
#rm -r %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
#ln -s %{_javadocdir}/%{name} %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %doc %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%doc %{_docdir}/%{name}-%{version}/README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with maven
#files manual
#%doc %{_docdir}/%{name}-%{version}
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt2_2jpp6
- fixed build with java 7

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt1_2jpp6
- new version

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt2_5jpp6
- rebuild with target=5

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp6
- new version

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp5
- reverted to version 1.6.1

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp5
- fixed build with jpackage 5

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- rebuilt with maven1

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp1.7
- converted from JPackage by jppimport script

