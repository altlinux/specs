%define _unpackaged_files_terminate_build 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
# Use the immutable upstream Git commit for this release.
%global commit      c81d54aa0b107aed8528c47b7ddb1ab868502af0

Epoch: 1
Name: automaton
Version: 1.13
Release: alt1

Summary: A Java finite state automata/regular expression library
License: BSD-3-Clause
Group: Development/Java
URL: https://www.brics.dk/automaton/
VCS: https://github.com/cs-au-dk/dk.brics.automaton

Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-macros-java
BuildRequires: jpackage-11-compat
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)

BuildArch: noarch

%description
This Java package contains a DFA/NFA (finite-state automata) implementation
with Unicode alphabet (UTF-16) and support for the standard regular expression
operations (concatenation, union, Kleene star) and a number of non-standard
ones (intersection, complement, etc.).

In contrast to many other automaton/regexp packages, this package is fast,
compact, and implements real, unrestricted regular operations.  It uses a
symbolic representation based on intervals of Unicode characters.

%package javadoc
Group: Development/Documentation
Summary: A Java finite state automata/regular expression library

%description javadoc
Javadoc documentation for automaton.

%prep
%setup -q -n dk.brics.%name-%commit
# This artifact is not signed or published during package builds.
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
# The SOURCE package does not ship a sources.jar.
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

%build
%mvn_build -s -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-%name
%doc --no-dereference COPYING
%doc ChangeLog

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1:1.13-alt1
- New version.

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1:1.12.2-alt1_4jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.12r1-alt1_6jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.12r1-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.12r1-alt1_3jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.12r1-alt1_2jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.12r1-alt1_1jpp8
- new version

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_11jpp8
- new version

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_5jpp7
- update to new release by jppimport

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_4jpp7
- update to new release by jppimport

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_3jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.11r8-alt1_2jpp7
- fc build
