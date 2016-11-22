Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name coro-mock
%define version 1.0
%global git e55ca83

%global namedreltag -SNAPSHOT
%global namedversion %{version}%{?namedreltag}

Name: coro-mock
Version: 1.0
Release: alt1_0.10.e55ca83gitjpp8
Summary: A mock library for compiling JVM coroutine-using code on JVMs without coroutines
License: Public Domain
Url: https://github.com/headius/coro-mock
Source0: https://github.com/headius/%{name}/tarball/%{git}/headius-%{name}-%{git}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)

BuildArch: noarch
Source44: import.info

%description
A small mock library for compiling JVM coroutine-utilizing code on JVMs
without coroutines.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n headius-%{name}-%{git}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.10.e55ca83gitjpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.9.e55ca83gitjpp8
- java8 mass update

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.7.e55ca83gitjpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.e55ca83gitjpp7
- new release

