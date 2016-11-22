# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jdeparser
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jdeparser
Version:          1.0.0
Release:          alt1_5jpp8
Summary:          Source generator library for Java
Group:            Development/Other
# See README.md
License:          (CDDL or GPLv2 with exceptions) and MIT
URL:              https://github.com/jdeparser/jdeparser

# git clone git://github.com/jdeparser/jdeparser.git
# cd jdeparser && git archive --format=tar --prefix=jdeparser-1.0.0.Final/ 1.0.0.Final | xz > jdeparser-1.0.0.Final.tar.xz
Source0:          jdeparser-%{namedversion}.tar.xz
BuildArch:        noarch

BuildRequires:    maven-local
Source44: import.info

%description
This project is a fork of Sun's (now Oracle's) com.sun.codemodel project. We
decided to fork the project because by all evidence, the upstream project is
dead and not actively accepting outside contribution. All JBoss projects are
urged to use this project instead for source code generation.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jdeparser-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-original.html
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE-original.html

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new release

