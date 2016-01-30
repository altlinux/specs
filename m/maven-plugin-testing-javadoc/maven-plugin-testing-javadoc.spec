Name: maven-plugin-testing-javadoc
Version: 3.3.0
Summary: Javadoc for maven-plugin-testing
License: ASL 2.0
Url: http://maven.apache.org/plugin-testing/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-testing-javadoc = 3.3.0-3.fc23
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-testing-javadoc-3.3.0-3.fc23.cpio

%description
API documentation for maven-plugin-testing.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

