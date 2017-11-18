BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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
Release:        alt6_21jpp8
Epoch:          0
Summary:        Automated web site testing toolkit
License:        MIT and ASL 2.0
# ./create-tarball.sh %%{version}
Source0:        httpunit-1.7-clean.tar.gz
Source1:        http://repo1.maven.org/maven2/httpunit/httpunit/1.7/httpunit-1.7.pom
# replacement for non-free XML DTD files
Source2:        https://raw.github.com/apache/tomcat/TOMCAT_7_0_42/java/javax/servlet/resources/web-app_2_2.dtd
Source3:        https://raw.github.com/apache/tomcat/TOMCAT_7_0_42/java/javax/servlet/resources/web-app_2_3.dtd
Source4:        https://raw.github.com/apache/tomcat/TOMCAT_7_0_42/java/javax/servlet/resources/web-app_2_4.xsd
# sources 2-4 are licensed under ASL 2.0
Source5:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch1:         %{name}-rhino-1.7.7.patch
Patch2:         %{name}-servlettest.patch
Patch3:         %{name}-servlet31.patch
Patch4:         junit4.patch
URL:            http://httpunit.sourceforge.net/
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  nekohtml
BuildRequires:  jtidy
BuildRequires:  junit >= 0:3.8
BuildRequires:  tomcat-servlet-3.1-api
BuildRequires:  javamail >= 0:1.3
BuildRequires:  rhino
BuildRequires:  java-devel >= 1.6.0

Requires:       junit >= 0:3.8
Requires:       tomcat-servlet-3.1-api
# As of 1.5, requires either nekohtml or jtidy, and prefers nekohtml.
Requires:       nekohtml
Requires:       rhino

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
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%package        doc
Group: Development/Java
Summary:        Documentation for %{name}
Requires:       %{name}-javadoc

%description    doc
Documentation for %{name}

%prep
%setup -q
# patch to work with rhino 1.7.7
%patch1 -p1
# add META-INF
%patch2
%patch3 -p1
%patch4

sed -i -e 's|destdir|encoding="iso-8859-1" destdir|g' build.xml

sed -i -e 's|setCharEncoding( org.w3c.tidy.Configuration.UTF8 )|setInputEncoding("UTF-8")|g' src/com/meterware/httpunit/parsing/JTidyHTMLParser.java

# remove all binary libs and javadocs
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

install -m 644 %{SOURCE1} pom.xml
install -m 644 %{SOURCE2} META-INF/
install -m 644 %{SOURCE3} META-INF/
install -m 644 %{SOURCE4} META-INF/
install -m 644 %{SOURCE5} LICENSE-ASL


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
pushd doc
ln -sf %{_javadocdir}/%{name} api
popd

%files -f .mfiles
%doc LICENSE-ASL

%files javadoc
%doc LICENSE-ASL
%{_javadocdir}/%{name}

%files doc
%doc --no-dereference doc/*

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt6_21jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt5_21jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt5_20jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt5_19jpp8
- java8 mass update

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

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

