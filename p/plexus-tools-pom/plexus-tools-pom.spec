Name: plexus-tools-pom
Version: 1.0.11
Summary: Plexus Tools POM
License: ASL 2.0
Url: http://plexus.codehaus.org/plexus-tools
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-tools-pom-1.0.11-7.fc19.cpio

%description
This package provides Plexus Tools parent POM used by different
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
* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

