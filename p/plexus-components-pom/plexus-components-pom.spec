Name: plexus-components-pom
Version: 1.2
Summary: Plexus Components POM
License: ASL 2.0
Url: http://plexus.codehaus.org/plexus-components
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-components-pom-1.2-6.fc19.cpio

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

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
* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

