Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/tjws/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           tjws
Version:        1.3.3
Release:        alt3_2jpp6
Epoch:          0
Summary:        Tiny Java Web Server and Servlet Container        
License:        GPLv2+
Group:          Development/Java
URL:            http://tjws.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/tjws/WebServer-133a.zip
# http://repository.jboss.com/maven2/tjws/webserver/1.3.1/webserver-1.3.1.pom
Source1:        webserver-1.3.3.pom
Source2:        %{name}-component-info.xml
Patch0:         tjws-build.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: bee
BuildRequires: servlet_2_5_api
BuildArch:      noarch

%description
The Miniature Java Web Server includes most of functionality of real
Web Servers including a servlet container capability. The server is
pretty small as in Java code as in result byte code. General purpose of
the Web server is running and debugging servlets. However, it can be
used as a regular web server for sites with low to medium load. I found
also very convenient shipping a servlet based product including this
server, so a user can start a product just after unwrapping. You can
try a web site hosted on this server under Linux. This web server
also works on PDA like Sharp Zaurus LS5xxx, or on Windows CE based
handhelds when JVM installed. It gives additional flexibility for your
PDA, since using file upload and download servlet can simplify file
synchronization and provide control of your PDA from web.

Features and Benefits

    * About 95Kb footprint (TJWS is the smallest one, like 5 times
      less in comparison to competitors LWS and Jetty, more than twice
      less than Winstone)
    * Very fast and reliable, it performs better than some C/C++ based
      web servers, 10%% faster than Apache 2.x 
    * Can scale to thousands connections, clustering configuration is
      about of development
    * Perfect solution for web interfaced applications
    * Standard J2EE servlet deployment for .war packaged applications
    * Simple configuration, no hundreds of config parameters
    * Flexible JSP support
    * Limited JSDK 2.5 support
    * built for Java 6 with intelligent downgraded support for Java 2

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n WebServer
%{__chmod} -Rf a+rX,u+w,g-w,o-w .
%{_bindir}/find -name "*.?ar" | %{_bindir}/xargs -t %{__rm}
%patch0 -p0 -b .build

find . -name '*.xml' -print0 | xargs -r0 sed -i 's,http://7bee.j2ee.us/xml/DTD/,%_datadir/sgml/bee/,g' --

%build
%{_bindir}/bee

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}/%{name}
%{__cp} -p lib/app.jar %{buildroot}%{_javadir}/%{name}/app-%{version}.jar
%{__cp} -p lib/war.jar %{buildroot}%{_javadir}/%{name}/war-%{version}.jar
%{__cp} -p lib/webserver.jar %{buildroot}%{_javadir}/%{name}/webserver-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-webserver.pom
%add_to_maven_depmap tjws webserver %{version} JPP/%{name} webserver

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}/webserver.jar %{buildroot}%{repodirlib}/webserver.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-webserver.pom %{buildroot}%{repodirlib}/webserver.pom
%endif

%files
%doc 
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/app-%{version}.jar
%{_javadir}/%{name}/app.jar
%{_javadir}/%{name}/war-%{version}.jar
%{_javadir}/%{name}/war.jar
%{_javadir}/%{name}/webserver-%{version}.jar
%{_javadir}/%{name}/webserver.jar
%{_datadir}/maven2/poms/JPP.%{name}-webserver.pom
%{_mavendepmapfragdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt3_2jpp6
- built with java 6 due to abstract getParentLogger

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt2_2jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_2jpp6
- new version

