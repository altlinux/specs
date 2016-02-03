Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-dataformat-cbor
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       Jackson data format module for Concise Binary Object Representation (CBOR)
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/
Source0:       https://github.com/FasterXML/jackson-dataformat-cbor/archive/%{name}-%{version}.tar.gz

%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
# test deps
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: replacer

BuildArch:     noarch
Source44: import.info

%description
Support for reading and writing Concise Binary Object Representation (CBOR),
see: https://www.rfc-editor.org/info/rfc7049 encoded data using Jackson
abstractions (streaming API, data binding, tree model).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp -p src/main/resources/META-INF/LICENSE .
sed -i 's/\r//' LICENSE

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

