Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jdepend
Version:        2.10
Release:        alt1_3jpp11
Summary:        Java Design Quality Metrics
License:        MIT
URL:            https://github.com/clarkware/jdepend
BuildArch:      noarch

Source0:        https://github.com/clarkware/jdepend/archive/refs/tags/2.10.tar.gz#/jdepend-2.10.tar.gz

BuildRequires:  ant
BuildRequires:  javapackages-local

# demo subpackages was removed in Fedora 37
Obsoletes:      %{name}-demo < 2.10
Source44: import.info

%description
JDepend traverses a set of Java class and source file directories and
generates design quality metrics for each Java package. JDepend allows
you to automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to effectively manage
and control package dependencies.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" -delete
# fix strange permissions
find . -type d -exec chmod 755 {} \;

%mvn_file %{name}:%{name} %{name}

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Dant.build.javac.source=1.7 -Dant.build.javac.target=1.7 jar javadoc

%install
%mvn_artifact jdepend:jdepend:%{version} dist/%{name}-%{version}.jar
%mvn_install -J build/docs/api

%files -f .mfiles
%doc README.md CHANGELOG.md docs
%doc --no-dereference LICENSE.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.10-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:2.9.1-alt4_27jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt4_22jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt4_20jpp8
- new version

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_18jpp8.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for jdepend

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_17jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_16jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_13jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_8jpp7
- new release

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:2.9.1-alt3_7jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for jdepend

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_7jpp7
- fc update

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_3jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_1jpp5
- new jpackage release

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_1jpp1.7
- rebuild with new packages

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt2_1jpp1.7
- converted from JPackage by jppimport script

* Wed Apr 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Sep 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.2-alt1
- Updated to upstream release 2.8.2
- Disabled debug compiler option by default

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.7-alt1
- New upstream release

* Fri Oct 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6-alt1
- Ported to Sisyphus from JPackage
