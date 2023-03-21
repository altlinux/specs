Epoch: 1
Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           bsf
Version:        2.4.0
Release:        alt3_46jpp11
Summary:        Bean Scripting Framework
License:        ASL 2.0
URL:            http://commons.apache.org/bsf/
BuildArch:      noarch

Source0:        http://apache.mirror.anlx.net//commons/%{name}/source/%{name}-src-%{version}.tar.gz
Source1:        %{name}-pom.xml

Patch0:         build-file.patch
Patch1:         build.properties.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  apache-parent
BuildRequires:  xalan-j2
BuildRequires:  apache-commons-logging
Source44: import.info
%add_findreq_skiplist /usr/share/bsf-*

%description
Bean Scripting Framework (BSF) is a set of Java classes which provides
scripting language support within Java applications, and access to Java
objects and methods from scripting languages. BSF allows one to write
JSPs in languages other than Java while providing access to the Java
class library. In addition, BSF permits any Java application to be
implemented in part (or dynamically extended) by a language that is
embedded within it. This is achieved by providing an API that permits
calling scripting language engines from within Java, as well as an
object registry that exposes Java objects to these scripting language
engines.

BSF supports several scripting languages currently:
* Javascript (using Rhino ECMAScript, from the Mozilla project)
* Python (using either Jython or JPython)
* Tcl (using Jacl)
* NetRexx (an extension of the IBM REXX scripting language in Java)
* XSLT Stylesheets (as a component of Apache XML project's Xalan and
Xerces)

In addition, the following languages are supported with their own BSF
engines:
* Java (using BeanShell, from the BeanShell project)
* JRuby
* JudoScript

%prep
%setup -q
%patch0 -p1
%patch1 -p1
find -name \*.jar -delete

%mvn_file : %{name}
%mvn_alias : org.apache.bsf:

%build
export CLASSPATH=$(build-classpath apache-commons-logging xalan-j2)
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Dsource.level=1.7 -Dant.build.javac.target=1.7 jar

%mvn_artifact %{SOURCE1} build/lib/%{name}.jar

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc AUTHORS.txt CHANGES.txt README.txt TODO.txt RELEASE-NOTE.txt

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:2.4.0-alt3_46jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:2.4.0-alt3_44jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:2.4.0-alt3_39jpp11
- update

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 1:2.4.0-alt3_35jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_32jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_28jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_27jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_26jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_23jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_22jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_17jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_16jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_15jpp7
- fc update

* Fri Sep 14 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_13jpp7
- fc version

* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_11jpp6
- restored repolib

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt2_11jpp6
- new jpp relase

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt2_2jpp6
- fixed repolib

* Fri Jan 07 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt1_2jpp6
- new version

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 1:2.3.0-alt1_13jpp5
- downgrade to match 5.0; added repolib

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt4_1jpp1.7
branch 4.0 compatible build

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt3_1jpp1.7
- do disabled python findreq on jython code
- added commons-lang dependency

* Tue Nov 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt2_1jpp1.7
- disabled python findreq on jython code

* Sun Nov 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_1jpp1.7
- updated to new jpackage release

* Mon Oct 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_11jpp1.7
- resurrected from orphaned
- added obsolete jakarta-bsf

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_11jpp1.7
- converted from JPackage by jppimport script

