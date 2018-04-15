Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Upstream uses version-release.  Control the madness here.
%global upver 1.12
%global uprel 1
%global filever %{upver}-%{uprel}

Name:           automaton
Version:        %{upver}r%{uprel}
Release:        alt1_2jpp8
Summary:        A Java finite state automata/regular expression library

License:        BSD
URL:            http://www.brics.dk/automaton/
Source0:        http://www.brics.dk/~amoeller/%{name}/%{name}-%{filever}.tar.gz
Source1:        https://github.com/cs-au-dk/dk.brics.automaton/blob/master/pom.xml

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)

BuildArch:      noarch
Source44: import.info

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
Summary:        A Java finite state automata/regular expression library
BuildArch:      noarch

%description javadoc
Javadoc documentation for automaton.

%prep
%setup -q -n %{name}-%{upver}

# Remove prebuilt artifacts
rm -fr dist/%{name}.jar doc/*

# Add the maven pom file, forgotten by upstream
cp -p %{SOURCE1} .

# Remove references to unneeded plugins
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog README
%doc --no-dereference COPYING

%files javadoc -f .mfiles-javadoc

%changelog
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

