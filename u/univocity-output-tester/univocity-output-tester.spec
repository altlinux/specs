Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           univocity-output-tester
Summary:        Simple project to validate expected outputs of univocity parsers
Version:        2.1
Release:        alt1_5jpp11
License:        ASL 2.0

URL:            https://github.com/uniVocity/univocity-output-tester
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
Source44: import.info

%description
This very simple project was created by univocity to help you validate
the expected results of test cases that produce data samples and
non-trivial outputs, such as XML, CSV, collections and arrays, etc.

It enforces a consistent and organized testing structure and enables
you to easily see what is going on with your tests if you want to.


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.


%prep
%setup -q


%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin


%build
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE-2.0.html
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.html
%doc README.md


%changelog
* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 2.1-alt1_5jpp11
- new version

