Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           lancer
Version:        0.0.2
Release:        alt1_14jpp11
Summary:        Probability and statistics classes for Java
License:        ASL 2.0
URL:            https://github.com/willb/lancer/
Source0:        https://github.com/willb/lancer/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-math3)
Source44: import.info

%description
Lancer is a reimplementation of some functionality provided by the
(non-free) Colt library.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q

echo %{summary} > README

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0.0.2-alt1_14jpp11
- new version

