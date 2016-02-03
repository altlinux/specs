Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-dataformat-xml
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       XML data binding extension for Jackson
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonExtensionXmlDataBinding
Source0:       https://github.com/FasterXML/jackson-dataformat-xml/archive/%{name}-%{version}.tar.gz

%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
BuildRequires: mvn(javax.xml.stream:stax-api)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)

# test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: replacer

BuildArch:     noarch
Source44: import.info

%description
Data format extension for Jackson (http://jackson.codehaus.org)
to offer alternative support for serializing POJOs as XML and
deserializing XML as POJOs. Support implemented on top of Stax API
(javax.xml.stream), by implementing core Jackson Streaming API types
like JsonGenerator, JsonParser and JsonFactory. Some data-binding types
overridden as well (ObjectMapper sub-classed as XmlMapper).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%mvn_file : %{name}

%build

# see https://github.com/FasterXML/jackson-jaxrs-providers/issues/20
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

