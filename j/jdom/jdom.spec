Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

Name:           jdom
Version:        1.1.3
Release:        alt3_14jpp8
Epoch:          0
Summary:        Java alternative to DOM and SAX
License:        ASL 1.1
URL:            http://www.jdom.org/
Source0:        http://jdom.org/dist/binary/archive/jdom-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/org/jdom/jdom/%{version}/jdom-%{version}.pom
Patch0:         %{name}-crosslink.patch
Patch1:         %{name}-1.1-OSGiManifest.patch

BuildRequires:  ant
BuildRequires:  javapackages-local

BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(xerces:xercesImpl)

BuildArch:      noarch
Source44: import.info

%description
JDOM is, quite simply, a Java representation of an XML document. JDOM
provides a way to represent that document for easy and efficient
reading, manipulation, and writing. It has a straightforward API, is a
lightweight and fast, and is optimized for the Java programmer. It's an
alternative to DOM and SAX, although it integrates well with both DOM
and SAX.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Group: Development/Other
Summary:        Demos for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.


%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%build
export CLASSPATH=$(build-classpath xerces-j2 jaxen)
ant -Dj2se.apidoc=%{_javadocdir}/java package javadoc-link

%install
%mvn_file : %{name}
%mvn_alias : jdom:jdom
%mvn_artifact %{SOURCE1} build/%{name}-*-snap.jar
%mvn_install -J build/apidocs

# demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr samples $RPM_BUILD_ROOT%{_datadir}/%{name}

%files -f .mfiles
%doc LICENSE.txt
%doc CHANGES.txt COMMITTERS.txt README.txt TODO.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files demo
%{_datadir}/%{name}
%doc LICENSE.txt

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_14jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_10jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_9jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_5jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_4jpp7
- update

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_3jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_2jpp7
- new version

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_2jpp6
- added jdom:jdom jppmap

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_2jpp6
- added osgi manifest

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new jpp release

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5.5jpp5
- added OSGi manifest for eclipse

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp1.7
- converted from JPackage by jppimport script

* Thu Apr 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux Sisyphus

