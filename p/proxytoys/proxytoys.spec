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


Name:           proxytoys
Version:        0.2.1
Release:        alt1_2jpp5
Epoch:          0
Summary:        ProxyToys
Group:          Development/Java
License:        BSD-Style
URL:            http://proxytoys.codehaus.org/
Source0:        http://dist.codehaus.org/proxytoys/distributions/proxytoys-src-0.2.1.zip
Patch0:         proxytoys-build_xml.patch
Requires: cglib >= 0:2.1.3
Requires: xstream >= 0:1.1.2
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: junit
BuildRequires: jmock
BuildRequires: cglib >= 0:2.1.3
BuildRequires: xstream >= 0:1.1.2
BuildRequires: xpp3
BuildArch:      noarch

%description
ProxyToys.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%prep
%setup -q -c
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t rm
%patch0 -p0

pushd lib
ln -s $(build-classpath cglib-nodep) .
#BUILD/xstream-1.1.3/lib/jmock-2004-03-19.jar.no
ln -s $(build-classpath jmock) .
#BUILD/xstream-1.1.3/lib/junit-3.8.1.jar.no
ln -s $(build-classpath junit) .
#BUILD/xstream-1.1.3/lib/xpp3-1.1.3.4d_b4_min.jar.no
ln -s $(build-classpath xpp3) .
#BUILD/proxytoys-0.2.1/lib/xstream-1.1.2.jar.no
ln -s $(build-classpath xstream) .
popd

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
%{ant} test javadoc

%install

install -Dpm 644 build/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/website/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt1_2jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt1_1jpp5
- fixed repocop warnings

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

