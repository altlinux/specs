Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           janino
Version:        3.1.6
Release:        alt1_3jpp11
Summary:        Super-small, super-fast Java compiler
License:        BSD
URL:            http://janino-compiler.github.io/janino
BuildArch:      noarch
Source0:        https://github.com/janino-compiler/janino/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)

Requires:       javapackages-tools
Requires:       janino = %{?epoch:%epoch:}%{version}-%{release}
Source44: import.info

%description
Janino is a super-small, super-fast Java compiler.

The "JANINO" implementation of the "commons-compiler" API: Super-small,
super-fast, independent from the JDK's "tools.jar".

%package     -n commons-compiler
Group: Development/Java
Summary:        Commons Compiler

%description -n commons-compiler
The "commons-compiler" API, including the "IExpressionEvaluator",
"IScriptEvaluator", "IClassBodyEvaluator" and "ISimpleCompiler" interfaces.

%package     -n commons-compiler-jdk
Group: Development/Java
Summary:        Commons Compiler JDK

%description -n commons-compiler-jdk
The "JDK" implementation of the "commons-compiler" API that uses the
JDK's Java compiler (JAVAC) in "tools.jar".

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep

%setup -q


find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

pushd %{name}-parent
  %pom_xpath_remove pom:maven.compiler.source
  %pom_xpath_remove pom:maven.compiler.target
  %pom_xpath_remove pom:maven.compiler.executable
  %pom_xpath_remove pom:maven.compiler.fork

  %pom_remove_plugin :nexus-staging-maven-plugin
  %pom_remove_plugin :maven-jarsigner-plugin
  %pom_remove_plugin :maven-javadoc-plugin
  %pom_remove_plugin :maven-source-plugin

  %pom_disable_module ../commons-compiler-tests

  %mvn_package :%{name}-parent __noinstall
popd

%build

pushd %{name}-parent
  %mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=8 -Dmaven.compiler.target=8
popd

%install

pushd %{name}-parent
  %mvn_install
  
  %jpackage_script org.codehaus.commons.compiler.samples.CompilerDemo "" "" %{name}/janino:%{name}/commons-compiler janinoc true
popd

%files                         -f %{name}-parent/.mfiles-%{name}
%doc --no-dereference LICENSE
%{_bindir}/janinoc

%files -n commons-compiler     -f %{name}-parent/.mfiles-commons-compiler
%doc --no-dereference LICENSE

%files -n commons-compiler-jdk -f %{name}-parent/.mfiles-commons-compiler-jdk
%doc --no-dereference LICENSE

%files javadoc                 -f %{name}-parent/.mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:3.1.6-alt1_3jpp11
- new version

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:2.7.8-alt1_13jpp11
- java11 build

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_13jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_11jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_10jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt2_18jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt2_16jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt2_14jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt1_14jpp7
- fc release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.5.11-alt1_2jpp5
- new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.5.11-alt1_1jpp1.7
- converted from JPackage by jppimport script

