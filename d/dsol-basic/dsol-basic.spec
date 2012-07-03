Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc maven-shared-archiver maven2-plugin-javadoc  maven2-plugin-antrun maven2-plugin-resources
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

Name:           dsol-basic
Version:        1.6.9
Release:        alt3_1jpp6
Summary:        Java D-SOL simulation basic libs

Group:          Development/Java
License:        LGPL
URL:            http://sk-3.tbm.tudelft.nl/simulation/index.php

Source0:        dsol-language-1.6.9.tgz
# cvs -d :pserver:dsoluser@sk-3.tbm.tudelft.nl:/home/dsol/1.6 export -r HEAD -d dsol-language-1.6.9 language
# tar czf dsol-language-1.6.9.tgz dsol-language-1.6.9
Source1:        dsol-event-1.6.9.tgz
# cvs -d :pserver:dsoluser@sk-3.tbm.tudelft.nl:/home/dsol/1.6 export -r HEAD -d dsol-event-1.6.9 event 
# tar czf dsol-event-1.6.9.tgz dsol-event-1.6.9
Source2:        dsol-logger-1.6.9.tgz
# cvs -d :pserver:dsoluser@sk-3.tbm.tudelft.nl:/home/dsol/1.6 export -r HEAD -d dsol-logger-1.6.9 logger
# tar czf dsol-logger-1.6.9.tgz dsol-logger-1.6.9
Source3:        dsol-naming-1.6.9.tgz
# cvs -d :pserver:dsoluser@sk-3.tbm.tudelft.nl:/home/dsol/1.6 export -r HEAD -d dsol-naming-1.6.9 naming
# tar czf dsol-naming-1.6.9.tgz dsol-naming-1.6.9
Source4:        dsol-jstats-1.6.9.tgz
# cvs -d :pserver:dsoluser@sk-3.tbm.tudelft.nl:/home/dsol/1.6 export -r HEAD -d dsol-jstats-1.6.9 jstats
# tar czf dsol-jstats-1.6.9.tgz dsol-jstats-1.6.9
Source5:        dsol-interpreter-1.6.9.tgz
# cvs -d :pserver:dsoluser@sk-3.tbm.tudelft.nl:/home/dsol/1.6 export -r HEAD -d dsol-interpreter-1.6.9 interpreter
# tar czf dsol-interpreter-1.6.9.tgz dsol-interpreter-1.6.9
Source6:        dsol-introspection-1.6.9.tgz
# cvs -d :pserver:dsoluser@sk-3.tbm.tudelft.nl:/home/dsol/1.6 export -r HEAD -d dsol-introspection-1.6.9 introspection
# tar czf dsol-introspection-1.6.9.tgz dsol-introspection-1.6.9

Source11:       %{name}-settings.xml
Source12:       %{name}-jpp-depmap.xml 
Source13:       dsol-LICENSE.txt
Patch0:         dsol-jstats-1.6.9-HistogramDataset.patch
Patch1:         dsol-jstats-1.6.9-HistogramSeries.patch
Patch2:         dsol-jstats-1.6.9-XYDataset.patch
Patch3:         dsol-jstats-1.6.9-XYSeries.patch
Patch4:         dsol-jstats-1.6.9-BoxAndWhiskerPlot.patch


BuildRequires: maven2 >= 2.0.8
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: colt
BuildRequires: commons-math
BuildRequires: java3d
BuildRequires: jcommon
BuildRequires: jfreechart
BuildRequires: xml-commons-jaxp-1.3-apis

Requires: jpackage-utils >= 0:5.0.0
Requires: colt
Requires: commons-math
Requires: java3d
Requires: jcommon
Requires: jfreechart
Requires: xml-commons-jaxp-1.3-apis

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
DSOL is an open source, Java based suite of Java classes for
multi-formalism (e.g. continuous, discrete event, flow, 
process, and agent-based) simulation. The first release of 
DSOL was introduced at IEEE's Winter Simulation Conference 
2002. The multi-formalism aspects and distributed character 
make DSOL an excellent Java library for web-based simulations, 
distributed simulation projects, and simulation games.

%package javadoc 
Summary:        Javadocs for %{name} 
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description javadoc 
%{summary}. 

%prep
%setup -q -c
gzip -dc %{SOURCE1} | tar xf -
gzip -dc %{SOURCE2} | tar xf -
gzip -dc %{SOURCE3} | tar xf -
gzip -dc %{SOURCE4} | tar xf -
gzip -dc %{SOURCE5} | tar xf -
gzip -dc %{SOURCE6} | tar xf -
%patch0 -b .jfree
%patch1 -b .jfree
%patch2 -b .jfree
%patch3 -b .jfree
%patch4 -b .jfree
cp -p %{SOURCE11} settings.xml
cp -p %{SOURCE13} LICENSE.txt
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

%build
export LANG=en_US.ISO8859-1
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE12} -Dmaven.repo.local=${MAVEN_REPO_LOCAL} -Djava.awt.headless=true -Daggregate=true"
for module in \
	language \
	event \
	logger \
	naming \
	jstats \
	interpreter \
	introspection \
	; do
pushd dsol-${module}-%{version}
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        install javadoc:javadoc
popd
done

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}/dsol
%__install -m 644 dsol-event-1.6.9/target/event-1.6.9.jar %{buildroot}%{_javadir}/dsol
%__install -m 644 dsol-interpreter-1.6.9/target/interpreter-1.6.9.jar %{buildroot}%{_javadir}/dsol
%__install -m 644 dsol-introspection-1.6.9/target/introspection-1.6.9.jar %{buildroot}%{_javadir}/dsol
%__install -m 644 dsol-jstats-1.6.9/target/jstats-1.6.9.jar %{buildroot}%{_javadir}/dsol
%__install -m 644 dsol-language-1.6.9/target/language-1.6.9.jar %{buildroot}%{_javadir}/dsol
%__install -m 644 dsol-logger-1.6.9/target/logger-1.6.9.jar %{buildroot}%{_javadir}/dsol
%__install -m 644 dsol-naming-1.6.9/target/naming-1.6.9.jar %{buildroot}%{_javadir}/dsol
(cd %{buildroot}%{_javadir}/dsol && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# poms
%__mkdir_p %{buildroot}%{_datadir}/maven2/poms
%__install -m 644 dsol-event-1.6.9/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.dsol-event.pom
%add_to_maven_depmap dsol event %{version} JPP/dsol event
%__install -m 644 dsol-interpreter-1.6.9/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.dsol-interpreter.pom
%add_to_maven_depmap dsol interpreter %{version} JPP/dsol interpreter
%__install -m 644 dsol-introspection-1.6.9/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.dsol-introspection.pom
%add_to_maven_depmap dsol introspection %{version} JPP/dsol introspection
%__install -m 644 dsol-jstats-1.6.9/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.dsol-jstats.pom
%add_to_maven_depmap dsol jstats %{version} JPP/dsol jstats
%__install -m 644 dsol-language-1.6.9/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.dsol-language.pom
%add_to_maven_depmap dsol language %{version} JPP/dsol language
%__install -m 644 dsol-logger-1.6.9/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.dsol-logger.pom
%add_to_maven_depmap dsol logger %{version} JPP/dsol logger
%__install -m 644 dsol-naming-1.6.9/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.dsol-naming.pom
%add_to_maven_depmap dsol naming %{version} JPP/dsol naming

# javadoc 
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}/event
%__cp -a dsol-event-1.6.9/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/event
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}/interpreter
%__cp -a dsol-interpreter-1.6.9/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/interpreter
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}/introspection
%__cp -a dsol-introspection-1.6.9/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/introspection
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}/jstats
%__cp -a dsol-jstats-1.6.9/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/jstats
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}/language
%__cp -a dsol-language-1.6.9/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/language
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}/logger
%__cp -a dsol-logger-1.6.9/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/logger
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}/naming
%__cp -a dsol-naming-1.6.9/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/naming

%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%files
%doc LICENSE.txt
%dir %{_javadir}/dsol
%{_javadir}/dsol/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc 
%{_javadocdir}/%{name}-%{version} 
%{_javadocdir}/%{name} 

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt3_1jpp6
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt2_1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1_1jpp6
- new version

