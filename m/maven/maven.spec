Provides: /etc/mavenrc /etc/java/maven.conf
Epoch: 0
Name: maven
Version: 3.3.3
Summary: Java project management and project comprehension tool
License: ASL 2.0
Url: http://maven.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven = 3.3.3-3.fc23
Provides: mvn(org.apache.maven:apache-maven:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-aether-provider) = 3.3.3
Provides: mvn(org.apache.maven:maven-aether-provider:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-artifact) = 3.3.3
Provides: mvn(org.apache.maven:maven-artifact:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-builder-support) = 3.3.3
Provides: mvn(org.apache.maven:maven-builder-support:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-compat) = 3.3.3
Provides: mvn(org.apache.maven:maven-compat:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-core) = 3.3.3
Provides: mvn(org.apache.maven:maven-core:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-embedder) = 3.3.3
Provides: mvn(org.apache.maven:maven-embedder:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-model) = 3.3.3
Provides: mvn(org.apache.maven:maven-model-builder) = 3.3.3
Provides: mvn(org.apache.maven:maven-model-builder:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-model:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-plugin-api) = 3.3.3
Provides: mvn(org.apache.maven:maven-plugin-api:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-repository-metadata) = 3.3.3
Provides: mvn(org.apache.maven:maven-repository-metadata:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-settings) = 3.3.3
Provides: mvn(org.apache.maven:maven-settings-builder) = 3.3.3
Provides: mvn(org.apache.maven:maven-settings-builder:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven-settings:pom:) = 3.3.3
Provides: mvn(org.apache.maven:maven:pom:) = 3.3.3
Requires: /bin/sh
Requires: aether-api
Requires: aether-connector-basic
Requires: aether-impl
Requires: aether-spi
Requires: aether-transport-wagon
Requires: aether-util
Requires: aopalliance
Requires: apache-commons-cli
Requires: apache-commons-codec
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: atinject
Requires: cdi-api
Requires: geronimo-annotation
Requires: google-guice
Requires: guava
Requires: httpcomponents-client
Requires: httpcomponents-core
Requires: java-headless
Requires: jpackage-utils
Requires: jsoup
Requires: jsr-305
Requires: maven-wagon-file
Requires: maven-wagon-http
Requires: maven-wagon-http-shared
Requires: maven-wagon-provider-api
Requires: mvn(com.google.guava:guava)
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(org.apache.maven.wagon:wagon-file)
Requires: mvn(org.apache.maven.wagon:wagon-http::shaded:)
Requires: mvn(org.apache.maven.wagon:wagon-provider-api)
Requires: mvn(org.codehaus.plexus:plexus-classworlds)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-interpolation)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.aether:aether-api)
Requires: mvn(org.eclipse.aether:aether-connector-basic)
Requires: mvn(org.eclipse.aether:aether-impl)
Requires: mvn(org.eclipse.aether:aether-spi)
Requires: mvn(org.eclipse.aether:aether-transport-wagon)
Requires: mvn(org.eclipse.aether:aether-util)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.slf4j:slf4j-simple)
Requires: mvn(org.sonatype.plexus:plexus-cipher)
Requires: mvn(org.sonatype.plexus:plexus-sec-dispatcher)
Requires: mvn(org.sonatype.sisu:sisu-guice::no_aop:)
Requires: objectweb-asm
Requires: plexus-cipher
Requires: plexus-classworlds
Requires: plexus-containers-component-annotations
Requires: plexus-interpolation
Requires: plexus-sec-dispatcher
Requires: plexus-utils
Requires: sisu-inject
Requires: sisu-plexus
Requires: slf4j

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-3.3.3-3.tar

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
tar xf %{SOURCE0}

%build
tar tf %{SOURCE0} | sed -e 's,^\.,,' > %name-list

sed -i '/^\/$/d;/\/tmp/d;/^\/etc\/$/d;/^\/usr\/$/d;/^\/usr\/bin\/$/d;/^\/usr\/share\/$/d;' %name-list
sed -i -e '/^\/usr\/share\/doc\/$/d;/^\/usr\/share\/man\/$/d;/^\/usr\/share\/man\/man1\/$/d;' %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt1_3jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.2jpp
- rebuild to add provides

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

