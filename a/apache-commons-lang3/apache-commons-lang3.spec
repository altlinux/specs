Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname commons-lang3

Name:           apache-commons-lang3
Version:        3.11
Release:        alt1_1jpp11
Summary:        Provides a host of helper utilities for the java.lang API
License:        ASL 2.0

URL:            https://commons.apache.org/lang
Source0:        https://archive.apache.org/dist/commons/lang/source/%{srcname}-%{version}-src.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
Source44: import.info

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


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}-src


# remove unnecessary maven plugins
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file : %{name} commons-lang3


%build
# test dependencies are not all packaged for fedora:
# - org.easymock:easymock 4.2
# - org.junit-pioneer:junit-pioneer
# - org.openjdk.jmh:jmh-core
# - org.openjdk.jmh:jmh-generator-annprocess
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt


%changelog
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

