Name: jackson-jaxrs-cbor-provider
Version: 2.5.0
Summary: Jackson-JAXRS-CBOR
License: ASL 2.0
Url: http://wiki.fasterxml.com/JacksonHome
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-jaxrs-cbor-provider = 2.5.0-2.fc23
Provides: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-cbor-provider) = 2.5.0
Provides: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-cbor-provider:pom:) = 2.5.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml.jackson.core:jackson-core)
Requires: mvn(com.fasterxml.jackson.core:jackson-databind)
Requires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
Requires: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-base)
Requires: mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-jaxrs-cbor-provider-2.5.0-2.fc23.cpio

%description
Functionality to handle CBOR encoded input/output for JAX-RS implementations
(like Jersey and RESTeasy) using standard Jackson data binding.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

