Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-datatype-guava
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       Add-on module for Jackson JSON processor which handles Guava data-types
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonModuleGuava
Source0:       https://github.com/FasterXML/jackson-datatype-guava/archive/%{name}-%{version}.tar.gz

%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.guava:guava) >= 15.0
# test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: replacer

BuildArch:     noarch
Source44: import.info

%description
Add-on datatype-support module for Jackson that handles
Guava types (currently mostly just collection ones).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i 's/\r//' src/main/resources/META-INF/LICENSE
cp -p src/main/resources/META-INF/LICENSE .

%pom_xpath_remove "pom:properties/pom:osgi.import"
%pom_xpath_inject "pom:properties" "
    <osgi.import>
com.google.common.collect,
com.google.common.base,
com.google.common.cache,
com.google.common.hash,
com.google.common.net,
com.fasterxml.jackson.core,
com.fasterxml.jackson.core.util,
com.fasterxml.jackson.databind,
com.fasterxml.jackson.databind.deser,
com.fasterxml.jackson.databind.deser.std,
com.fasterxml.jackson.databind.introspect,
com.fasterxml.jackson.databind.jsonFormatVisitors,
com.fasterxml.jackson.databind.jsontype,
com.fasterxml.jackson.databind.ser,
com.fasterxml.jackson.databind.ser.std,
com.fasterxml.jackson.databind.ser.impl,
com.fasterxml.jackson.databind.type,
com.fasterxml.jackson.databind.util
</osgi.import>"


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
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

