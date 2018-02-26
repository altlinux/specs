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


Name:           burlap
Version:        3.0.8
Release:	alt2_6jpp6
Epoch:          0
Summary:        Web service protocol
Group:          Development/Java
License:        ASL 1.1
URL:            http://www.caucho.com/%{name}
Source0:        http://distro.ibiblio.org/pub/linux/distributions/gentoo/distfiles/%{name}-%{version}.tar.bz2
Patch0:         burlap-proxy.patch
Requires: caucho-services
Requires: hessian
Requires: servlet_2_4_api
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: caucho-services
BuildRequires: hessian
BuildRequires: servlet_2_4_api
Obsoletes:      %{name}3 < %{epoch}:%{version}-%{release}
Provides:       %{name}3 = %{epoch}:%{version}-%{release}
BuildArch:      noarch
Source44: import.info
Patch33: burlap-3.0.8-alt-java5.patch

%description
The Burlap web service protocol makes web services 
usable without requiring a large framework, and without 
learning yet another alphabet soup of protocols. 
Creating a client is as simple as creating an API interface.
Creating a service is as simple as adding a method to a servlet.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%patch33 -p1

%build
export CLASSPATH=$(build-classpath caucho-services hessian servlet_2_4_api)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc

%install

%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/burlap.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/doc/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.8-alt2_6jpp6
- new jpp release

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0.8-alt2_3jpp5
- fixed build with java 5

* Mon Oct 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.0.8-alt1_3jpp1.7
- converted from JPackage by jppimport script

