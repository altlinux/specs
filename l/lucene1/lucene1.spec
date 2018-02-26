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

%define oname           lucene

Name:           lucene1
Version:        1.9.1
Release:        alt2_3jpp5
Epoch:          0
Summary:        High-performance, full-featured text search engine
License:        ASL 2.0
URL:            http://lucene.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/lucene/java/lucene-1.9.1-src.tar.gz
Patch0:		lucene-1.9-common-build_xml.patch
Patch1:		lucene-1.9-contrib-db-bdb-build_xml.patch
Patch2:		lucene-1.9-contrib-db-bdb-je-build_xml.patch
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: berkeleydb
BuildRequires: berkeleydb-native >= 0:4.3.29
BuildRequires: junit
BuildRequires: javacc
BuildRequires: java-javadoc
BuildRequires: jline
BuildRequires: jtidy
BuildRequires: regexp
BuildArch:      noarch

%description
Jakarta Lucene is a high-performance, full-featured text search engine
written entirely in Java. It is a technology suitable for nearly any
application that requires full-text search, especially cross-platform.

%package javadoc
Summary:        Javadoc for Lucene
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Lucene demonstration library
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
%{summary}.

%package contrib
Summary:        Lucene contributed extensions
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description contrib
%{summary}.

%package contrib-db
Summary:        Lucene contributed bdb extensions
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: berkeleydb
Requires: berkeleydb-native >= 0:4.3.29

%description contrib-db
%{summary}.


%prep
%setup -q -n %{oname}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav

%build
mkdir -p docs
mkdir -p lib
export OPT_JAR_LIST="ant/ant-junit junit jaxp_transform_impl ant/ant-trax xalan-j2-serializer"
export CLASSPATH=$(build-classpath jline jtidy regexp)
pushd contrib/db/bdb/lib
ln -sf $(build-classpath berkeleydb-native) .
popd
pushd contrib/db/bdb-je/lib
ln -sf $(build-classpath berkeleydb) .
popd
ant -Dbuild.sysclasspath=first \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=%{_javadocdir}/java \
  package test generate-test-reports


%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 0644 build/%{oname}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 0644 build/%{oname}-demos-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-demos-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# contrib jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib
for c in analyzers ant highlighter lucli memory misc queries similarity snowball spellchecker surround swing wordnet xml-query-parser; do
    install -m 0644 build/contrib/$c/%{oname}-${c}-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}-contrib
done
(cd $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# bdb contrib jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib-db
install -m 0644 build/contrib/db/bdb/%{oname}-bdb-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}-contrib-db
install -m 0644 build/contrib/db/bdb-je/%{oname}-bdb-je-%{version}.jar \
		$RPM_BUILD_ROOT%{_javadir}/%{name}-contrib-db
(cd $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib-db && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/api/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# webapp
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -m 0644 build/%{oname}web.war \
  $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/%{oname}web.war

%files
%doc CHANGES.txt LICENSE.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files contrib
%{_javadir}/%{name}-contrib

%files contrib-db
%{_javadir}/%{name}-contrib-db

%files demo
%{_javadir}/%{name}-demos-%{version}.jar
%{_javadir}/%{name}-demos.jar

%changelog
* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt2_3jpp5
- fixed dep on lucene2

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1.5_1jpp5
- rebuild with osgi provides

* Wed Jan 16 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1.5_1jpp1.7
- import from fc8

* Tue Nov 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt4jvm4.2
- enabled check, disabled devel, added contrib (required for eclipse >= 3.3)

* Mon Nov 05 2007 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt3jvm4.2
- NMU: added -devel subpackage

* Tue Jul 17 2007 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2
- NMU: partial jpackage compatibility added
- enabled demo (required for eclipse).
- demo is packaged according to jpackage.
- added source=1.4 and target=1.4

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.1.0-alt1
- Update to 2.1.0 release

* Thu Nov 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.0.0-alt1
- Update to 2.0.0 release

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.9.1-alt1
- Updated to 1.9.1
- Disabled tests (fail to build for some bogus reason)
- Disabled demo by default

* Wed Dec 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.3-alt1
- Updated to 1.4.3
- Spec cleanup for rpm-build-java

* Tue Jun 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.3-alt1
- New upstream release
- Disable debug for non-debug builds

* Tue Sep 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.2-alt1
- Released for ALT Linux
