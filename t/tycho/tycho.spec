
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: tycho
Version: 1.3.0
Summary: Plugins and extensions for building Eclipse plugins and OSGI bundles with Maven
License: ASL 2.0 and EPL-1.0
Url: http://eclipse.org/tycho
Group: Development/Java
Release: alt0.2jpp

Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.core.shared) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.core.shared.tests) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.embedder.shared) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.noopsecurity) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.maven.repository) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.maven.repository.tests) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.resolver.impl) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.resolver.impl.test) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.resolver.shared) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.resolver.shared.tests) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.tools.impl) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.tools.shared) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.p2.tools.tests) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit4) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit47) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit47:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit4:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit5) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit5:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.junit:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.osgibooter) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.testng) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.surefire.testng:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:org.eclipse.tycho.test.utils) = 1.3.0
Provides: mvn(org.eclipse.tycho:sisu-equinox-api) = 1.3.0
Provides: mvn(org.eclipse.tycho:sisu-equinox-api:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:sisu-equinox-embedder) = 1.3.0
Provides: mvn(org.eclipse.tycho:sisu-equinox-embedder:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:sisu-equinox-launching) = 1.3.0
Provides: mvn(org.eclipse.tycho:sisu-equinox-launching:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:sisu-equinox:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:target-platform-configuration) = 1.3.0
Provides: mvn(org.eclipse.tycho:target-platform-configuration:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-artifactcomparator) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-artifactcomparator:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-bundles-external:txt:manifest:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-bundles-external:zip:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-bundles-target:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-bundles:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-compiler-jdt) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-compiler-jdt:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-compiler-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-compiler-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-core) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-core:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-embedder-api) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-embedder-api:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-lib-detector) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-lib-detector:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-maven-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-maven-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-metadata-model) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-metadata-model:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-director-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-director-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-facade) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-facade:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-publisher-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-publisher-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-repository-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2-repository-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-p2:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-packaging-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-packaging-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-pomgenerator-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-pomgenerator-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-release:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-source-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-source-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-standalone-p2-director:zip:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-surefire-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-surefire-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-surefire:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-testing-harness) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-testing-harness:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-versions-plugin) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho-versions-plugin:pom:) = 1.3.0
Provides: mvn(org.eclipse.tycho:tycho:pom:) = 1.3.0
Provides: mvn(org.fedoraproject.p2:fedoraproject-p2:pom:) = 0.0.1.SNAPSHOT
Provides: mvn(org.fedoraproject.p2:org.fedoraproject.p2) = 0.0.1.SNAPSHOT
Provides: mvn(org.fedoraproject.p2:org.fedoraproject.p2:pom:) = 0.0.1.SNAPSHOT
Provides: mvn(org.fedoraproject.p2:xmvn-p2-installer-plugin) = 0.0.1.SNAPSHOT
Provides: mvn(org.fedoraproject.p2:xmvn-p2-installer-plugin:pom:) = 0.0.1.SNAPSHOT
Provides: osgi(org.eclipse.tycho.core.shared) = 1.3.0
Provides: osgi(org.eclipse.tycho.core.shared.tests) = 1.3.0
Provides: osgi(org.eclipse.tycho.embedder-api) = 1.3.0
Provides: osgi(org.eclipse.tycho.embedder.shared) = 1.3.0
Provides: osgi(org.eclipse.tycho.noopsecurity) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.maven.repository) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.maven.repository.tests) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.resolver.impl) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.resolver.impl.test) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.resolver.shared) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.resolver.shared.tests) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.tools.impl) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.tools.shared) = 1.3.0
Provides: osgi(org.eclipse.tycho.p2.tools.tests) = 1.3.0
Provides: osgi(org.eclipse.tycho.sisu-equinox-api) = 1.3.0
Provides: osgi(org.eclipse.tycho.sisu-equinox-launching) = 1.3.0
Provides: osgi(org.eclipse.tycho.surefire.junit) = 1.3.0
Provides: osgi(org.eclipse.tycho.surefire.junit4) = 1.3.0
Provides: osgi(org.eclipse.tycho.surefire.junit47) = 1.3.0
Provides: osgi(org.eclipse.tycho.surefire.junit5) = 1.3.0
Provides: osgi(org.eclipse.tycho.surefire.osgibooter) = 1.3.0
Provides: osgi(org.eclipse.tycho.surefire.testng) = 1.3.0
Provides: osgi(org.eclipse.tycho.test.utils) = 1.3.0
Provides: osgi(org.fedoraproject.p2) = 0.0.1
Requires: ecj
Requires: eclipse-platform
Requires: java-headless
Requires: javapackages-filesystem
Requires: maven-clean-plugin
Requires: maven-local
Requires: mvn(de.pdark:decentxml)
Requires: mvn(junit:junit)
Requires: mvn(org.apache.commons:commons-compress)
Requires: mvn(org.apache.commons:commons-exec)
Requires: mvn(org.apache.commons:commons-lang3)
Requires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
Requires: mvn(org.apache.maven.plugins:maven-source-plugin)
Requires: mvn(org.apache.maven.shared:maven-verifier)
Requires: mvn(org.apache.maven.surefire:maven-surefire-common)
Requires: mvn(org.apache.maven.surefire:surefire-api)
Requires: mvn(org.apache.maven:maven-archiver)
Requires: mvn(org.apache.maven:maven-compat)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-archiver)
Requires: mvn(org.codehaus.plexus:plexus-compiler-api)
Requires: mvn(org.codehaus.plexus:plexus-compiler-manager)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.jdt:ecj)
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)
Requires: mvn(org.fedoraproject.xmvn:xmvn-core)
Requires: mvn(org.hamcrest:hamcrest-core)
Requires: mvn(org.ow2.asm:asm-tree)
Requires: mvn(org.ow2.asm:asm-util)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.slf4j:slf4j-simple)
Requires: xmvn-minimal

BuildArch: noarch
Source: tycho-1.3.0-4.fc30.cpio


%description
Tycho is a set of Maven plugins and extensions for building Eclipse
plugins and OSGI bundles with Maven. Eclipse plugins and OSGI bundles
have their own metadata for expressing dependencies, source folder
locations, etc. that are normally found in a Maven POM. Tycho uses
native metadata for Eclipse plugins and OSGi bundles and uses the POM
to configure and drive the build. Tycho supports bundles, fragments,
features, update site projects and RCP applications. Tycho also knows
how to run JUnit test plugins using OSGi runtime and there is also
support for sharing build results using Maven artifact repositories.

Tycho plugins introduce new packaging types and the corresponding
lifecycle bindings that allow Maven to use OSGi and Eclipse metadata
during a Maven build. OSGi rules are used to resolve project
dependencies and package visibility restrictions are honored by the
OSGi-aware JDT-based compiler plugin. Tycho will use OSGi metadata and
OSGi rules to calculate project dependencies dynamically and injects
them into the Maven project model at build time. Tycho supports all
attributes supported by the Eclipse OSGi resolver (Require-Bundle,
Import-Package, Eclipse-GenericRequire, etc). Tycho will use proper
classpath access rules during compilation. Tycho supports all project
types supported by PDE and will use PDE/JDT project metadata where
possible. One important design goal in Tycho is to make sure there is
no duplication of metadata between POM and OSGi metadata.

%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}
sed -i '1s,usr/bin/sh,bin/sh,;s,^run ,jvm_run ,' usr/share/java-utils/p2-install.sh

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Mon Jun 07 2021 Igor Vlasenko <viy@altlinux.org> 1.3.0-alt0.2jpp
- use jvm_run

* Wed Jul 10 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.26.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- new version

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.23.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

