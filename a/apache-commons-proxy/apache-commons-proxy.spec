BuildRequires: jmock
BuildRequires: /proc mojo-maven2-plugin-jdepend mojo-maven2-plugin-rat
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

%define short_name commons-proxy
%define base_name proxy

Name:           apache-commons-proxy
Version:        1.0
Release:        alt3_4jpp6
Epoch:          0
Summary:        Apache Commons Proxy Component
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://commons.apache.org/proxy/
Source0:        http://www.apache.org/dist/commons/proxy/source/commons-proxy-1.0-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source4:        %{name}-build.xml
Source5:        %{name}-maven-build.xml
Source6:        %{name}-maven-build.properties

Patch0:         %{name}-pom.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: fonts-ttf-liberation
BuildRequires: ant >= 0:1.7
BuildRequires: junit
BuildRequires: java-javadoc
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
%endif
BuildRequires: aopalliance
BuildRequires: axis
BuildRequires: burlap
BuildRequires: cglib
BuildRequires: concurrent
BuildRequires: hessian
BuildRequires: javassist
BuildRequires: xmlrpc2

Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
The Proxy design pattern (GoF ) allows you to provide "a 
surrogate or placeholder for another object to control 
access to it". Proxies can be used in many ways. Some of 
which are:
* Deferred Initialization - the proxy acts as a "stand-in" 
  for the actual implementation allowing it to be 
  instantiated only when absolutely necessary.
* Security - the proxy object can verify that the user 
  actually has the permission to execute the method (a la 
  EJB).
* Logging - the proxy can log evey method invocation, 
  providing valuable debugging information.
* Performance Monitoring - the proxy can log each method 
  invocation to a performance monitor allowing system 
  administrators to see what parts of the system are 
  potentially bogged down.
Commons Proxy supports dynamic proxy generation using proxy
factories, object providers, invokers, and interceptors. 

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    javadoc
%{summary}.

%if %with maven
%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Provides:       %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -b .sav0
%{__perl} -pi \
    -e 's/\r$//g;' \
  PROPOSAL.html LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
cp -p %{SOURCE1} settings.xml

%if %with maven
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%else
cp %{SOURCE4} build.xml
cp %{SOURCE5} maven-build.xml
cp %{SOURCE6} maven-build.properties
%endif

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
%if %with maven
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Dmaven.test.failure.ignore=true"
mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc site
%else
ln -sf $(build-classpath aopalliance) .m2/repository/
ln -sf $(build-classpath axis/jaxrpc) .m2/repository/axis-jaxrpc.jar
ln -sf $(build-classpath burlap) .m2/repository/
ln -sf $(build-classpath caucho-services) .m2/repository/
ln -sf $(build-classpath cglib-nodep) .m2/repository/
ln -sf $(build-classpath commons-codec) .m2/repository/
ln -sf $(build-classpath commons-collections) .m2/repository/
ln -sf $(build-classpath commons-logging) .m2/repository/
ln -sf $(build-classpath concurrent) .m2/repository/
ln -sf $(build-classpath hessian) .m2/repository/
ln -sf $(build-classpath javassist) .m2/repository/
ln -sf $(build-classpath jmock) .m2/repository/
ln -sf $(build-classpath junit44) .m2/repository/junit4.jar
ln -sf $(build-classpath xmlrpc2) .m2/repository/

ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dmaven.mode.offline=true \
  package test javadoc
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}.jar
%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
install -m 644 LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
rm -rf target/site/apidocs
cp -pR target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
#%{__install} -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/*

%if %with maven
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
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp6
- fixed build - added jmock dep

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp6
- new version

