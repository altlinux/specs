Name: maven-shared-io
Version: 1.1
Summary: API for I/O support like logging, download or file scanning.
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-shared-io
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-io = 1:1.1-12.fc23
Provides: mvn(org.apache.maven.shared:maven-shared-io) = 1.1
Provides: mvn(org.apache.maven.shared:maven-shared-io:pom:) = 1.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.wagon:wagon-provider-api)
Requires: mvn(org.apache.maven:maven-artifact-manager)
Requires: mvn(org.apache.maven:maven-artifact:2.0.2)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: maven-shared-io-1.1-12.fc23.cpio

%description
API for I/O support like logging, download or file scanning.

This is a replacement package for maven-shared-io

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_5jpp7
- update

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

