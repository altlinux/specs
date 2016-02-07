Name: castor-maven-plugin
Version: 2.5
Summary: Maven plugin for Castor XML's code generator
License: ASL 2.0
Url: http://www.mojohaus.org/castor-maven-plugin/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: castor-maven-plugin = 2.5-1.fc23
Provides: mvn(org.codehaus.mojo:castor-maven-plugin) = 2.5
Provides: mvn(org.codehaus.mojo:castor-maven-plugin:pom:) = 2.5
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.codehaus.castor:castor-codegen)
Requires: mvn(org.codehaus.castor:castor-xml-schema)
Requires: mvn(org.codehaus.plexus:plexus-compiler-api)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: castor-maven-plugin-2.5-1.fc23.cpio

%description
The Castor plugin is a Maven plugin that provides the functionality of Castor
XML's code generator for generating Java beans and associated descriptor
classes (required for marshaling to and unmarshaling from XML documents) from
XML Schema files.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

