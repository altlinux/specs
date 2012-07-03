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

Name:           socr
Version:        2.6
Release:        alt2_1jpp6
Summary:        Statistics Online Computational Resource

Group:          Development/Java
License:        GPL v2
URL:            http://www.socr.ucla.edu/

# The source for this package was pulled from upstream's svn.  Use the
# following commands to generate the tarball:
#
# svn export http://socr.googlecode.com/svn/trunk/SOCR2.6
# tar -czf SOCR2.0.tgz SOCR2.6
#
Source0:        SOCR2.6.tgz
Patch0:         SOCR2.6-build.patch
Patch1:         SOCR2.6-JSci-build.patch


BuildRequires: ant >= 1.7.0
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: jgraph
BuildRequires: servlet_2_5_api

Requires: jpackage-utils >= 0:5.0.0
Requires: jcommon
Requires: jfreechart
Requires: jgraph
Requires: servlet_2_5_api

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
What is SOCR?
The goals of the Statistics Online Computational Resource 
(SOCR) are to design, validate and freely disseminate 
knowledge. Our Resource specifically provides portable 
online aids for probability and statistics education, 
technology based instruction and statistical computing. SOCR
tools and resources include a repository of interactive 
applets, computational and graphing tools, instructional and
course materials.
What are the main SOCR Components?
The core SOCR educational and computational components 
include: Distributions (interactive graphs and calculators),
Experiments (virtual computer-generated analogs of popular 
games and processes), Analyses (collection of common 
web-accessible tools for statistical data analysis), Games 
(interfaces and simulations to real-life processes), Modeler 
(tools for distribution, polynomial and spectral 
model-fitting and simulation), Graphs, Plots and Charts 
(comprehensive web-based tools for exploratory data 
analysis), Additional Tools (other statistical tools and 
resources), SOCR Wiki (collaborative Wiki resource), 
Educational Materials and Hands-on Activities (varieties of 
SOCR educational materials), SOCR Statistical Consulting and 
Statistical Computing Libraries.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils >= 0:5.0.0
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n SOCR%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
#ln -s $(build-classpath jcommon) jars
#ln -s $(build-classpath servlet_2_5_api) jars/servlet.jar
#ln -s $(build-classpath jgraph) jars/SOCR_jgraph.jar
%patch0 -b .sav0
%patch1 -b .sav1
rm -rf src/edu/ucla/stat/SOCR/TG_distributome
rm -rf src/edu/ucla/stat/SOCR/touchgraph

%build
export LANG=en_US.ISO8859-1
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f src/JSci/build.xml package apidocs
export CLASSPATH=$(build-classpath jcommon jfreechart jgraph servlet_2_5_api):classes
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first jfreechart
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first compilecore
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first core 
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first applications 
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first jar_SOCRPlugins
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first charts 
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first apidocs


%install
%__rm -rf %{buildroot}

# jar
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -m 644 SOCRJSci.jar %{buildroot}%{_javadir}/%{name}/SOCRJSci-%{version}.jar
install -m 644 jars/SOCR_applications.jar %{buildroot}%{_javadir}/%{name}/SOCR_applications-%{version}.jar
install -m 644 jars/jfreechart-1.0.11.jar %{buildroot}%{_javadir}/%{name}/SOCR_jfreechart-%{version}.jar
install -m 644 jars/SOCR_plugin.jar %{buildroot}%{_javadir}/%{name}/SOCR_plugin-%{version}.jar
install -m 644 jars/SOCR_chart.jar %{buildroot}%{_javadir}/%{name}/SOCR_chart-%{version}.jar
install -m 644 jars/SOCR_core.jar %{buildroot}%{_javadir}/%{name}/SOCR_core-%{version}.jar

(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)


# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}/JSci
%__cp -a docs/* %{buildroot}%{_javadocdir}/%{name}
%__cp -a src/JSci/docs.dir/* %{buildroot}%{_javadocdir}/%{name}/JSci

# doc
%__mkdir_p %{buildroot}%{_docdir}/%{name}-%{version}
%__cp -a *.html *.css %{buildroot}%{_docdir}/%{name}-%{version}

%files
%doc %{_docdir}/%{name}-%{version}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt2_1jpp6
- fixed build with java 7

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_1jpp6
- new version

