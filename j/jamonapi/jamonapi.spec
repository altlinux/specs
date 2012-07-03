BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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


Summary:	JAMon Java Application Monitor
URL:		http://jamonapi.sourceforge.net/
Source0:        jamonapi-2.7-src.tar.gz
# cvs -d:pserver:anonymous@jamonapi.cvs.sourceforge.net:/cvsroot/jamonapi login
# cvs -z3 -d:pserver:anonymous@jamonapi.cvs.sourceforge.net:/cvsroot/jamonapi export -r v2_70 jamonapi
Source1:        jamonapi-catalina_tomcat4.jar
Patch0:         jamonapi-JAMonDataSource.patch

Name:		jamonapi
Version:	2.7
Release:	alt3_2jpp6
Epoch:		0
License:	BSD-style License
Group:		Development/Java
BuildArch:	noarch
BuildRequires:	jpackage-utils >= 0:1.7.5
BuildRequires:	ant >= 0:1.7.1
BuildRequires:	hsqldb
BuildRequires:	interceptor_3_0_api
BuildRequires:	jakarta-oro
BuildRequires:	jetty6-core
BuildRequires:	log4j
BuildRequires:	servlet_2_4_api
BuildRequires:	tomcat5-server-lib

Requires:	jpackage-utils >= 0:1.7.5
Requires:	hsqldb
Requires:	interceptor_3_0_api
Requires:	jakarta-oro
Requires:	log4j
Requires:	servlet_2_4_api
Source44: import.info

%description
The Java Application Monitor (JAMon) is a free, simple, 
high performance, thread safe, Java API that allows 
developers to easily monitor production applications. 
JAMon can be used to determine application performance 
bottlenecks, user/application interactions, and application 
scalability. JAMon gathers summary statistics such as hits, 
execution times (total, average, minimum, maximum, standard 
deviation), and simultaneous application requests. JAMon 
statistics are displayed in the clickable JAMon Report. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath ant) lib
ln -sf $(build-classpath tomcat5/catalina) lib
cp %{SOURCE1} lib/catalina_tomcat4.jar
ln -sf $(build-classpath tomcat5/catalina-optional) lib
#fdsapi-1.2.jar.no
ln -sf $(build-classpath hsqldb) lib
ln -sf $(build-classpath oro) lib
ln -sf $(build-classpath interceptor_3_0_api) lib/javaee.jar
ln -sf $(build-classpath jetty6/jetty6) lib
ln -sf $(build-classpath jetty6/jetty6-util) lib
ln -sf $(build-classpath log4j) lib
ln -sf $(build-classpath servlet_2_4_api) lib
%patch0 -b .sav0


%build
export CLASSPATH=

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f src/ant/build.xml dist javadoc

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 dist/jamon-%{version}.jar \
                   $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 0644 dist/jamontomcat-%{version}.jar \
                   $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-tomcat-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat.jar

# war
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 0644 dist/jamon.war \
                   $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.war

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr src/doc/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr src/JAMonUsersGuide $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p src/JAMonUsersGuide/JAMonLicense.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%files
%{_javadir}/*
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/JAMonLicense.html
%{_datadir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}/JAMonUsersGuide
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt3_2jpp6
- built with java 6 due to abstract getParentLogger

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt2_2jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt2_1jpp5
- selected java5 compiler explicitly

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_1jpp5
- new jpp5.0 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

