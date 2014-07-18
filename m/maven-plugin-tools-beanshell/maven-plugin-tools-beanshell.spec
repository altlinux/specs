Name: maven-plugin-tools-beanshell
Version: 3.1
Summary: Maven Plugin Tool for Beanshell
License: ASL 2.0
Url: http://maven.apache.org/plugin-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-plugin-tools-beanshell
Requires: bsh
Requires: java
Requires: jpackage-utils
Requires: maven-plugin-descriptor
Requires: maven-plugin-tools
Requires: maven-plugin-tools-api
Requires: plexus-containers-component-annotations

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-tools-beanshell-3.1-5.fc18.cpio

%description
Descriptor extractor for plugins written in Beanshell.

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

