Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jackson-jaxrs-providers
Version:       2.6.3
Release:       alt1_2jpp8
Summary:       Jackson JAX-RS providers
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonHome
Source0:       https://github.com/FasterXML/jackson-jaxrs-providers/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires: mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(com.sun.jersey:jersey-core:1)
BuildRequires: mvn(com.sun.jersey:jersey-server:1)
BuildRequires: mvn(com.sun.jersey:jersey-servlet:1)
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlet)

BuildArch:     noarch
Source44: import.info

%description
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats:

* JSON (https://github.com/FasterXML/jackson-core)
* Smile (https://github.com/FasterXML/jackson-dataformat-smile)
* XML (https://github.com/FasterXML/jackson-dataformat-xml)
* CBOR (https://github.com/FasterXML/jackson-dataformat-cbor)
* YAML (https://github.com/FasterXML/jackson-dataformat-yaml) 

%package -n jackson-jaxrs-cbor-provider
Group: Development/Java
Summary:       Jackson-JAXRS-CBOR

%description -n jackson-jaxrs-cbor-provider
Functionality to handle CBOR encoded input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n jackson-jaxrs-json-provider
Group: Development/Java
Summary:       Jackson-JAXRS-JSON

%description -n jackson-jaxrs-json-provider
Functionality to handle JSON input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n jackson-jaxrs-smile-provider
Group: Development/Java
Summary:       Jackson-JAXRS-Smile

%description -n jackson-jaxrs-smile-provider
Functionality to handle Smile (binary JSON) input/output for
JAX-RS implementations (like Jersey and RESTeasy) using standard
Jackson data binding.

%package -n jackson-jaxrs-xml-provider
Group: Development/Java
Summary:       Jackson-JAXRS-XML

%description -n jackson-jaxrs-xml-provider
Functionality to handle Smile XML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n jackson-jaxrs-yaml-provider
Group: Development/Java
Summary:       Jackson-JAXRS-YAML

%description -n jackson-jaxrs-yaml-provider
Functionality to handle YAML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p xml/src/main/resources/META-INF/LICENSE .
cp -p xml/src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%pom_xpath_set "pom:properties/pom:version.jersey" 1

# Disable jar with no-meta-inf-services classifier, breaks build
%pom_remove_plugin :maven-jar-plugin cbor
%pom_remove_plugin :maven-jar-plugin json
%pom_remove_plugin :maven-jar-plugin smile
%pom_remove_plugin :maven-jar-plugin xml
%pom_remove_plugin :maven-jar-plugin yaml

# Circular dep?
%pom_remove_dep org.jboss.resteasy:resteasy-jackson2-provider json
rm json/src/test/java/com/fasterxml/jackson/jaxrs/json/resteasy/RestEasyProviderLoadingTest.java

%mvn_package ":jackson-jaxrs-providers" %{name}
%mvn_package ":jackson-jaxrs-base" %{name}

%build

%mvn_build -s 

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md release-notes/*
%doc LICENSE NOTICE

%files -n jackson-jaxrs-cbor-provider -f .mfiles-jackson-jaxrs-cbor-provider
%doc LICENSE NOTICE

%files -n jackson-jaxrs-json-provider -f .mfiles-jackson-jaxrs-json-provider
%doc LICENSE NOTICE

%files -n jackson-jaxrs-smile-provider -f .mfiles-jackson-jaxrs-smile-provider
%doc LICENSE NOTICE

%files -n jackson-jaxrs-xml-provider -f .mfiles-jackson-jaxrs-xml-provider
%doc LICENSE NOTICE

%files -n jackson-jaxrs-yaml-provider -f .mfiles-jackson-jaxrs-yaml-provider
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

