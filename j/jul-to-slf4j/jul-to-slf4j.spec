Name: jul-to-slf4j
Version: 1.7.12
Summary: JUL to SLF4J bridge
License: MIT and ASL 2.0
Url: http://www.slf4j.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jul-to-slf4j = 0:1.7.12-2.fc23
Provides: mvn(org.slf4j:jul-to-slf4j) = 1.7.12
Provides: mvn(org.slf4j:jul-to-slf4j:pom:) = 1.7.12
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jul-to-slf4j-1.7.12-2.fc23.cpio

%description
JUL to SLF4J bridge.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

