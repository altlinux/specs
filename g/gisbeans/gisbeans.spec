Packager: Igor Vlasenko <viy@altlinux.ru>
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

Name:           gisbeans
Version:        1.0.0
Release:        alt1_1jpp6
Summary:        GisBeans

Group:          Development/Java
License:        GPL
URL:            http://gisbeans.sourceforge.net

Source0:        gisbeans-1.0.0.tgz
#cvs -d:pserver:anonymous@gisbeans.cvs.sourceforge.net:/cvsroot/gisbeans login 
#cvs -z3 -d:pserver:anonymous@gisbeans.cvs.sourceforge.net:/cvsroot/gisbeans export -r version_1_0_0 -d gisbeans-1.0.0 gisbeans
#tar czf gisbeans-1.0.0.tgz gisbeans-1.0.0/

BuildRequires: ant >= 1.6.5
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: dsol-basic
BuildRequires: jdom

Requires: jpackage-utils >= 0:5.0.0
Requires: dsol-basic
Requires: jdom

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
GisBeans is an OpenSource (GPL) development environment for
building spatially enabled Internet applications. The
software builds upon Mapserver, JAI, IText, MSV and others.
Gisbeans runs both as standalone, as Enterprise Java Bean,
and as Applet.

%package javadoc 
Summary:        Javadocs for %{name} 
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description javadoc 
%{summary}. 

%prep
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
export CLASSPATH=$(build-classpath dsol/language jdom)
%ant -Dbuild.sysclasspath=first jar javadoc

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# javadoc 
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__cp -a docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%files
%{_javadir}/*.jar

%files javadoc 
%{_javadocdir}/%{name}-%{version} 
%{_javadocdir}/%{name} 

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp6
- new version

