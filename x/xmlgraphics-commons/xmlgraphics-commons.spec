BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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


Name:           xmlgraphics-commons
Version:        1.4
Release:        alt2_4jpp6
Epoch:          0
Summary:        XML Graphics Commons
Group:          Development/Java
License:        ASL 2.0
URL:            http://xmlgraphics.apache.org/
Source0:        http://www.apache.org/dist//xmlgraphics/commons/source/xmlgraphics-commons-1.4-src.tar.gz
Patch0:         xmlgraphics-commons-build_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jakarta-commons-io >= 0:1.1
Requires:       jakarta-commons-logging
Requires:       jpackage-utils
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  jakarta-commons-io >= 0:1.1
BuildRequires:  jakarta-commons-logging
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildArch:      noarch
Source44: import.info

%description
Apache XML Graphics Commons is a library that consists of 
several reusable components used by Apache Batik and 
Apache FOP. Many of these components can easily be used 
separately outside the domains of SVG and XSL-FO. You will 
find components such as a PDF library, an RTF library, 
Graphics2D implementations that let you generate PDF & 
PostScript files, and much more.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

pushd lib
ln -s $(build-classpath commons-io) .
ln -s $(build-classpath commons-logging) .
popd

%build
export LANG=en_US.ISO8859-1
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 package javadocs maven-artifacts

%install

install -Dpm 644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 build/maven/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.xmlgraphics xmlgraphics-commons %{version} JPP %{name}

install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc examples/ KEYS LICENSE NOTICE README status.xml
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp6
- fixed build with java 7

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_4jpp6
- new jpp relase

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp5
- converted from JPackage by jppimport script

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

