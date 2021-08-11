Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jdeparser
Version:          2.0.3
Release:          alt1_8jpp11
Summary:          Source generator library for Java
License:          ASL 2.0
URL:              https://github.com/jdeparser/jdeparser2
# old repos https://github.com/jdeparser/jdeparser
Source0:          %{url}/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Patch1:           0001-Drop-Assertions.callerIs.patch

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
This project is a fork of Sun's (now Oracle's) com.sun.codemodel project. We
decided to fork the project because by all evidence, the upstream project is
dead and not actively accepting outside contribution. All JBoss projects are
urged to use this project instead for source code generation.

%prep
%setup -q -n jdeparser2-%{namedversion}
%patch1 -p1


%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.0.3-alt1_8jpp11
- update

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 2.0.3-alt1_5jpp8
- jvm8 update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.0.3-alt1_2jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_5jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new release

