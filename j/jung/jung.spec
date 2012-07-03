Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%define gcj_support 0


Name:           jung
Version:        1.7.6
Release:        alt2_1jpp5
Epoch:          0
Summary:        Java Universal Network/Graph Framework
License:        BSD
Url:            http://jung.sourceforge.net/
Source0:        jung-1.7.6.tar.gz
#cvs -d:pserver:anonymous@jung.cvs.sourceforge.net:/cvsroot/jung login 
#cvs -z3 -d:pserver:anonymous@jung.cvs.sourceforge.net:/cvsroot/jung export -r JUNG_1_7_6 jung
Source1:        jung-build.xml
Source2:        http://repo1.maven.org/maven2/jung/jung/1.7.6/jung-1.7.6.pom

Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: colt
BuildRequires: jakarta-commons-collections >= 0:3.1
BuildRequires: junit
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires: colt
Requires: jakarta-commons-collections >= 0:3.1

%description
JUNG a.. the Java Universal Network/Graph Framework--is a software 
library that provides a common and extendible language for the 
modeling, analysis, and visualization of data that can be 
represented as a graph or network. It is written in Java, which 
allows JUNG-based applications to make use of the extensive 
built-in capabilities of the Java API, as well as those of other 
existing third-party Java libraries.
The JUNG architecture is designed to support a variety of 
representations of entities and their relations, such as 
directed and undirected graphs, multi-modal graphs, graphs 
with parallel edges, and hypergraphs. It provides a mechanism 
for annotating graphs, entities, and relations with metadata. 
This facilitates the creation of analytic tools for complex 
data sets that can examine the relations between entities as 
well as the metadata attached to each entity and relation.
The current distribution of JUNG includes implementations of
a number of algorithms from graph theory, data mining, and 
social network analysis, such as routines for clustering, 
decomposition, optimization, random graph generation, 
statistical analysis, and calculation of network distances, 
flows, and importance measures (centrality, PageRank, HITS, etc.).
JUNG also provides a visualization framework that makes it easy to 
construct tools for the interactive exploration of network data. 
Users can use one of the layout algorithms provided, or use the 
framework to create their own custom layouts. In addition, 
filtering mechanisms are provided which allow users to focus their 
attention, or their algorithms, on specific portions of the graph.
As an open-source library, JUNG provides a common framework for 
graph/network analysis and visualization. We hope that JUNG will 
make it easier for those who work with relational data to make use 
of one anothers' development efforts, and thus avoid continually 
re-inventing the wheel. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
cp %{SOURCE1} build.xml

%build
export CLASSPATH=$(build-classpath colt commons-collections)
ant \
   -Dbuild.sysclasspath=only \
   build javadoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} 
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/%{name}*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt2_1jpp5
- fixes for java6 support

* Tue Sep 30 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7.6-alt1_1jpp5
- converted from JPackage by jppimport script

