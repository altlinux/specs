Name: maven-plugin-descriptor
Version: 2.2.1
Summary: Maven Plugin Description Model
License: ASL 2.0 and MIT and BSD
Url: http://maven.apache.org
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-descriptor = 2.2.1-52.fc23
Provides: mvn(org.apache.maven:maven-plugin-descriptor) = 2.2.1
Provides: mvn(org.apache.maven:maven-plugin-descriptor:pom:) = 2.2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-container-default)

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: maven-plugin-descriptor-2.2.1-52.fc23.cpio

%description
Maven plugin descriptor artifact

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

