Name: jackson-jaxrs-providers
Version: 2.5.0
Summary: Jackson JAX-RS providers
License: ASL 2.0
Url: http://wiki.fasterxml.com/JacksonHome
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-jaxrs-providers = 2.5.0-2.fc23
Provides: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-base) = 2.5.0
Provides: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-base:pom:) = 2.5.0
Provides: mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-providers:pom:) = 2.5.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml.jackson.core:jackson-core)
Requires: mvn(com.fasterxml.jackson.core:jackson-databind)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-jaxrs-providers-2.5.0-2.fc23.cpio

%description
This is a multi-module project that contains Jackson-based JAX-RS providers for
following data formats:

* JSON (https://github.com/FasterXML/jackson-core)
* Smile (https://github.com/FasterXML/jackson-dataformat-smile)
* XML (https://github.com/FasterXML/jackson-dataformat-xml)
* CBOR (https://github.com/FasterXML/jackson-dataformat-cbor)

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

