Name: maven-archiver
Version: 2.5
Summary: Maven Archiver
Epoch: 0
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-archiver/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-archiver
Requires: maven
Requires: plexus-archiver
Requires: plexus-interpolation
Requires: plexus-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-archiver-2.5-2.fc18.cpio

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

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
* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

