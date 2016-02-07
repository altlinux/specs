Name: maven-xbean-plugin
Version: 4.3
Summary: XBean plugin for Apache Maven
License: ASL 2.0
Url: http://geronimo.apache.org/xbean/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-xbean-plugin = 4.3-1.fc23
Provides: mvn(org.apache.xbean:maven-xbean-plugin) = 4.3
Provides: mvn(org.apache.xbean:maven-xbean-plugin::sources:) = 4.3
Provides: mvn(org.apache.xbean:maven-xbean-plugin:pom:) = 4.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.thoughtworks.qdox:qdox)
Requires: mvn(org.apache.maven:maven-archiver)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.xbean:xbean-spring)
Requires: mvn(org.codehaus.plexus:plexus-archiver)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.springframework:spring-beans)
Requires: mvn(org.springframework:spring-context)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-xbean-plugin-4.3-1.fc23.cpio

%description
This package provides XBean plugin for Apache Maven.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

