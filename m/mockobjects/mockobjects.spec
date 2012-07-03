BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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


Name:           mockobjects
Version:        0.09
Release:        alt4_19jpp6
Epoch:          0
Summary:        Java MockObjects package
License:        BSD Style
Group:          Development/Java
URL:            http://www.mockobjects.com/
Source0:        http://www.mockobjects.com/dist/%{name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/mockobjects/mockobjects-core/0.09/mockobjects-core-0.09.pom
Source2:        http://repo1.maven.org/maven2/mockobjects/mockobjects-jdk1.4/0.09/mockobjects-jdk1.4-0.09.pom
Source3:        http://repo1.maven.org/maven2/mockobjects/mockobjects-alt-jdk1.4/0.09/mockobjects-alt-jdk1.4-0.09.pom
Source4:        mockobjects-httpclient-0.09.pom
Source5:        mockobjects-alt-httpclient-0.09.pom
Source6:        mockobjects-jdk1.4-j2ee1.4-0.09.pom
Patch0:         %{name}-build.patch
Patch1:         %{name}-ext-httpmethod-abstract.patch
Patch2:         %{name}-AssertMo.patch
Patch3:         %{name}-MockPageContext.patch
Patch4:         %{name}-MockConnection.patch
Patch5:         %{name}-MockMessagePublisher.patch
Patch6:         %{name}-MockQueueConnectionFactory.patch
Patch7:         %{name}-MockQueueSender.patch
Patch8:         %{name}-MockSession.patch
Patch9:         %{name}-MockTopicConnectionFactory.patch
Patch10:        mockobjects-0.09-j2ee14-MockHttpServletRequest.patch
Patch11:        mockobjects-0.09-j2ee14-MockHttpServletResponse.patch
Patch12:        mockobjects-FileImpl.patch
Patch13:        mockobjects-java6.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: jpackage-utils >= 0:1.7.5
Requires: junit
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: apache-commons-httpclient
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: geronimo-j2ee-1.4-apis
BuildArch:      noarch
Source44: import.info

%description
The Mock Objects project is a generic unit testing framework whose goal
is to facilitate developing unit tests in the mock object style. The
goal of this project is to provide, a core mock objects framework. This
is a library of code that supports the implementation of mock objects.
It is based around a set of expectation classes for values and
collections. There are also various other classes to make mock objects
easier to write or to use.

%package jdk1.4
Summary:        MockObjects for 1.4 JDK
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description jdk1.4
MockObjects specific to JDK >= 1.4.x

%package httpclient
Summary:        MockObjects for Commons HttpClient
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: apache-commons-httpclient

%description httpclient
MockObjects for Commons HttpClient

%package alt-httpclient
Summary:        Mockable API for Commons HttpClient
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-httpclient = %{epoch}:%{version}-%{release}
Requires: apache-commons-httpclient

%description alt-httpclient
Alternative API for Commons HttpClient to allow for testing

%package alt-jdk1.4
Summary:        Mockable API for JDK 1.4
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-jdk1.4 = %{epoch}:%{version}-%{release}

%description alt-jdk1.4
Alternative API for JDK 1.4 to allow for testing

%package jdk1.4-j2ee1.4
Summary:        Mockable J2EE API for JDK 1.4 and J2EE 1.4
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-jdk1.4 = %{epoch}:%{version}-%{release}

%description jdk1.4-j2ee1.4
API for JDK 1.4 to allow testing with J2EE 1.4 mocks

%prep
%setup -q
cp -pr src/j2ee/1.3/com/mockobjects/servlet src/j2ee/1.4/com/mockobjects/
%patch0 -b .sav0
%patch1 -p1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch12 -b .sav12
%patch13 -b .sav13

mkdir -p out/ext/httpclient/classes

%build
CLASSPATH=`build-classpath junit` %{ant} jar-core
CLASSPATH=`build-classpath junit` %{ant} jar-jdk
CLASSPATH=`build-classpath commons-httpclient junit` %{ant} jar-ext-httpclient
CLASSPATH=`build-classpath geronimo-j2ee-1.4-apis junit` %{ant} -d -Djdk.version=1.4 -Dj2ee.version=1.4 jar-j2ee

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

pushd out
install -p -m 644 %{name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
install -p -m 644 %{name}-httpclient.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-httpclient-%{version}.jar
install -p -m 644 alt-httpclient.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-alt-httpclient-%{version}.jar

# Install JDK Mocks and alternatives
install -p -m 644 %{name}-jdk1.4-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-jdk1.4-%{version}.jar
install -p -m 644 %{name}-alt-jdk1.4-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-alt-jdk1.4-%{version}.jar

# Install J2EE Mocks
install -p -m 644 %{name}-jdk1.4-j2ee1.4-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-jdk1.4-j2ee1.4-%{version}.jar
popd

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-mockobjects-core.pom
%add_to_maven_depmap %{name} %{name}-core %{version} JPP %{name}-core
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-mockobjects-jdk1.4.pom
%add_to_maven_depmap %{name} %{name}-jdk1.4 %{version} JPP %{name}-jdk1.4
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-mockobjects-alt-jdk1.4.pom
%add_to_maven_depmap %{name} %{name}-alt-jdk1.4 %{version} JPP %{name}-alt-jdk1.4
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-mockobjects-httpclient.pom
%add_to_maven_depmap %{name} %{name}-httpclient %{version} JPP %{name}-httpclient
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-mockobjects-alt-httpclient.pom
%add_to_maven_depmap %{name} %{name}-alt-httpclient %{version} JPP %{name}-alt-httpclient
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-mockobjects-jdk1.4-j2ee1.4.pom
%add_to_maven_depmap %{name} %{name}-jdk1.4-j2ee1.4 %{version} JPP %{name}-jdk1.4-j2ee1.4

pushd $RPM_BUILD_ROOT%{_javadir} 
for jar in *-%{version}.jar; do
        ln -s ${jar} $(/bin/echo ${jar} | sed "s|-%{version}||g")
done
popd

%files
%doc doc/README
%{_javadir}/mockobjects-core-%{version}.jar
%{_javadir}/mockobjects-core.jar
%{_datadir}/maven2/poms/JPP-mockobjects-core.pom
#%%{_datadir}/maven2/poms/
%{_mavendepmapfragdir}/%{name}

%files jdk1.4
%{_javadir}/%{name}-jdk1.4-%{version}.jar
%{_javadir}/%{name}-jdk1.4.jar
%{_datadir}/maven2/poms/JPP-mockobjects-jdk1.4.pom

%files httpclient
%{_javadir}/%{name}-httpclient-%{version}.jar
%{_javadir}/%{name}-httpclient.jar
%{_datadir}/maven2/poms/JPP-mockobjects-httpclient.pom

%files alt-jdk1.4
%{_javadir}/%{name}-alt-jdk1.4-%{version}.jar
%{_javadir}/%{name}-alt-jdk1.4.jar
%{_datadir}/maven2/poms/JPP-mockobjects-alt-jdk1.4.pom

%files alt-httpclient
%{_javadir}/%{name}-alt-httpclient-%{version}.jar
%{_javadir}/%{name}-alt-httpclient.jar
%{_datadir}/maven2/poms/JPP-mockobjects-alt-httpclient.pom

%files jdk1.4-j2ee1.4
%{_javadir}/%{name}-jdk1.4-j2ee1.4-%{version}.jar
%{_javadir}/%{name}-jdk1.4-j2ee1.4.jar
%{_datadir}/maven2/poms/JPP-mockobjects-jdk1.4-j2ee1.4.pom

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.09-alt4_19jpp6
- built with java 6 due to abstract getParentLogger

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.09-alt3_19jpp6
- new jpp release

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.09-alt3_17jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.09-alt2_17jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.09-alt1_17jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.09-alt1_16jpp1.7
- converted from JPackage by jppimport script

