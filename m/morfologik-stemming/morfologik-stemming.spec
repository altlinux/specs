%define _unpackaged_files_terminate_build 1

Name: morfologik-stemming
Version: 2.1.9
Release: alt1

Summary: Morfologik stemming libraries and tools
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/morfologik/morfologik-stemming
VCS: https://github.com/morfologik/morfologik-stemming

Source0: %name-%version.tar.gz
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(de.thetaphi:forbiddenapis)
BuildRequires: mvn(com.beust:jcommander)
BuildRequires: mvn(com.carrotsearch:hppc)
BuildRequires: mvn(com.carrotsearch.randomizedtesting:junit4-maven-plugin)
BuildRequires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)

BuildArch: noarch

%description
Morfologik provides finite state automata, stemming, spelling, Polish
dictionary and command-line tools.

%package fsa
Group: Development/Java
Summary: Finite state automata library

%description fsa
Morfologik finite state automata library.

%package fsa-builders
Group: Development/Java
Summary: Finite state automata builders

%description fsa-builders
Morfologik finite state automata construction library.

%package speller
Group: Development/Java
Summary: Spelling library

%description speller
Morfologik spelling library.

%package polish
Group: Development/Java
Summary: Polish stemming and dictionary support

%description polish
Morfologik Polish language stemmer and dictionary.

%package tools
Group: Development/Java
Summary: Command-line tools

%description tools
Command-line utilities for building and inspecting Morfologik dictionaries.

%package javadoc
Group: Development/Java
Summary: Javadoc for Morfologik

%description javadoc
API documentation for Morfologik modules.

%prep
%setup -q
%autopatch -p1

%mvn_package :morfologik-parent morfologik-stemming
%mvn_package :morfologik-fsa morfologik-fsa
%mvn_package :morfologik-fsa-builders morfologik-fsa-builders
%mvn_package :morfologik-stemming morfologik-stemming
%mvn_package :morfologik-speller morfologik-speller
%mvn_package :morfologik-polish morfologik-polish
%mvn_package :morfologik-tools morfologik-tools
%mvn_package :::sources: __noinstall

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-assembly-plugin morfologik-tools
%pom_xpath_set pom:addClasspath false morfologik-tools

%build
%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-morfologik-stemming
%doc --no-dereference LICENSE.txt
%doc CHANGES.txt CONTRIBUTING.txt

%files fsa -f .mfiles-morfologik-fsa

%files fsa-builders -f .mfiles-morfologik-fsa-builders

%files speller -f .mfiles-morfologik-speller

%files polish -f .mfiles-morfologik-polish

%files tools -f .mfiles-morfologik-tools

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 2.1.9-alt1
- New version.

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.0.1-alt2_9jpp8
- fixed build with new beust-jcommander 1.78

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_9jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_4jpp8
- new fc release

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1_4jpp8
- java 8 mass update
