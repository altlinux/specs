Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          javapoet
Version:       1.7.0
Release:       alt1_12jpp11
Summary:       A Java API for generating .java source files
License:       ASL 2.0
URL:           https://github.com/square/javapoet
Source0:       https://github.com/square/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local

%if 0
# test dependencies
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.eclipse.jdt.core.compiler:ecj:4.4.2)
BuildRequires: mvn(org.mockito:mockito-core:1.10.16)
# missing test dependencies
BuildRequires: mvn(com.google.jimfs:jimfs:1.0)
BuildRequires: mvn(com.google.testing.compile:compile-testing:0.6)
BuildRequires: mvn(com.google.truth:truth:0.25)
%endif

BuildArch:     noarch
Source44: import.info

%description
A utility class which aids in generating Java source files.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file : %{name}

%build
# skip tests due to missing test dependencies
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.7.0-alt1_12jpp11
- fc34 update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_5jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_4jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_3jpp8
- new version

