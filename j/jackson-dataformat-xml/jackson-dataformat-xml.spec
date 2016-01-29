Name: jackson-dataformat-xml
Version: 2.5.0
Summary: XML data binding extension for Jackson
License: ASL 2.0
Url: http://wiki.fasterxml.com/JacksonExtensionXmlDataBinding
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-dataformat-xml = 2.5.0-2.fc23
Provides: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml) = 2.5.0
Provides: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-xml:pom:) = 2.5.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml.jackson.core:jackson-annotations)
Requires: mvn(com.fasterxml.jackson.core:jackson-core)
Requires: mvn(com.fasterxml.jackson.core:jackson-databind)
Requires: mvn(com.fasterxml.jackson.module:jackson-module-jaxb-annotations)
Requires: mvn(org.codehaus.woodstox:stax2-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-dataformat-xml-2.5.0-2.fc23.cpio

%description
Data format extension for Jackson (http://jackson.codehaus.org)
to offer alternative support for serializing POJOs as XML and
deserializing XML as POJOs. Support implemented on top of Stax API
(javax.xml.stream), by implementing core Jackson Streaming API types
like JsonGenerator, JsonParser and JsonFactory. Some data-binding types
overridden as well (ObjectMapper sub-classed as XmlMapper).

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

