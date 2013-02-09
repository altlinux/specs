# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
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

Name:           velocity
Version:        1.7
Release:        alt1_6jpp7
Epoch:          1
Summary:        Java-based template engine
License:        ASL 2.0
URL:            http://velocity.apache.org/
Source0:        http://www.apache.org/dist/%{name}/engine/%{version}/%{name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Patch0:         0001-Remove-avalon-logkit.patch
Patch2:         0003-Use-system-jars.patch
Patch3:         0004-JDBC-41-compat.patch
Group:          Development/Java
Requires:       apache-commons-collections
Requires:       apache-commons-logging
Requires:       apache-commons-lang
Requires:       servlet3
Requires:       jakarta-oro
Requires:       werken-xpath
Requires:       junit
Requires:       hsqldb
Requires:       jdom
Requires:       bcel
Requires:       log4j

BuildRequires:	werken-xpath
BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  junit
BuildRequires:	ant-junit
BuildRequires:  hsqldb
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-lang
BuildRequires:  servlet3
BuildRequires:  jakarta-oro
BuildRequires:  jdom
BuildRequires:  bcel
BuildRequires:  log4j
BuildRequires:  jpackage-utils

# It fails one of the arithmetic test cases with gcj
BuildArch:      noarch
Source44: import.info

%description
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
Documentation for %%{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
Javadoc for %%{name}.

%package        demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    demo
Demonstrations and samples for %%{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

# remove bundled libs/classes (except those used for testing)
find . -name '*.jar' -o -name '*.class' -not -path '*test*' -print -delete

# Remove dependency on avalon-logkit
rm -f src/java/org/apache/velocity/runtime/log/AvalonLogChute.java
rm -f src/java/org/apache/velocity/runtime/log/AvalonLogSystem.java
rm -f src/java/org/apache/velocity/runtime/log/VelocityFormatter.java

# need porting to new servlet API. We would just add a lot of empty functions
rm  src/test/org/apache/velocity/test/VelocityServletTestCase.java

cp %{SOURCE1} ./pom.xml

# remove rest of avalon logkit refences
%patch0 -p1

# Use system jar files instead of downloading from net
%patch2 -p1

%patch3 -p1

# -----------------------------------------------------------------------------

%build
export CLASSPATH=$(build-classpath \
antlr \
apache-commons-collections \
commons-lang \
commons-logging \
tomcat-servlet-api \
junit \
jakarta-oro \
log4j \
jdom \
bcel \
werken-xpath \
hsqldb \
junit)
ant \
  -buildfile build/build.xml \
  -Dbuild.sysclasspath=first \
  jar javadocs test

# fix line-endings in generated files
sed -i 's/\r//' docs/api/stylesheet.css docs/api/package-list

# -----------------------------------------------------------------------------

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 bin/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr examples test %{buildroot}%{_datadir}/%{name}

# Maven metadata
install -pD -T -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap -a "%{name}:%{name}"


%files
%doc LICENSE NOTICE README.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files manual
%doc LICENSE NOTICE
%doc docs/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%files demo
%doc LICENSE NOTICE
%{_datadir}/%{name}

%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_6jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_5jpp7
- new version

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt3_1jpp6
- fixed build

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt2_1jpp6
- added velocity:velocity jppmap

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_1jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt2_4jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_3jpp5
- converted from JPackage by jppimport script

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_2jpp1.7
- pom fixes

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_1jpp1.7
- updated to new jpackage release

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_6jpp1.7
- import from jpackage;set epoch 1; overrides unstable version

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.3
- rebuild with excalibur-avalon-logkit

* Fri Dec 02 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.2
- nightly build 20051125053934 

* Sat May 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.1
- 1.5-dev
- svn snapshot 20050507

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Initial build for ALT Linux Sisyphus

