Name: maven-timestamp-plugin
Version: 1.1
Summary: Provides formatted timestamps for maven builds
License: ASL 2.0
Url: http://code.google.com/p/maven-timestamp-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: java
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-timestamp-plugin-1.1-3.fc18.cpio

%description
There are a few ways to get a timestamp in your maven build. Unfortunately
most of them make you jump through giant hoops. This maven plugin makes it
as simple as 1-2-3 to create a timestamp at your disposal.
Also, it enables you to use the syntax of SimpleDateFormat to form custom
formatted dates.

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
* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

