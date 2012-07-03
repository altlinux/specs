BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
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

Summary:                CORBA ORB used in GlassFish v2
Name:                   gfv2corba
Version:                9.1
Release:                alt1_0.b01.1jpp6
Epoch:                  0
Group:                  Development/Java
License:                GPL + CDDL
Url:                    http://gf-corba-v3-mirror.kenai.com/
BuildArch:              noarch
BuildRequires:          jpackage-utils >= 0:1.7.5
BuildRequires:          ant >= 0:1.7.1
BuildRequires:          ejb_2_1_api
BuildRequires:          emma
BuildRequires:          apache-jdo-2.0-api
BuildRequires:          jscheme
BuildRequires:          junit
BuildRequires:          testng

Source0:                gfv2corba.tgz
# hg clone https://hg.kenai.com/hg/gf-corba-v3-mirror~gfv2-master gfv2corba
# tar czf gfv2corba.tgz gfv2corba/
Patch0:                 gfv2corba-ArrayFactory.patch
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
This project contains the source code, documentation, and 
tests for the CORBA ORB that is used in the GlassFish v2
application server project.  The GlassFish ORB complies 
with the CORBA 2.3.1 specification, and with the CORBA 3.0 
specifications for the Interoperable Name Service and 
Portable Interceptors. It includes both IDL and RMI-IIOP 
support. The GlassFish ORB has an open, extensible 
architecture that supports flexible configuration and 
extension through an open SPI. This ORB is written 
completely in Java.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}
# remove external jars
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
# lib/ejb-2_1-api.jar.no
ln -sf $(build-classpath ejb_2_1_api) lib/ejb-2_1-api.jar
# lib/emma_ant.jar.no
ln -sf $(build-classpath emma_ant) lib/emma_ant.jar
# lib/emma.jar.no
ln -sf $(build-classpath emma) lib/emma.jar
# lib/japex.jar.no

# lib/jdo2-api-2.3-SNAPSHOT.jar.no
ln -sf $(build-classpath apache-jdo-2.0-api) lib/jdo2-api-2.3-SNAPSHOT.jar
# lib/jscheme.jar.no
ln -sf $(build-classpath jscheme) lib/jscheme.jar
# lib/jschemelogutil.jar.no
mv lib/jschemelogutil.jar.no lib/jschemelogutil.jar

# lib/junit.jar.no
ln -sf $(build-classpath junit) lib/junit.jar
# lib/maven-repository-importer-1.1.jar.no
# lib/testng.jar.no
ln -sf $(build-classpath testng) lib/testng.jar
%patch0 -b .sav0

%build
ant -f make/build.xml build javadoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 build/release/lib/idlj.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/idlj-%{version}.jar
install -m 644 build/release/lib/omgapi.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/omgapi-%{version}.jar
install -m 644 build/release/lib/optorbcomp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/optorbcomp-%{version}.jar
install -m 644 build/release/lib/orblib.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/orblib-%{version}.jar
install -m 644 build/release/lib/peorb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/peorb-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -prf www/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf www/javadoc

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -prf www/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:9.1-alt1_0.b01.1jpp6
- converted from JPackage by jppimport script

