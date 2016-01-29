Name: maven-archetype-common
Version: 2.3
Summary: Maven Archetype common classes
License: ASL 2.0
Url: https://maven.apache.org/archetype/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-archetype-common = 2.3-2.fc23
Provides: mvn(org.apache.maven.archetype:archetype-common) = 2.3
Provides: mvn(org.apache.maven.archetype:archetype-common:pom:) = 2.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(dom4j:dom4j)
Requires: mvn(jdom:jdom)
Requires: mvn(net.sourceforge.jchardet:jchardet)
Requires: mvn(org.apache.maven.archetype:archetype-catalog)
Requires: mvn(org.apache.maven.archetype:archetype-descriptor)
Requires: mvn(org.apache.maven.archetype:archetype-registry)
Requires: mvn(org.apache.maven.shared:maven-invoker)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model:2.2.1)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.codehaus.plexus:plexus-velocity)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-archetype-common-2.3-2.fc23.cpio

%description
Maven Archetype common classes.

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

