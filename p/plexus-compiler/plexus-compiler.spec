Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           plexus-compiler
Version:        2.11.1
Release:        alt1_2jpp11
Summary:        Compiler call initiators for Plexus
# extras subpackage has a bit different licensing
# parts of compiler-api are ASL2.0/MIT
License:        MIT and ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-compiler
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        LICENSE.MIT

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif
Source44: import.info

%description
Plexus Compiler adds support for using various compilers from a
unified api. Support for javac is available in main package. For
additional compilers see %{name}-extras package.

%package extras
Group: Development/Java
Summary:        Extra compiler support for %{name}
# ASL 2.0: src/main/java/org/codehaus/plexus/compiler/util/scan/
#          ...codehaus/plexus/compiler/csharp/CSharpCompiler.java
# ASL 1.1/MIT: ...codehaus/plexus/compiler/jikes/JikesCompiler.java
License:        MIT and ASL 2.0 and ASL 1.1

%description extras
Additional support for csharp, eclipse and jikes compilers

%package pom
Group: Development/Java
Summary:        Maven POM files for %{name}

%description pom
This package provides %{summary}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
License:        MIT and ASL 2.0 and ASL 1.1
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find -name '.class' -delete

cp %{SOURCE1} LICENSE
cp %{SOURCE2} LICENSE.MIT

%pom_remove_dep :junit-bom

%pom_disable_module plexus-compiler-aspectj plexus-compilers
# missing com.google.errorprone:error_prone_core
%pom_disable_module plexus-compiler-javac-errorprone plexus-compilers

%pom_disable_module plexus-compiler-eclipse plexus-compilers

# don't build/install compiler-test module, it needs maven2 test harness
%pom_disable_module plexus-compiler-test
%pom_disable_module plexus-compiler-its

# don't install sources jars
%mvn_package ":*::sources:" __noinstall

%mvn_package ":plexus-compiler{,s}" pom
%mvn_package ":*{csharp,eclipse,jikes}*" extras

# don't generate requires on test dependency (see #1007498)
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='plexus-compiler-test']]" plexus-compilers

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_dep -r org.codehaus.plexus:plexus-compiler-javac-errorprone

%build
# Tests are skipped because of unavailable plexus-compiler-test artifact
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE LICENSE.MIT
%files extras -f .mfiles-extras
%files pom -f .mfiles-pom

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE.MIT

%changelog
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

