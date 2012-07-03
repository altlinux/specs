Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define short_name	scout

Name:		ws-scout
Version:	1.0
Release:	alt6_5jpp5
Epoch:		0
Summary:	Apache Scout Implementation of JSR 93 (JAXR)
License:	Apache Software License 2.0
Url:		http://ws.apache.org/scout/
Group:		Development/Java
Source0:	%{name}-%{version}-src.tgz
##svn export https://svn.apache.org/repos/asf/webservices/scout

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-%{version}-jpp-depmap.xml
Patch0:         ws-scout-1.0-jaxr-api-project_xml.patch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: junit
BuildRequires: maven1 >= 1.0.2
BuildRequires: maven1-plugins-base >= 1.0.2
BuildRequires: maven1-plugin-multiproject >= 1.0.2
BuildRequires: maven1-plugin-license >= 1.0.2
BuildRequires: maven1-plugin-test >= 1.0.2
BuildRequires: maven1-plugin-xdoc >= 1.0.2
BuildRequires: axis >= 0:1.2
BuildRequires: jaf
BuildRequires: jakarta-commons-discovery
BuildRequires: jakarta-commons-logging
BuildRequires: jdom
BuildRequires: juddi
BuildRequires: saxon-scripts
Requires: axis >= 0:1.2
Requires: jaf
Requires: jakarta-commons-discovery
Requires: jakarta-commons-logging
Requires: jdom
Requires: juddi
BuildArch:	noarch

%description
Apache Scout is an implementation of the 
JSR 93 (JAXR). 

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
# remove all binary libs
for f in $(find . -name "*.jar"); do
    mv $f $f.no
done
# These tests need a running juddi server instance
rm modules/scout/src/test/org/apache/ws/scout/registry/publish/PublishConceptTest.java
rm modules/scout/src/test/org/apache/ws/scout/registry/query/JAXRQueryTest.java
# for checkstyle
cp LICENSE.TXT modules/jaxr-api/LICENSE.txt

# Remove log4j.properties file. It is not needed by scout directly, and may 
# cause conflicts/problems with other applications.
rm -f modules/scout/src/conf/log4j.properties

%patch0

%build
export DEPCAT=$(pwd)/ws-scout-1.0-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > ws-scout-1.0-depmap.new.xml
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

export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository
pushd modules/jaxr-api
maven -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository javadoc:generate
popd
pushd modules/scout
maven -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository javadoc:generate
popd

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 modules/jaxr-api/target/jaxr-api-1.0-SNAPSHOT.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}/jaxr-api-%{version}.jar
install -m 644 modules/scout/target/scout-1.0-SNAPSHOT.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar

# create unprefixed and unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name}
ln -sf %{name}-%{version}.jar %{short_name}-%{version}.jar
for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done
)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jaxr-api
cp -pr modules/jaxr-api/target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/jaxr-api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/scout
cp -pr modules/scout/target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/scout
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.TXT $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE.TXT
%{_javadir}/%{name}/*.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6_5jpp5
- fixed build with java 7

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_5jpp5
- fixed build with moved maven1

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_5jpp5
- java5 target

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp5
- use maven1

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp5
- converted from JPackage by jppimport script

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp1.7
- converted from JPackage by jppimport script

