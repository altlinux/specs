Epoch: 0
Group: Text tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           fop
Summary:        XSL-driven print formatter
Version:        2.7
Release:        alt1_2jpp11
# ASL 1.1:
# several files in fop-core/src/main/resources/org/apache/fop/render/awt/viewer/resources
# rest is ASL 2.0
License:        ASL 2.0 and ASL 1.1
URL:            https://xmlgraphics.apache.org/fop
Source0:        https://www.apache.org/dist/xmlgraphics/%{name}/source/%{name}-%{version}-src.tar.gz
Source1:        %{name}.script
Source2:        batik-pdf-MANIFEST.MF
Source4:        https://www.apache.org/licenses/LICENSE-1.1.txt
#Patch0:        fop-xmlunit.patch
Patch1:		0001-Main.patch
Patch2:		0002-Use-sRGB.icc-color-profile-from-colord-package.patch
Patch4:         0004-Port-to-QDox-2.0.patch

BuildArch:      noarch

Requires:       java
Requires:       xalan-j2 >= 2.7.0
Requires:       xml-commons-apis >= 1.3.04
# Explicit requires for javapackages-tools since fop script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-logging
BuildRequires:  batik
BuildRequires:  fontbox
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-local
BuildRequires:  maven-plugin-build-helper
BuildRequires:  mvn(javax.servlet:servlet-api)
# For servlet, not packaged
#BuildRequires:  maven-war-plugin
BuildRequires:  pdfbox
BuildRequires:  qdox
BuildRequires:  xml-maven-plugin
BuildRequires:  xmlgraphics-commons >= 1.5
BuildRequires:  xmlunit
BuildRequires:  xmlunit-assertj
BuildRequires:  xmlunit-core
Source44: import.info

%description
FOP is the world's first print formatter driven by XSL formatting
objects. It is a Java application that reads a formatting object tree
and then turns it into a PDF document. The formatting object tree, can
be in the form of an XML document (output by an XSLT engine like XT or
Xalan) or can be passed in memory as a DOM Document or (in the case of
XT) SAX events.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch4 -p1


cp %{SOURCE4} LICENSE-1.1

rm -f fop/lib/*.jar fop/lib/build/*.jar

# Not packaged
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_dep javax.media:jai-core fop-core
%pom_remove_dep com.sun.media:jai-codec fop-core
%pom_remove_dep net.sf.offo:fop-hyph fop-core
%pom_remove_dep net.sf.saxon:saxon fop-core
# Update to current xmlunit
%pom_change_dep xmlunit:xmlunit org.xmlunit:xmlunit-core fop-core
%pom_add_dep org.xmlunit:xmlunit-assertj3 fop-core
# Requires maven-war-plugin
%pom_disable_module fop-servlet
# Requires JAI, not packaged
rm fop-core/src/main/java/org/apache/fop/util/bitmap/JAIMonochromeBitmapConverter.java


%build
# Skip tests for now, make dirs needed by build but created by tests
mkdir -p fop-events/target/test-classes
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install
# inject OSGi manifest
jar ufm %{buildroot}%{_javadir}/%{name}/%{name}.jar %{SOURCE2}

# script
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/fop

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf
cp -rp fop/conf/* %{buildroot}%{_datadir}/%{name}/conf

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/xmvn-apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/fop.conf`
touch $RPM_BUILD_ROOT/etc/fop.conf


%files -f .mfiles
%doc LICENSE LICENSE-1.1 README NOTICE
%{_datadir}/%{name}
%{_bindir}/fop
%config(noreplace,missingok) /etc/fop.conf

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE LICENSE-1.1


%changelog
* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:2.7-alt1_2jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 0:2.6-alt1_2jpp11
- new version

* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 0:2.5-alt2_2jpp11
- migrated to %%mvn_artifact

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:2.5-alt1_2jpp11
- new version

* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt2_1jpp8
- use zerg@'s hack for armh

* Tue Oct 13 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_1jpp8
- new version
- note: manually edited fop.pom, dropped parent

* Fri Jun 21 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_8jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_5jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp7
- new version

* Sun Mar 31 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_20jpp7
- fc update

* Sat Oct 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_4jpp6
- fixed classpath for new batik

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp6
- fixed build w/new batik

* Sun Jan 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp6
- new jpp relase

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt5_6jpp6
- added commons-logging to the classpath

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt4_6jpp6
- add xmlgraphics-commons to classpath

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_6jpp6
- added OSGi provides

* Thu May 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_6jpp5
- new jpp release

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt3_5jpp5
- obsoletes fop 0.20.5

* Tue Oct 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt2_5jpp5
- fixed #17536

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt1_5jpp5
- added config

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.95-alt1_4jpp5
- converted from JPackage by jppimport script

