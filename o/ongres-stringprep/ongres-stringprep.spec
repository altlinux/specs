Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global     upstream_name   stringprep

Name:       ongres-%upstream_name
Version:    1.1
Release:    alt1_2jpp11
Summary:    RFC 3454 Preparation of Internationalized Strings in pure Java
License:    BSD
URL:            https://github.com/ongres/%upstream_name
Source0:        https://github.com/ongres/%upstream_name/archive/%{version}/%upstream_name-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  junit5
BuildRequires:  velocity
BuildRequires:  maven-plugin-build-helper
BuildRequires:  exec-maven-plugin
BuildRequires:  maven-enforcer-plugin
BuildArch:  noarch
Source44: import.info

%description
The stringprep protocol does not stand on its own;
it has to be used by other protocols at precisely-defined 
places in those other protocols.

%package javadoc
Group: Development/Java
Summary:    Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}

%prep
%setup -q -n %upstream_name-%{version}

find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep :velocity-tools codegenerator

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 1.1-alt1_2jpp11
- new version

