Name: maven-release-plugin
Version: 2.2.1
Summary: Release a project updating the POM and tagging in the SCM
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-release-plugin/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-release-plugin = 2.2.1-13.fc21
Provides: mvn(org.apache.maven.plugins:maven-release-plugin) = 2.2.1
Provides: mvn(org.apache.maven.plugins:maven-release-plugin:pom:) = 2.2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.release:maven-release-manager)
Requires: mvn(org.apache.maven.scm:maven-scm-api)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.maven:maven-settings)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.jdom:jdom)

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: maven-release-plugin-2.2.1-13.fc21.cpio

%description
This plugin is used to release a project with Maven, saving a lot of
repetitive, manual work. Releasing a project is made in two steps:
prepare and perform.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

