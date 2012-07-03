BuildRequires: jansi
BuildRequires: velocity
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

%define with_tests %{!?_with_tests:0}%{?_with_tests:1}
%define without_tests %{?_with_tests:0}%{!?_with_tests:1}

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without maven
#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name  email
%define short_name commons-%{base_name}

Name:           apache-commons-email
Version:        1.1
Release:        alt3_4jpp6
Epoch:          0
Summary:        Apache Commons Email Package
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://commons.apache.org/email
Source0:        http://www.apache.org/dist/commons/email/source/commons-email-1.1-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml

Patch0:         apache-commons-email-pom.patch
Patch1:         apache-commons-email-maven-build.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-checkstyle
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-default-skin
BuildRequires: mojo-maven2-plugin-clirr
BuildRequires: mojo-maven2-plugin-findbugs
BuildRequires: checkstyle4
BuildRequires: checkstyle4-optional
%endif
BuildRequires: gmaven
BuildRequires: gmaven-runtime-1.5
BuildRequires: groovy15
BuildRequires: jaf_1_1_api
BuildRequires: javamail_1_4_api
BuildRequires: fonts-ttf-liberation
BuildRequires: qdox
BuildRequires: retrotranslator
BuildRequires: retroweaver
BuildRequires: servlet_2_3_api
BuildRequires: subethasmtp1
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Requires: jaf_1_1_api
Requires: javamail_1_4_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
Commons-Email aims to provide a API for sending email. It 
is built on top of the Java Mail API, which it aims to 
simplify. 
Some of the mail classes that are provided are as follows: 

SimpleEmail    - This class is used to send basic text based
                 emails. 
MultiPartEmail - This class is used to send multipart messages. 
                 This allows a text message with attachments 
                 either inline or attached. 
HtmlEmail      - This class is used to send HTML formatted 
                 emails. It has all of the capabilities as 
                 MultiPartEmail allowing attachments to be 
                 easily added. It also supports embedded images. 
EmailAttachment - This is a simple container class to allow
                 for easy handling of attachments. It is for 
                 se with instances of MultiPartEmail and HtmlEmail. 

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

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    javadoc
%{summary}.

%if %with maven
%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -b .sav0
%patch1 -b .sav1
%{__perl} -pi \
    -e 's/\r$//g;' \
  PROPOSAL.html LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

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

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%if %with maven
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL}"
mkdir -p .m2/repository/JPP/maven2/default_poms/
cp pom.xml .m2/repository/JPP/maven2/default_poms/JPP-commons-email.pom
mkdir -p .m2/repository/commons-email/commons-email/1.0/
ln -sf $(pwd)/target/commons-email-1.1.jar .m2/repository/commons-email/commons-email/1.0/commons-email-1.0.jar
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
	-Dmaven.test.skip=true \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc 
#	site
%else
mkdir -p .m2/repository/backport-util-concurrent/backport-util-concurrent/3.0/
ln -sf $(build-classpath backport-util-concurrent) .m2/repository/backport-util-concurrent/backport-util-concurrent/3.0/backport-util-concurrent-3.0.jar
export CLASSPATH=$(build-classpath subethasmtp1-smtp subethasmtp1-wiser commons-logging)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
         -Dbuild.sysclasspath=first \
         -Dmaven.mode.offline=true \
         -Dmaven.repo.local=$(pwd)/.m2/repository \
         jar javadoc test
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|apache-|jakarta-|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|apache-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 0644 README.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 0644 NOTICE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 0644 LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 0644 RELEASE-NOTES.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

%if %with maven_no
# manual
rm -rf target/site/apidocs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/*.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/*

%if %with maven_no
%files manual
%doc %{_docdir}/%{name}-%{version}/site
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_4jpp6
- fixed build (added jansi BR:)

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed symlinks

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- added osgi manifest

