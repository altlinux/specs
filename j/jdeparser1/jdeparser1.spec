Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jdeparser1
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jdeparser1
Version:          1.0.0
Release:          alt1_2jpp8
Summary:          Source generator library for Java
# MIT: src/main/java/org/jboss/jdeparser/JSynchronized.java
License:          (CDDL or GPLv2 with exceptions) and MIT
URL:              https://github.com/jdeparser/jdeparser
Source0:          https://github.com/jdeparser/jdeparser/archive/%{namedversion}.tar.gz
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
This project is a fork of Sun's (now Oracle's) com.sun.codemodel project. We
decided to fork the project because by all evidence, the upstream project is
dead and not actively accepting outside contribution. All JBoss projects are
urged to use this project instead for source code generation.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jdeparser-%{namedversion}

%mvn_compat_version : 1

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE-original.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE-original.html

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp8
- new version

