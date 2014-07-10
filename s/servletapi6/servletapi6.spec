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



Name:		servletapi6
Version:	6.0.18
Release:	alt2_1jpp5
Epoch:		0
Summary:	Java servlet and JSP implementation classes
License: 	ASL 2.0
Group: 		Development/Java
Source0:	http://www.apache.org/dist/tomcat/tomcat-6/v6.0.18/src/apache-tomcat-6.0.18-src.tar.gz
Source1:	servletapi6-servlet-build.xml
Source2:	servletapi6-jsp-build.xml
Url: 		http://tomcat.apache.org/
#Requires(post,postun):       /usr/sbin/update-alternatives
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6.5
BuildRequires: java-javadoc
BuildArch:	noarch
Provides:	servlet
Provides:	servletapi
Provides:	servlet_api
Provides:	servlet_2_5_api
Provides:	jsp_api
Provides:	jsp_2_1_api
#Provides:	servlet6
#Provides:	servlet25

%description
This subproject contains the source code for the implementation classes
of the Java Servlet 2.5 and JSP 2.1 APIs (packages javax.servlet).

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

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_%{name}<<EOF
%{_javadir}/servlet.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_2_5_api_%{name}<<EOF
%{_javadir}/servlet_2_5_api.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_api_%{name}<<EOF
%{_javadir}/servlet_api.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_2_1_api_%{name}<<EOF
%{_javadir}/jsp_2_1_api.jar	%{_javadir}/jspapi6-%{version}.jar	10200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_api_%{name}<<EOF
%{_javadir}/jsp_api.jar	%{_javadir}/jspapi6-%{version}.jar	10200
EOF

cat >>$RPM_BUILD_ROOT/%_altdir/servletapi_%{name}<<EOF
%{_javadir}/servletapi.jar	%{_javadir}/%{name}-%{version}.jar	20300
EOF

%files
%doc apache-tomcat-%{version}-src/LICENSE apache-tomcat-%{version}-src/NOTICE
%_altdir/jsp_api_%{name}
%_altdir/jsp_2_1_api_%{name}
%_altdir/servlet_api_%{name}
%_altdir/servlet_2_5_api_%{name}
%_altdir/servlet_%{name}
%_altdir/servletapi_%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jspapi6-%{version}.jar
%{_javadir}/jspapi6.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt2_1jpp5
- added jpackage alternatives

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt1_1jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.10-alt2_4jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.10-alt1_4jpp5
- converted from JPackage by jppimport script

