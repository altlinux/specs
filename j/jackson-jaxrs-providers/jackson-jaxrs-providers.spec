Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-jaxrs-providers
Version:       2.9.4
Release:       alt1_2jpp8
Summary:       Jackson JAX-RS providers
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-jaxrs-providers
Source0:       https://github.com/FasterXML/jackson-jaxrs-providers/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.glassfish.jersey.containers:jersey-container-servlet)
BuildRequires:  mvn(org.glassfish.jersey.core:jersey-server)
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires:  mvn(org.ow2.asm:asm)

BuildArch:      noarch
Source44: import.info

%description
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats: JSON, Smile (binary JSON), XML, CBOR (another kind of
binary JSON), YAML.

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

%package datatypes
Group: Development/Java
Summary: Functionality for reading/writing core JAX-RS helper types

%description datatypes
Functionality for reading/writing core JAX-RS helper types.

%package parent
Group: Development/Java
Summary: Parent for Jackson JAX-RS providers

%description parent
Parent POM for Jackson JAX-RS providers.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p xml/src/main/resources/META-INF/LICENSE .
cp -p xml/src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

# Disable jar with no-meta-inf-services classifier, breaks build
%pom_remove_plugin :maven-jar-plugin cbor
%pom_remove_plugin :maven-jar-plugin json
%pom_remove_plugin :maven-jar-plugin smile
%pom_remove_plugin :maven-jar-plugin xml
%pom_remove_plugin :maven-jar-plugin yaml
%pom_remove_plugin :maven-jar-plugin datatypes

# Add missing deps to fix java.lang.ClassNotFoundException during tests
%pom_add_dep com.google.guava:guava:18.0:test datatypes cbor json smile xml yaml
%pom_add_dep org.ow2.asm:asm:5.1:test cbor json smile xml yaml

# Circular dep?
%pom_remove_dep org.jboss.resteasy:resteasy-jackson2-provider json
rm json/src/test/java/com/fasterxml/jackson/jaxrs/json/resteasy/RestEasyProviderLoadingTest.java

%build
%mvn_build -s 

%install
%mvn_install

%files -f .mfiles-jackson-jaxrs-base
%doc README.md release-notes/*
%doc --no-dereference LICENSE NOTICE

%files -n jackson-jaxrs-cbor-provider -f .mfiles-jackson-jaxrs-cbor-provider
%files -n jackson-jaxrs-json-provider -f .mfiles-jackson-jaxrs-json-provider
%files -n jackson-jaxrs-smile-provider -f .mfiles-jackson-jaxrs-smile-provider
%files -n jackson-jaxrs-xml-provider -f .mfiles-jackson-jaxrs-xml-provider
%files -n jackson-jaxrs-yaml-provider -f .mfiles-jackson-jaxrs-yaml-provider

%files datatypes -f .mfiles-jackson-datatype-jaxrs
%doc --no-dereference LICENSE NOTICE

%files parent -f .mfiles-jackson-jaxrs-providers
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_1jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

