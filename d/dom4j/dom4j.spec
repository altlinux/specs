Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2007, JPackage Project
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

Name:           dom4j
Version:        2.0.0
Release:        alt1_2jpp8
Epoch:          0
Summary:        Open Source XML framework for Java
License:        BSD
URL:            https://dom4j.github.io/
BuildArch:      noarch

Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/%{name}/%{name}/%{version}/%{name}-%{version}.pom

Obsoletes:      %{name}-demo < 2.0.0
Obsoletes:      %{name}-manual < 2.0.0

BuildRequires:  maven-local
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(net.java.dev.msv:xsdlib)
BuildRequires:  mvn(xpp3:xpp3)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)

# Test deps
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xalan:xalan)
Source44: import.info

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM and SAX and is seamlessly integrated with full XPath support.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q

%mvn_alias org.%{name}:%{name} %{name}:%{name}
%mvn_file : %{name}/%{name} %{name}

cp %{SOURCE1} pom.xml

# optional deps missing from pom
%pom_add_dep javax.xml.stream:stax-api::provided
%pom_add_dep net.java.dev.msv:xsdlib::provided
%pom_add_dep xpp3:xpp3::provided
%pom_add_dep javax.xml.bind:jaxb-api::provided

# Remove support for ancient xpp2 (deprecated and not developed since 2003)
rm -r src/main/java/org/dom4j/xpp
rm src/main/java/org/dom4j/io/XPPReader.java

# non-deterministic test
rm src/test/java/org/dom4j/util/PerThreadSingletonTest.java

%build
export LANG=en_US.ISO8859-1
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt6_28jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt6_27jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt6_26jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt6_25jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt4_13jpp7
- update

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt4_13jpp6
- switched to jpp due to repolib and fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_7jpp7
- fc version

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_13jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_10jpp5
- use default jpp profile

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_8jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_8jpp5
- converted from JPackage by jppimport script

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.6-alt1
- Initial release for ALT Linux Sisyphus

