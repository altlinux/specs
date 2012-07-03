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


Name:		omquery
Version:	0.92.3
Release:	alt2_3jpp5
Epoch:          0
Summary:	XPath interface for XT
License:	BSD style
Group:		Development/Java
URL:		http://www.geocities.com/takuki_kamiya/pub/XPath4XT.html
Source:		%{name}.zip
Source1:        %{name}.build.script
Requires: xt-dash
BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: xt-dash
BuildArch:	noarch

%description
XPath interface for XT provides for DOM query API facifities on top of XT.
It is implemented in Java language and complies with W3C's XPath Proposed
Recommendation as is currently implemented in XT.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n omquery
find . -name "*.jar" | xargs -t rm
cp -a %{SOURCE1} build.xml
perl -pi -e 's/\r$//g' README.txt copying.txt

%build
export CLASSPATH=$(build-classpath xt-dash)
export OPT_JAR_LIST=:
ant jar
ant javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc README.txt copying.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.92.3-alt2_3jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.92.3-alt1_3jpp5
- converted from JPackage by jppimport script

