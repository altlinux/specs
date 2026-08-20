Name:           jackson-jaxrs-providers
Version:        2.22.1
Release:        alt1

Summary:        Jackson JAX-RS providers
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/FasterXML/jackson-jaxrs-providers
VCS:            https://github.com/FasterXML/jackson-jaxrs-providers

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server:9.4)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet:9.4)
BuildRequires:  mvn(org.glassfish.jersey.core:jersey-server)
BuildRequires:  mvn(org.glassfish.jersey.containers:jersey-container-servlet)
BuildRequires:  mvn(org.glassfish.jersey.inject:jersey-hk2)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires:  mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jackson2-provider)
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)

BuildArch:      noarch

%description
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats: JSON, Smile (binary JSON), XML, CBOR (another kind of
binary JSON), YAML.

%javadoc_package

%package -n     jackson-jaxrs-base
Summary:        Jackson-JAXRS: base
Group:          Development/Java

%description -n jackson-jaxrs-base
Pile of code that is shared by all Jackson-based JAX-RS providers.

%package -n     jackson-datatype-jaxrs
Summary:        Jackson-JAXRS: Datatypes
Group:          Development/Java

%description -n jackson-datatype-jaxrs
Functionality for reading/writing core JAX-RS helper types.

%package -n     jackson-jaxrs-cbor-provider
Summary:        Jackson-JAXRS: CBOR
Group:          Development/Java

%description -n jackson-jaxrs-cbor-provider
Functionality to handle CBOR encoded input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n     jackson-jaxrs-json-provider
Summary:        Jackson-JAXRS: JSON
Group:          Development/Java

%description -n jackson-jaxrs-json-provider
Functionality to handle JSON input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n     jackson-jaxrs-smile-provider
Summary:        Jackson-JAXRS: Smile
Group:          Development/Java

%description -n jackson-jaxrs-smile-provider
Functionality to handle Smile (binary JSON) input/output for JAX-RS
implementations (like Jersey and RESTeasy) using standard Jackson data binding.

%package -n     jackson-jaxrs-xml-provider
Summary:        Jackson-JAXRS: XML
Group:          Development/Java

%description -n jackson-jaxrs-xml-provider
Functionality to handle XML input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

%package -n     jackson-jaxrs-yaml-provider
Summary:        Jackson-JAXRS: YAML
Group:          Development/Java

%description -n jackson-jaxrs-yaml-provider
Functionality to handle YAML input/output for JAX-RS implementations (like
Jersey and RESTeasy) using standard Jackson data binding.

%prep
%setup

%pom_change_dep javax.ws.rs:javax.ws.rs-api org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec

# Use packaged Jetty 9 compat artifacts
%pom_xpath_set "pom:properties/pom:version.jetty" "9.4"

%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :cyclonedx-maven-plugin
%pom_remove_plugin -r :moditect-maven-plugin

%build
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-jackson-jaxrs-providers
%doc *.md LICENSE

%files -n jackson-jaxrs-base -f .mfiles-jackson-jaxrs-base
%files -n jackson-datatype-jaxrs -f .mfiles-jackson-datatype-jaxrs
%files -n jackson-jaxrs-cbor-provider -f .mfiles-jackson-jaxrs-cbor-provider
%files -n jackson-jaxrs-json-provider -f .mfiles-jackson-jaxrs-json-provider
%files -n jackson-jaxrs-smile-provider -f .mfiles-jackson-jaxrs-smile-provider
%files -n jackson-jaxrs-xml-provider -f .mfiles-jackson-jaxrs-xml-provider
%files -n jackson-jaxrs-yaml-provider -f .mfiles-jackson-jaxrs-yaml-provider

%changelog
* Wed Aug 19 2026 Evgeniy Serov <scala@altlinux.org> 2.22.1-alt1
- Updated to 2.22.1.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.11.2-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.10.2-alt1_2jpp8
- new version

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt2_1jpp8
- build with new jersey

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_4jpp8
- new version

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

