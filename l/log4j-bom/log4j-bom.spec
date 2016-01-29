Name: log4j-bom
Version: 2.3
Summary: Apache Log4j BOM
License: ASL 2.0
Url: http://logging.apache.org/log4j
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: log4j-bom = 2.3-2.fc23
Provides: mvn(org.apache.logging.log4j:log4j-bom:pom:) = 2.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.rat:apache-rat-plugin)
Requires: mvn(org.apache:apache:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: log4j-bom-2.3-2.fc23.cpio

%description
Apache Log4j 2 Bill of Material

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

