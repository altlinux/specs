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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/sun-servlet/2.5-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:		servletapi6
Version:	6.0.18
Release:	alt1_1jpp5
Epoch:		0
Summary:	Java servlet and JSP implementation classes
License: 	ASL 2.0
Group: 		Development/Java
Source0:	http://www.apache.org/dist/tomcat/tomcat-6/v6.0.18/src/apache-tomcat-6.0.18-src.tar.gz
Source1:	servletapi6-servlet-build.xml
Source2:	servletapi6-jsp-build.xml
Source3:	servletapi6-component-info.xml
Url: 		http://tomcat.apache.org/
#Requires(post,postun):       /usr/sbin/update-alternatives
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6.5
BuildRequires: java-javadoc
BuildArch:	noarch
Provides:	servlet
Provides:	servlet6
Provides:	servlet25

%description
This subproject contains the source code for the implementation classes
of the Java Servlet 2.5 and JSP 2.1 APIs (packages javax.servlet).

%if %{with_repolib}
%package repolib
Summary:	 Artifacts to be uploaded to a repository library
Group:	         Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Group: 		Development/Documentation
Summary:	Javadoc for %{name}

%description javadoc
Javadoc generated Documentation for %{name}.

%prep
%setup -q -c -T -a 0 -n apache-servletapi-6-src
find . -type f -name "*.jar" | xargs %{__rm}

%build
export CLASSPATH=
export OPT_JAR_LIST=:

cd apache-tomcat-%{version}-src/java

# Servlet
echo "Build Servelet API"
cp -p %{SOURCE1} build.xml
ant dist -Dservletapi.build=build -Dservletapi.dist=dist

# JSP
echo "Build JSP API"
echo `pwd`
cp -p %{SOURCE2} build.xml
ant dist -Dservletapi.build=build -Dservletapi.dist=dist

%install

cd apache-tomcat-%{version}-src
pushd java
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/lib/jsp-api.jar $RPM_BUILD_ROOT%{_javadir}/jspapi6-%{version}.jar
install -m 644 dist/lib/servlet-api.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
popd

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        sed -i "s/@VERSION@/2.5-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/servletapi6-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/servlet-api.jar
	cp -p $RPM_BUILD_ROOT%{_javadir}/jspapi6-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/jsp-api.jar
%endif

%files
%doc apache-tomcat-%{version}-src/LICENSE apache-tomcat-%{version}-src/NOTICE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jspapi6-%{version}.jar
%{_javadir}/jspapi6.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
#%ghost %{_javadocdir}/%{name}
#%ghost %{_javadocdir}/jsp-api

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt1_1jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.10-alt2_4jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.10-alt1_4jpp5
- converted from JPackage by jppimport script

