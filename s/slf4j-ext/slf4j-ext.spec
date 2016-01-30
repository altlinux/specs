Name: slf4j-ext
Version: 1.7.12
Summary: SLF4J Extensions Module
License: MIT and ASL 2.0
Url: http://www.slf4j.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.slf4j:slf4j-ext) = 1.7.12
Provides: mvn(org.slf4j:slf4j-ext:pom:) = 1.7.12
Provides: slf4j-ext = 0:1.7.12-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(ch.qos.cal10n:cal10n-api)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: slf4j-ext-1.7.12-2.fc23.cpio

%description
Extensions to the SLF4J API.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

