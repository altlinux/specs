Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-module-jsonSchema
Version:       2.9.4
Release:       alt1_2jpp8
Summary:       Jackson JSON Schema Module
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-module-jsonSchema
Source0:       https://github.com/FasterXML/jackson-module-jsonSchema/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(javax.validation:validation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

BuildArch:      noarch
Source44: import.info

%description
Add-on module for to support JSON Schema version 3 generation.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i 's/\r//' src/main/resources/META-INF/LICENSE
cp -p src/main/resources/META-INF/LICENSE .

%mvn_file ":{*}" jackson-modules/@1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_2jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- java 8 mass update

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

