Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global project     clojure
%global groupId     org.clojure
%global artifactId  clojure
%global archivename %{project}-%{artifactId}

Name:           clojure
Epoch:          1
Version:        1.11.1
Release:        alt1_3jpp11
Summary:        A dynamic programming language that targets the Java Virtual Machine

License:        EPL-1.0
URL:            http://clojure.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-%{version}.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.clojure:core.specs.alpha)
BuildRequires:  mvn(org.clojure:spec.alpha)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:       javapackages-tools
Source44: import.info

%description 
Clojure is a dynamic programming language that targets the Java
Virtual Machine. It is designed to be a general-purpose language,
combining the approachability and interactive development of a
scripting language with an efficient and robust infrastructure for
multithreaded programming. Clojure is a compiled language - it
compiles directly to JVM bytecode, yet remains completely
dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides easy access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
%setup -q -n %{archivename}-%{version}

%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

%build
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install

%mvn_install

# startup script
%jpackage_script clojure.main "" "" clojure:clojure-spec-alpha:clojure-core-specs-alpha clojure false

%files -f .mfiles
%doc --no-dereference epl-v10.html 
%doc changes.md readme.txt 
%{_bindir}/%{name}

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:1.11.1-alt1_3jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 1:1.10.3-alt1_2jpp11
- new version

* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 1:1.10.2-alt1_1jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:1.10.1-alt1_5jpp11
- new version

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1:1.10.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.8.0-alt1_1jpp8
- new version

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7.0-alt2_1jpp8
- fixed build

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7.0-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.5.1-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.5.1-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_3jpp7
- new release

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.3.0-alt1_1jpp6
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_1jpp6
- update to new release by jppimport

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.2.0-alt1_1jpp6
- new version (closes: #24726)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 20080916-alt1_2jpp5
- first build

