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

Name:           docbook-xml
Version:        4.4
Release:	alt2_2jpp5
Epoch:          0
Summary:        DocBook XML DTDs as Jar
License:        Distributable
Url:            http://docbook.sourceforge.net/
Group:          Development/Java
Source0:        docbook-xml-4.4.tar.gz
# # steps to reproduce
# svn export http://docbook.svn.sourceforge.net/svnroot/docbook/tags/V44/docbook/xml/ docbook-xml-4.4
# pushd docbook-xml-4.4/ent/
# for e in $(curl -s -l 'http://www.w3.org/2003/entities/2007/' | cut -d\" -f 12 | grep ent$); do curl -s -O http://www.w3.org/2003/entities/2007/$e; done
# popd
# tar cf docbook-xml-4.4.tar docbook-xml-4.4/
# gzip docbook-xml-4.4.tar

Source1:        http://repo1.maven.org/maven2/org/docbook/docbook-xml/4.4/docbook-xml-4.4.pom

BuildRequires: jpackage-utils >= 0:1.7.4
Buildarch:     noarch

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
XML document type definitions for DocBook.

%prep
%setup -q 

%build
rm README Makefile
jar cf %{name}-%{version}.jar *

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.docbook %{name} %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done
)


%files
%{_javadir}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_1jpp5
- converted from JPackage by jppimport script

