Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: ant-bsf
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


%define aptdoc_pver     1.0
%define axis_pver       0.7
%define cobertura_pver  1.1.1
%define dbunit_pver     1.6
%define deb_pver        0.5
%define files_pver      1.0
%define findbugs_pver   0.9.1
%define flash_pver      0.1
%define help_pver       1.0
%define izpack_pver     0.3.1
%define javaapp_pver    1.4
%define javancss_pver   1.3
%define junitpp_pver    1.1
%define news_pver       1.0
%define rpm_pver        1.0
%define runtime_builder_pver   0.5
%define sdocbook_pver   1.4.2
%define springgraph_pver   0.2
%define tasks_pver      1.2.0
%define uberdist_pver   1.0.11
%define vignette_pver   1.0.0
%define was40_pver      1.4.2
%define was5_pver       2.0
%define webtest_pver    1.2
%define word2html_pver  1.4
%define xmlresume_pver  0.2.1

Name:           sf-maven-plugins
Version:        1.0
Release:        alt6_0.20050908.9jpp5
Epoch:          0
Summary:        Maven Plugins hosted at sf.net

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://maven-plugins.sourceforge.net/
Source0:        sf-maven-plugins-20050908.tar.gz
##cvs -d :pserver:anonymous@cvs.sourceforge.net:/cvsroot/maven-plugins login
##cvs -z3 -d :pserver:anonymous@cvs.sourceforge.net:/cvsroot/maven-plugins export -r HEAD maven-plugins
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        sf-maven-plugins-1.0-20050908-jpp-depmap.xml

Patch0:         sf-maven-plugins-1.0-20050908-javancss-xdocs-index_xml.patch
Patch1:         sf-maven-plugins-1.0-20050908-plugin-project_xml.patch
Patch2:         sf-maven-plugins-1.0-20050908-sdocbook-project_xml.patch
Patch3:         sf-maven-plugins-1.0-20050908-xmlresume-project_xml.patch
Patch4:         sf-maven-plugins-1.0-20050908-axis-project_xml.patch
Patch5:         sf-maven-plugins-1.0-20050908-findbugs-project_xml.patch
Patch6:         sf-maven-plugins-1.0-20050908-help-project_xml.patch
Patch7:         sf-maven-plugins-1.0-20050908-rpm-project_xml.patch
Patch8:         sf-maven-plugins-1.0-20050908-tasks-project_xml.patch
Patch9:         sf-maven-plugins-1.0-20050908-webtest-project_xml.patch
Patch10:        sf-maven-plugins-1.0-20050908-help-xdocs-index_xml.patch
Patch11:        sf-maven-plugins-1.0-20050908-sourceforge-xdocs-index_xml.patch
Patch12:        sf-maven-plugins-1.0-20050908-xdocs-installing_xml.patch
Patch13:        sf-maven-plugins-1.0-20050908-xmlresume-xdocs-navigation_xml.patch
Patch14:        sf-maven-plugins-1.0-20050908-runtime-builder-xdocs-navigation_xml.patch
Patch15:        sf-maven-plugins-1.0-20050908-deb-xdocs-navigation_xml.patch
Patch16:        sf-maven-plugins-1.0-20050908-cobertura-project_xml.patch
Patch17:        sf-maven-plugins-1.0-20050908-news-project_xml.patch
Patch18:        sf-maven-plugins-1.0-20050908-files-project_xml.patch
Patch19:        sf-maven-plugins-1.0-20050908-db2-plugin_jelly.patch
Patch20:        sf-maven-plugins-1.0-20050908-deb-project_xml.patch
Patch21:        sf-maven-plugins-1.0-20050908-flash-project_xml.patch
Patch22:        sf-maven-plugins-1.0-20050908-sdocbook-plugin_jelly.patch
Patch23:        sf-maven-plugins-1.0-20050908-kodo-plugin_jelly.patch
Patch24:        sf-maven-plugins-1.0-20050908-macker-plugin_jelly.patch
Patch25:        sf-maven-plugins-1.0-20050908-findbugs-plugin_jelly.patch
Patch26:        sf-maven-plugins-1.0-20050908-strutsdoc-plugin_jelly.patch
Patch27:        sf-maven-plugins-1.0-20050908-junitpp-plugin_jelly.patch
Patch28:        sf-maven-plugins-1.0-20050908-xmlresume-plugin_jelly.patch
Patch29:        sf-maven-plugins-1.0-20050908-axis-plugin_jelly.patch
Patch30:        sf-maven-plugins-1.0-20050908-javancss-plugin_jelly.patch
Patch31:        sf-maven-plugins-1.0-20050908-middlegen-plugin_jelly.patch
Patch32:        sf-maven-plugins-1.0-20050908-izpack-plugin_jelly.patch
Patch33:        sf-maven-plugins-1.0-20050908-dotuml-plugin_jelly.patch
Patch34:        sf-maven-plugins-1.0-20050908-vignette-plugin_jelly.patch
Patch35:        sf-maven-plugins-1.0-20050908-webtest-plugin_jelly.patch
Patch36:        sf-maven-plugins-1.0-20050908-transform-plugin_jelly.patch
Patch37:        sf-maven-plugins-1.0-20050908-cobertura-plugin_jelly.patch
Patch38:        sf-maven-plugins-1.0-20050908-dbunit-plugin_jelly.patch 
Patch39:        sf-maven-plugins-1.0-20050908-runtime-builder-project_xml.patch
Patch40:        sf-maven-plugins-1.0-20050908-springgraph-project_xml.patch
Patch41:        sf-maven-plugins-1.0-20050908-was5-project_xml.patch
Patch42:        sf-maven-plugins-1.0-20050908-javancss-project_xml.patch
# this patch seems bad but it's required for a successful mock build
# and after all it's just a docfile *innocent whistle*
Patch43:        sf-maven-plugins-1.0-20050908-springgraph-xdocs-applicationContext_xml.patch

Patch100: sf-maven-plugins-alt-maven1.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
%endif


BuildRequires: jpackage-utils >= 0:1.6.5
BuildRequires: junit
BuildRequires: ant >= 0:1.6
BuildRequires: ant-apache-bsf
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: maven1 >= 0:1.1
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: aptconvert
BuildRequires: asm
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-logkit
BuildRequires: axis
BuildRequires: batik
BuildRequires: batik-rasterizer
BuildRequires: bcel
BuildRequires: cobertura
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-cli
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-discovery
BuildRequires: jakarta-commons-httpclient >= 1:3.0
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-jelly
BuildRequires: jakarta-commons-jelly-tags-interaction
BuildRequires: jakarta-commons-jelly-tags-jsl
BuildRequires: jakarta-commons-jelly-tags-log
BuildRequires: jakarta-commons-jelly-tags-util
BuildRequires: jakarta-commons-jelly-tags-velocity
BuildRequires: jakarta-commons-jelly-tags-xml
BuildRequires: jakarta-commons-jxpath
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-net
BuildRequires: jakarta-commons-pool
BuildRequires: dbunit
BuildRequires: docbook-xsl-java-xalan
BuildRequires: dom4j
BuildRequires: xmlgraphics-fop
BuildRequires: groovy11
#BuildRequires:  jai
BuildRequires: gnu-getopt
BuildRequires: gnu-regexp
BuildRequires: jaxen
BuildRequires: jcommon
BuildRequires: jdom
BuildRequires: jfreechart
#BuildRequires:  jimi
BuildRequires: jline
BuildRequires: log4j
BuildRequires: maven1-plugin-announcement
BuildRequires: maven1-plugin-changelog
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-faq
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-linkcheck
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: maven1-plugins-base
BuildRequires: mx4j
BuildRequires: nekohtml
BuildRequires: oro
BuildRequires: jakarta-poi
BuildRequires: regexp
BuildRequires: relaxngDatatype
BuildRequires: servletapi4
BuildRequires: velocity
BuildRequires: xalan-j2 >= 0:2.7
BuildRequires: xerces-j2 >= 0:2.7
BuildRequires: xml-commons-apis >= 0:1.3
BuildRequires: xml-commons-resolver
BuildRequires: msv-xsdlib
BuildRequires: ccl-util
BuildRequires: izpack
BuildRequires: wsdl4j

Requires: sf-cobertura-maven-plugin
Requires: sf-dbunit-maven-plugin
Requires: sf-deb-maven-plugin
Requires: sf-files-maven-plugin
Requires: sf-findbugs-maven-plugin
Requires: sf-flash-maven-plugin
Requires: sf-help-maven-plugin
Requires: sf-izpack-maven-plugin
Requires: sf-javaapp-maven-plugin
Requires: sf-javancss-maven-plugin
Requires: sf-junitpp-maven-plugin
Requires: sf-news-maven-plugin
Requires: sf-rpm-maven-plugin
Requires: sf-runtime-builder-maven-plugin
Requires: sf-sdocbook-maven-plugin
Requires: sf-springgraph-maven-plugin
Requires: sf-tasks-maven-plugin
Requires: sf-uberdist-maven-plugin
Requires: sf-vignette-maven-plugin
Requires: sf-was40-maven-plugin
Requires: sf-was5-maven-plugin
Requires: sf-webtest-maven-plugin
Requires: sf-word2html-maven-plugin
Requires: sf-xmlresume-maven-plugin

%description
This is a subset of the maven plugins hosted at
sourceforge.net.

%package -n sf-aptdoc-maven-plugin
Summary:        Aptconvert Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: aptconvert
Requires: gnu-regexp
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-aptdoc-maven-plugin
%{summary}.

%package -n sf-axis-maven-plugin
Summary:        Axis Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: axis
Requires: jakarta-commons-logging
Requires: jakarta-commons-discovery
Requires: jakarta-commons-jelly-tags-log
Requires: wsdl4j
Requires: xerces-j2
Requires: xml-commons-apis

%description -n sf-axis-maven-plugin
%{summary}.

%package -n sf-cobertura-maven-plugin
Summary:        Cobertura Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: cobertura
Requires: oro
Requires: asm
Requires: log4j
Requires: gnu.getopt
Requires: ccl-util
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-cobertura-maven-plugin
%{summary}.

%package -n sf-dbunit-maven-plugin
Summary:        DBUnit Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: dbunit
Requires: jakarta-poi
Requires: jakarta-commons-lang
Requires: xml-commons-apis
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-dbunit-maven-plugin
%{summary}.

%package -n sf-deb-maven-plugin
Summary:        DEB Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: jakarta-commons-logging
Requires: jakarta-commons-lang
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif


%description -n sf-deb-maven-plugin
%{summary}.

%package -n sf-files-maven-plugin
Summary:        Files Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: ant
Requires: xalan-j2
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif


%description -n sf-files-maven-plugin
%{summary}.

%package -n sf-findbugs-maven-plugin
Summary:        Findbugs Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: dom4j
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-findbugs-maven-plugin
%{summary}.

%package -n sf-flash-maven-plugin
Summary:        Flash Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-flash-maven-plugin
%{summary}.

%package -n sf-help-maven-plugin
Summary:        Help Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-help-maven-plugin
%{summary}.

%package -n sf-izpack-maven-plugin
Summary:        IZPack Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: jakarta-commons-jelly-tags-xml
Requires: jakarta-commons-jelly-tags-jsl
Requires: izpack

%description -n sf-izpack-maven-plugin
%{summary}.

%package -n sf-javaapp-maven-plugin
Summary:        Java App Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: jakarta-commons-lang
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-javaapp-maven-plugin
%{summary}.

%package -n sf-javancss-maven-plugin
Summary:        Java NCSS Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-apis
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-javancss-maven-plugin
%{summary}.

%package -n sf-junitpp-maven-plugin
Summary:        JUnitpp Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: junit
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-junitpp-maven-plugin
%{summary}.

%package -n sf-news-maven-plugin
Summary:        News Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-news-maven-plugin
%{summary}.

%package -n sf-rpm-maven-plugin
Summary:        RPM Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-rpm-maven-plugin
%{summary}.

%package -n sf-runtime-builder-maven-plugin
Summary:        Runtime Builder Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: jakarta-commons-jelly-tags-velocity
Requires: velocity
Requires: ant


%description -n sf-runtime-builder-maven-plugin
%{summary}.

%package -n sf-sdocbook-maven-plugin
Summary:        SDocbook Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: docbook-xsl-java-xalan
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-logkit
Requires: batik
Requires: xmlgraphics-fop
#Requires:       jimi
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-apis
Requires: xml-commons-resolver

%description -n sf-sdocbook-maven-plugin
%{summary}.

%package -n sf-springgraph-maven-plugin
Summary:        Springgraph Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-springgraph-maven-plugin
%{summary}.

%package -n sf-tasks-maven-plugin
Summary:        Tasks Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-tasks-maven-plugin
%{summary}.

%package -n sf-uberdist-maven-plugin
Summary:        Uberdist Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-uberdist-maven-plugin
%{summary}.

%package -n sf-vignette-maven-plugin
Summary:        Vignette Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: servlet >= 0:2.3

%description -n sf-vignette-maven-plugin
%{summary}.

%package -n sf-was40-maven-plugin
Summary:        WAS40 Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: jakarta-commons-jelly-tags-util

%description -n sf-was40-maven-plugin
%{summary}.

%package -n sf-was5-maven-plugin
Summary:        WAS5 Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-was5-maven-plugin
%{summary}.

%package -n sf-webtest-maven-plugin
Summary:        WebTest Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: ant
Requires: ant-apache-bsf
Requires: ant-junit
Requires: ant-trax
Requires: asm
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-cli
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-jelly-tags-interaction
Requires: jakarta-commons-httpclient >= 1:3.0
Requires: jakarta-commons-io
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: groovy11
Requires: jaxen
Requires: junit
Requires: log4j
Requires: nekohtml
Requires: oro
Requires: xalan-j2
Requires: xml-commons-apis
%if %{gcj_support}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description -n sf-webtest-maven-plugin
%{summary}.

%package -n sf-word2html-maven-plugin
Summary:        Word2html Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1

%description -n sf-word2html-maven-plugin
%{summary}.

%package -n sf-xmlresume-maven-plugin
Summary:        XMLResume Maven Plugin hosted at sf.net
Group:          Development/Java
Requires: maven1 >= 0:1.1
Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-logkit
Requires: batik
Requires: xmlgraphics-fop
Requires: xalan-j2
Requires: xerces-j2
Requires: xml-commons-apis

%description -n sf-xmlresume-maven-plugin
%{summary}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.


%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.


%prep
%setup -q -n %{name}

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav
%patch9 -b .sav
%patch10 -b .sav
%patch11 -b .sav
%patch12 -b .sav
%patch13 -b .sav
%patch14 -b .sav
%patch15 -b .sav
%patch16 -b .sav
%patch17 -b .sav
%patch18 -b .sav
%patch19 -b .sav
%patch20 -b .sav
%patch21 -b .sav
%patch22 -b .sav
%patch23 -b .sav
%patch24 -b .sav
%patch25 -b .sav
%patch26 -b .sav
%patch27 -b .sav
%patch28 -b .sav
%patch29 -b .sav
%patch30 -b .sav
%patch31 -b .sav
%patch32 -b .sav
%patch33 -b .sav
%patch34 -b .sav
%patch35 -b .sav
%patch36 -b .sav
%patch37 -b .sav
%patch38 -b .sav
%patch39 -b .sav
%patch40 -b .sav
%patch41 -b .sav
%patch42 -b .sav
%patch43 -b .sav

%patch100 -p1

%build
if [ ! -f %{SOURCE4} ]; then
  export DEPCAT=$(pwd)/sf-maven-plugins-1.0-depcat.new.xml
  echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
  echo '<depset>' >> $DEPCAT
  for p in $(find . -name project.xml); do
      pushd $(dirname $p)
      /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
      popd
  done
  echo >> $DEPCAT
  echo '</depset>' >> $DEPCAT
  /usr/bin/saxon $DEPCAT %{SOURCE2} > sf-maven-plugins-1.0-depmap.new.xml
fi

for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

mkdir -p .maven

export MAVEN_HOME_LOCAL=$(pwd)/.maven

ALL_PLUGINS="aptdoc axis cobertura db2 dbunit deb dotuml doxygen files findbugs flash help izpack javaapp javancss jaxb junitpp kodo macker maven-dashboard-history middlegen news rpm runtime-builder sdocbook sourceforge springgraph strutsdoc tasks transform uberdist vignette was40 was5 weblogic webtest wiki word2html xmlresume"

PEND_PLUGINS="db2 dotuml doxygen jaxb kodo macker middlegen maven-dashboard-history/maven-plugins sourceforge strutsdoc transform weblogic wiki"


for p in aptdoc axis cobertura dbunit deb news files findbugs flash help izpack javaapp javancss junitpp rpm runtime-builder sdocbook springgraph tasks uberdist vignette was40 was5 webtest word2html xmlresume; do
pushd $p
maven \
	-Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5 \
        -Dmaven.mode.offline=true \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository \
        -Dmaven.home.local=$MAVEN_HOME_LOCAL \
        plugin:install-now plugin:repository-install \
        javadoc:generate xdoc:transform
popd
cp .maven/repository/maven-plugins/plugins/* .maven/plugins/ 
done

%install
# maven-plugins
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven1/plugins

install -m 644 \
aptdoc/target/maven-aptdoc-plugin-%{aptdoc_pver}-SNAPSHOT.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-aptdoc-plugin-%{aptdoc_pver}.jar
install -m 644 \
axis/target/maven-axis-plugin-%{axis_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-axis-plugin-%{axis_pver}.jar
install -m 644 \
cobertura/target/maven-cobertura-plugin-%{cobertura_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-cobertura-plugin-%{cobertura_pver}.jar
install -m 644 \
dbunit/target/maven-dbunit-plugin-%{dbunit_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-dbunit-plugin-%{dbunit_pver}.jar
install -m 644 \
deb/target/maven-deb-plugin-%{deb_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-deb-plugin-%{deb_pver}.jar
install -m 644 \
files/target/maven-files-plugin-%{files_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-files-plugin-%{files_pver}.jar
install -m 644 \
findbugs/target/maven-findbugs-plugin-%{findbugs_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-findbugs-plugin-%{findbugs_pver}.jar
install -m 644 \
flash/target/maven-flash-plugin-%{flash_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-flash-plugin-%{flash_pver}.jar
install -m 644 \
help/target/maven-help-plugin-%{help_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-help-plugin-%{help_pver}.jar
install -m 644 \
izpack/target/maven-izpack-plugin-%{izpack_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-izpack-plugin-%{izpack_pver}.jar
install -m 644 \
javaapp/target/maven-javaapp-plugin-%{javaapp_pver}-SNAPSHOT.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-javaapp-plugin-%{javaapp_pver}.jar
install -m 644 \
javancss/target/maven-javancss-plugin-%{javancss_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-javancss-plugin-%{javancss_pver}.jar
install -m 644 \
junitpp/target/maven-junitpp-plugin-%{junitpp_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-junitpp-plugin-%{junitpp_pver}.jar
install -m 644 \
news/target/maven-news-plugin-%{news_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-news-plugin-%{news_pver}.jar
install -m 644 \
rpm/target/maven-rpm-plugin-%{rpm_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-rpm-plugin-%{rpm_pver}.jar
install -m 644 \
runtime-builder/target/maven-runtime-builder-plugin-%{runtime_builder_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-runtime-builder-plugin-%{runtime_builder_pver}.jar
install -m 644 \
sdocbook/target/maven-sdocbook-plugin-%{sdocbook_pver}-SNAPSHOT.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-sdocbook-plugin-%{sdocbook_pver}.jar
install -m 644 \
springgraph/target/maven-springgraph-plugin-%{springgraph_pver}-SNAPSHOT.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-springgraph-plugin-%{springgraph_pver}.jar
install -m 644 \
tasks/target/maven-tasks-plugin-%{tasks_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-tasks-plugin-%{tasks_pver}.jar
install -m 644 \
uberdist/target/maven-uberdist-plugin-%{uberdist_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-uberdist-plugin-%{uberdist_pver}.jar
install -m 644 \
vignette/target/maven-vignette-plugin-%{vignette_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-vignette-plugin-%{vignette_pver}.jar
install -m 644 \
was40/target/maven-was40-plugin-%{was40_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-was40-plugin-%{was40_pver}.jar
install -m 644 \
was5/target/maven-was5-plugin-%{was5_pver}-SNAPSHOT.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-was5-plugin-%{was5_pver}.jar
install -m 644 \
webtest/target/maven-webtest-plugin-%{webtest_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-webtest-plugin-%{webtest_pver}.jar
install -m 644 \
word2html/target/maven-word2html-plugin-%{word2html_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-word2html-plugin-%{word2html_pver}.jar
install -m 644 \
xmlresume/target/maven-xmlresume-plugin-%{xmlresume_pver}.jar \
$RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-xmlresume-plugin-%{xmlresume_pver}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven1-plugins
pushd $RPM_BUILD_ROOT%{_javadir}/maven1-plugins
ln -sf %{_datadir}/maven1/plugins/maven-aptdoc-plugin-%{aptdoc_pver}.jar maven-aptdoc-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-axis-plugin-%{axis_pver}.jar maven-axis-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-cobertura-plugin-%{cobertura_pver}.jar maven-cobertura-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-dbunit-plugin-%{dbunit_pver}.jar maven-dbunit-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-deb-plugin-%{deb_pver}.jar maven-deb-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-files-plugin-%{files_pver}.jar maven-files-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-findbugs-plugin-%{findbugs_pver}.jar maven-findbugs-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-flash-plugin-%{flash_pver}.jar maven-flash-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-help-plugin-%{help_pver}.jar maven-help-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-izpack-plugin-%{izpack_pver}.jar maven-izpack-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-javaapp-plugin-%{javaapp_pver}.jar maven-javaapp-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-javancss-plugin-%{javancss_pver}.jar maven-javancss-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-junitpp-plugin-%{junitpp_pver}.jar maven-junitpp-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-news-plugin-%{news_pver}.jar maven-news-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-rpm-plugin-%{rpm_pver}.jar maven-rpm-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-runtime-builder-plugin-%{runtime_builder_pver}.jar maven-runtime-builder-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-sdocbook-plugin-%{sdocbook_pver}.jar maven-sdocbook-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-springgraph-plugin-%{springgraph_pver}.jar maven-springgraph-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-tasks-plugin-%{tasks_pver}.jar maven-tasks-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-uberdist-plugin-%{uberdist_pver}.jar maven-uberdist-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-vignette-plugin-%{vignette_pver}.jar maven-vignette-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-was40-plugin-%{was40_pver}.jar maven-was40-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-was5-plugin-%{was5_pver}.jar maven-was5-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-webtest-plugin-%{webtest_pver}.jar maven-webtest-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-word2html-plugin-%{word2html_pver}.jar maven-word2html-plugin.jar
ln -sf %{_datadir}/maven1/plugins/maven-xmlresume-plugin-%{xmlresume_pver}.jar maven-xmlresume-plugin.jar
popd

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
for p in aptdoc dbunit deb files javaapp; do
        install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$p
cp -pr $p/target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$p
rm -rf $p/target/docs/apidocs
done
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink


install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
for p in aptdoc axis cobertura dbunit deb news files findbugs flash help izpack javaapp javancss junitpp rpm runtime-builder sdocbook springgraph tasks uberdist vignette was40 was5 webtest word2html xmlresume; do
        install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$p
cp -pr $p/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$p
done
cp -p LICENSE.txt README $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%doc %{_docdir}/%{name}-%{version}/README
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%files -n sf-aptdoc-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-aptdoc-plugin*.jar
%{_javadir}/maven1-plugins/maven-aptdoc-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-aptdoc-plugin-%{aptdoc_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-axis-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-axis-plugin*.jar
%{_javadir}/maven1-plugins/maven-axis-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-cobertura-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-cobertura-plugin*.jar
%{_javadir}/maven1-plugins/maven-cobertura-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-cobertura-plugin-%{cobertura_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-dbunit-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-dbunit-plugin*.jar
%{_javadir}/maven1-plugins/maven-dbunit-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-dbunit-plugin-%{dbunit_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-deb-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-deb-plugin*.jar
%{_javadir}/maven1-plugins/maven-deb-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-deb-plugin-%{deb_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-files-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-files-plugin*.jar
%{_javadir}/maven1-plugins/maven-files-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-files-plugin-%{files_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-findbugs-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-findbugs-plugin*.jar
%{_javadir}/maven1-plugins/maven-findbugs-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-findbugs-plugin-%{findbugs_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-flash-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-flash-plugin*.jar
%{_javadir}/maven1-plugins/maven-flash-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-help-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-help-plugin*.jar
%{_javadir}/maven1-plugins/maven-help-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-izpack-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-izpack-plugin*.jar
%{_javadir}/maven1-plugins/maven-izpack-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-javaapp-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-javaapp-plugin*.jar
%{_javadir}/maven1-plugins/maven-javaapp-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-javaapp-plugin-%{javaapp_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-javancss-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-javancss-plugin*.jar
%{_javadir}/maven1-plugins/maven-javancss-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-javancss-plugin-%{javancss_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-junitpp-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-junitpp-plugin*.jar
%{_javadir}/maven1-plugins/maven-junitpp-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-junitpp-plugin-%{junitpp_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-news-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-news-plugin*.jar
%{_javadir}/maven1-plugins/maven-news-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-rpm-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-rpm-plugin*.jar
%{_javadir}/maven1-plugins/maven-rpm-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-runtime-builder-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-runtime-builder-plugin*.jar
%{_javadir}/maven1-plugins/maven-runtime-builder-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-sdocbook-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-sdocbook-plugin*.jar
%{_javadir}/maven1-plugins/maven-sdocbook-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-springgraph-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-springgraph-plugin*.jar
%{_javadir}/maven1-plugins/maven-springgraph-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-tasks-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-tasks-plugin*.jar
%{_javadir}/maven1-plugins/maven-tasks-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-uberdist-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-uberdist-plugin*.jar
%{_javadir}/maven1-plugins/maven-uberdist-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-vignette-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-vignette-plugin*.jar
%{_javadir}/maven1-plugins/maven-vignette-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-was40-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-was40-plugin*.jar
%{_javadir}/maven1-plugins/maven-was40-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-was5-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-was5-plugin*.jar
%{_javadir}/maven1-plugins/maven-was5-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-webtest-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-webtest-plugin*.jar
%{_javadir}/maven1-plugins/maven-webtest-plugin.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/maven-webtest-plugin-%{webtest_pver}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-word2html-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-word2html-plugin*.jar
%{_javadir}/maven1-plugins/maven-word2html-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files -n sf-xmlresume-maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-xmlresume-plugin*.jar
%{_javadir}/maven1-plugins/maven-xmlresume-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}


%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_0.20050908.9jpp5
- fixed build with java 7

* Mon Mar 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.20050908.9jpp5
- moved to /usr/share/maven1

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.20050908.9jpp5
- maven1 dependency translaton

* Fri Oct 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.20050908.9jpp5
- fixed build

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.20050908.9jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.20050908.8jpp5
- fixed repocop warnings

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.20050908.8jpp1.7
- enabled jpox plugin

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.20050908.8jpp1.7
- release based on 1.0-0.20050908.8jpp

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.20050908.7jpp1.7
- converted from JPackage by jppimport script

