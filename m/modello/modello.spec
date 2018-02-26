BuildRequires: xmlunit
Patch33: modello-alt-maven3.patch
BuildRequires: jaxb_2_1_api
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.3
%define name modello
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


%define repo_dir    .m2/repository

%define namedversion 1.3
%define maven_settings_file %{_builddir}/%{name}-%{namedversion}/settings.xml

Name:           modello
Version:        1.3
Release:        alt3_1jpp6
Epoch:          0
Summary:        Modello Data Model toolkit
License:        MIT  
Group:          Development/Java
URL:            http://modello.codehaus.org/
Source0:        %{name}-%{namedversion}.tgz
# svn export https://svn.codehaus.org/modello/tags/modello-1.3/
# tar czf modello-1.3.tgz modello-1.3/
Source1:        modello.script
Source2:        %{name}-jpp-depmap.xml
Patch0:         modello-1.1-ModelloConvertersMojoTest.patch
Patch1:         modello-1.1-ModelloJavaMojoTest.patch
Patch99:        modello-maven-plugin-pom.patch
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: maven2 >= 2.0.8
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia
BuildRequires: maven-doxia-sitetools
BuildRequires: maven2-plugin-plugin
BuildRequires: apache-commons-parent
BuildRequires: classworlds >= 0:1.1
BuildRequires: dtdparser
BuildRequires: geronimo-jpa-3.0-api
BuildRequires: plexus-build-api
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-containers-component-api
BuildRequires: plexus-utils
BuildRequires: plexus-velocity
BuildRequires: excalibur-avalon-framework
BuildRequires: stax_1_0_api
BuildRequires: stax-utils
BuildRequires: velocity
BuildRequires: wstx


Requires: classworlds >= 0:1.1
Requires: dtdparser
Requires: jpa_3_0_api
Requires: plexus-build-api
Requires: plexus-container-default
Requires: plexus-utils
Requires: plexus-velocity
Requires: stax_1_0_api
Requires: stax-utils
Requires: velocity


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

Provides:       modello-maven-plugin = %{epoch}:%{version}-%{release}
Obsoletes:      modello-maven-plugin < 0:1.0-0.a8.3jpp
Source44: import.info

%description
Modello is a Data Model toolkit in use by the 
http://maven.apache.org/maven2.
It all starts with the Data Model. Once a data model is defined, 
the toolkit can be used to generate any of the following at compile 
time.
Java POJOs of the model.
Java POJOs to XML Writer (provided via xpp3 or dom4j).
XML to Java Pojos Reader (provided via xpp3 or dom4j).
XDoc documentation of the data model.
Java model to [Prevayler|http://www.prevayler.org/] Store.
Java model to [JPOX|http://www.jpox.org/] Store.
Java model to [JPOX|http://www.jpox.org/] Mapping.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -b .sav0
%patch1 -b .sav1
%patch99 -b .sav99
find . -name release-pom.xml -exec rm -f '{}' \;
for p in $(find . -name pom.xml); do
    sed -i -e 's|<groupId>plexus</groupId>|<groupId>org.codehaus.plexus</groupId>|' $p
done

%patch33

%build

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.test.failure.ignore=true \
        install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Daggregate=true \
        javadoc:javadoc

%install

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
for i in `find . -name pom.xml | grep -v \\\./pom.xml`; do
        cp -p $i $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.`basename \`dirname $i\``.pom
done

# Depmap fragments
for i in `find . -name pom.xml | grep -v \\\./pom.xml |  grep -v modello-plugins-sandbox`; do
    # i is in format ..../artifactid/pom.xml
    artifactname=`basename \`dirname $i\` | sed -e s:^modello-::g`

    %add_to_maven_depmap org.codehaus.modello modello-$artifactname %{namedversion} JPP/%{name} $artifactname
done

cp -p pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.modello-modello.pom
%add_to_maven_depmap org.codehaus.modello modello %{namedversion} JPP/%{name} modello

# script
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
for jar in $(find -type f -name "*.jar" | grep -E target/.*.jar); do 
        install -m 644 $jar $RPM_BUILD_ROOT%{_javadir}/%{name}/`basename $jar |sed -e s:modello-::g`
done

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{namedversion}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{namedversion}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%attr(755,root,root) %{_bindir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_1jpp6
- fixed build with new plexus-containers

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp6
- fixed build with maven3

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp6
- new jpp release

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.2.a15.5jpp6
- reverted to a15

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.a17.1jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a17.1jpp5
- rebuild with maven

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a17.1jpp5
- new version a17

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp5
- fixed build w/java5

* Fri Dec 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp1.7
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a8.6jpp1.7
- build with maven2

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a8.6jpp1.7
- converted from JPackage by jppimport script

