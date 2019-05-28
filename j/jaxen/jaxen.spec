Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without dom4j

Name:           jaxen
Epoch:          0
Version:        1.1.6
Release:        alt1_19jpp8
Summary:        An XPath engine written in Java
# src/java/main/org/w3c/dom/UserDataHandler.java is W3C
# rest is BSD
License:        BSD and W3C
URL:            http://jaxen.codehaus.org/
BuildArch:      noarch

Source0:        http://dist.codehaus.org/jaxen/distributions/%{name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
%if %{with dom4j}
BuildRequires:  mvn(dom4j:dom4j)
%endif
Source44: import.info

%description
Jaxen is an open source XPath library written in Java. It is adaptable
to many different object models, including DOM, XOM, dom4j, and JDOM.
Is it also possible to write adapters that treat non-XML trees such as compiled
Java byte code or Java beans as XML, thus enabling you to query these trees
with XPath too.

%package demo
Group: Development/Documentation
Summary:        Samples for %{name}
Requires:       %{name} = 0:%{version}-%{release}

%description demo
%{summary}.

%package javadoc
Group: Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 

%if %{without dom4j}
rm -rf src/java/main/org/jaxen/dom4j
%pom_remove_dep dom4j:dom4j
%endif

rm -rf src/java/main/org/jaxen/xom
%pom_remove_dep xom:xom

%mvn_file : %{name}

%build
%mvn_build -f

%install
%mvn_install

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/samples
cp -pr src/java/samples/* %{buildroot}%{_datadir}/%{name}/samples

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files demo
%{_datadir}/%{name}

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_19jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_12jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_10jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_9jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_9jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_5jpp7
- fc update

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt3_1jpp6
- fixed build with moved maven1

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt2_1jpp6
- rebuild with target=5 (to avoid class poisoning)

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_1jpp6
- new version

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp5
- added repolib

* Fri Nov 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.4beta2
- added JPackage compat stuff

* Fri Mar 24 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.3beta2
- Fix typo in requires of javadoc package

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.2beta2
- Fix build with j2se1.5

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt0.1beta2
- Initial build for ALT Linux Sisyphus

