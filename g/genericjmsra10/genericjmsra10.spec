Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0

%define oname genericjmsra
%define sname genericra

Summary:        Generic JMS Resource Adapter
Name:           genericjmsra10
Version:        1.0
Release:        alt1_1jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            https://genericjmsra.dev.java.net/
Group:          Development/Java
Source0:        genericjmsra10.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r RELEASE_1_0 genericjmsra
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/jencks/genericra/1.0/genericra-1.0.pom
Patch0:         genericjmsra10-config-properties.patch
Patch1:         genericjmsra10-build.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: j2ee_connector_1_5_api
BuildRequires: jms_1_1_api
Requires: j2ee_connector_1_5_api
Requires: jms_1_1_api

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
J2EE 1.4 specifies J2EE Connector Architecture 1.5 as the 
basic mechanism to integrate JMS providers with J2EE 
application servers. However some JMS provider vendors do 
not provide a J2EE Connector Architecture 1.5 compliant 
resource adapter to enable such an integration. This project
helps such JMS providers to integrate with J2EE application
servers by wrapping their JMS client library in a J2EE
Connector Architecture 1.5 resource adapter. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%prep
%setup -q -n %{oname}
for j in $(find . -name "*.jar"); do
      mv $j $j.no
done
%patch0 -b .sav0
%patch1 -b .sav1

%build
export RA_HOME=$(pwd)
export CLASSPATH=$(build-classpath \
j2ee_connector_1_5_api \
jms_1_1_api \
)
ant -Dbuild.sysclasspath=first build javadoc

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}

# jars
install -m 644 build/dist/%{sname}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# rars
install -m 644 build/dist/%{sname}.rar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap jencks genericra %{version} JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%doc LICENSE
%{_datadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- first build

