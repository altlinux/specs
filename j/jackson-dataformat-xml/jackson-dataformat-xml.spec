Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-dataformat-xml
Version:       2.7.6
Release:       alt1_4jpp8
Summary:       XML data binding extension for Jackson
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonExtensionXmlDataBinding
Source0:       https://github.com/FasterXML/jackson-dataformat-xml/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
BuildRequires: mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(javax.xml.stream:stax-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

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
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_3jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_3jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

