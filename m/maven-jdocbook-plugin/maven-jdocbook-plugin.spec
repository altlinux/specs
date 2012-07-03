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


Name:           maven-jdocbook-plugin
Version:        2.1.2
Release:        alt1_1jpp6
Epoch:          0
Summary:        jDocBook Maven Plugin
License:        LGPL
Url:            http://www.jboss.org/maven-jdocbook-plugin/
Group:          Development/Java
Source0:        %{name}-%{version}.tar.gz
# svn export http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/maven-plugins/tags/maven-jdocbook-plugin-2.1.2/
Source1:        %{name}-settings.xml
Source2:        %{name}-%{version}-jpp-depmap.xml
Source3:        jboss-parent-3.pom
## get it from http://anonsvn.jboss.org/repos/labs/labs/jbossbuild/jboss-parent/tags/jboss-parent-3/pom.xml

Patch0:         maven-jdocbook-plugin-ResourceMojo.patch
Patch1:         maven-jdocbook-plugin-nojai-pom.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-release
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin

BuildRequires: docbook-xsl-saxon
BuildRequires: saxon
BuildRequires: xml-commons-resolver11
BuildRequires: xmlgraphics-batik
BuildRequires: xmlgraphics-fop

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

Requires: maven2
Requires: docbook-xsl-saxon
Requires: saxon
Requires: xml-commons-resolver11
Requires: xmlgraphics-batik
Requires: xmlgraphics-fop

BuildArch:      noarch
BuildRequires: jboss-parent3

%description
DocBook is, in part, "an XML vocabulary that lets you create
documents in a presentation-neutral form that captures the
logical structure of your content". Another aspect of DocBook
is the rendering of that content into various formats using
DocBook-supplied (or custom) XSLT stylesheets. Basically,
DocBook allows you to write and maintain a single source for
documentation, and to then render that single source into
multiple formats such as PDF or HTML.

The purpose of the jDocBook Plugin is to allow these DocBook
transformations to occur as a natural part of the users Maven
build. The main difficulty with this has always been the fact
that DocBook transformations are usually very closely tied to
the user's local environment. The design goal with writing
this plugin was to utilize Maven's dependency mechanism to
bring all the pieces together on demand. Those pieces are:

1. the DocBook distribution;
2. custom XSLT;
3. custom fonts;
4. custom images;
5. custom css.

These are the ingredients that when mixed with the source
file(s) and stirred with an XSLT transformer produce the
desired output(s).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0
%patch1 -b .sav1

cp %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" settings.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp %{SOURCE3} $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.jboss-jboss-parent.pom

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2_SETTINGS=$(pwd)/settings.xml
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $M2_SETTINGS \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 755 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss.maven.plugins %{name} %{version} JPP %{name}

install -m 644 target/%{name}-%{version}.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_1jpp6
- new version

* Tue Mar 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.2-alt1_1jpp5
- first build

