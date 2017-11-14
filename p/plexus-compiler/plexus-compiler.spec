Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
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
%bcond_without eclipse

Name:       plexus-compiler
Epoch:      0
Version:    2.8.1
Release:    alt1_5jpp8
Summary:    Compiler call initiators for Plexus
# extras subpackage has a bit different licensing
# parts of compiler-api are ASL2.0/MIT
License:    MIT and ASL 2.0
URL:        https://github.com/codehaus-plexus/plexus-compiler
BuildArch:  noarch

Source0:    https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:    LICENSE.MIT

# https://github.com/codehaus-plexus/plexus-compiler/pull/25
Patch0:     0001-Copy-input-map-in-setCustomCompilerArguments-AsMap.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%if %{with eclipse}
BuildRequires:  mvn(org.eclipse.tycho:org.eclipse.jdt.core)
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

%patch0 -p1

cp %{SOURCE1} LICENSE
cp %{SOURCE2} LICENSE.MIT

%pom_disable_module plexus-compiler-aspectj plexus-compilers
# missing com.google.errorprone:error_prone_core
%pom_disable_module plexus-compiler-javac-errorprone plexus-compilers

%if %{without eclipse}
%pom_disable_module plexus-compiler-eclipse plexus-compilers
%endif

# don't build/install compiler-test module, it needs maven2 test harness
%pom_disable_module plexus-compiler-test

# don't install sources jars
%mvn_package ":*::sources:" __noinstall

%mvn_package ":plexus-compiler{,s}" pom
%mvn_package ":*{csharp,eclipse,jikes}*" extras

# don't generate requires on test dependency (see #1007498)
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='plexus-compiler-test']]" plexus-compilers

%pom_remove_plugin :maven-site-plugin

%build
# Tests are skipped because of unavailable plexus-compiler-test artifact
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE LICENSE.MIT
%files extras -f .mfiles-extras
%files pom -f .mfiles-pom

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE.MIT

%changelog
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

