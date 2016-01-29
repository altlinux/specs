Name: plexus-containers-container-default
Version: 1.6
Summary: Default Container from plexus-containers
License: ASL 2.0 and MIT
Url: https://github.com/codehaus-plexus/plexus-containers
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.plexus:containers-component-api) = 1.6
Provides: mvn(org.codehaus.plexus:containers-component-api:pom:) = 1.6
Provides: mvn(org.codehaus.plexus:plexus-container-default) = 1.6
Provides: mvn(org.codehaus.plexus:plexus-container-default:pom:) = 1.6
Provides: plexus-containers-component-api = 1.6-4.fc23
Provides: plexus-containers-container-default = 1.6-4.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.google.collections:google-collections)
Requires: mvn(org.apache.xbean:xbean-reflect)
Requires: mvn(org.codehaus.plexus:plexus-classworlds)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.ow2.asm:asm)
Requires: mvn(org.ow2.asm:asm-commons)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: plexus-containers-container-default-1.6-4.fc23.cpio

%description
Default Container from plexus-containers.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

