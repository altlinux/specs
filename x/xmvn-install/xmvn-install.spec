Name: xmvn-install
Version: 2.4.0
Summary: XMvn Install
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-install) = 2.4.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-install:pom:) = 2.4.0
Provides: xmvn-install = 2.4.0-5.fc23
Requires: /bin/sh
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.beust:jcommander)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
Requires: mvn(org.fedoraproject.xmvn:xmvn-core)
Requires: mvn(org.ow2.asm:asm)
Requires: mvn(org.slf4j:slf4j-simple)
Requires: mvn(org.sonatype.sisu:sisu-guice::no_aop:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-install-2.4.0-5.fc23.cpio

%description
This package provides XMvn Install, which is a command-line interface
to XMvn installer.  The installer reads reactor metadata and performs
artifact installation according to specified configuration.

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

