Name: maven-release-javadoc
Version: 2.2.1
Summary: Javadoc for maven-release
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-release-plugin/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-release-javadoc = 2.2.1-13.fc21
Provides: maven-release-manager-javadoc = 2.2.1-13.fc21
Provides: maven-release-plugin-javadoc = 2.2.1-13.fc21
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: maven-release-javadoc-2.2.1-13.fc21.cpio

%description
This package contains the API documentation for maven-release.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

