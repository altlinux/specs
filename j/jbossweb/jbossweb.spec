BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.1.3
%define name jbossweb
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

#def_with bootstrap
%bcond_with bootstrap
#def_with jci
%bcond_with jci
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/jboss/web/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%define reltag  GA


%define jspspec 2.1
%define major_version 2
%define minor_version 1
%define micro_version 3
%define packdname .
%define servletspec 2.5

Name:           jbossweb
Version:        2.1.3
Release:        alt1_2jpp6
Epoch:          0
Summary:        JBoss Web Server based on Apache Tomcat
Group:          Development/Java
License:        LGPLv2+
URL:            http://labs.jboss.com/jbossweb/
# svn export -q http://anonsvn.jboss.org/repos/jbossweb/tags/JBOSSWEB_2_1_3_GA/ jbossweb2-2.1.3 && tar cjf jbossweb2-2.1.3.tar.bz2 jbossweb2-2.1.3
Source0:        jbossweb2-2.1.3.tar.bz2
Source1:        jbossweb-component-info.xml
Requires:       ecj3 >= 0:3.1.2
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  ant-trax
BuildRequires:  axis
BuildRequires:  jakarta-commons-daemon
%if %with jci
BuildRequires:  jakarta-commons-jci
%endif
BuildRequires:  javamail_1_3_1_api
BuildRequires:  ecj3 >= 0:3.1.2
BuildRequires:  jpackage-utils >= 0:1.6.0
BuildRequires:  wsdl4j
BuildArch:      noarch
Source44: import.info

%description
JBoss Web Server is an enterprise ready web server designed for medium
and large applications, based on the Apache Tomcat. It is meant to be
used as a replacement for the standard Web servers on all major
platforms. JBoss Web Server provides organizations with a single
deployment platform for Java Server Pages (JSP) and Java Servlet
technologies, Microsoft .NET, PHP, and CGI. It uses a genuine high
performance hybrid technology that incorporates the best of the most
recent OS technologies for processing high volume data, while keeping
all the reference Java specifications. It supports both in and out of
the process execution of CGI and PHP scripts, aas well as .NET
applications. The hybrid technology model offers the best from
threading and event processing models, and that makes the JBoss Web
Server one of the fastest and most scalable web servers in the market.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
AutoReqProv: yes,noosgi

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n jbossweb2-%{version}
find . -type f -name *.jar | xargs -t %{__rm}

pushd lib
%if %with jci
build-jar-repository -s -p . commons-jci-core
%endif
build-jar-repository -s -p . axis/jaxrpc
ln -s $(build-classpath ecj3) jasper-jdt.jar
build-jar-repository -s -p . javamail_1_3_1_api
build-jar-repository -s -p . wsdl4j
popd

%if %without jci
rm java/org/apache/jasper/compiler/JCICompiler.java
%endif

%build
export CLASSPATH=
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/{nodeps,trax}`

pushd %{packdname}
    # we don't care about the tarballs and we're going to replace
    # tomcat-dbcp.jar with jakarta-commons-{collections,dbcp,pool}-tomcat5.jar
    # so just create a dummy file for later removal
    touch HACK
    # who needs a build.properties file anyway
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbase.path="." \
        -Dbuild.compiler="modern" \
        -Dcommons-collections.jar="$(build-classpath commons-collections)" \
        -Dcommons-daemon.jar="$(build-classpath commons-daemon)" \
        -Dcommons-daemon.jsvc.tar.gz="HACK" \
        -Djasper-jdt.jar="lib/jasper-jdt.jar" \
        -Djdt.jar="$(build-classpath ecj3)" \
        -Dtomcat-dbcp.jar="HACK" \
        -Dtomcat-native.tar.gz="HACK" \
        -Dversion="%{version}" \
        -Dversion.build="%{micro_version}"
popd

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__mkdir_p} %{buildroot}%{_javadir}/%{name}

pushd %{packdname}/output/jars
for i in *.jar ; do
    cp -p $i %{buildroot}%{_javadir}/%{name}/${i/\.jar/}-%{version}.jar ;
done
ln -sf $(build-classpath ecj3) %{buildroot}%{_javadir}/%{name}/jasper-jdt-%{version}.jar

pushd %{buildroot}%{_javadir}/%{name} >& /dev/null && \
for jar in *-%{version}*; do \
    ln -sf ${jar} ${jar/-%{version}/}; \
done 
popd

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/@VERSION@/%{version}.%{reltag}-brew/g' %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}/el-api-%{version}.jar %{buildroot}%{repodirlib}/el-api.jar
cp -p %{buildroot}%{_javadir}/%{name}/jasper-jdt-%{version}.jar %{buildroot}%{repodirlib}/jasper-jdt.jar
cp -p %{buildroot}%{_javadir}/%{name}/jbossweb-%{version}.jar %{buildroot}%{repodirlib}/jbossweb.jar
cp -p %{buildroot}%{_javadir}/%{name}/jsp-api-%{version}.jar %{buildroot}%{repodirlib}/jsp-api.jar
cp -p %{buildroot}%{_javadir}/%{name}/servlet-api-%{version}.jar %{buildroot}%{repodirlib}/servlet-api.jar
%endif

%files
%doc %{packdname}/{LICENSE,NOTICE,RELEASE*}
%doc %{packdname}/{KEYS,PATCHES.txt,BUILDING.txt,RUNNING.txt}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/el-api-%{version}.jar
%{_javadir}/%{name}/el-api.jar
%{_javadir}/%{name}/jasper-jdt-%{version}.jar
%{_javadir}/%{name}/jasper-jdt.jar
%{_javadir}/%{name}/jbossweb-%{version}.jar
%{_javadir}/%{name}/jbossweb.jar
%{_javadir}/%{name}/jsp-api-%{version}.jar
%{_javadir}/%{name}/jsp-api.jar
%{_javadir}/%{name}/servlet-api-%{version}.jar
%{_javadir}/%{name}/servlet-api.jar

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp6
- new jpp release

* Sat Jan 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_1jpp6
- new version

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt2_4jpp6
- rebuild to get rid of osgi requires. 

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_4jpp6
- fixed build

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_4jpp5
- new version

