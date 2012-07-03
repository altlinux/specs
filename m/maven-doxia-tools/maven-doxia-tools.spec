Name: maven-doxia-tools
Version: 1.4
Summary: Maven Doxia Integration Tools
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-doxia-tools/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: apache-commons-io
Requires: jpackage-utils
Requires: maven-doxia
Requires: maven-doxia-sitetools
Requires: maven-shared
Requires: plexus-container-default
Requires: plexus-i18n
Requires: plexus-interpolation
Requires: plexus-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-doxia-tools-1.4-4.fc17.cpio

%description
A collection of tools to help the integration of Doxia in Maven plugins.

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
* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

