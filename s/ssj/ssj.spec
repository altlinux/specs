Packager: Igor Vlasenko <viy@altlinux.ru>
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

Name:           ssj
Version:        2.2
Release:        alt2_1jpp6
Summary:        Stochastic Simulation in Java

Group:          Development/Java
License:        GPL
URL:            http://www.iro.umontreal.ca/~simardr/ssj/ssj-2.2-source.zip

Source0:        http://www.iro.umontreal.ca/~simardr/ssj/ssj-2.2-source.zip

BuildRequires: ant >= 1.6.5
BuildRequires: colt
BuildRequires: dsol-basic
BuildRequires: fpl-optimization
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: latex2html
BuildRequires: perl
BuildRequires: tcode
BuildRequires: jpackage-utils >= 0:5.0.0

Requires: jpackage-utils >= 0:5.0.0
Requires: colt
Requires: dsol-basic
Requires: fpl-optimization
Requires: jcommon
Requires: jfreechart

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
SSJ is a Java library for stochastic simulation, developed 
under the direction of Pierre L'Ecuyer, in the DApartement 
d'Informatique et de Recherche OpArationnelle (DIRO), at the
UniversitA de MontrAal. It provides facilities for generating
uniform and nonuniform random variates, computing different
measures related to probability distributions, performing
goodness-of-fit tests, applying quasi-Monte Carlo methods,
collecting (elementary) statistics, and programming
discrete-event simulations with both events and processes.

%package javadoc 
Summary:        Javadocs for %{name} 
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description javadoc 
%{summary}. 

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
export LANG=en_US.ISO8859-1
export TCODEHOME=/usr/share/tcode
export CLASSPATH=$(build-classpath \
colt \
fpl-optimization \
tcode \
dsol/event \
dsol/interpreter \
jcommon \
jfreechart \
)
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 lib htmldoc

# charts         Provides tools to draw charts and plots
# clean          Cleans auxiliary and backup files
# cleanall       Cleans all generated files
# cleanbuild     Cleans the build tree
# cleandoc       Cleans the generated documentation
# cleanlib       Cleans the generated library files
# cleanmore      Cleans backup and class files
# dist           Creates the SSJ binary distribution
# doc            Creates the PDF and HTML documentation
# functionfit    Compiles tools to compute function fittings
# functions      Provides tools to use mathematical functions
# gof            Compiles the goodness of fit tests
# htmldoc        Creates the HTML documentation
# hups           Compiles the highly uniform point sets
# jni            Builds SSJ native methods, only if ssj.buildjnichrono or ssj.buildjniunuran are set
# lib            Creates the JAR file
# pdfdoc         Creates the PDF documentation
# probdist       Compiles the probability distributions
# probdistmulti  Compiles the multivariate probability distributions
# randvar        Compiles the random variate generators
# randvarmulti   Compiles the random multi-variate generators
# rng            Compiles the uniform random streams
# simevents      Compiles the event-driven simulation package
# simprocs       Compiles the process-driven simulation package
# srcdist        Cleans the tree and zip it as a source distribution
# stat           Compiles the statistics tools
# stochprocess   Simulates stochastic processes
# util           Compiles the basic utilities

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# javadoc 
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__cp -a doc/html/* %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%__mkdir_p %{buildroot}%{_datadir}/%{name}

%files
%doc README.txt
%{_javadir}/*.jar
%{_datadir}/%{name}

%files javadoc 
%{_javadocdir}/%{name}-%{version} 
%{_javadocdir}/%{name} 

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_1jpp6
- fixed build with java 7

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1jpp6
- new version

