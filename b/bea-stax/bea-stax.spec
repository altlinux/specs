BuildRequires: javapackages-local
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

%global mainver 1.2.0
%global apiver  1.0.1

Summary:        Streaming API for XML
URL:            http://stax.codehaus.org/Home
Source0:        http://dist.codehaus.org/stax/distributions/stax-src-1.2.0.zip
Source1:        http://dist.codehaus.org/stax/jars/stax-1.2.0.pom
Source2:        http://dist.codehaus.org/stax/jars/stax-api-1.0.1.pom
Name:           bea-stax
Version:        %{mainver}
Release:        alt4_13jpp8
License:        ASL 1.1 and ASL 2.0
Group:          Development/Java
BuildArch:      noarch

BuildRequires:          jpackage-utils
BuildRequires:          ant
BuildRequires:          xerces-j2 xalan-j2
BuildRequires:          java-devel
Requires:               jpackage-utils
Source44: import.info
Obsoletes: stax-bea <= 1.0-alt1

%description
The Streaming API for XML (StAX) is a groundbreaking
new Java API for parsing and writing XML easily and
efficiently.

%package api
Summary:        The StAX API
Group:          Development/Documentation
Requires:       jpackage-utils

%description api
%{summary}

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}

%prep
%setup -q -c -n %{name}-%{version}

# Convert CR+LF to LF
%{__sed} -i 's/\r//' ASF2.0.txt

%build
export CLASSPATH=`pwd`/build/stax-api-%{apiver}.jar
ant all javadoc

%install
# jar
install -Dpm 0644 build/stax-api-%{apiver}.jar %{buildroot}%{_javadir}/%{name}-api.jar
install -Dpm 0644 build/stax-%{version}-dev.jar %{buildroot}%{_javadir}/%{name}.jar
# the following symlink can be removed once no package needs "bea-stax-ri"
ln -s %{name}.jar %{buildroot}%{_javadir}/%{name}-ri.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# pom
install -Dpm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dpm 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}-api.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap -f api -a "javax.xml.stream:stax-api" JPP-%{name}-api.pom %{name}-api.jar

%files -f .mfiles
%doc ASF2.0.txt
%{_javadir}/%{name}-ri.jar

%files api -f .mfiles-api
%doc ASF2.0.txt

%files javadoc
%doc ASF2.0.txt
%doc %{_javadocdir}/*

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt4_13jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_4jpp7
- fc version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_0.rc1.4jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_0.rc1.3jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_0.rc1.3jpp5
- converted from JPackage by jppimport script

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_0.rc1.2jpp1.7
- converted from JPackage by jppimport script

