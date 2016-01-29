Name: jna-contrib
Version: 4.1.0
Summary: Contrib for jna
License: LGPLv2 or ASL 2.0
Url: https://github.com/twall/jna
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jna-contrib = 4.1.0-9.fc23
Provides: mvn(net.java.dev.jna:jna-platform) = 4.1.0.SNAPSHOT
Provides: mvn(net.java.dev.jna:jna-platform:pom:) = 4.1.0.SNAPSHOT
Provides: mvn(net.java.dev.jna:platform) = 4.1.0.SNAPSHOT
Provides: mvn(net.java.dev.jna:platform:pom:) = 4.1.0.SNAPSHOT
Requires: java-headless
Requires: jna
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jna-contrib-4.1.0-9.fc23.cpio

%description
This package contains the contributed examples for jna.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

