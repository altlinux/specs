# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define oname hessian

Name: hessian-nodep
Epoch: 0
Version: 3.1.3
Release: alt1_4jpp6
Summary: Hessian binary web service protocol with deps

Group: Development/Java
License: Apache Software License
URL: http://www.caucho.com/%{name}
Source0: http://hessian.caucho.com/download/hessian-%{version}-src.jar
Source1: %{oname}-%{version}-build.xml
Source2: http://www.caucho.com/download/resin-3.1.3-src.zip
Source3: http://repo1.maven.org/maven2/com/caucho/hessian/3.1.3/hessian-3.1.3.pom
BuildArch: noarch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: servlet_2_4_api
BuildRequires: jms_1_1_api
Requires: servlet_2_4_api
Requires: jms_1_1_api

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
The Hessian binary web service protocol makes web 
services usable without requiring a large framework, 
and without learning yet another alphabet soup of 
protocols. Because it is a binary protocol, it is 
well-suited to sending binary data without any need 
to extend the protocol with attachments.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%prep
%setup -q -c -n %{oname}-%{version}
%{__mkdir} src
%{__mv} com src
%{__cp} %{SOURCE1} build.xml
unzip -qq %{SOURCE2}
%{__cp} -R resin-%{version}/modules/util/src/com src
mkdir -p src/com/caucho/jms/util/
%{__cp} resin-%{version}/modules/resin/src/com/caucho/jms/util/BytesMessageOutputStream.java src/com/caucho/jms/util/
#%{__rm} -rf resin-%{version}

%build
CLASSPATH="$(build-classpath servlet_2_4_api jms_1_1_api):target/classes" \
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath="only" dist

%install
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}/%{_javadir}
%{__install} -p -m 0644 dist/%{oname}-%{version}.jar \
    ${RPM_BUILD_ROOT}/%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar \
    ${RPM_BUILD_ROOT}/%{_javadir}/%{name}.jar
%add_to_maven_depmap com.caucho %{oname} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}/%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/docs/api/* ${RPM_BUILD_ROOT}/%{_javadocdir}/%{name}-%{version}
# ghost symlink
%{__ln_s} %{name}-%{version} ${RPM_BUILD_ROOT}/%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_4jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_2jpp5
- converted from JPackage by jppimport script

