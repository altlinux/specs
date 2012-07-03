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


Name:           apache-mime4j
Version:        0.6
Release:        alt3_2jpp6
Epoch:          0
Summary:        Mime stream parser
Group:          Development/Java
License:        BSD
URL:            http://james.apache.org/mime4j
Source0:        http://www.apache.org/dist/james/mime4j/apache-mime4j-0.6-src.tar.gz
Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml
Patch0:         %{name}-pom.patch
Patch1:         %{name}-TestHandler.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: jakarta-commons-logging
Requires: jpackage-utils
BuildRequires: apache-jar-resource-bundle >= 0:1.3
BuildRequires: james-project >= 0:1.2
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-remote-resources
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-shared-downloader
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: mojo-maven2-plugin-javacc
BuildRequires: maven-plugin-bundle
BuildRequires: apache-commons-parent
BuildRequires: apache-commons-io
BuildRequires: jakarta-commons-logging
BuildRequires: log4j
BuildArch:      noarch
Source44: import.info

%description
Apache Mime4j is developed by the Apache James team but now
has a dedicated mailing list.
mime4j provides a parser, MimeStreamParser, for e-mail 
message streams in plain rfc822 and MIME format. The parser 
uses a callback mechanism to report parsing events such as 
the start of an entity header, the start of a body, etc. If 
you are familiar with the SAX XML parser interface you 
should have no problem getting started with mime4j.
The parser only deals with the structure of the message 
stream. It won't do any decoding of base64 or quoted-printable 
encoded header fields and bodies. This is intentional - the 
parser should only provide the most basic functionality needed 
to build more complex parsers. However, mime4j does include 
facilities to decode bodies and fields and the Message class 
described below handles decoding of fields and bodies 
transparently. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
%patch0 -b .sav0
%patch1 -b .sav1

cp -p %{SOURCE2} maven2-settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.james apache-mime4j %{version} JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt3_2jpp6
- dropped felix-maven2 dependency

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt2_2jpp6
- fixed build with maven3

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_2jpp6
- new version

