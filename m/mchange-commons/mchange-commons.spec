Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.2.11
%global git_tag mchange-commons-java-%{version}

Name:          mchange-commons
Version:       0.2.11
Release:       alt2_9jpp8
Summary:       A collection of general purpose utilities for c3p0
License:       LGPLv2 or EPL
URL:           https://github.com/swaldman/mchange-commons-java
Source0:       https://github.com/swaldman/mchange-commons-java/archive/%{git_tag}/mchange-commons-%{version}.tar.gz
Source1:       https://raw.github.com/willb/climbing-nemesis/master/climbing-nemesis.py

# There is a missing dep in Fedora so cannot build tests
Patch0:        mchange-no-tests.patch

BuildRequires: sbt
BuildRequires: ivy-local
BuildRequires: maven-local
BuildRequires: log4j12
BuildRequires: slf4j
BuildRequires: typesafe-config
BuildRequires: python

BuildArch:     noarch
Source44: import.info

%description
Originally part of c3p0, mchange-commons is a set of general purpose
utilities.

%package javadoc
Group: Development/Java
Summary:       API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n mchange-commons-java-%{git_tag}

%patch0

find -name '*.class' -delete
find -name '*.jar' -delete

cp %{SOURCE1} .
chmod 755 climbing-nemesis.py

sed -i -e 's/0.13.6/0.13.1/' project/build.properties

cp -pr /usr/share/sbt/ivy-local .

%build
# XXX: Link deps, I understand this is a temp measure until sbt gains real xmvn integration
# XXX: Switch to Python 3 before Fedora 32
python2 climbing-nemesis.py com.typesafe config any ivy-local --version 1.2.1
python2 climbing-nemesis.py log4j log4j 12 ivy-local --version 1.2.14
python2 climbing-nemesis.py org.slf4j slf4j-api any ivy-local --version 1.7.5

export SBT_BOOT_DIR=$PWD/boot
export SBT_IVY_DIR=$PWD/ivy-local
sbt package make-pom doc

%mvn_artifact target/mchange-commons-java-%{version}.pom target/mchange-commons-java-%{version}.jar

%install
%mvn_install -J target/api

%files -f .mfiles
%doc --no-dereference LICENSE*

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE*

%changelog
* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt2_9jpp8
- fixed build

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt2_8jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt2_5jpp8
- java fc28+ update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt2_3jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt2_2jpp8
- fixed build

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt1_2jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt1_1jpp8
- new jpp release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.7-alt1_4jpp8
- unbootstrap build

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3.4-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3.4-alt1_2jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_0.7.20110130hgjpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_0.5.20110130hgjpp7
- fc version

