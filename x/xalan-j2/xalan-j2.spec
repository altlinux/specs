Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-alternatives rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.7.2
%global cvs_version %(echo %{version} | tr . _)

Name:           xalan-j2
Version:        2.7.2
Release:        alt1_9jpp11
Summary:        Java XSLT processor
# src/org/apache/xpath/domapi/XPathStylesheetDOM3Exception.java is W3C
License:        ASL 2.0 and W3C
URL:            http://xalan.apache.org/

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        xalan-j2-serializer-MANIFEST.MF
Source2:        http://repo1.maven.org/maven2/xalan/xalan/%{version}/xalan-%{version}.pom
Source3:        http://repo1.maven.org/maven2/xalan/serializer/%{version}/serializer-%{version}.pom
Source4:        xsltc-%{version}.pom
Source5:        xalan-j2-MANIFEST.MF
# Remove bundled binaries which cannot be easily verified for licensing
Source6:        generate-tarball.sh

Patch0:         xalan-j2-noxsltcdeps.patch

BuildArch:      noarch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  apache-parent
BuildRequires:  bcel
BuildRequires:  java_cup
BuildRequires:  regexp
BuildRequires:  sed
BuildRequires:  xerces-j2 >= 0:2.7.1
BuildRequires:  xml-commons-apis >= 0:1.3

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
License:        ASL 2.0
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
License:        ASL 2.0
BuildArch: noarch

%description    manual
Documentation for %{name}.

%prep
%setup -q -n xalan-j_%{cvs_version}
%patch0 -p0

find . -name '*.jar' -delete
find . -name '*.class' -delete

sed -i '/<bootclasspath/d' build.xml
(cd ./src && tar xf xml-commons-external-*-src.tar.gz)

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
popd
export CLASSPATH=$(build-classpath glassfish-servlet-api)

ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  \
  -Dcompiler.source=1.6 \
  -Dcompiler.target=1.6 \
  -Djava.awt.headless=true \
  -Dbuild.xalan-interpretive.jar=build/xalan-interpretive.jar \
  xalan-interpretive.jar\
  xsltc.unbundledjar \
  docs

# inject OSGi manifests
jar ufm build/serializer.jar %{SOURCE1}
jar ufm build/xalan-interpretive.jar %{SOURCE5}

%mvn_artifact %{SOURCE2} build/xalan-interpretive.jar
%mvn_artifact %{SOURCE3} build/serializer.jar
%mvn_artifact %{SOURCE4} build/xsltc.jar

%install
%mvn_install

find $RPM_BUILD_ROOT -name '*.sh' -print0 | xargs -0 dos2unix
grep -r -m 1 -l -Z '^#!/bin/sh' $RPM_BUILD_ROOT%_bindir | xargs -0 dos2unix

%post
mv %{_javadir}/jaxp_transform_impl.jar{,.tmp} || :
# alternatives removed in f26
:
# restore the symlink
mv %{_javadir}/jaxp_transform_impl.jar{.tmp,} || :

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc KEYS readme.html

%files xsltc -f .mfiles-xsltc
%doc --no-dereference LICENSE.txt NOTICE.txt

%files manual
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc --no-dereference build/docs/*

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:2.7.2-alt1_9jpp11
- update

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 0:2.7.2-alt1_6jpp8
- jvm8 update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.7.2-alt1_2jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt4_39jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt4_34jpp8
- java update

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
