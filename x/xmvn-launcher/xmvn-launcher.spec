%filter_from_requires /^java-headless/d
Name: xmvn-launcher
Version: 2.5.0
Summary: XMvn Launcher
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-launcher) = 2.5.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-launcher:pom:) = 2.5.0
Provides: xmvn-launcher = 2.5.0-6.fc24
Requires: jpackage-utils
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-launcher-2.5.0-6.fc24.cpio

%description
This package provides XMvn Launcher module, which provides a way of
launching XMvn running in isolated class realm and locating XMVn
services.

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
* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

