%define _unpackaged_files_terminate_build 1

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

%define source_version %(echo %version | tr . -)
%define major_version %(echo %version | cut -d. -f1)
%define minor_version %(echo %version | cut -d. -f2)

Name: saxon
Version: 13.1
Release: alt1

Summary: Java XPath, XSLT and XQuery implementation
License: MPL-2.0
Group: Text tools
URL: https://www.saxonica.com/
VCS: https://github.com/Saxonica/Saxon-HE.git

BuildArch: noarch

Source0: %name-%source_version.tar
Source1: saxon.pom
Source3: %name.saxon.script
Source4: %name.saxonq.script
Source5: %name.1
Source6: %{name}q.1
Source8: saxon-NOTICE-jamesclark.txt
Source9: qt3tests-201a6e466940cdfc727f4babfedcde5332b9f578.tar.gz
Source10: saxon-qt3-exceptions.xml
Patch0: saxon-axiom2.patch
Patch1: saxon-errors.patch
Patch2: saxon-offline-qt3.patch
Patch3: saxon-qt3-repairs.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: javapackages-local
BuildRequires: unzip
BuildRequires: jline2
BuildRequires: xmlresolver
BuildRequires: xom
BuildRequires: dom4j
BuildRequires: jdom2
BuildRequires: mvn(org.apache.ws.commons.axiom:axiom-api)
BuildRequires: mvn(org.apache.ws.commons.axiom:axiom-impl)

Provides: saxon-scripts = %EVR
Obsoletes: saxon-scripts < %EVR

%description
Saxon-HE is Saxonica's open-source implementation of XPath, XSLT and XQuery.
It provides the Saxon Java processor and its command-line interfaces.

%package javadoc
Group: Development/Java
Summary: API documentation for %name

%description javadoc
API documentation for Saxon-HE.

%package manual
Group: Text tools
Summary: Reference manual for %name

%description manual
Upstream reference documentation for Saxon-HE.

%prep
%setup -q -n %name-%source_version
unzip -q source/saxon%{source_version}source.zip
mkdir qt3tests
tar -xf %SOURCE9 --strip-components=1 -C qt3tests
unzip -q resources/saxon-resources-%major_version.zip -d manual
unzip -q manual/source-userdoc.zip -d manual/userdoc
%autopatch -p1
grep -q "MAJOR_VERSION = %major_version;" net/sf/saxon/Version.java
grep -q "MINOR_VERSION = %minor_version;" net/sf/saxon/Version.java
cp -p %SOURCE1 Saxon-HE.pom
cp -p manual/notices/LICENSE.txt LICENSE.txt
cp -p manual/notices/JLINE2.txt NOTICE-jline2.txt
cp -p %SOURCE8 NOTICE-jamesclark.txt

%build
mkdir -p build/classes build/lib build/api
cat > build/classes/edition.properties <<EOF
config=net.sf.saxon.Configuration
platform=net.sf.saxon.java.JavaPlatform
EOF
find net -name '*.java' -print > build/sources.list
classpath=$(build-classpath jline2 xmlresolver xom dom4j jdom2 \
  ws-axiom/axiom-api ws-axiom/axiom-impl)
javac --release 17 -encoding UTF-8 -classpath "$classpath" \
  -d build/classes @build/sources.list
cp -a net/sf/saxon/data build/classes/net/sf/saxon/
mkdir -p build/classes/META-INF/services
printf '%%s\n' net.sf.saxon.TransformerFactoryImpl \
  > build/classes/META-INF/services/javax.xml.transform.TransformerFactory
printf '%%s\n' net.sf.saxon.xpath.XPathFactoryImpl \
  > build/classes/META-INF/services/javax.xml.xpath.XPathFactory
cat > build/manifest.mf <<EOF
Manifest-Version: 1.0
Main-Class: net.sf.saxon.Transform
Automatic-Module-Name: net.sf.saxon
EOF
jar --create --file build/lib/Saxon-HE.jar --manifest build/manifest.mf \
  -C build/classes .
# The upstream test classifier is a reusable QT3/XSLT test-driver tool.
mkdir -p build/test-classes
find manual/drivers/java/net -name '*.java' -print > build/test-sources.list
javac --release 17 -encoding UTF-8 \
  -classpath "build/lib/Saxon-HE.jar:$classpath" \
  -d build/test-classes @build/test-sources.list
jar --create --file build/lib/Saxon-HE-test.jar -C build/test-classes .
cat build/sources.list build/test-sources.list > build/api-sources.list
javadoc -quiet -Xdoclint:none -encoding UTF-8 -classpath "$classpath" \
  -d build/api @build/api-sources.list
%mvn_artifact %SOURCE1 build/lib/Saxon-HE.jar
%mvn_artifact net.sf.saxon:Saxon-HE:jar:test:%version \
  build/lib/Saxon-HE-test.jar

%install
# Override XMvn's default exclusion of auxiliary classifiers.
%mvn_package net.sf.saxon:Saxon-HE:jar:test:
%mvn_install
ln -s saxon/Saxon-HE.jar %buildroot%_javadir/saxon.jar
mkdir -p %buildroot%_javadocdir/%name
cp -a build/api/. %buildroot%_javadocdir/%name/
install -d %buildroot%_bindir %buildroot%_mandir/man1
install -p -m755 %SOURCE3 %buildroot%_bindir/saxon
install -p -m755 %SOURCE4 %buildroot%_bindir/saxonq
install -p -m644 %SOURCE5 %buildroot%_mandir/man1/saxon.1
install -p -m644 %SOURCE6 %buildroot%_mandir/man1/saxonq.1

mkdir -p %buildroot%_docdir/%name-manual
cp -a manual/userdoc/viewer_appJS/. %buildroot%_docdir/%name-manual/

%check
# Use the source-built upstream driver classifier, also installed in the RPM.
mkdir -p build/qt3
cp -p %SOURCE10 build/qt3/saxon-qt3-exceptions.xml
classpath="build/lib/Saxon-HE.jar:$(build-classpath xmlresolver)"
java -Dsaxon.test.offline=true \
  -classpath "build/lib/Saxon-HE-test.jar:$classpath" \
  net.sf.saxon.testdriver.QT3TestDriverHE qt3tests catalog.xml \
  -o:build/qt3 -reportfilename:qt3-results.xml -lang:XQ31 \
  -exceptions:saxon-qt3-exceptions.xml -quiet \
  > build/qt3.log 2>&1
# The upstream driver exits zero even for assertion failures.
grep -Eq '^Result: [1-9][0-9]* successes, 0 failures, 0 incorrect ErrorCode,' \
  build/qt3.log
! grep -Eq 'result="(fail|wrongError)"' build/qt3/qt3-results.xml

%files -f .mfiles
%doc LICENSE.txt NOTICE-jline2.txt NOTICE-jamesclark.txt
%_javadir/saxon.jar
%_bindir/saxon
%_bindir/saxonq
%_mandir/man1/saxon.1*
%_mandir/man1/saxonq.1*

%files javadoc
%_javadocdir/%name

%files manual
%_docdir/%name-manual

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 13.1-alt1
- New version.

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:9.4.0.9-alt2_10jpp11
- java11 build

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 0:9.4.0.9-alt2_10jpp8
- use jvm_run

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:9.4.0.9-alt1_10jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:9.4.0.9-alt1_9jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:9.4.0.9-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:9.4.0.9-alt1_6jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:9.4.0.9-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.4.0.9-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt3_16jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_16jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_8jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:9.3.0.4-alt1_5jpp7
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_3jpp6
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.5.5-alt1_1jpp5
- converted from JPackage by jppimport script

* Thu Jul 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt2_5jpp1.7
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:6.5.3-alt1_5jpp1.7
- converted from JPackage by jppimport script

