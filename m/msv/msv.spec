BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          msv
Epoch:         1
Version:       2009.1
Release:       alt2_12jpp7
Summary:       Multi-Schema Validator
Group:         Development/Java
License:       BSD
URL:           https://msv.dev.java.net/

# To generate tarball from upstream source control:
# $ svn export https://msv.dev.java.net/svn/msv/tags/msv-2009.1/ --username guest
# $ tar zcf msv-2009.1.tar.gz msv-2009.1
Source0:       %{name}-%{version}.tar.gz

# The "maven-wagon-svn" plug-in is not in Fedora
Patch0:        %{name}-disable-maven-wagon-svn.patch

# There is a build time dependency on crimson which needs to be stripped
# (We're using xerces-j2 instead)
Patch1:        %{name}-disable-crimson.patch

# Link to locally installed javadocs
Patch2:        %{name}-link-local-javadoc.patch

BuildRequires: java-javadoc
BuildRequires: jpackage-utils
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-plugin-build-helper
BuildRequires: isorelax
BuildRequires: isorelax-javadoc
BuildRequires: relaxngDatatype
BuildRequires: relaxngDatatype-javadoc
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: junit

BuildArch:     noarch
Source44: import.info

%description
The Sun Multi-Schema XML Validator (MSV) is a Java technology tool to validate
XML documents against several kinds of XML schemata. It supports RELAX NG,
RELAX Namespace, RELAX Core, TREX, XML DTDs, and a subset of XML Schema Part 1.
This latest (version 1.2) release includes several bug fixes and adds better
conformance to RELAX NG/W3C XML standards and JAXP masquerading.

%package       msv
Summary:       Multi-Schema Validator Core
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2
Requires:      msv-xsdlib
Provides: msv = %version
Obsoletes: msv < 1.3

%description   msv
%{summary}.

%package       relames
Summary:       Multi-Schema Validator Schematron Plugin
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xalan-j2
Requires:      xerces-j2
Requires:      msv-msv = %{?epoch:%epoch:}%{version}-%{release}
Requires:      msv-xsdlib

%description   relames
%{summary}.

%package       rngconv
Summary:       Multi-Schema Validator RNG Converter
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2
Requires:      msv-msv = %{?epoch:%epoch:}%{version}-%{release}
Requires:      msv-xsdlib

%description   rngconv
%{summary}.

%package       xmlgen
Summary:       Multi-Schema Validator Generator
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2
Requires:      msv-msv = %{?epoch:%epoch:}%{version}-%{release}
Requires:      msv-xsdlib

%description    xmlgen
%{summary}.

%package       xsdlib
Summary:       Multi-Schema Validator XML Schema Library
Group:         Development/Java
Requires:      jpackage-utils
Requires:      isorelax
Requires:      relaxngDatatype
Requires:      xerces-j2

# Can remove these obsoletes at Fedora 17 time
Obsoletes:     xsdlib < %{version}-%{release}
Conflicts: msv < 1.3
Provides: xsdlib

%description   xsdlib
%{summary}.

 Sun XML Datatypes Library. An implementation of W3C XML Schema Part 2.

%package       javadoc
Summary:       API documentation for Multi-Schema Validator
Group:         Development/Java
Requires:      java-javadoc
Requires:      jpackage-utils
Requires:      isorelax-javadoc
Requires:      relaxngDatatype-javadoc

# Can remove these obsoletes at Fedora 17 time
Obsoletes:     msv-msv-javadoc < %{version}-%{release}
Obsoletes:     msv-relames-javadoc < %{version}-%{release}
Obsoletes:     msv-xmlgen-javadoc < %{version}-%{release}
Obsoletes:     msv-xsdlib-javadoc < %{version}-%{release}
Obsoletes:     xsdlib-javadoc < %{version}-%{release}
BuildArch: noarch

%description   javadoc
%{summary}.

%package       manual
Summary:       Manual for Multi-Schema Validator
Group:         Development/Java
BuildArch: noarch

%description   manual
%{summary}.

%package       demo
Summary:       Samples for Multi-Schema Validator
Group:         Development/Java
Requires:      msv-msv
Requires:      msv-xsdlib
Requires:      jpackage-utils

%description   demo
%{summary}.

%prep
%setup -q

# Delete anything pre-compiled
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.zip' -exec rm -f '{}' \;

# Delete class-path entries from manifests
for m in $(find . -name MANIFEST.MF) ; do
  sed --in-place -e '/^[Cc]lass-[Pp]ath:/d' $m
done

# Apply patches
%patch0 -p0 -b .orig
%patch1 -p0 -b .orig
%patch2 -p0 -b .orig2

# Change encoding of non utf-8 files
for m in $(find . -name copyright.txt) ; do
  iconv -f iso-8859-1 -t utf-8 < $m > $m.utf8
  mv $m.utf8 $m
done

%build
mvn-rpmbuild install javadoc:aggregate

%install
# Jars
install -pD -T msv/target/%{name}-core-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-core.jar
install -pD -T relames/target/%{name}-relames-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-relames.jar
install -pD -T rngconverter/target/%{name}-rngconverter-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-rngconverter.jar
install -pD -T generator/target/%{name}-generator-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-generator.jar
install -pD -T xsdlib/target/xsdlib-%{version}.jar \
  %{buildroot}%{_javadir}/xsdlib.jar
install -pD -T testharness/target/%{name}-testharness-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}-testharness.jar

# Alternate jar names
ln -s %{name}-core.jar         \
  %{buildroot}%{_javadir}/%{name}-msv.jar
ln -s %{name}-rngconverter.jar \
  %{buildroot}%{_javadir}/%{name}-rngconv.jar
ln -s %{name}-generator.jar    \
  %{buildroot}%{_javadir}/%{name}-xmlgen.jar
ln -s xsdlib.jar               \
  %{buildroot}%{_javadir}/%{name}-xsdlib.jar

# Poms
install -pD -T -m 644 pom.xml              %{buildroot}%{_mavenpomdir}/JPP-msv.pom
install -pD -T -m 644 parent/pom.xml       %{buildroot}%{_mavenpomdir}/JPP-msv-parent.pom
install -pD -T -m 644 msv/pom.xml          %{buildroot}%{_mavenpomdir}/JPP-msv-core.pom
install -pD -T -m 644 relames/pom.xml      %{buildroot}%{_mavenpomdir}/JPP-msv-relames.pom
install -pD -T -m 644 rngconverter/pom.xml %{buildroot}%{_mavenpomdir}/JPP-msv-rngconverter.pom
install -pD -T -m 644 generator/pom.xml    %{buildroot}%{_mavenpomdir}/JPP-msv-generator.pom
install -pD -T -m 644 testharness/pom.xml  %{buildroot}%{_mavenpomdir}/JPP-msv-testharness.pom
install -pD -T -m 644 xsdlib/pom.xml       %{buildroot}%{_mavenpomdir}/JPP-xsdlib.pom
%add_to_maven_depmap net.java.dev.msv msv              %{version} JPP msv
%add_to_maven_depmap net.java.dev.msv msv-parent       %{version} JPP msv-parent
%add_to_maven_depmap net.java.dev.msv msv-core         %{version} JPP msv-core
%add_to_maven_depmap net.java.dev.msv msv-relames      %{version} JPP msv-relames
%add_to_maven_depmap net.java.dev.msv msv-rngconverter %{version} JPP msv-rngconverter
%add_to_maven_depmap net.java.dev.msv msv-generator    %{version} JPP msv-generator
%add_to_maven_depmap net.java.dev.msv msv-testharness  %{version} JPP msv-testharness
%add_to_maven_depmap net.java.dev.msv xsdlib           %{version} JPP xsdlib
%add_to_maven_depmap msv msv         %{version} JPP msv-core
%add_to_maven_depmap com.sun.msv.datatype.xsd xsdlib   %{version} JPP xsdlib

# Javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# Manuals
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/msv
install -m 644 msv/doc/*.html     %{buildroot}%{_docdir}/%{name}-%{version}/msv
install -m 644 msv/doc/*.gif      %{buildroot}%{_docdir}/%{name}-%{version}/msv
install -m 644 msv/doc/README.txt %{buildroot}%{_docdir}/%{name}-%{version}/msv

install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/relames
install -m 644 relames/doc/README.txt %{buildroot}%{_docdir}/%{name}-%{version}/relames

install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/rngconverter
install -m 644 rngconverter/doc/README.txt %{buildroot}%{_docdir}/%{name}-%{version}/rngconverter

install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/generator
install -m 644 generator/doc/*.html     %{buildroot}%{_docdir}/%{name}-%{version}/generator
install -m 644 generator/doc/README.txt %{buildroot}%{_docdir}/%{name}-%{version}/generator

install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}/xsdlib
install -m 644 xsdlib/doc/*.html     %{buildroot}%{_docdir}/%{name}-%{version}/xsdlib
install -m 644 xsdlib/doc/README.txt %{buildroot}%{_docdir}/%{name}-%{version}/xsdlib

# Examples
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/msv
cp -pr msv/examples/* %{buildroot}%{_datadir}/%{name}-%{version}/msv
install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/xsdlib
cp -pr xsdlib/examples/* %{buildroot}%{_datadir}/%{name}-%{version}/xsdlib

# Scripts
%jpackage_script com.sun.msv.driver.textui.Driver "" "" msv-msv:msv-xsdlib:relaxngDatatype:isorelax msv true
%jpackage_script com.sun.msv.generator.Driver "" "" msv-xmlgen:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 xmlgen true
%jpackage_script com.sun.msv.schematron.Driver "" "" msv-relames:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xalan-j2 relames true
%jpackage_script com.sun.msv.writer.relaxng.Driver "" "" msv-rngconv:msv-msv:msv-xsdlib:relaxngDatatype:isorelax:xerces-j2 rngconv true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/msv.conf`
touch $RPM_BUILD_ROOT/etc/java/msv.conf
ln -s msv-core.jar %buildroot%_javadir/msv.jar
# compat depmap
%add_to_maven_depmap msv msv %{version} JPP %{name}
%add_to_maven_depmap msv xsdlib %{version} JPP %{name}-xsdlib


%files msv
%{_bindir}/msv
%{_mavenpomdir}/JPP-%{name}-core.pom
%{_mavenpomdir}/JPP-%{name}-testharness.pom
%{_javadir}/%{name}-core.jar
%{_javadir}/%{name}-msv.jar
%{_javadir}/%{name}-testharness*
%doc msv/doc/license.txt
%config(noreplace,missingok) /etc/java/msv.conf

%files relames
%{_bindir}/relames
%{_mavenpomdir}/JPP-%{name}-relames.pom
%{_javadir}/%{name}-relames.jar
%doc relames/doc/copyright.txt

%files rngconv
%{_bindir}/rngconv
%{_mavenpomdir}/JPP-%{name}-rngconverter.pom
%{_javadir}/%{name}-rngconverter.jar
%{_javadir}/%{name}-rngconv.jar
%doc rngconverter/doc/license.txt
%doc rngconverter/doc/copyright.txt

%files xmlgen
%{_bindir}/xmlgen
%{_mavenpomdir}/JPP-%{name}-generator.pom
%{_javadir}/%{name}-generator.jar
%{_javadir}/%{name}-xmlgen.jar
%doc generator/doc/license.txt
%doc generator/doc/copyright.txt

%files xsdlib
%{_mavenpomdir}/JPP-xsdlib.pom
%{_javadir}/xsdlib.jar
%{_javadir}/%{name}-xsdlib.jar
%doc xsdlib/doc/license.txt
%doc xsdlib/doc/copyright.txt

# This subpackage wins the parent poms and the depmap because all the other
# subpackages require this one
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-parent.pom
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt2_12jpp7
- applied repocop patches

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt1_12jpp7
- new version

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.7jpp6
- ant 18 support; added description (closes: #22125)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.6jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_0.20050722.6jpp5
- fixed docdir ownership

* Fri Sep 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.3jpp1.7
- build without bootstrap

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1_0.20050722.3jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.1
- Initial build for ALT Linux Sisyphus
- cvs version 20050424
