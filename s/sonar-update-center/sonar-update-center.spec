Name: sonar-update-center
Version: 1.12.1
Summary: Sonar Update Center
License: LGPLv3+
Url: http://www.sonarqube.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.sonar:sonar-update-center-common) = 1.12.1
Provides: mvn(org.codehaus.sonar:sonar-update-center-common:pom:) = 1.12.1
Provides: mvn(org.codehaus.sonar:sonar-update-center:pom:) = 1.12.1
Provides: sonar-update-center = 1.12.1-4.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.google.code.findbugs:jsr305)
Requires: mvn(com.google.guava:guava)
Requires: mvn(commons-io:commons-io)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sonar-update-center-1.12.1-4.fc23.cpio

%description
Update center for Sonar - platform for continuous inspection of code quality.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

