Name: sonar-jacoco-plugin
Version: 3.2
Summary: JaCoCo plugin for Sonar
License: LGPLv3+
Url: http://www.sonarqube.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.codehaus.sonar.plugins:sonar-jacoco-plugin) = 3.2
Provides: mvn(org.codehaus.sonar.plugins:sonar-jacoco-plugin:pom:) = 3.2
Provides: sonar-jacoco-plugin = 3.2-5.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.google.code.findbugs:jsr305)
Requires: mvn(org.jacoco:org.jacoco.agent)
Requires: mvn(org.jacoco:org.jacoco.core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sonar-jacoco-plugin-3.2-5.fc23.cpio

%description
JaCoCo is an alternative to Clover and Cobertura to measure coverage by unit
tests.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

