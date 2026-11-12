%define _unpackaged_files_terminate_build 1

Name: jackson-jakarta-rs-providers
Version: 2.22.1
Release: alt1

Summary: Jackson providers for Jakarta RESTful Web Services
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-jakarta-rs-providers
VCS: https://github.com/FasterXML/jackson-jakarta-rs-providers.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.module:jackson-module-jakarta-xmlbind-annotations)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-smile)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires: mvn(jakarta.ws.rs:jakarta.ws.rs-api)
BuildRequires: mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)

%description
Parent POM for Jackson providers for Jakarta RESTful Web Services.

%package -n jackson-jakarta-rs-base
Summary: Jackson shared support for Jakarta RESTful Web Services
Group: Development/Java

%description -n jackson-jakarta-rs-base
Jackson shared support for the Jakarta RESTful Web Services API.

%package -n jackson-jakarta-rs-cbor-provider
Summary: Jackson CBOR provider for Jakarta RESTful Web Services
Group: Development/Java

%description -n jackson-jakarta-rs-cbor-provider
Jackson CBOR provider for the Jakarta RESTful Web Services API.

%package -n jackson-jakarta-rs-json-provider
Summary: Jackson JSON provider for Jakarta RESTful Web Services
Group: Development/Java

%description -n jackson-jakarta-rs-json-provider
Jackson JSON provider for the Jakarta RESTful Web Services API.

%package -n jackson-jakarta-rs-smile-provider
Summary: Jackson SMILE provider for Jakarta RESTful Web Services
Group: Development/Java

%description -n jackson-jakarta-rs-smile-provider
Jackson SMILE provider for the Jakarta RESTful Web Services API.

%package -n jackson-jakarta-rs-xml-provider
Summary: Jackson XML provider for Jakarta RESTful Web Services
Group: Development/Java

%description -n jackson-jakarta-rs-xml-provider
Jackson XML provider for the Jakarta RESTful Web Services API.

%package -n jackson-jakarta-rs-yaml-provider
Summary: Jackson YAML provider for Jakarta RESTful Web Services
Group: Development/Java

%description -n jackson-jakarta-rs-yaml-provider
Jackson YAML provider for the Jakarta RESTful Web Services API.

%prep
%setup

# Include the system Jakarta REST 4 API in the qualified bundle range.
%pom_xpath_set pom:project/pom:properties/pom:jakarta.ws.rs.version \
    '[3.0.0,5.0)'

# External publication metadata is not needed by the system Maven repository.
for module in base cbor json smile xml yaml; do
    %pom_remove_plugin org.gradlex:gradle-module-metadata-maven-plugin \
        "$module"
    %pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin "$module"
done

%mvn_package :jackson-jakarta-rs-providers jackson-jakarta-rs-providers
%mvn_package :jackson-jakarta-rs-base jackson-jakarta-rs-base
%mvn_package :jackson-jakarta-rs-cbor-provider jackson-jakarta-rs-cbor-provider
%mvn_package :jackson-jakarta-rs-json-provider jackson-jakarta-rs-json-provider
%mvn_package :jackson-jakarta-rs-smile-provider jackson-jakarta-rs-smile-provider
%mvn_package :jackson-jakarta-rs-xml-provider jackson-jakarta-rs-xml-provider
%mvn_package :jackson-jakarta-rs-yaml-provider jackson-jakarta-rs-yaml-provider

%build
%mvn_build -f -j -s -- -Dmaven.source.skip=true

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%files -n jackson-jakarta-rs-base -f .mfiles-jackson-jakarta-rs-base

%files -n jackson-jakarta-rs-cbor-provider -f .mfiles-jackson-jakarta-rs-cbor-provider

%files -n jackson-jakarta-rs-json-provider -f .mfiles-jackson-jakarta-rs-json-provider

%files -n jackson-jakarta-rs-smile-provider -f .mfiles-jackson-jakarta-rs-smile-provider

%files -n jackson-jakarta-rs-xml-provider -f .mfiles-jackson-jakarta-rs-xml-provider

%files -n jackson-jakarta-rs-yaml-provider -f .mfiles-jackson-jakarta-rs-yaml-provider

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 2.22.1-alt1
- Initial build for ALT.
