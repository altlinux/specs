BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2012, JPackage Project
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

%define grname  excalibur
%define usname  configuration

Name:           excalibur-configuration
Version:        1.1
Release:        alt5_3jpp6
Epoch:          0
Summary:        Excalibur Configuration Manager
License:        Apache Software License 2.0
Url:            http://excalibur.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/excalibur/excalibur-configuration/source/excalibur-configuration-1.1-src.tar.gz
Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        excalibur-configuration-1.1-jpp-depmap.xml
Source6:        excalibur-buildsystem.tar.gz
Source7:        excalibur-deprecated-project-common.xml
Source8:        excalibur-configuration-1.1-LICENSE.txt
Source9:        excalibur-configuration-1.1-NOTICE.txt
Source10:       http://mirrors.ibiblio.org/pub/mirrors/maven2/excalibur-configuration/excalibur-configuration/1.1/excalibur-configuration-1.1.pom
Patch0:         excalibur-configuration-1.1-project_xml.patch
Patch1:         excalibur-configuration-1.1-CascadingConfiguration.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  maven1 >= 0:1.1
BuildRequires:  maven1-plugins-base
BuildRequires:  maven1-plugin-license
BuildRequires:  maven1-plugin-test
BuildRequires:  maven1-plugin-xdoc
BuildRequires:  junit
BuildRequires:  saxon
BuildRequires:  saxon-scripts
BuildRequires:  excalibur-avalon-framework-api
BuildRequires:  excalibur-avalon-framework-impl
BuildRequires:  excalibur-avalon-logkit
BuildRequires:  isorelax
BuildRequires:  msv-msv
BuildRequires:  relaxngDatatype
BuildRequires:  msv-xsdlib

Requires:       excalibur-avalon-framework-api
Requires:       excalibur-avalon-framework-impl
Requires:       excalibur-avalon-logkit
Requires:       isorelax
Requires:       msv-msv
Requires:       relaxngDatatype
Requires:       msv-xsdlib
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
This project contains utilities for managing components. 
ECM is what we call an "avalon container", though it is 
somewhat different in architecture to newer developments 
like Phoenix and Fortress. Our intend is to someday 
completely replace ECM with Fortress. In particular, 
this package contains the ExcaliburComponentManager, 
usually abbreviated to ECM.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
gzip -dc %{SOURCE6} | tar xf -
mkdir components
cp %{SOURCE7} components/project.xml
cp %{SOURCE8} LICENSE.txt
cp %{SOURCE9} NOTICE.txt

%patch0 -b .sav
%patch1 -b .sav

%build
export DEPCAT=$(pwd)/excalibur-configuration-1.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > excalibur-configuration-1.1-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:/usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    jar javadoc
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Davalon.buildsystem=$(pwd)/buildsystem

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{grname}
install -m 644 \
target/%{name}-%{version}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{grname}/%{name}-%{version}.jar

# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{grname} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{grname}-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP/%{grname} %{name}

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files 
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{grname}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_3jpp6
- fixed build with java 7

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_3jpp6
- fixed build with moved maven1

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_3jpp6
- new jpp relase

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_2jpp5
- java5 target

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_2jpp5
- use maven1

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- fixed repocop warnings

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

