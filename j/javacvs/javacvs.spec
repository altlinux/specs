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


Name:           javacvs
Version:        5.0
Release:        alt1_5jpp6
Epoch:          0
Summary:        Netbeans CVS module and library

Group:          Development/Java
License:        Sun Public License
URL:            http://javacvs.netbeans.org/

BuildArch:      noarch

Source0:        %{name}-%{version}.tar.gz
# cvs -d :pserver:anoncvs@cvs.netbeans.org:/cvs login
# cvs -d :pserver:anoncvs@cvs.netbeans.org:/cvs export -r release50-BLD200601252030 javacvs
Source1:        http://repo1.maven.org/maven2/org/netbeans/lib/cvsclient/20060125/cvsclient-20060125.pom
Source2:        javacvs-projectized.xml
# curl -o javacvs-projectized.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/templates/projectized.xml?content-type=text%2Fplain&rev=1.61'
Source3:        javacvs-default.xml
# curl -o javacvs-default.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/default.xml?content-type=text%2Fplain&rev=1.19'
Source4:        javacvs-default-properties.xml
# curl -o javacvs-default-properties.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/default-properties.xml?content-type=text%2Fplain&rev=1.10'
Source5:        javacvs-common.xml
# curl -o javacvs-common.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/templates/common.xml?content-type=text%2Fplain&rev=1.27.4.1'
Source6:        javacvs-javadoctools-template.xml
# curl -o javacvs-javadoctools-template.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/template.xml?content-type=text%2Fplain&rev=1.59'
Source7:        javacvs-javadoctools-properties.xml
# curl -o javacvs-javadoctools-properties.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/properties.xml?content-type=text%2Fplain&rev=1.16'
Source8:        javacvs-javadoctools-links.xml
# curl -o javacvs-javadoctools-links.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/links.xml?content-type=text%2Fplain&rev=1.16'
Source9:        javacvs-javadoctools-replaces.xml
# curl -o javacvs-javadoctools-replaces.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/replaces.xml?content-type=text%2Fplain&rev=1.17'
Source10:        javacvs-javadoctools-disallowed-links.xml
# curl -o javacvs-javadoctools-disallowed-links.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/disallowed-links.xml?content-type=text%2Fplain&rev=1.4'
Source11:        javacvs-javadoctools-apichanges-empty.xml
# curl -o javacvs-javadoctools-apichanges-empty.xml 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/apichanges-empty.xml?content-type=text%2Fplain&rev=1.1'
Source12:        javacvs-javadoctools-apichanges.xsl
# curl -o javacvs-javadoctools-apichanges.xsl 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/apichanges.xsl?content-type=text%2Fplain&rev=1.8'
Source13:        javacvs-javadoctools-javadoc.css
# curl -o javacvs-javadoctools-javadoc.css 'http://nbbuild.netbeans.org/source/browse/*checkout*/nbbuild/javadoctools/javadoc.css?content-type=text%2Fplain&rev=1.4'

Patch0:         %{name}-libmodule-build.patch

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4
Source44: import.info

%description
The module provides UI frontend to the CVS in the Netbeans 
IDE. Just now there is work in progress addressing project 
and typical workflow integration. 
Supported commands are: commit, update, add, remove, tag, 
checkout, import, history, diff, status, log, annotate. 
The library implements a CVS client protocol in Java. It 
allows to access CVS servers without setting up an external 
cvs program. It's base for the module. 

%package        lib
Summary:        Netbeans %{name} library
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description    lib
%{summary}.

%package        lib-javadoc
Summary:        Javadoc for %{name} lib
Group:          Development/Documentation

%description    lib-javadoc
%{summary}.


%prep
%setup -q -n %{name}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav
mkdir -p libs/external
mkdir -p nbbuild/dummy
mkdir -p nbbuild/javadoctools
mkdir -p nbbuild/netbeans/
mkdir -p nbbuild/templates/
cp %{SOURCE2} nbbuild/templates/projectized.xml
cp %{SOURCE3} nbbuild/default.xml
cp %{SOURCE4} nbbuild/default-properties.xml
cp %{SOURCE5} nbbuild/templates/common.xml
cp %{SOURCE6} nbbuild/javadoctools/template.xml
cp %{SOURCE7} nbbuild/javadoctools/properties.xml
cp %{SOURCE8} nbbuild/javadoctools/links.xml
cp %{SOURCE9} nbbuild/javadoctools/replaces.xml
cp %{SOURCE10} nbbuild/javadoctools/disallowed-links.xml
cp %{SOURCE11} nbbuild/javadoctools/apichanges-empty.xml
cp %{SOURCE12} nbbuild/javadoctools/apichanges.xsl
cp %{SOURCE13} nbbuild/javadoctools/javadoc.css

%build
cd libmodule
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dcluster=netbeans -Dcode.name.base.dashes=cvsclient jar javadoc

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -pm 644 libmodule/netbeans/modules/cvsclient.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cvslib-%{version}.jar
ln -s cvslib-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cvslib.jar
ln -s cvslib-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/cvsclient.jar
%add_to_maven_depmap org.netbeans lib %{version} JPP/%{name} cvslib
%add_to_maven_depmap org.netbeans.lib cvsclient %{version} JPP/%{name} cvsclient

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cvslib.pom
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cvsclient.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lib
cp -pr nbbuild/build/javadoc/cvsclient/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-lib

%files
%dir %{_javadir}/%{name}

%files lib
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}

%files lib-javadoc
%doc %{_javadocdir}/%{name}-lib


%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_5jpp6
- jpp6 update

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_1jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_2jpp1.7
- updated to new jpackage release

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp1.7
- converted from JPackage by jppimport script

