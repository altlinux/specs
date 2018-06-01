Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           univocity-parsers
Version:        2.5.5
Release:        alt1_2jpp8
Summary:        Collection of parsers for Java
License:        ASL 2.0
URL:            https://github.com/uniVocity/univocity-parsers
BuildArch:      noarch

Source0:        https://github.com/uniVocity/univocity-parsers/archive/v%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
Source44: import.info

%description
uniVocity-parsers is a suite of extremely fast and reliable parsers
for Java.  It provides a consistent interface for handling different
file formats, and a solid framework for the development of new
parsers.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin :nexus-staging-maven-plugin

%build
# Tests require univocity-output-tester, which is not packaged yet.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-2.0.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.html

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1_2jpp8
- new version

