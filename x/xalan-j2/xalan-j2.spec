Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

%global cvs_version 2_7_1

Name:           xalan-j2
Version:        2.7.1
Release:        alt4_33jpp8
Epoch:          0
Summary:        Java XSLT processor
# src/org/apache/xpath/domapi/XPathStylesheetDOM3Exception.java is W3C
License:        ASL 2.0 and W3C
URL:            http://xalan.apache.org/
Source0:        http://archive.apache.org/dist/xml/xalan-j/xalan-j_2_7_1-src.tar.gz
Source1:        %{name}-serializer-MANIFEST.MF
Source2:        http://repo1.maven.org/maven2/xalan/xalan/2.7.1/xalan-2.7.1.pom
Source3:        http://repo1.maven.org/maven2/xalan/serializer/2.7.1/serializer-2.7.1.pom
Source4:        xsltc-%{version}.pom
Source5:        %{name}-MANIFEST.MF

Patch0:         %{name}-noxsltcdeps.patch
# Fix CVE-2014-0107: insufficient constraints in secure processing
# feature (oCERT-2014-002).  Generated form upstream revisions 1581058
# and 1581426.
Patch2:         %{name}-CVE-2014-0107.patch

BuildArch:      noarch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  apache-parent
BuildRequires:  bcel
BuildRequires:  java_cup
BuildRequires:  regexp
BuildRequires:  sed
BuildRequires:  glassfish-servlet-api
BuildRequires:  xerces-j2 >= 0:2.7.1
BuildRequires:  xml-commons-apis >= 0:1.3
BuildRequires:  xml-stylebook

Requires:       xerces-j2

Provides:       jaxp_transform_impl
Source44: import.info
BuildRequires: dos2unix
Provides: xalan-j = %{name}-%{version}
Obsoletes: xalan-j <= 2.7.0-alt3

%description
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C Recommendations
for XSL Transformations (XSLT) and the XML Path Language (XPath). It can
be used from the command line, in an applet or a servlet, or as a module
in other program.

%package        xsltc
Group: Development/Java
Summary:        XSLT compiler
Requires:       java_cup
Requires:       bcel
Requires:       regexp
Requires:       xerces-j2

%description    xsltc
The XSLT Compiler is a Java-based tool for compiling XSLT stylesheets into
lightweight and portable Java byte codes called translets.

%package        manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description    manual
Documentation for %{name}.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Group: Development/Java
Summary:        Demo for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       glassfish-servlet-api

%description    demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n xalan-j_%{cvs_version}
%patch0 -p0
%patch2 -p1

find . -name '*.jar' -delete
find . -name '*.class' -delete

# this tar.gz contains bundled software, some of which has unclear
# licensing terms (W3C Software/Document license) . We could probably
# replicate this with our jars but it's too much work so just generate
# non-interlinked documentation
rm src/*tar.gz
sed -i '/<!-- Expand jaxp sources/,/<delete file="${xml-commons-srcs.tar}"/{d}' build.xml

# Remove classpaths from manifests
sed -i '/class-path/I d' $(find -iname '*manifest*')

# Convert CR-LF to LF-only
sed -i 's/\r//' KEYS LICENSE.txt NOTICE.txt xdocs/style/resources/script.js \
    xdocs/sources/xsltc/README* `find -name '*.sh'`

%mvn_file :xalan %{name} jaxp_transform_impl
%mvn_file :serializer %{name}-serializer
%mvn_file :xsltc xsltc
%mvn_package :xsltc xsltc

%build
pushd lib
ln -sf $(build-classpath java_cup-runtime) runtime.jar
ln -sf $(build-classpath bcel) BCEL.jar
ln -sf $(build-classpath regexp) regexp.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
popd
pushd tools
ln -sf $(build-classpath java_cup) java_cup.jar
ln -sf $(build-classpath ant) ant.jar
ln -sf $(build-classpath xml-stylebook) stylebook-1.0-b3_xalan-2.jar
popd
export CLASSPATH=$(build-classpath glassfish-servlet-api)

ant \
  -Djava.awt.headless=true \
  -Dapi.j2se=%{_javadocdir}/java \
  -Dbuild.xalan-interpretive.jar=build/xalan-interpretive.jar \
  xalan-interpretive.jar\
  xsltc.unbundledjar \
  docs \
  javadocs \
  samples \
  servlet

# inject OSGi manifests
jar ufm build/serializer.jar %{SOURCE1}
jar ufm build/xalan-interpretive.jar %{SOURCE5}

%mvn_artifact %{SOURCE2} build/xalan-interpretive.jar
%mvn_artifact %{SOURCE3} build/serializer.jar
%mvn_artifact %{SOURCE4} build/xsltc.jar

%install
%mvn_install -J build/docs/apidocs

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 build/xalansamples.jar \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-samples.jar
install -p -m 644 build/xalanservlet.war \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}-servlet.war
cp -pr samples $RPM_BUILD_ROOT%{_datadir}/%{name}

# fix link between manual and javadoc
(cd build/docs; ln -sf %{_javadocdir}/%{name} apidocs)

find $RPM_BUILD_ROOT -name '*.sh' -print0 | xargs -0 dos2unix
grep -r -m 1 -l -Z '^#!/bin/sh' $RPM_BUILD_ROOT%_bindir | xargs -0 dos2unix

%post
mv %{_javadir}/jaxp_transform_impl.jar{,.tmp} || :
# alternatives removed in f26
:
# restore the symlink
mv %{_javadir}/jaxp_transform_impl.jar{.tmp,} || :

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%doc KEYS readme.html

%files xsltc -f .mfiles-xsltc
%doc LICENSE.txt NOTICE.txt

%files manual
%doc LICENSE.txt NOTICE.txt
%doc --no-dereference build/docs/*

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt4_33jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt4_31jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt4_28jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt4_27jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_21jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_18jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_17jpp7
- update

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_16jpp7
- new release

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_1jpp6
- fixed xerces dependency in repolib

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_1jpp6
- added OSGi provides to serializer.jar

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_10jpp5
- fixed repocop warnings

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_9jpp5
- jpp5 build

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_7jpp1.7
- rebuild on x86_64; added explicit source and target 1.4
- obsoletes: xalan-j

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt5_7jpp1.7
- rebuild on x86_64; added explicit source and target 1.4
- obsoletes: xalan-j

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt3_7jpp1.7
- converted from JPackage by jppimport script

* Tue Jun 20 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt3
- Fixed the dependency in xalan-j-manual

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt2
- Install serializer.jar

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt1
- 2.7.0
- Use new xml-commons-external

* Sat Jan 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3
- Enable xsltc by default
- Converted to rpm-build-java macros
- Stripped the source archive from unnecessary jars.
  Building from original archive is still available via --with origsrc

* Fri Aug 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- Do not BuildRequire system stylebook as it BuildRequires xalan-j
- New alternatives format (ugh)
- Grouped everything under Development/Java

* Sat Apr 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- New upstream release
- Updated manifest patch

* Mon Jan 12 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt3
- Migration to the new alternatives scheme

* Fri Dec 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt2
- Build using XML APIs and a JAXP parser installed in the system
- Enabled javadoc back
- Added update-alternatives to install-time dependencies
- Added xml-commons-apis to Requires

* Thu Dec 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt1
- New upstream release

* Sat Sep 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.1-alt1
- Ported to ALT Linux from JPackage project
- Don't build xsltc and demo for now, due to dependencies.
