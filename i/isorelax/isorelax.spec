# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with tests
%bcond_with tests

%define cvsversion 20041111

Name:           isorelax
Version:        0.1
Release:        alt4_0.20041111.7jpp6
Epoch:          1
Summary:        Public interfaces useful for applications to support RELAX Core
License:        MIT-style
Group:          Development/Java
URL:            http://iso-relax.sourceforge.net/
Source0:        %{name}.%{cvsversion}.zip
Source1:        %{name}-build.xml
Source2:        isorelax-maven-project.xml
Source3:        isorelax-maven-project.xsd
Source4:        isorelax.pom
Patch0:         isorelax-jdk15.patch
Obsoletes:      isorelax-bootstrap < %{epoch}:%{version}-%{release}
Provides:       isorelax-bootstrap = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.6
%if %with tests
BuildRequires:  xercesjarv
%endif
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildArch:      noarch
Source44: import.info

%description
The ISO RELAX project is started to host the public interfaces 
useful for applications to support RELAX Core. But nowadays 
some of the stuff we have is schema language neutral.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -n %{name}-%{version}
mkdir src
(cd src; unzip -q ../src.zip)
%{__rm} src.zip
cp -p %{SOURCE1} build.xml
mkdir test
cp -p %{SOURCE2} test
cp -p %{SOURCE3} test
chmod -R go=u-w *
%{_bindir}/find -type f -name "*.jar" | xargs -t %{__rm}
%{__rm} -r src/jp/gr/xml/relax/swift
%patch0 -p0 -b .sav0
%{__perl} -pi -e 's/\r$//g;' COPYING.txt

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(%{_bindir}/build-classpath xerces-j2 xml-commons-jaxp-1.3-apis)
%if %with tests
CLASSPATH=$CLASSPATH:$(build-classpath xercesjarv)
ln -sf $(find-jar xercesjarv) xercesjarv.jar
%endif
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only release
%if %with tests
CLASSPATH=`pwd`/isorelax.jar:$CLASSPATH
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first ant-task-test
%endif

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 isorelax.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar | sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap isorelax isorelax %{cvsversion} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc COPYING.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt4_0.20041111.7jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt4_0.20041111.6jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt3_0.20041111.6jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.1-alt2_0.20041111.6jpp5
- converted from JPackage by jppimport script

