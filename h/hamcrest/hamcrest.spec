Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

Name:           hamcrest
Version:        1.3
Release:        alt3_25jpp8
Epoch:          0
Summary:        Library of matchers for building test expressions
License:        BSD
URL:            https://github.com/hamcrest/JavaHamcrest
Source0:        https://github.com/hamcrest/JavaHamcrest/archive/hamcrest-java-%{version}.tar.gz

Source8:        hamcrest-core-MANIFEST.MF
Source9:        hamcrest-library-MANIFEST.MF
Source11:       hamcrest-integration-MANIFEST.MF
Source12:       hamcrest-generator-MANIFEST.MF

Patch0:         %{name}-%{version}-build.patch
Patch1:         %{name}-%{version}-no-jarjar.patch
Patch3:         %{name}-%{version}-javadoc.patch
Patch4:         %{name}-%{version}-qdox-2.0.patch
Patch5:         %{name}-%{version}-fork-javac.patch

Requires:       qdox
Requires:       easymock >= 3.0
Requires:       %{name}-core = %{epoch}:%{version}-%{release}

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  easymock
BuildRequires:  junit
BuildRequires:  qdox
BuildRequires:  testng

BuildArch:      noarch
Source44: import.info

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.

%package core
Group: Development/Java
Summary:        Core API of hamcrest matcher framework.
Obsoletes:      %{name} < 0:1.3-10

%description core
The core API of hamcrest matcher framework to be used by third-party framework providers. 
This includes the a foundation set of matcher implementations for common operations. 

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
Requires:       junit
Requires:       testng

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n JavaHamcrest-%{name}-java-%{version}

find . -type f -name "*.jar" | xargs -t rm
rm -fr hamcrest-integration/src/main/java/org/hamcrest/integration/JMock1Adapter.java
rm -fr hamcrest-integration/src/main/java/org/hamcrest/JMock1Matchers.java
rm -fr hamcrest-unit-test/src/main/java/org/hamcrest/integration/JMock1AdapterTest.java
# BUILD/hamcrest-1.1/lib/generator/qdox-1.6.1.jar.no
ln -sf $(build-classpath qdox) lib/generator/
# BUILD/hamcrest-1.1/lib/integration/easymock-2.2.jar.no
ln -sf $(build-classpath easymock3) lib/integration/
# BUILD/hamcrest-1.1/lib/integration/jmock-1.10RC1.jar.no
ln -sf $(build-classpath jmock) lib/integration/
# BUILD/hamcrest-1.1/lib/integration/testng-4.6-jdk15.jar.no
ln -sf $(build-classpath testng-jdk15) lib/integration/

%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i 's/\r//' LICENSE.txt

%build
export CLASSPATH=$(build-classpath qdox)
export OPT_JAR_LIST="junit ant/ant-junit"
# The unit-test goal is switched off as some tests fail with JDK 7
# see https://github.com/hamcrest/JavaHamcrest/issues/30
ant -Dant.build.javac.source=1.5 -Dversion=%{version} -Dbuild.sysclasspath=last clean core generator library bigjar javadoc

# inject OSGi manifests
jar ufm build/%{name}-core-%{version}.jar %{SOURCE8}
jar ufm build/%{name}-library-%{version}.jar %{SOURCE9}
jar ufm build/%{name}-integration-%{version}.jar %{SOURCE11}
jar ufm build/%{name}-generator-%{version}.jar %{SOURCE12}

%install
sed -i 's/@VERSION@/%{version}/g' pom/*.pom

%mvn_artifact pom/hamcrest-parent.pom

for mod in all core generator library integration; do
    %mvn_artifact pom/hamcrest-$mod.pom build/%{name}-$mod-%{version}.jar
done

%mvn_package :hamcrest-parent core
%mvn_package :hamcrest-core core

%mvn_file ':hamcrest-{*}' %{name}/@1

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr %{name}-examples $RPM_BUILD_ROOT%{_datadir}/%{name}/

%mvn_install -J build/temp/hamcrest-all-1.3-javadoc.jar.contents/

%files -f .mfiles

%files core -f .mfiles-core
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%files demo
%{_datadir}/%{name}

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_25jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_23jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_22jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_18jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_14jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_13jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_5jpp7
- new release

* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp7
- new version

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_21jpp7
- source and target to 1.5

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_21jpp7
- fix for arm

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_21jpp7
- fc update

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_19jpp7
- java6 build for jmock2

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_19jpp7
- fc release

* Tue Oct 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_9.2jpp6
- added OSGi manifest for eclipse

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp5
- rebuild to fix jmock2

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

