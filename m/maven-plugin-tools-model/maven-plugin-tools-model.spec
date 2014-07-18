Name: maven-plugin-tools-model
Version: 3.1
Summary: Maven Plugin Metadata Model
License: ASL 2.0
Url: http://maven.apache.org/plugin-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-plugin-tools-model
Requires: java
Requires: jpackage-utils
Requires: maven-plugin-descriptor
Requires: maven-plugin-tools
Requires: plexus-containers-container-default
Requires: plexus-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-tools-model-3.1-5.fc18.cpio

%description
The Maven Plugin Metadata Model provides an API to play with the Metadata
model.

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
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

