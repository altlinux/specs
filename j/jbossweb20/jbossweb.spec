%define oldname jbossweb
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with bootstrap

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jboss/web/%{version}.%{reltag}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%define reltag  GA

Name:           jbossweb20
Version:        2.0.1
Release:        alt3_4jpp6
Epoch:          0
Summary:        JBoss Web Server based on Apache Tomcat
Group:          Development/Java
License:        LGPLv2+
URL:            http://labs.jboss.com/jbossweb/
# svn export http://anonsvn.jboss.org/repos/jbossweb/tags/JBOSSWEB_2_0_1_GA/ ;
# tar -zcf JBOSSWEB_2_0_1_GA.tar.gz JBOSSWEB_2_0_1_GA
Source0:        JBOSSWEB_2_0_1_GA.tar.gz
Source1:        jbossweb-component-info.xml
Patch0:         jbossweb-versionless-jbossas-dep.patch
BuildRequires: ant
BuildRequires: ecj
BuildRequires: jpackage-utils >= 0:1.6.0
Requires: ecj
Requires: jpackage-utils >= 0:1.6.0
BuildArch:      noarch

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

%if %{with_repolib}
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
%setup -q -n JBOSSWEB_2_0_1_GA
%patch0 -p0
find . -type f -name *.jar | xargs -t %{__rm}
ln -s $(build-classpath ecj) lib/jasper-jdt.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install
%{__mkdir_p} %{buildroot}%{_javadir}
%{__mkdir_p} %{buildroot}%{_javadir}/%{name}

pushd output/jars >& /dev/null ; 
for i in *.jar ; do
    install -m 644 $i %{buildroot}%{_javadir}/%{name}/${i/\.jar/}-%{version}.jar ;
done
ln -s $(build-classpath ecj) %{buildroot}%{_javadir}/%{name}/jasper-jdt-%{version}.jar

pushd %{buildroot}%{_javadir}/%{name} >& /dev/null && \
for jar in *-%{version}*; do \
    ln -sf ${jar} ${jar/-%{version}/}; \
done 
popd >& /dev/null


%if %{with_repolib}
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -a %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/@VERSION@/%{version}.%{reltag}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -a %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -a %{PATCH0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}/el-api.jar %{buildroot}%{repodirlib}
cp -p $(build-classpath ecj) %{buildroot}%{repodirlib}/jasper-jdt.jar
cp -p %{buildroot}%{_javadir}/%{name}/jbossweb.jar %{buildroot}%{repodirlib}
cp -p %{buildroot}%{_javadir}/%{name}/jbossweb-extras.jar %{buildroot}%{repodirlib}
cp -p %{buildroot}%{_javadir}/%{name}/jsp-api.jar %{buildroot}%{repodirlib}
cp -p %{buildroot}%{_javadir}/%{name}/servlet-api.jar %{buildroot}%{repodirlib}
cp -p jbossweb-src.zip %{buildroot}%{repodirlib}
%endif

%files
%doc output/README.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/annotations-api-%{version}.jar
%{_javadir}/%{name}/annotations-api.jar
%{_javadir}/%{name}/el-api-%{version}.jar
%{_javadir}/%{name}/el-api.jar
%{_javadir}/%{name}/jasper-jdt-%{version}.jar
%{_javadir}/%{name}/jasper-jdt.jar
%{_javadir}/%{name}/jbossweb-%{version}.jar
%{_javadir}/%{name}/jbossweb-extras-%{version}.jar
%{_javadir}/%{name}/jbossweb-extras.jar
%{_javadir}/%{name}/jbossweb.jar
%{_javadir}/%{name}/jsp-api-%{version}.jar
%{_javadir}/%{name}/jsp-api.jar
%{_javadir}/%{name}/servlet-api-%{version}.jar
%{_javadir}/%{name}/servlet-api.jar

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_4jpp6
- compat build

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt2_4jpp6
- rebuild to get rid of osgi requires. 

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_4jpp6
- fixed build

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_4jpp5
- new version

