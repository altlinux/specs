BuildRequires: crimson
%define _without_maven 1
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
# Copyright (c) 2000-2009, JPackage Project
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

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}


%define repo_dir    .m2/repository

Name:           cewolf
Version:        1.0
Release:        alt2_5jpp5
Epoch:          0
Summary:        Chart Taglib Library
License:        LGPLv2+
URL:            http://cewolf.sourceforge.net/
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/cewolf/cewolf-1.0-bin-src.zip
Source1:        cewolf-build.xml
Source3:        cewolf-settings.xml
Source4:        cewolf-1.0-jpp-depmap.xml
Patch0:          cewolf-1.0-fix_tld_places.diff
Patch1:          cewolf-1.0-build.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: xmlgraphics-batik
BuildRequires: jakarta-commons-logging
BuildRequires: jcommon >= 0:1.0.0
BuildRequires: jfreechart >= 0:1.0.0
BuildRequires: log4j
BuildRequires: servletapi4
BuildRequires: xml-commons-jaxp-1.3-apis
%if %{with_maven}
BuildRequires: maven2
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-install
BuildRequires: maven-surefire-plugin
BuildRequires: excalibur-avalon-framework
%endif
Requires: xmlgraphics-batik
Requires: jakarta-commons-logging
Requires: jcommon >= 0:1.0.0
Requires: jfreechart >= 0:1.0.0
Requires: log4j
Requires: servletapi4
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif

%description
Cewolf can be used inside a Servlet/JSP based web application
to embed complex graphical charts of all kinds (e.g. line,
pie, bar chart, plots, etc.) into a web page. Therefore it
provides a full featured tag library to define all properties
of the chart (colors, strokes, legend, etc.). Thus the JSP
which embedds the chart is not polluted with any java code.
Everything is described with XML conform tags.
Cewolf is based on JFreeChart and uses it's rendering engine
to render the final chart image into the clients response
stream. No files are created on server side. Everything is
based on lightweight session objects and dynamic data analysis.
Cewolf consists of one servlet which handles the chart
rendering and a taglibrary which translates the chart
definition included in the JSP into an HTML img tag which
consults the rendering servlet for retrieval of the
appropriate chart.

%package        demo
Summary:        Demos for %{name}
Group:          Development/Documentation

%description    demo
Demonstrations and samples for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q 
%patch0 -p1
%patch1 -b .sav1
# remove all binary libs
find . -name "*.jar" | xargs rm
cp -p %{SOURCE1} build.xml
cp -p %{SOURCE3} settings.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL/JPP

%if %{with_maven}
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
cp src/main/resources/cewolf-1.1.tld src/main/resources/taglib.tld

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE4} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%else
export CLASSPATH=""
CLASSPATH=${CLASSPATH}:$(build-classpath batik/awt-util)
CLASSPATH=${CLASSPATH}:$(build-classpath batik/dom)
CLASSPATH=${CLASSPATH}:$(build-classpath batik/svggen)
CLASSPATH=${CLASSPATH}:$(build-classpath batik/util)
CLASSPATH=${CLASSPATH}:$(build-classpath batik/xml)
CLASSPATH=${CLASSPATH}:$(build-classpath commons-logging)
CLASSPATH=${CLASSPATH}:$(build-classpath crimson)
CLASSPATH=${CLASSPATH}:$(build-classpath jcommon)
CLASSPATH=${CLASSPATH}:$(build-classpath jfreechart)
CLASSPATH=${CLASSPATH}:$(build-classpath log4j)
CLASSPATH=${CLASSPATH}:$(build-classpath servletapi4)
CLASSPATH=${CLASSPATH}:$(build-classpath xml-commons-jaxp-1.3-apis)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
%endif

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
for jar in $(find -type f -name "*.jar" | grep -E target/.*.jar); do
        install -m 644 $jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
done
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
for target in $(find -type d -name target); do
        install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/`basename \`dirname $target\` | sed -e s:jline-::g`
        cp -pr $target/site/apidocs/* $jar $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/`basename \`dirname $target\` | sed -e s:jline-::g`
done
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp5
- built with java 6 due to com.sun.image.codec.jpeg

* Sat Aug 08 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp5
- dropped crimson buildreq

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

