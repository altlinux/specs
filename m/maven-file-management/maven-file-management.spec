Name: maven-file-management
Version: 1.2.1
Summary: Maven File Management API
License: ASL 2.0
Url: http://maven.apache.org/shared/file-management
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-file-management = 1:1.2.1-12.fc23
Provides: maven-shared-file-management = 1:1.2.1-12.fc23
Provides: mvn(org.apache.maven.shared:file-management) = 1.2.1
Provides: mvn(org.apache.maven.shared:file-management:pom:) = 1.2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.shared:maven-shared-io)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: maven-file-management-1.2.1-12.fc23.cpio

%description
Provides a component for plugins to easily resolve project dependencies.

This is a replacement package for maven-shared-file-management.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_0jpp7
- new release

