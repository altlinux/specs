Name: javaewah-javadoc
Version: 0.8.4
Summary: Javadoc for javaewah
License: ASL 2.0
Url: http://code.google.com/p/javaewah/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: javaewah-javadoc = 0.8.4-5.fc23
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: javaewah-javadoc-0.8.4-5.fc23.cpio

%description
API documentation for javaewah.

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

