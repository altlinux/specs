Name: jackson-datatype-joda
Version: 2.5.0
Summary: Add-on module for Jackson to support Joda data-types
License: ASL 2.0
Url: http://wiki.fasterxml.com/JacksonModuleJoda
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-datatype-joda = 2.5.0-1.fc23
Provides: mvn(com.fasterxml.jackson.datatype:jackson-datatype-joda) = 2.5.0
Provides: mvn(com.fasterxml.jackson.datatype:jackson-datatype-joda:pom:) = 2.5.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml.jackson.core:jackson-annotations)
Requires: mvn(com.fasterxml.jackson.core:jackson-core)
Requires: mvn(com.fasterxml.jackson.core:jackson-databind)
Requires: mvn(joda-time:joda-time)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-datatype-joda-2.5.0-1.fc23.cpio

%description
This is a Jackson module that aims to provide
full support for data types of Joda date-time
library.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

