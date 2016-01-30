Name: maven-plugin-plugin
Version: 3.4
Summary: Maven Plugin Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugin-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-plugin-plugin = 0:3.4-3.fc23
Provides: mvn(org.apache.maven.plugins:maven-plugin-plugin) = 3.4
Provides: mvn(org.apache.maven.plugins:maven-plugin-plugin:pom:) = 3.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-annotations)
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-api)
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-generators)
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-tools-java)
Requires: mvn(org.apache.maven.reporting:maven-reporting-api)
Requires: mvn(org.apache.maven.reporting:maven-reporting-impl)
Requires: mvn(org.apache.maven:maven-artifact:2.2.1)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-model:2.2.1)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-repository-metadata)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.codehaus.plexus:plexus-velocity)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-plugin-3.4-3.fc23.cpio

%description
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

