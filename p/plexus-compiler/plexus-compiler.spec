Name:           plexus-compiler
Version:        2.16.2
Release:        alt1.1

Summary:        Compiler call initiators for Plexus
License:        MIT and Apache-2.0
Group:          Development/Java
URL:            https://codehaus-plexus.github.io/plexus-compiler/
VCS:            https://github.com/codehaus-plexus/plexus-compiler

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  java-devel

BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.eclipse.jdt:ecj)
BuildRequires:  mvn(commons-lang:commons-lang)

BuildArch:      noarch

%description
Plexus Compiler adds support for using various compilers from a
unified api. Support for javac is available in main package. For
additional compilers see %name-extras package.

%package extras
Group:          Development/Java
Summary:        Extra compiler support for %name
License:        MIT and Apache-2.0 and Apache-1.1

%description extras
Additional support for csharp, eclipse and jikes compilers.

%package pom
Group:          Development/Java
Summary:        Maven POM files for %name

%description pom
This package provides %summary.

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin

%pom_disable_module plexus-compiler-aspectj plexus-compilers
%pom_disable_module plexus-compiler-javac-errorprone plexus-compilers

%pom_disable_module plexus-compiler-test
%pom_disable_module plexus-compiler-its

%mvn_package ":*::sources:" __noinstall
%mvn_package ":plexus-compiler{,s}" pom
%mvn_package ":*{csharp,eclipse,jikes}*" extras

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files extras -f .mfiles-extras
%files pom -f .mfiles-pom

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.16.2-alt1.1
- Cosmetic fixes.

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 2.16.2-alt1
- Updated to 2.16.2.

* Sun Feb 23 2025 Andrey Cherepanov <cas@altlinux.org> 0:2.15.0-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.11.1-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:2.8.8-alt1_3jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.8.8-alt1_1jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.8.5-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt1_4jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8.2-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt1_5jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_3jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_0jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt2_1jpp7.qa1
- rebuild with maven-local

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:1.9.2-alt1_1jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for plexus-compiler

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt1_1jpp7
- fc update

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_3jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt2_1jpp7
- applied repocop patches

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

