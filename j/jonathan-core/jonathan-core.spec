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


Name:           jonathan-core
Version:        4.1
Release:        alt1_4jpp6
Epoch:          0
Summary:        Distributed Object Platform (DOP) written entirely in Java
License:        LGPL
URL:            http://jonathan.objectweb.org/
Group:          Development/Java
Source0:        jonathancore-%{version}-src.tar.gz
Source1:        jonathan-%{version}.pom
# cvs -d:pserver:anonymous@cvs.forge.objectweb.org:/cvsroot/jonathan login
# cvs -z3 -d:pserver:anonymous@cvs.forge.objectweb.org:/cvsroot/jonathan export -r JONATHAN_CORE_4_1 jonathancore

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  kilim1
BuildRequires:  monolog
BuildRequires:  nanoxml-lite
BuildRequires:  objectweb-anttask
Requires:       kilim1
Requires:       monolog
Requires:       nanoxml-lite
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
Jonathan is a Distributed Object Platform (DOP) written entirely in
Java. Jonathan was developed originally at the research labs of France
Telecom in the context of the European project ReTINA, whose aim was to
define an architecture for telecommunications distributed environments.
Telecommunications applications such as multimedia services have
stringent requirements in terms of scalability, adaptability and
realtime. Jonathan's response to this is through its "openness" in the
sense that contrary to standard DOPs (and in particular, most CORBA
ORBs), the abstractions that make up its internal machinery are
accessible by an application programmer and may be specialized to meet
specific requirements.

Jonathan is organised around a very small kernel (namely Kilim) that
essentially lets the infrastructure components communicate. Currently,
these components consist of a number of independently developed
protocols, marshallers, stub factories, etc.

Different personalities can be built using these components. A
personality is a set of normalized Application Programming Interfaces:
Java RMI is a personality, CORBA is another, COM still another...
Jonathan provides two personnalities:

    * David is a CORBA ORB implementation. David lacks a number of CORBA
      features (POA, interface repository, Dynamic Any,...) and provides only
      a naive naming service implementation. However, our ambition is to fill
      these gaps and to provide a reference CORBA implementation.

    * Jeremie provides an RMI-like programming style.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jonathancore
find . -name "*.jar" -exec rm -f {} \;

%build
export CLASSPATH=

pushd config
    ln -sf $(build-classpath kilim1-tools) kilim-tools.jar
    ln -sf $(build-classpath objectweb-anttask) ow_util_ant_tasks.jar
    ln -sf $(build-classpath nanoxml-lite) nanoxml-lite-2.2.1.jar
popd
pushd externals
    ln -sf $(build-classpath kilim1) kilim.jar
    ln -sf $(build-classpath monolog/ow_monolog) ow_monolog.jar
popd

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar jdoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 output/dist/lib/jonathan-core.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/ && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.objectweb.jonathan jonathan %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/* \
                  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
(cd $RPM_BUILD_ROOT%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%files
%{_javadir}/*
%doc README.txt
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_4jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_3jpp5
- new jpp release

* Mon Jul 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

