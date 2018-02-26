BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define gcj_support 0


Name:           jrms
Summary:        JRMS - Java Reliable Multicast Service
Url:            http://www.experimentalstuff.com/Technologies/JRMS/
Version:        1.1
Release:        alt3_3jpp6
Epoch:          0
License:        BSD-style
Group:          Development/Java
Source0:        jrms1.1.jar
Source1:        jrms-build.xml
Source2:        http://repo1.maven.org/maven2/jrms/jrms/1.1/jrms-1.1.pom
Patch0:         jrms-1.1-inria.util.Utilities.patch
Patch1:         jrms-1.1-KeyProtector.patch
Patch2:         jrms-1.1-DataSender.patch
BuildRequires:  ant >= 0:1.7.1
%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
The Java Reliable Multicast Service[tm] is a set of libraries 
and services for building multicast applications. It enables 
building applications that multicast data from senders to 
receivers. The JRM Service supports multiple reliable multicast 
transports through a federated interface, which provides 
isolation to applications, and a service provider interface 
underneath to allow third parties to plug in other reliable 
multicast transport implementations. 

The JRM Service can be used by information distribution 
applications as the transport for delivery of content to very 
large constituencies. As compared to unicast protocols (i.e., 
HTTP), reliable multicast enables broadcasting to groups of 
receivers, ensuring bandwidth conservation and timely delivery. 
TRAM, a reliable multicast transport protocol developed along 
with the JRM Service, is designed for high scalability, targeted 
at very large numbers of receivers. The JRM Service also includes 
new services for multicast address allocation and management of 
channels, as well as a dynamic filtering mechanism that uses Java 
software classes which are pushed into the network for the purpose 
of interpreting the data downstream from the server.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -n %{name}-%{version}
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done
rm -f jrms1.1/src/reliable/transport/tram/TRAMCongestion.java
rm -f jrms1.1/src/reliable/transport/tram/TRAMCongestionPacket.java
rm -f jrms1.1/src/reliable/transport/tram/TRAMCongestionPacketEvent.java
rm -f jrms1.1/src/reliable/transport/tram/TRAMCongestionPacketListener.java

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav

%build
cd jrms1.1
cp %{SOURCE1} build.xml
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc

%install
# jars
cd jrms1.1
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc jrms1.1/*.TXT jrms1.1/*.html
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_3jpp6
- built with java 6

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_3jpp6
- new jpp relase

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_2jpp5
- fixed build with java 5

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

