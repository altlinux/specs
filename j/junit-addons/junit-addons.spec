# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.4
%define name junit-addons
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

%global namedversion %{version}


Name:		junit-addons
Version:	1.4
Release:	alt2_7jpp6
Epoch:		0
Summary:	JUnitX helper classes for JUnit
License:	ASL 1.1
Group:		Development/Java
URL:		http://sourceforge.net/projects/junit-addons/
Source0:	%{name}-%{namedversion}.zip
Source1:	%{name}-build.xml
Source2:        http://repo1.maven.org/maven2/junit-addons/junit-addons/1.4/junit-addons-1.4.pom
Patch0:         junit-addons-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:	ant
Requires:	jakarta-commons-logging
Requires:	jaxen
Requires:	jdom
Requires:       jpackage-utils
Requires:	junit
BuildRequires:	ant
BuildRequires:	jakarta-commons-logging
BuildRequires:	jaxen
BuildRequires:	jdom
BuildRequires:  jpackage-utils
BuildRequires:	junit
BuildRequires:	xerces-j2
BuildRequires:	xml-commons-jaxp-1.3-apis
BuildArch:	noarch
Source44: import.info

%description
JUnit-addons is a collection of helper classes for JUnit. 
This library can be used with both JUnit 3.7 and JUnit 3.8.x

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%{__chmod} -Rf a+rX,u+w,g-w,o-w *
%{jar} xf src.jar
# FIXME: (dwalluck): removing this jar (which contains bianry class files) will break the tests
find . -type f -name "*.jar" -a -type f -not -name tests.jar | xargs -t rm
cp -p %{SOURCE1} build.xml
%{__cp} -p %{SOURCE2} junit-addons-%{namedversion}.pom
%patch0 -p0 -b .sav0

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 \
        -Dant.build.javac.source=1.4 \
	-Djdom.jar=$(build-classpath jdom) \
	-Djaxen.jar=$(build-classpath jaxen) \
	-Dsaxpath.jar=$(build-classpath jaxen) \
	-Dant.jar=$(build-classpath ant) \
	-Djunit.jar=$(build-classpath junit) \
	-Dxerces.jar=$(build-classpath xerces-j2) \
	-Dxml-apis.jar=$(build-classpath xml-commons-jaxp-1.3-apis) \
	-Dcommons-logging.jar=$(build-classpath commons-logging) \
	-Dproject.name=junit-addons \
	-Dproject.version=%{namedversion} \
	release

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p dist/junit-addons-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}-%{namedversion}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{namedversion}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{namedversion}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p junit-addons-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap junit-addons junit-addons %{namedversion} JPP %{name}

# examples
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp -pr src/example/* %{buildroot}%{_datadir}/%{name}/examples

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
cp -pr api/* %{buildroot}%{_javadocdir}/%{name}-%{namedversion}
ln -s %{name}-%{namedversion} %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE README WHATSNEW
%{_javadir}*/%{name}-%{namedversion}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/%{name}
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{namedversion}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_7jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp5
- new version

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_2jpp5
- fixed build with java 5

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp1.7
- converted from JPackage by jppimport script

