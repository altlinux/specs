# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name clojure
%define version 1.7.0
%global project     clojure
%global groupId     org.clojure
%global artifactId  clojure
%global archivename %{project}-%{artifactId}
%global full_version %{version}

Name:           clojure
Epoch:          1
Version:        1.7.0
Release:        alt1_1jpp8
Summary:        A dynamic programming language that targets the Java Virtual Machine

Group:          Development/Java
License:        EPL
URL:            http://clojure.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-%{full_version}.zip

Source1:        clojure.sh

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-local
BuildRequires:  ant >= 1.6
BuildRequires:  objectweb-asm

%if 0%{?fedora} > 20
%else
%endif

Requires:       objectweb-asm
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
%setup -q -n %{archivename}-%{full_version}

%build
ant -Dmaven.test.skip=1

%mvn_artifact pom.xml %{name}.jar

%install
# jar - link to prefix'd jar so that java stuff knows where to look
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# startup script
install -d -m 755 %{buildroot}%{_bindir}
install -pm 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%mvn_install

%files -f .mfiles
%doc epl-v10.html changes.md readme.txt 
%{_mavenpomdir}/*
%{_javadir}/%{name}.jar
%{_bindir}/%{name}

%changelog
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

