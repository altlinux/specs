Group: Development/Java
BuildRequires(pre): rpm-macros-java
Name:          mchange-commons
Version:       0.7.1
Release:       alt1
Summary:       A collection of general purpose utilities for c3p0
License:       LGPL-2.1-or-later or EPL-1.0
URL:           https://github.com/swaldman/mchange-commons-java
VCS:           https://github.com/swaldman/mchange-commons-java.git
Source0:       %name-%version.tar

BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(com.typesafe:config)
BuildRequires: mvn(ch.qos.reload4j:reload4j)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

BuildArch:     noarch

%description
Originally part of c3p0, mchange-commons is a set of general purpose
utilities.

%package javadoc
Group: Development/Java
Summary:       API documentation for %name
BuildArch: noarch

%description javadoc
This package contains javadoc for %name.

%prep
%setup -q

%mvn_file : %name

%build
# Match upstream -source7/-target7; javac21 no longer accepts these flags.
export JAVA_HOME=%_jvmdir/java-17-openjdk
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE LICENSE-LGPL LICENSE-EPL

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 0.7.1-alt1
- New version.

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

