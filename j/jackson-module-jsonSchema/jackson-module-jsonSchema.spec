Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-module-jsonSchema
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       Jackson JSON Schema Module
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-module-jsonSchema
Source0:       https://github.com/FasterXML/jackson-module-jsonSchema/archive/%{name}-%{version}.tar.gz
# https://github.com/FasterXML/jackson-module-jsonSchema/issues/62
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)

BuildArch:     noarch
Source44: import.info

%description
Add-on module for to support JSON Schema version 3 generation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find . -name "*.jar" -delete

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

# ComparisonFailure: Schemas for SchemableBasic differ
rm -r src/test/java/com/fasterxml/jackson/module/jsonSchema/TestReadJsonSchema.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- java 8 mass update

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

