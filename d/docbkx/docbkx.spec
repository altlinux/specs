BuildRequires: maven-shared-ant
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


Name:           docbkx
Version:        2.0.8
Release:        alt5_4jpp6
Epoch:          0
Summary:        Docbkx Tools
License:        ASL 2.0
Group:          Development/Java
URL:            http://agilejava.com/docbkx/
# svn export http://docbkx-tools.googlecode.com/svn/tags/docbkx-2.0.8/
Source0:        docbkx-2.0.8.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        docbkx-fop-xsl-post.patch
Patch0:         docbkx-AbstractTransformerMojo.patch
Patch1:         docbkx-pom.patch
Patch2:         docbkx-maven-plugin-pom.patch
Patch3:         docbkx-docbkx-samples-pom.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: ant >= 0:1.7
Requires: excalibur-avalon-framework
Requires: xmlgraphics-fop
Requires: jakarta-commons-el
Requires: jakarta-commons-io
Requires: jaxen
Requires: jpackage-utils
Requires: jsp_2_0_api
Requires: maven2
Requires: maven2-plugin-antrun
Requires: plexus-container-default
Requires: plexus-utils
Requires: saxon
Requires: stringtemplate22
Requires: xml-commons-resolver11
BuildRequires: apache-commons-parent
BuildRequires: ant >= 0:1.7
BuildRequires: ant-trax
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildRequires: maven2-common-poms
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-changes
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-plugin-surefire-report
BuildRequires: maven-wagon
BuildRequires: mojo-maven2-plugin-xml
BuildRequires: excalibur-avalon-framework
BuildRequires: xmlgraphics-fop
BuildRequires: jakarta-commons-el
BuildRequires: jakarta-commons-io
BuildRequires: jaxen
BuildRequires: jsp_2_0_api
BuildRequires: plexus-archiver
BuildRequires: plexus-utils
BuildRequires: saxon
BuildRequires: servlet_2_5_api
BuildRequires: stringtemplate22
BuildRequires: xslthl
BuildRequires: xml-commons-resolver11
BuildArch:      noarch
Source44: import.info
Patch33: docbkx-2.0.8-alt-AntPropertyHelper.patch

%description
The Docbkx Tools project provides a number of tools for 
supporting DocBook in a Maven environment. This may seem odd
to you, since 1) Maven 2 is supposed to support DocBook 
natively, relying on Doxia, and 2) there is already another 
DocBook plugin at mojo.codehaus.org.

The thruth however is that DocBook support in Doxia is fairly
limited, mainly because Doxia as a framework supports only a 
small fraction of the concepts found in DocBook. The subset 
of DocBook supported by Doxia is not even close to simplified 
DocBook.

The DocBook plugin at mojo.codehaus.org is supporting a wider 
range of DocBook markup, and is in fact more similar to the 
DocBook tools provided with this project. There are however 
some significant differences.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%if 0
# omit samples: they need mojo:xml-maven-plugin we don't have yet
%patch1 -p0 -b .sav1
%endif
# add excalibur-avalon-framework to docbkx-maven-plugin pom; should not be necessary in the future
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3

%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
ln -s $(build-classpath xslthl) docbkx-maven-plugin/lib/

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%patch33 -p1

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dsaxon65.jar=$(build-classpath saxon) \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

mkdir tmpd
pushd tmpd
%{jar} xf ../docbkx-maven-plugin/target/docbkx-maven-plugin-%{version}.jar
patch -p0 < %{SOURCE3}
%{jar} cmf META-INF/MANIFEST.MF ../docbkx-maven-plugin/target/docbkx-maven-plugin-%{version}.jar *
popd

%install

# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins

install -p -m 644 pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.agilejava.docbkx docbkx %{version} JPP %{name}

install -p -m 644 docbkx-builder-maven-plugin/target/docbkx-builder-maven-plugin-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}/builder-maven-plugin-%{version}.jar
install -p -m 644 docbkx-builder-maven-plugin/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-builder-maven-plugin.pom
%add_to_maven_depmap com.agilejava.docbkx docbkx-builder-maven-plugin %{version} JPP/%{name} builder-maven-plugin

install -p -m 644 docbkx-maven-base/target/docbkx-maven-base-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-base-%{version}.jar
%add_to_maven_depmap com.agilejava.docbkx docbkx-maven-base %{version} JPP/%{name} maven-base
install -p -m 644 docbkx-maven-base/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-maven-base.pom

install -p -m 644 docbkx-maven-plugin/target/docbkx-maven-plugin-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-plugin-%{version}.jar
%add_to_maven_depmap com.agilejava.docbkx docbkx-maven-plugin %{version} JPP/%{name} maven-plugin
install -p -m 644 docbkx-maven-plugin/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-maven-plugin.pom

install -p -m 644 docbkx-fop-support/target/docbkx-fop-support-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/%{name}/fop-support-%{version}.jar
%add_to_maven_depmap com.agilejava.docbkx docbkx-fop-support %{version} JPP/%{name} fop-support
install -p -m 644 docbkx-fop-support/pom.xml $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-fop-support.pom

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
    ln -sf %{_javadir}/%{name}/builder-maven-plugin-%{version}.jar %{name}-builder-maven-plugin.jar
    ln -sf %{_javadir}/%{name}/maven-plugin-%{version}.jar %{name}-maven-plugin.jar
)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/builder-maven-plugin
cp -pr %{name}-builder-maven-plugin/target/site/apidocs/* \
                    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/builder-maven-plugin
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-base
cp -pr %{name}-maven-base/target/site/apidocs/* \
                    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-base
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-plugin
cp -pr %{name}-maven-plugin/target/site/apidocs/* \
                    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/maven-plugin
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/fop-support
cp -pr %{name}-fop-support/target/site/apidocs/* \
                    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/fop-support
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/builder-maven-plugin-%{version}.jar
%{_javadir}/%{name}/builder-maven-plugin.jar
%{_javadir}/%{name}/fop-support-%{version}.jar
%{_javadir}/%{name}/fop-support.jar
%{_javadir}/%{name}/maven-base-%{version}.jar
%{_javadir}/%{name}/maven-base.jar
%{_javadir}/%{name}/maven-plugin-%{version}.jar
%{_javadir}/%{name}/maven-plugin.jar
%{_datadir}/maven2/plugins/docbkx-builder-maven-plugin.jar
%{_datadir}/maven2/plugins/docbkx-maven-plugin.jar
%{_datadir}/maven2/poms/JPP-docbkx.pom
%{_datadir}/maven2/poms/JPP.docbkx-builder-maven-plugin.pom
%{_datadir}/maven2/poms/JPP.docbkx-fop-support.pom
%{_datadir}/maven2/poms/JPP.docbkx-maven-base.pom
%{_datadir}/maven2/poms/JPP.docbkx-maven-plugin.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt5_4jpp6
- built with patched assembly plugin

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt4_4jpp6
- fixed build

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt3_4jpp6
- new jpp release

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt3_2jpp5
- fixes for java6 support

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_2jpp5
- converted from JPackage by jppimport script

