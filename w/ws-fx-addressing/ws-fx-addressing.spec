Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define short_name	addressing


Name:		ws-fx-addressing
Version:	1.0
Release:	alt4_3jpp5
Epoch:		0
Summary:	WS-Addressing on top of Axis
License:	Apache Software License 2.0
Url:		http://ws.apache.org/ws-fx/addressing/
Group:		Development/Java
Source0:	ws-fx-addressing-1.0-src.tar.gz
##cvs -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic login
##cvs -z3 -d :pserver:anoncvs@cvs.apache.org:/home/cvspublic export -r HEAD ws-fx/addressing/

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        ws-fx-addressing-1.0-jpp-depmap.xml
Source5:        addressing-1.0.pom
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: axis >= 0:1.4
BuildRequires: wsdl4j >= 0:1.5
BuildRequires: jakarta-commons-discovery
BuildRequires: jakarta-commons-logging
Requires: axis >= 0:1.4
Requires: wsdl4j >= 0:1.5
Requires: jakarta-commons-discovery
Requires: jakarta-commons-logging
BuildArch:	noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
Apache Addressing is an implementation of the Web 
Services Addressing (WS-Addressing), published by the 
IBM, Microsoft and BEA as a joint specification, on 
top of Apache Axis (The Next Generation SOAP).

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}
# remove all binary libs
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done

%build
export DEPCAT=$(pwd)/ws-fx-addressing-1.0-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > ws-fx-addressing-1.0-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

for p in $(find . -name project.properties); do
    echo >> $p
    echo maven.repo.remote=file:/usr/share/maven1/repository >> $p
    echo maven.home.local=$(pwd)/.maven >> $p
done

mkdir -p .maven/repository/JPP/jars
build-jar-repository .maven/repository/JPP/jars \
axis/axis \
axis/axis-ant \
axis/jaxrpc \
axis/saaj \
wsdl4j \
junit \
commons-discovery \
commons-logging \

export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.5 -Dmaven.compile.source=1.5 -Dmaven.javadoc.source=1.5  \
	-Dmaven.repo.remote=file:/usr/share/maven1/repository \
	-Dmaven.home.local=$MAVEN_HOME_LOCAL \
	jar javadoc:generate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{short_name}-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir} 
ln -sf %{name}-%{version}.jar %{short_name}-%{version}.jar
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)
%add_to_maven_depmap org.apache.ws addressing %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_3jpp5
- fixed build with java 7

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_3jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_3jpp5
- use maven1

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- fixed repocop warnings

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

