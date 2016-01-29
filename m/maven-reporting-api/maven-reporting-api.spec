Name: maven-reporting-api
Version: 3.0
Summary: API to manage report generation
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-reporting-api
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-reporting-api = 1:3.0-9.fc23
Provides: maven-shared-reporting-api = 1:3.0-9.fc23
Provides: mvn(org.apache.maven.reporting:maven-reporting-api) = 3.0
Provides: mvn(org.apache.maven.reporting:maven-reporting-api:pom:) = 3.0
Provides: mvn(org.apache.maven.shared:maven-reporting-api) = 3.0
Provides: mvn(org.apache.maven.shared:maven-reporting-api:pom:) = 3.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: maven-reporting-api-3.0-9.fc23.cpio

%description
API to manage report generation. Maven-reporting-api is included in Maven 2.x
core distribution, but moved to shared components to achieve report decoupling
from Maven 3 core.

This is a replacement package for maven-shared-reporting-api

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt1_3jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.0-alt1_0jpp7
- new version

