Name: maven-plugin-testing-harness
Version: 3.3.0
Summary: Maven Plugin Testing Mechanism
License: ASL 2.0
Url: http://maven.apache.org/plugin-testing/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-testing-harness = 3.3.0-3.fc23
Provides: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness) = 3.3.0
Provides: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness:pom:) = 3.3.0
Provides: mvn(org.apache.maven.shared:maven-plugin-testing-harness) = 3.3.0
Provides: mvn(org.apache.maven.shared:maven-plugin-testing-harness:pom:) = 3.3.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(org.codehaus.plexus:plexus-archiver)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-testing-harness-3.3.0-3.fc23.cpio

%description
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

