Name: maven-wagon-providers
Version: 2.9
Summary: providers module for maven-wagon
License: ASL 2.0
Url: http://maven.apache.org/wagon
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-wagon-providers = 0:2.9-4.fc23
Provides: mvn(org.apache.maven.wagon:wagon-providers:pom:) = 2.9
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.wagon:wagon-provider-api)
Requires: mvn(org.apache.maven.wagon:wagon:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-wagon-providers-2.9-4.fc23.cpio

%description
providers module for maven-wagon

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

