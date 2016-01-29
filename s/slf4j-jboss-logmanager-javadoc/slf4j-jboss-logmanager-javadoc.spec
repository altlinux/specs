Name: slf4j-jboss-logmanager-javadoc
Version: 1.0.0
Summary: Javadocs for slf4j-jboss-logmanager
License: LGPLv2+
Url: http://www.jboss.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: slf4j-jboss-logmanager-javadoc = 1.0.0-9.fc22
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: slf4j-jboss-logmanager-javadoc-1.0.0-9.fc22.cpio

%description
This package contains the API documentation for slf4j-jboss-logmanager.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

