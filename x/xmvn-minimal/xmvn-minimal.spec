Name: xmvn-minimal
Version: 3.0.0
Summary: Dependency-reduced version of XMvn
License: ASL 2.0
Url: https://fedora-java.github.io/xmvn/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: xmvn-minimal = 3.0.0-6.fc27
Requires: /bin/sh
Requires: apache-commons-cli
Requires: apache-commons-lang3
Requires: atinject
Requires: google-guice
Requires: guava
Requires: maven-lib
Requires: maven-lib
Requires: maven-resolver-api
Requires: maven-resolver-impl
Requires: maven-resolver-spi
Requires: maven-resolver-util
Requires: maven-wagon-provider-api
Requires: plexus-cipher
Requires: plexus-classworlds
Requires: plexus-containers-component-annotations
Requires: plexus-interpolation
Requires: plexus-sec-dispatcher
Requires: plexus-utils
Requires: sisu-inject
Requires: sisu-plexus
Requires: slf4j
Requires: xmvn-api
Requires: xmvn-connector-aether
Requires: xmvn-core

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-minimal-3.0.0-6.fc27.tar

%description
This package provides minimal version of XMvn, incapable of using
remote repositories.

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
* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

