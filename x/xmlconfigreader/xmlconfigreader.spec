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

Name:           xmlconfigreader
Version:        1.0.003
Release:        alt1_1jpp6
Summary:        ResourceBundle extension

Group:          Development/Java
License:        LGPL
URL:            http://xmlconfigreader.sourceforge.net

Source0:        xmlconfigreader_1_0_003.zip
Source1:        xmlconfigreader-build.xml
Source2:        xmlconfigreader-1.0.003.pom

BuildRequires: ant >= 1.6.5
BuildRequires: ant-junit
BuildRequires: junit
BuildRequires: jpackage-utils >= 0:5.0.0

Requires: jpackage-utils >= 0:5.0.0

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
XMLConfigReader is an Open Source Java class extension of 
Java ResourceBundle class to read configuration data 
directly from an XML file.
XMLConfigReader reads structured resource text data from an
XML file and store it on a hashtable.
The hashtable keys are taken from the value of the first 
attribute of the <item> elements.
The hash table values are hashtables containing the sub-items
names as keys and the sub-items data as value.
You instantiate the XMLConfigReader class in a program to 
read data from a XML file. Once the class is instantiated, 
it reads all the data in a XML file and loads into a DOM 
(Document Object Model) tree. Then it populates a hashtable 
so the getString, getInt and getDouble methods can be called 
to find text information based on a key and subkey.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
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
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.003-alt1_1jpp6
- new version

