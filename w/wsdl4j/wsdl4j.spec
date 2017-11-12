Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        Web Services Description Language Toolkit for Java
Name:           wsdl4j
Epoch:          0
Version:        1.6.3
Release:        alt1_11jpp8
License:        CPL
URL:            http://sourceforge.net/projects/wsdl4j
BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/project/wsdl4j/WSDL4J/%{version}/wsdl4j-src-%{version}.zip
Source1:        %{name}-MANIFEST.MF
Source2:        http://repo1.maven.org/maven2/wsdl4j/wsdl4j/%{version}/wsdl4j-%{version}.pom

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  javapackages-local

Provides:       javax.wsdl
Source44: import.info

%description
The Web Services Description Language for Java Toolkit (WSDL4J) allows the
creation, representation, and manipulation of WSDL documents describing
services.  This code base will eventually serve as a reference implementation
of the standard created by JSR110.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-1_6_3

%mvn_file ":{*}" @1

%build
ant compile javadocs
# inject OSGi manifests
jar ufm build/lib/%{name}.jar %{SOURCE1}

%install
%mvn_artifact %{SOURCE2} build/lib/%{name}.jar
%mvn_artifact %{name}:qname:%{version} build/lib/qname.jar
%mvn_install -J build/javadocs

install -d -m 755 %{buildroot}%{_javadir}/javax.wsdl/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.wsdl/
ln -sf ../qname.jar %{buildroot}%{_javadir}/javax.wsdl/

%files -f .mfiles
%doc license.html
%{_javadir}/javax.wsdl/

%files javadoc -f .mfiles-javadoc
%doc license.html

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_11jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_6jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_1jpp7
- new version

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_7jpp7
- fc update

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_7jpp6
- jpp 6 release

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_5jpp6
- fixed OSGi provides

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt3_5jpp6
- added OSGi provides

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_6jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_4jpp5
- alternatives 0.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_3jpp5
- converted from JPackage by jppimport script

* Thu Dec 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_2jpp1.7
- removed ghost jar

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_2jpp1.7
- updated to new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_4jpp1.7
- converted from JPackage by jppimport script

* Thu Mar 24 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt1
- 1.5
- rpm-build-java macroces

* Fri Sep 24 2004 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt2
- corrected requires (xerces-j -> jaxp_parser_impl)

* Fri Sep 17 2004 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Mon Aug 30 2004 Ralph Apel <r.apel at r-apel.de> 0:1.4-3jpp
- Build with ant-1.6.2

* Thu Jun 26 2003 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net> 0:1.4-2jpp
- Do not drop qname.jar

* Tue May 06 2003 David Walluck <david@anti-microsoft.org> 0:1.4-1jpp
- 1.4
- update for JPackage 1.5

* Sat Sep  7 2002 Ville Skyttä <ville.skytta at iki.fi> 1.1-1jpp
- First JPackage release.
