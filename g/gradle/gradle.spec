Provides: /etc/java/gradle.conf
AutoReq: no
Name: gradle
Version: 2.5
Summary: Build automation tool
License: ASL 2.0
Url: http://www.gradle.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: gradle = 2.5-3.fc23
Provides: mvn(org.gradle:gradle-base-services) = 2.5
Provides: mvn(org.gradle:gradle-base-services-groovy) = 2.5
Provides: mvn(org.gradle:gradle-base-services-groovy:pom:) = 2.5
Provides: mvn(org.gradle:gradle-base-services:pom:) = 2.5
Provides: mvn(org.gradle:gradle-core) = 2.5
Provides: mvn(org.gradle:gradle-core:pom:) = 2.5
Provides: mvn(org.gradle:gradle-dependency-management) = 2.5
Provides: mvn(org.gradle:gradle-dependency-management:pom:) = 2.5
Provides: mvn(org.gradle:gradle-messaging) = 2.5
Provides: mvn(org.gradle:gradle-messaging:pom:) = 2.5
Provides: mvn(org.gradle:gradle-resources) = 2.5
Provides: mvn(org.gradle:gradle-resources:pom:) = 2.5
Provides: mvn(org.gradle:gradle-tooling-api) = 2.5
Provides: mvn(org.gradle:gradle-tooling-api:pom:) = 2.5
Provides: mvn(org.gradle:gradle-wrapper) = 2.5
Provides: mvn(org.gradle:gradle-wrapper:pom:) = 2.5
Requires: /bin/sh
Requires: aether-ant-tasks
Requires: aether-api
Requires: aether-connector-basic
Requires: aether-impl
Requires: aether-spi
Requires: aether-transport-classpath
Requires: aether-transport-file
Requires: aether-transport-http
Requires: aether-transport-wagon
Requires: aether-util
Requires: ant
Requires: ant-antlr
Requires: ant-junit
Requires: antlr-tool
Requires: apache-commons-cli
Requires: apache-commons-codec
Requires: apache-commons-collections
Requires: apache-commons-io
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: apache-ivy
Requires: aqute-bndlib
Requires: atinject
Requires: base64coder
Requires: bash
Requires: bea-stax
Requires: bea-stax-api
Requires: beust-jcommander
Requires: bouncycastle
Requires: bouncycastle-pg
Requires: bsf
Requires: bsh
Requires: cglib
Requires: dom4j
Requires: ecj
Requires: extra166y
Requires: felix-osgi-core
Requires: geronimo-annotation
Requires: geronimo-jms
Requires: glassfish-servlet-api
Requires: google-gson
Requires: gpars
Requires: groovy-lib
Requires: guava
Requires: hamcrest
Requires: hawtjni
#Requires: hicolor-icon-theme
Requires: httpcomponents-client
Requires: httpcomponents-core
Requires: isorelax
Requires: jackson-annotations
Requires: jackson-core
Requires: jackson-databind
Requires: jansi
Requires: jansi-native
Requires: jarjar
Requires: jatl
Requires: java-headless
Requires: javamail
Requires: javapackages-tools
Requires: jaxen
Requires: jcifs
Requires: jcip-annotations
Requires: jcl-over-slf4j
Requires: jcsp
Requires: jdom
Requires: jdom2
Requires: jettison
Requires: jetty-annotations
Requires: jetty-jsp
Requires: jetty-plus
Requires: jetty-security
Requires: jetty-server
Requires: jetty-servlet
Requires: jetty-util
Requires: jetty-webapp
Requires: jetty-xml
Requires: jline
Requires: jna
Requires: joda-convert
Requires: joda-time
Requires: jpackage-utils
Requires: jsch
Requires: jul-to-slf4j
Requires: junit
Requires: jzlib
Requires: kryo
Requires: kxml
Requires: log4j-over-slf4j
Requires: log4j12
Requires: logback
Requires: maven
Requires: maven-wagon-http
Requires: maven-wagon-http-shared
Requires: maven-wagon-provider-api
Requires: minlog
Requires: msv-msv
Requires: msv-xsdlib
Requires: multiverse
Requires: mvn(com.esotericsoftware.kryo:kryo)
Requires: mvn(com.google.guava:guava-jdk5)
Requires: mvn(org.slf4j:slf4j-api)
Requires: native-platform
Requires: nekohtml
Requires: netty3
Requires: objectweb-asm
Requires: objenesis
Requires: plexus-cipher
Requires: plexus-classworlds
Requires: plexus-containers-component-annotations
Requires: plexus-containers-container-default
Requires: plexus-interpolation
Requires: plexus-sec-dispatcher
Requires: plexus-utils
Requires: qdox
Requires: reflectasm
Requires: relaxngDatatype
Requires: rhino
Requires: sisu-plexus
Requires: slf4j
Requires: snakeyaml
Requires: sonar-batch-bootstrapper
Requires: stax2-api
Requires: tesla-polyglot-common
Requires: tesla-polyglot-groovy
Requires: testng
Requires: woodstox-core
Requires: xalan-j2
Requires: xbean
Requires: xerces-j2
Requires: xml-commons-apis
Requires: xml-commons-resolver
Requires: xom
Requires: xstream

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: gradle-2.5-3.fc23.cpio

%description
Gradle is build automation evolved. Gradle can automate the building,
testing, publishing, deployment and more of software packages or other
types of projects such as generated static websites, generated
documentation or indeed anything else.

Gradle combines the power and flexibility of Ant with the dependency
management and conventions of Maven into a more effective way to
build. Powered by a Groovy DSL and packed with innovation, Gradle
provides a declarative way to describe all kinds of builds through
sensible defaults. Gradle is quickly becoming the build system of
choice for many open source projects, leading edge enterprises and
legacy automation challenges.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}
sed -i -e s,/usr/bin/bash,/bin/bash, usr/bin/gradle

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done

%post
update-desktop-database &>/dev/null || :
touch --no-create /usr/share/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &>/dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create /usr/share/icons/hicolor &>/dev/null
    gtk-update-icon-cache /usr/share/icons/hicolor &>/dev/null || :
fi


%files -f %name-list

%changelog
* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_13jpp7
- rebuild with maven-local

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_13jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

