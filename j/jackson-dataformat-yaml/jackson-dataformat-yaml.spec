Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jackson-dataformat-yaml
Version:       2.7.6
Release:       alt1_1jpp8
Summary:       Jackson module to add YAML back-end (parser/generator adapters)
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonExtensionYAML
Source0:       https://github.com/FasterXML/jackson-dataformat-yaml/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.yaml:snakeyaml)

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

cp -p src/main/resources/META-INF/{LICENSE,NOTICE} .
sed -i 's/\r//' LICENSE NOTICE

%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin org.apache.servicemix.tooling:depends-maven-plugin

%pom_xpath_remove "pom:properties/pom:osgi.private"

# test deps
%pom_remove_dep org.ops4j.pax.exam:pax-exam-container-native
%pom_remove_dep org.ops4j.pax.exam:pax-exam-junit4
%pom_remove_dep org.ops4j.pax.exam:pax-exam-link-mvn
%pom_remove_dep org.ops4j.pax.url:pax-url-aether
rm -r src/test/java/com/fasterxml/jackson/dataformat/yaml/failsafe/OSGiIT.java

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_1jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

