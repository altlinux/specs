Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with jp_minimal

Name:          jackson-datatypes-collections
Version:       2.9.8
Release:       alt1_1jpp8
Summary:       Jackson datatypes: collections
# Source files without license headers https://github.com/FasterXML/jackson-datatypes-collections/issues/10
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-datatypes-collections
Source0:       https://github.com/FasterXML/jackson-datatypes-collections/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%if %{without jp_minimal}
BuildRequires:  mvn(com.carrotsearch:hppc)
%endif

BuildArch:      noarch
Source44: import.info

%description
This is a multi-module umbrella project for various Jackson
Data-type modules to support 3rd party Collection libraries.

Currently included are:
* Guava data-type
* HPPC data-type
* PCollections data-type

%package -n jackson-datatype-guava
Group: Development/Java
Summary:       Add-on module for Jackson which handles Guava data-types

%description -n jackson-datatype-guava
Add-on datatype-support module for Jackson that handles
Guava types (currently mostly just collection ones).

%if %{without jp_minimal}
%package -n jackson-datatype-hppc
Group: Development/Java
Summary:       Add-on module for Jackson to support HPPC data-types

%description -n jackson-datatype-hppc
Jackson data-type module to support JSON serialization and
deserialization of High-Performance Primitive Collections
data-types.
%endif

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i 's/\r//' hppc/src/main/resources/META-INF/LICENSE
cp -p hppc/src/main/resources/META-INF/LICENSE .

%if %{with jp_minimal}
# Disable modules with additional deps
%pom_disable_module hppc
%endif

# Deps are missing from Fedora for these modules:
%pom_disable_module eclipse-collections
%pom_disable_module pcollections

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-datatypes-collections
%doc README.md release-notes
%doc --no-dereference LICENSE

%files -n jackson-datatype-guava -f .mfiles-jackson-datatype-guava
%doc guava/README.md guava/release-notes
%doc --no-dereference LICENSE

%if %{without jp_minimal}
%files -n jackson-datatype-hppc -f .mfiles-jackson-datatype-hppc
%doc hppc/README.md hppc/release-notes
%doc --no-dereference LICENSE
%endif

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_4jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_3jpp8
- new version

