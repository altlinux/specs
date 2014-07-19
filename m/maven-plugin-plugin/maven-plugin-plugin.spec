Name: maven-plugin-plugin
Version: 3.1
Summary: Maven Plugin Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugin-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven2-plugin-plugin
Requires: java
Requires: jpackage-utils
Requires: maven
Requires: maven-artifact-manager
Requires: maven-doxia
Requires: maven-doxia-sitetools
Requires: maven-plugin-descriptor
Requires: maven-plugin-registry
Requires: maven-plugin-tools
Requires: maven-plugin-tools-annotations
Requires: maven-plugin-tools-api
Requires: maven-plugin-tools-beanshell
Requires: maven-plugin-tools-generators
Requires: maven-plugin-tools-java
Requires: maven-plugin-tools-model
Requires: maven-project
Requires: maven-shared-reporting-api
Requires: maven-shared-reporting-impl
Requires: plexus-utils
Requires: plexus-velocity
Requires: velocity

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-plugin-3.1-5.fc18.cpio

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
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

