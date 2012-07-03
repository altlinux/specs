#BuildRequires: maven2-plugin-resources maven2-plugin-source maven2-plugin-jar maven2-plugin-dependency maven2-plugin-javadoc java-1.6.0-openjdk-devel
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

%define gcj_support 0


Name:           jung2
Version:        2.0.1
Release:        alt3_1jpp6
Epoch:          0
Summary:        Java Universal Network/Graph Framework
License:        BSD
Url:            http://jung.sourceforge.net/
Source0:        jung2-2.0.1.tgz
#cvs -d:pserver:anonymous@jung.cvs.sourceforge.net:/cvsroot/jung login 
#cvs -z3 -d:pserver:anonymous@jung.cvs.sourceforge.net:/cvsroot/jung export -r jung2-2_0_1 jung2
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Patch0:         %{name}-io-pom.patch
Group:          Development/Java
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: fonts-ttf-liberation
BuildRequires: ant >= 0:1.7.1
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven2-plugin-pmd
BuildRequires: maven2-default-skin
BuildRequires: mojo-maven2-plugin-cobertura
BuildRequires: colt
BuildRequires: apache-commons-collections
BuildRequires: junit
BuildRequires: junit44
BuildRequires: sf-collections-generic
BuildRequires: wstx
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
Requires: apache-commons-collections
Requires: sf-collections-generic
Requires: wstx
Source44: import.info

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
%setup -q -n jung2
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .orig
%if %with maven
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Djava.awt.headless=true"
%{_bindir}/mvn-jpp \
        -e \
        install

%{_bindir}/mvn-jpp \
        -e \
        javadoc:javadoc 
#site

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 jung-algorithms/target/jung-algorithms-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/algorithms-%{version}.jar
%add_to_maven_depmap net.sf.jung jung-algorithms %{version} JPP/jung2 algorithms

install -m 644 jung-api/target/jung-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/api-%{version}.jar
%add_to_maven_depmap net.sf.jung jung-api %{version} JPP/jung2 api
install -m 644 jung-api/target/jung-api-%{version}-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/api-tests-%{version}.jar

install -m 644 jung-graph-impl/target/jung-graph-impl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/graph-impl-%{version}.jar
%add_to_maven_depmap net.sf.jung jung-graph-impl %{version} JPP/jung2 graph-impl

install -m 644 jung-io/target/jung-io-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/io-%{version}.jar
%add_to_maven_depmap net.sf.jung jung-io %{version} JPP/jung2 io

install -m 644 jung-samples/target/jung-samples-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/samples-%{version}.jar
%add_to_maven_depmap net.sf.jung jung-samples %{version} JPP/jung2 samples

install -m 644 jung-visualization/target/jung-visualization-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/visualization-%{version}.jar
%add_to_maven_depmap net.sf.jung jung-visualization %{version} JPP/jung2 visualization

%add_to_maven_depmap net.sf.jung jung2 %{version} JPP/jung2 jung2

(cd $RPM_BUILD_ROOT%{_javadir}/%{name}  
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
install -m 644 jung-algorithms/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-algorithms.pom
install -m 644 jung-api/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-api.pom
install -m 644 jung-graph-impl/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-graph-impl.pom
install -m 644 jung-io/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-io.pom
install -m 644 jung-samples/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-samples.pom
install -m 644 jung-visualization/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-visualization.pom

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}/*.jar
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
* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_1jpp6
- fixed build

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt2_1jpp6
- added maven2-plugin-resources dep

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_1jpp6
- rebuild to restore plexus components info

