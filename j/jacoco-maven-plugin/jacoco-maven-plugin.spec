Name: jacoco-maven-plugin
Version: 0.7.5
Summary: A Jacoco plugin for maven
License: EPL
Url: http://www.eclemma.org/jacoco/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jacoco-maven-plugin = 0.7.5-2.fc23
Provides: mvn(org.jacoco:jacoco-maven-plugin) = 0.7.5.201505241946
Provides: mvn(org.jacoco:jacoco-maven-plugin:pom:) = 0.7.5.201505241946
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.reporting:maven-reporting-impl)
Requires: mvn(org.apache.maven.shared:file-management)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.jacoco:org.jacoco.agent::runtime:)
Requires: mvn(org.jacoco:org.jacoco.core)
Requires: mvn(org.jacoco:org.jacoco.report)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jacoco-maven-plugin-0.7.5-2.fc23.cpio

%description
A Jacoco plugin for maven.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

