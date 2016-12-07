Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jackson-dataformat-xml
Version:       2.6.3
Release:       alt1_3jpp8
Summary:       XML data binding extension for Jackson
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonExtensionXmlDataBinding
Source0:       https://github.com/FasterXML/jackson-dataformat-xml/archive/%{name}-%{version}.tar.gz
# fix for CVE-2016-3720 (jackson-dataformat-xml issues#190)
# https://github.com/FasterXML/jackson-dataformat-xml/commit/f0f19a4c924d9db9a1e2830434061c8640092cc0
Patch0:        jackson-dataformat-xml-2.6.3-CVE-2016-3720.patch

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
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
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
%patch0 -p1

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
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_3jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

