Name: maven-repository-builder
Version: 1.0
Summary: Maven repository builder
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-repository-builder/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-repository-builder = 1:1.0-2.fc23
Provides: maven-shared-repository-builder = 1:1.0-2.fc23
Provides: mvn(org.apache.maven.shared:maven-repository-builder) = 1.0
Provides: mvn(org.apache.maven.shared:maven-repository-builder:pom:) = 1.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-codec:commons-codec)
Requires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-artifact-manager)
Requires: mvn(org.apache.maven:maven-project)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: maven-repository-builder-1.0-2.fc23.cpio

%description
Maven repository builder.

This is a replacement package for maven-shared-repository-builder

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.3.alpha2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.0.alpha2jpp7
- new release

