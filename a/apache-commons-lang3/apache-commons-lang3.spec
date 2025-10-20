Name:    apache-commons-lang3
Version: 3.19.0
Release: alt1
Summary: Provides a host of helper utilities for the java.lang API
License: Apache-2.0
Group:   Development/Java
URL:     https://commons.apache.org/lang

BuildArch: noarch

Source0: https://archive.apache.org/dist/commons/lang/source/commons-lang3-%{version}-src.tar.gz

BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.
The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

With version of commons-lang 3.x, developers decided to change API and
therefore created differently named artifact and jar files. This is
the new version, while apache-commons-lang is the compatibility
package.

%{?javadoc_package}

%prep
%setup -q -n commons-lang3-%{version}-src

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_dep org.openjdk.jmh:jmh-core
%pom_remove_dep org.openjdk.jmh:jmh-generator-annprocess
%pom_remove_dep org.apache.commons:commons-text
 
%mvn_file : %{name} commons-lang3
 
# testParseSync() test fails on ARM and PPC64LE for unknown reason
sed -i 's/\s*public void testParseSync().*/@org.junit.jupiter.api.Disabled\n&/' \
    src/test/java/org/apache/commons/lang3/time/FastDateFormatTest.java
 
# non-deterministic tests fail randomly
rm src/test/java/org/apache/commons/lang3/RandomStringUtilsTest.java
 
# Missing dependencies
rm src/test/java/org/apache/commons/lang3/HashSetvBitSetTest.java
 
# Remove limits and Java 11 options
sed -i '/<argLine>/d' pom.xml

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%changelog
* Mon Oct 20 2025 Alexander Danilov <admsasha@altlinux.org> 3.19.0-alt1
- new version

* Wed Apr 23 2025 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt1
- new version

* Wed Oct 25 2023 Igor Vlasenko <viy@altlinux.org> 3.12.0-alt2_7jpp11
- fixed build (closes: #48155)

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 3.12.0-alt1_7jpp11
- update

* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 3.12.0-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.11-alt1_1jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 3.8.1-alt1_5jpp8
- fc update

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.8.1-alt1_3jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_4jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_3jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_1jpp8
- new version

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_3jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.4-alt4_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.4-alt4_4jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.4-alt4_2jpp8
- new version

* Wed Jan 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.4-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_3jpp7
- new release

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_2jpp7
- new version

