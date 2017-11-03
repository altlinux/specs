Name: xmvn-install
Version: 3.0.0
Summary: XMvn Install
License: ASL 2.0
Url: https://fedora-java.github.io/xmvn/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-install) = 3.0.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-install:pom:) = 3.0.0
Provides: xmvn-install = 3.0.0-6.fc27
Requires: /bin/bash
Requires: java-headless
Requires: javapackages-tools
Requires: mvn(com.beust:jcommander)
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)
Requires: mvn(org.fedoraproject.xmvn:xmvn-core)
Requires: mvn(org.ow2.asm:asm)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.slf4j:slf4j-simple)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-install-3.0.0-6.fc27.cpio

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

mkdir -p %buildroot/etc/java
touch %buildroot/etc/java/xmvn.conf

%files -f %name-list
/etc/java/xmvn.conf

%changelog
* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

