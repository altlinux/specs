# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

Name:           httpunit
Version:        1.7
Release:        alt3_11jpp7
Epoch:          0
Summary:        Automated web site testing toolkit
License:        MIT
Source0:        http://download.sourceforge.net/httpunit/httpunit-%{version}.zip
Source1:        http://repo1.maven.org/maven2/httpunit/httpunit/1.7/httpunit-1.7.pom
Patch1:         %{name}-JavaScript-NotAFunctionException.patch
Patch2:         %{name}-servlettest.patch
Patch3:         %{name}-not-implemented.patch
Patch4:         junit4.patch
URL:            http://httpunit.sourceforge.net/
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  nekohtml
BuildRequires:  jtidy
BuildRequires:  junit >= 0:3.8
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  javamail >= 0:1.3
BuildRequires:  rhino
BuildRequires:  %{__unzip}
Requires:       junit >= 0:3.8
Requires:       jpackage-utils
Requires:       tomcat-servlet-3.0-api
# As of 1.5, requires either nekohtml or jtidy, and prefers nekohtml.
Requires:       nekohtml
Requires:       rhino
Group:          Development/Java
BuildArch:      noarch
Obsoletes:      %{name}-demo < %{epoch}:%{version}
Source44: import.info

%description
HttpUnit emulates the relevant portions of browser behavior, including form
submission, JavaScript, basic http authentication, cookies and automatic page
redirection, and allows Java test code to examine returned pages either as
text, an XML DOM, or containers of forms, tables, and links.
A companion framework, ServletUnit is included in the package.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%package        doc
Summary:        Documentation for %{name}
Group:          Development/Java
Requires:       %{name}-javadoc

%description    doc
Documentation for %{name}

%prep
%setup -q
# to create the test and examples jar
#%%patch0 -p0
# patch to work with rhino 1.5
%patch1 -b .sav
# add META-INF
%patch2
%patch3 -p1
#%%{__unzip} -qd META-INF lib/httpunit.jar "*.dtd" # 1.6 dist zip is borked
# remove all binary libs and javadocs

%patch4

sed -i -e 's|destdir|encoding="iso-8859-1" destdir|g' build.xml

sed -i -e 's|setCharEncoding( org.w3c.tidy.Configuration.UTF8 )|setInputEncoding("UTF-8")|g' src/com/meterware/httpunit/parsing/JTidyHTMLParser.java
find . -name "*.jar" -exec rm -f {} \;
rm -rf doc/api
ln -s \
  %{_javadir}/junit.jar \
  %{_javadir}/jtidy.jar \
  %{_javadir}/nekohtml.jar \
  %{_javadir}/tomcat-servlet-api.jar \
  %{_javadir}/js.jar \
  %{_javadir}/xerces-j2.jar \
  jars

cp %{SOURCE1} pom.xml


%build
export CLASSPATH=$(build-classpath javamail)
export ANT_OPTS="-Dfile.encoding=iso-8859-1"
ant -Dbuild.compiler=modern -Dbuild.sysclasspath=last \
  jar javadocs test servlettest 

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar


# Avoid having api in doc
rm -rf doc/api

# Fix link between doc and javadoc

%files
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%files doc
%doc doc/*

%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_11jpp7
- update

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_4jpp6
- fixed build

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_4jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_4jpp6
- new jpp relase

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1jpp5
- new version

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

