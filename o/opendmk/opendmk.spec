Packager: Igor Vlasenko <viy@altlinux.ru>
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

Name:           opendmk
Version:        1.0
Release:        alt1_0.b01.ea.1jpp6
Summary:        Open Dynamic Management Kit

Group:          Development/Java
License:        GPL 2
URL:            http://opendmk.dev.java.net/

Source0:        https://opendmk.dev.java.net/download/opendmk-1.0-b01-ea-src-dual-04-Apr-2007_18-00-43.zip
Source1:        http://download.java.net/maven/glassfish/org/jvnet/opendmk/jmxremote_optional/1.0_01-ea/jmxremote_optional-1.0_01-ea.pom
Source2:        jdmkrt-1.0-b01-ea.pom
Source3:        jdmktk-1.0-b01-ea.pom

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 1.7

Requires: jpackage-utils >= 0:1.7.5

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
The Project OpenDMK source code is based on the Java DMK 5.1
patch level 3 code base. It supports the following features:
* Virtual MBeans: Project OpenDMK includes an MBeanServerBuilder
  which adds MBeanServerInterceptors on top of a JMX API 
  MBeanServer. MBeanServerInterceptors can be used to support
  Virtual MBeans.
* Federated MBean Servers: Project OpenDMK includes a Cascading
  API, with a naming scheme based on ObjectName prefixes 
  (com.sun.jdmk.remote.cascading).
* Agent Discovery: Project OpenDMK includes a Discovery API
  (based on IP multicast), which allows OpenDMK agents to 
  discover each other dynamically.
* Interoperability: Project OpenDMK includes all Java DMK 5.1 
  Legacy Connectors, providing interoperability with legacy
  Java DMK agents. In addition, these connectors can be wrapped
  in JMX Remote API compliant connectors, allowing a smooth
  migration towards standard implementations. The legacy 
  connectors include:
  o A legacy RMI JRMP/IIOP connector
  o A legacy HTTP/HTTPS connector
* HTML Console: Project OpenDMK includes a legacy HTML Adaptor,
  which can provide limited access to JMX MBeans from a regular
  web browser.
* JMXMP connector: Project OpenDMK includes an implementation
  of JSR 160 (JMX Remote API 1.0) optional packages 
  (jmxremote_optional.jar) for the JMXMP protocol, which can
  run on top of the mandatory implementations of the
  JMX API 1.2 and JMX Remote API 1.0.
* SNMP interoperability: NOT INCLUDED HERE

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n OpenDMK-src
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
%ant buildall

%install
%__rm -rf %{buildroot}

# jar
%__install -d -m 755 %{buildroot}%{_javadir}/%{name}

%__install -m 644 dist/lib/jdmkrt.jar %{buildroot}%{_javadir}/%{name}/jdmkrt-%{version}.jar
%__install -m 644 dist/lib/jdmktk.jar %{buildroot}%{_javadir}/%{name}/jdmktk-%{version}.jar
%__install -m 644 dist/lib/jmxremote_optional.jar %{buildroot}%{_javadir}/%{name}/jmxremote_optional-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# pom
%__install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
%__install -m 644 %{SOURCE1} \
        %{buildroot}%{_datadir}/maven2/poms/JPP.opendmk-jmxremote_optional.pom
%add_to_maven_depmap org.jvnet.opendmk jmxremote_optional 1.0_01-ea JPP/opendmk jmxremote_optional
%add_to_maven_depmap javax.management jmxremote_optional 1.0_01-ea JPP/opendmk jmxremote_optional
%__install -m 644 %{SOURCE2} \
        %{buildroot}%{_datadir}/maven2/poms/JPP.opendmk-jdmkrt.pom
%add_to_maven_depmap org.jvnet.opendmk jdmkrt 1.0_01-ea JPP/opendmk jdmkrt
%__install -m 644 %{SOURCE3} \
        %{buildroot}%{_datadir}/maven2/poms/JPP.opendmk-jdmktk.pom
%add_to_maven_depmap org.jvnet.opendmk jdmktk 1.0_01-ea JPP/opendmk jdmktk

%__install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%__install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
%__cp -pr dist/LEGAL_NOTICES %{buildroot}%{_docdir}/%{name}-%{version}

%__install -d -m 755 %{buildroot}%{_datadir}/%{name}
%__install -d -m 755 %{buildroot}%{_datadir}/%{name}/bin
%__install -m 755 dist/bin/mibgen %{buildroot}%{_datadir}/%{name}/bin
%__cp -pr dist/etc %{buildroot}%{_datadir}/%{name}
%__install -d -m 755 %{buildroot}%{_datadir}/%{name}/lib
%__ln_s %{_javadir}/%{name}/jdmkrt.jar %{buildroot}%{_datadir}/%{name}/lib
%__ln_s %{_javadir}/%{name}/jdmktk.jar %{buildroot}%{_datadir}/%{name}/lib
%__ln_s %{_javadir}/%{name}/jmxremote_optional.jar %{buildroot}%{_datadir}/%{name}/lib


%files
%{_javadir}/%{name}/*.jar
%{_datadir}/%{name}
%{_docdir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.b01.ea.1jpp6
- new version

