Epoch: 1
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Upstream has not made a tarball for the 1.12.2 release, so pull it from git
%global commit      328cf493ec2537af9d2bbce0eb4b4ef118b66547
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           automaton
Version:        1.12.2
Release:        alt1_4jpp11
Summary:        A Java finite state automata/regular expression library

License:        BSD
URL:            https://www.brics.dk/automaton/
Source0:        https://github.com/cs-au-dk/dk.brics.automaton/archive/%{commit}/%{name}-%{version}.tar.gz
# Fix for javadoc error: tag not supported in the generated HTML version
Patch0:         %{name}-javadoc.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
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
%setup -q -n dk.brics.%{name}-%{commit}
%patch0 -p1


# Remove references to unneeded plugins
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

# Generate code for JDK 8 instead of JDK 6
sed -e 's,>1.6<,>1.8<,g' \
    -e 's,Xdoclint.*,&\n          <source>8</source>,' \
    -i pom.xml

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc ChangeLog README
%doc --no-dereference COPYING

%files javadoc -f .mfiles-javadoc

%changelog
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

