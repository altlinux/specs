Name: xmvn
Version: 0.3.1
Summary: Local Extensions for Apache Maven
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: beust-jcommander
Requires: java
Requires: jpackage-utils
Requires: maven
Requires: plexus-classworlds
Requires: xml-commons-apis

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-0.3.1-2.fc19.cpio

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

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
mkdir -p %buildroot/etc/java/
touch %buildroot/etc/java/xmvn.conf

%files -f %name-list
/etc/java/xmvn.conf
%changelog
* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

