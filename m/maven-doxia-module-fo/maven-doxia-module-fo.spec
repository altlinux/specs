Name: maven-doxia-module-fo
Version: 1.6
Summary: FO module for maven-doxia
License: ASL 2.0
Url: http://maven.apache.org/doxia/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-doxia-module-fo = 0:1.6-3.fc23
Provides: mvn(org.apache.maven.doxia:doxia-module-fo) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-module-fo:pom:) = 1.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-configuration:commons-configuration)
Requires: mvn(log4j:log4j:1.2.12)
Requires: mvn(org.apache.maven.doxia:doxia-core)
Requires: mvn(org.apache.maven.doxia:doxia-logging-api)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.xmlgraphics:fop)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(xerces:xercesImpl)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-doxia-module-fo-1.6-3.fc23.cpio

%description
This package provides FO module for maven-doxia.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

