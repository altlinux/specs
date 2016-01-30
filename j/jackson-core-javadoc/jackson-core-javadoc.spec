Name: jackson-core-javadoc
Version: 2.5.0
Summary: Javadoc for jackson-core
License: ASL 2.0
Url: http://wiki.fasterxml.com/JacksonHome
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-core-javadoc = 2.5.0-2.fc23
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-core-javadoc-2.5.0-2.fc23.cpio

%description
This package contains javadoc for jackson-core.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

