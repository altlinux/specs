Name: maven-test-tools
Version: 3.3.0
Summary: Maven Testing Tool
License: ASL 2.0
Url: http://maven.apache.org/plugin-testing/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-test-tools = 3.3.0-3.fc23
Provides: mvn(org.apache.maven.plugin-testing:maven-test-tools) = 3.3.0
Provides: mvn(org.apache.maven.plugin-testing:maven-test-tools:pom:) = 3.3.0
Provides: mvn(org.apache.maven.shared:maven-test-tools) = 3.3.0
Provides: mvn(org.apache.maven.shared:maven-test-tools:pom:) = 3.3.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.easymock:easymock)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-test-tools-3.3.0-3.fc23.cpio

%description
Framework to test Maven Plugins with Easymock objects.

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
* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

