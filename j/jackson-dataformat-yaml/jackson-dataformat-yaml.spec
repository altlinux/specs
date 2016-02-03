Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-dataformat-yaml
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       Jackson module to add YAML back-end (parser/generator adapters)
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonExtensionYAML
Source0:       https://github.com/FasterXML/jackson-dataformat-yaml/archive/%{name}-%{version}.tar.gz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
BuildRequires: mvn(org.yaml:snakeyaml)
# Test deps
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)

BuildArch:     noarch
Source44: import.info

%description
Support for reading and writing YAML-encoded data via Jackson
abstractions.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} .
cp -p src/main/resources/META-INF/{LICENSE,NOTICE} .
sed -i 's/\r//' LICENSE NOTICE LICENSE-2.0.txt

%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin org.apache.servicemix.tooling:depends-maven-plugin

%pom_xpath_remove "pom:properties/pom:osgi.private"
%pom_xpath_remove "pom:properties/pom:osgi.import"
%pom_xpath_inject "pom:properties" "
    <osgi.import>
com.fasterxml.jackson.core,
com.fasterxml.jackson.core.base,
com.fasterxml.jackson.core.format,
com.fasterxml.jackson.core.io,
com.fasterxml.jackson.core.json,
com.fasterxml.jackson.core.type,
com.fasterxml.jackson.core.util,
com.fasterxml.jackson.databind,
org.yaml.snakeyaml,
org.yaml.snakeyaml.emitter,
org.yaml.snakeyaml.error,
org.yaml.snakeyaml.events,
org.yaml.snakeyaml.parser,
org.yaml.snakeyaml.reader
</osgi.import>"

# test deps
# pax-exam 4.3.0
%pom_remove_dep org.ops4j.pax.exam:pax-exam-container-native
%pom_remove_dep org.ops4j.pax.exam:pax-exam-junit4
%pom_remove_dep org.ops4j.pax.exam:pax-exam-link-mvn
# pax-url 2.2.0
%pom_remove_dep org.ops4j.pax.url:pax-url-aether
rm -r src/test/java/com/fasterxml/jackson/dataformat/yaml/failsafe/OSGiIT.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE LICENSE-2.0.txt NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE-2.0.txt NOTICE

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

