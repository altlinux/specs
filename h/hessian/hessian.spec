Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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


Name: hessian
Epoch: 1
Version: 3.0.8
Release: alt2_1jpp5
Summary: Hessian binary web service protocol

Group: Development/Java
License: Apache Software License
URL: http://www.caucho.com/%{name}
Source0: http://www.caucho.com/%{name}/download/%{name}-%{version}-src.tar.bz2
Source1: %{name}-%{version}-build.xml
BuildArch: noarch
Obsoletes: %{name}3
Provides: %{name}3
Patch: hessian-3.0.8-alt-java5fix.patch

BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: servletapi5
Requires: servletapi5

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

%description    javadoc
Javadoc for %{name}

%prep
%setup -q -c -n %{name}-%{version}
%{__mkdir} src
%{__mv} com src
%{__cp} %{SOURCE1} build.xml
%patch -p1

%build
CLASSPATH="$(build-classpath servletapi5):target/classes" \
    ant -Dbuild.sysclasspath="only" dist

%install
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}/%{_javadir}
%{__install} -p -m 0644 dist/%{name}-%{version}.jar \
    ${RPM_BUILD_ROOT}/%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar \
    ${RPM_BUILD_ROOT}/%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}/%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/docs/api/* ${RPM_BUILD_ROOT}/%{_javadocdir}/%{name}-%{version}
# ghost symlink
%{__ln_s} %{name}-%{version} ${RPM_BUILD_ROOT}/%{_javadocdir}/%{name}

%post javadoc
%{__rm} -f %{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    %{__rm} -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}


%changelog
* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt2_1jpp5
- fixed Sisyphus build 

* Fri Jul 25 2008 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt2_1jpp1.7
- rebuild with java 1.4.2

* Mon Jul 09 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.0.8-alt1_1jpp1.7
- converted from JPackage by jppimport script

