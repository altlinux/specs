Name: maven-release-manager
Version: 2.2.1
Summary: Release a project updating the POM and tagging in the SCM
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-release-plugin/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-release-manager = 2.2.1-13.fc21
Provides: mvn(org.apache.maven.release:maven-release-manager) = 2.2.1
Provides: mvn(org.apache.maven.release:maven-release-manager:pom:) = 2.2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(jaxen:jaxen)
Requires: mvn(org.apache.maven.scm:maven-scm-api)
Requires: mvn(org.apache.maven.scm:maven-scm-manager-plexus)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-svn-commons)
Requires: mvn(org.apache.maven.scm:maven-scm-providers-standard:pom:)
Requires: mvn(org.apache.maven.shared:maven-invoker)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-artifact-manager)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.maven:maven-settings)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-interactivity-api)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.jdom:jdom)
Requires: mvn(org.sonatype.plexus:plexus-sec-dispatcher)

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: maven-release-manager-2.2.1-13.fc21.cpio

%description
This package contains maven-release-manager needed by maven-release-plugin.

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

