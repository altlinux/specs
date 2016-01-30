Name: maven-doxia-sitetools-javadoc
Version: 1.6
Summary: Javadoc for maven-doxia-sitetools
License: ASL 2.0
Url: http://maven.apache.org/doxia/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-doxia-sitetools-javadoc = 1.6-2.fc23
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-doxia-sitetools-javadoc-1.6-2.fc23.cpio

%description
API documentation for maven-doxia-sitetools.

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

