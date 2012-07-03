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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without maven
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0

%define base_name       digester
%define short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.8.1
Release:        alt3_11jpp6
Epoch:          0
Summary:        Apache Commons Digester
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/digester/
Source0:        http://www.apache.org/dist/jakarta/commons/digester/source/commons-digester-1.8.1-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Patch0:         apache-commons-digester-pom.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
%endif
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-logging
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: apache-commons-beanutils
Requires: apache-commons-collections
Requires: apache-commons-logging
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info

%description
Many projects read XML configuration files to provide 
initialization of various Java objects within the system. 
There are several ways of doing this, and the Digester 
component was designed to provide a common implementation 
that can be used in many different projects.
Basically, the Digester package lets you configure an 
XML -> Java object mapping module, which triggers certain 
actions called rules whenever a particular pattern of nested 
XML elements is recognized. A rich set of predefined rules 
is available for your use, or you can also create your own. 
Advanced features of Digester include:
- Ability to plug in your own pattern matching engine, if 
  the standard one is not sufficient for your requirements. 
- Optional namespace-aware processing, so that you can 
  define rules that are relevant only to a particular XML 
  namespace. 
- Encapsulation of Rules into RuleSets that can be easily 
  and conveniently reused in more than one application that 
  requires the same type of processing. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%{__perl} -pi -e 's/\r$//g' LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%if %with maven
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif
%patch0 -b .sav0

%build
export CLASSPATH=
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL}"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc

export CLASSPATH=$(build-classpath commons-beanutils commons-collections commons-logging junit)
CLASSPATH=${CLASSPATH}:`pwd`/target/%{short_name}-%{version}.jar
%else

export CLASSPATH=$(build-classpath commons-beanutils commons-collections commons-logging junit)
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/junit`"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first dist


# Build rss -- needed by struts
CLASSPATH=${CLASSPATH}:`pwd`/dist/%{short_name}.jar
%endif

(cd src/examples/rss; %{ant} dist)

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
%if %with maven
cp -p target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
cp -p dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
cp -p src/examples/rss/dist/%{short_name}-rss.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-rss-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{name}-rss.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-rss.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-rss-%{version}.jar
ln -s %{name}-rss-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-rss.jar

%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{short_name}.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/apache-commons-digester-%{version}-rss.jar.*
%{_libdir}/gcj/%{name}/apache-commons-digester-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/*

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Mar 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt3_11jpp6
- bumped release to fix obsoletes

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt2_11jpp6
- fixed repolib version

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.1-alt1_11jpp6
- new version

