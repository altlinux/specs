BuildRequires: /proc
BuildRequires: jpackage-compat
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
#


Name:           texen
Version:        1.0
Release:        alt3_2jpp6
Epoch:          0
Summary:        Text generating utility

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://velocity.apache.org/texen/releases/texen-1.0/
Source0:        texen-1.0.tar.gz
# svn export http://svn.apache.org/repos/asf/velocity/texen/tags/Texen-1.0 texen-1.0

Patch0:         texen-build.patch


BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  jdom
BuildRequires:  antlr
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-lang
BuildRequires:  velocity

Requires:  apache-commons-collections
Requires:  apache-commons-lang
Requires:  velocity

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Texen is a general purpose text generating utility. It is 
capable of producing almost any sort of text output. Driven 
by Ant, essentially an Ant Task, Texen uses a control 
template, an optional set of worker templates, and control 
context to govern the generated output. Although TexenTask 
can be used directly, it is usually subclassed to initialize 
your control context before generating any output.
Texen was created to deal with the source generating 
requirements of the Turbine web application framework. The 
Torque uses a subclass of the TexenTask to generate SQL and 
the Object-Relational mapping sources for its O/R layer. This 
is only one example; you can use Texen to generate almost any 
sort of text output! 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}


%prep
%setup -q 
mkdir -p bin/lib
ln -sf $(build-classpath ant) bin/lib
ln -sf $(build-classpath commons-collections) bin/lib
ln -sf $(build-classpath commons-lang) bin/lib
ln -sf $(build-classpath velocity) bin/lib
mkdir -p bin/test-lib
ln -sf $(build-classpath junit) bin/test-lib
mkdir -p bin/docs-lib
ln -sf $(build-classpath antlr) bin/docs-lib
ln -sf $(build-classpath jdom) bin/docs-lib

%patch0 -b .sav0

%build
cd build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 bin/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -m 644 pom.xml \
  $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.texen texen %{version} JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr bin/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%doc LICENSE
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

