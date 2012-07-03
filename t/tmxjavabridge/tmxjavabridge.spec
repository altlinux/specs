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

Name:           tmxjavabridge
Version:        1.1.008
Release:        alt1_1jpp6
Summary:        TMXResourceBundle - TMX Java Bridge

Group:          Development/Java
License:        LGPL
URL:            http://tmxjavabridge.sourceforge.net

Source0:        tmxjavabridge_1_1_008.zip
Source1:        tmxjavabridge-build.xml
Source2:        tmxjavabridge-1.1.008.pom

BuildRequires: ant >= 1.6.5
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jpackage-utils >= 0:5.0.0

Requires: jpackage-utils >= 0:5.0.0

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
TMXResourceBundle is an Open Source extension of Java 
ResourceBundle class to read text resources directly from a
TMX file.
TMX (Translation Memory eXchange) is the vendor-neutral open
XML standard for the exchange of Translation Memory (TM) 
data created by Computer Aided Translation (CAT) and 
localization tools. The purpose of TMX is to allow easier 
exchange of translation memory data between tools and/or 
translation vendors with little or no loss of critical data
during the process. In existence since 1998, TMX is a 
certifiable standard format. TMX is developed and maintained
by OSCAR (Open Standards for Container/Content Allowing 
Re-use), a LISA (Localization Industry Standards Association)
Special Interest Group.
One of the main concerns of internationalization consists of
separating the main source code from the texts, the labels, 
the messages and all the other objects related to the specific 
language in use. This facilitates the translation process as 
such as all the resources related to the local language 
context are well identified and separated.
Since version JDK 1.1, Java provides great support for 
internationalization (i18n) by offering several instruments 
and tools, for example the support to Unicode 2.0, the 
multilingual environments and the object localization, just 
to mention a few.
However, all these instruments may not be sufficient when we 
target a global market in which the costs to translate and 
update the texts (including labels, messages, menu elements 
and so on) can easily become quite high.
This is the context where the TMX standard comes to help by 
applying to the translation and management process of these 
texts the concepts of reuse, increase of consistency, and the 
shortening of the production cycle. All this with the added 
bonus of cutting the development costs.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n tmxresourcebundle
cp %{SOURCE1} build.xml

%build
export OPT_JAR_LIST="ant/ant-junit junit"
%ant -Djunit.jar=$(build-classpath junit) jar test javadoc

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 build/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

%__install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%__install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.tecnick.htmlutils %{name} %{version} JPP %{name}

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a build/javadoc %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc *.TXT
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.008-alt1_1jpp6
- new version

