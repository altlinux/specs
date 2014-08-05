# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name gradle
%define version 1.0

%global namedreltag  %{nil}
%global namedversion %{version}%{?namedreltag}
%global nameddottag  %(echo %{?namedreltag} | tr - . ) 
%global bootstrap   0

# TODO grails-core.jar http://repo1.maven.org/maven2/org/grails/grails-core/1.3.7/grails-core-1.3.7.jar
# https://github.com/grails/grails-core/

# sonar plugin
# gradle/lib/plugins/gradle-sonar-1.0-milestone-9.jar
# gradle/lib/plugins/sonar-batch-bootstrapper-2.9.jar
# maven plugin
# gradle/lib/plugins/pmaven-common-0.8-20100325.jar
# gradle/lib/plugins/pmaven-groovy-0.8-20100325.jar
# jetty 6.x plugin
# gradle/lib/plugins/core-3.1.1.jar
# gradle/lib/plugins/geronimo-annotation_1.0_spec-1.0.jar
# gradle/lib/plugins/gradle-jetty-1.0-milestone-9.jar
# gradle/lib/plugins/jetty-6.1.25.jar
# gradle/lib/plugins/jetty-annotations-6.1.25.jar
# gradle/lib/plugins/jetty-naming-6.1.25.jar
# gradle/lib/plugins/jetty-plus-6.1.25.jar
# gradle/lib/plugins/jetty-util-6.1.25.jar
# gradle/lib/plugins/jsp-2.1-6.1.14.jar
# gradle/lib/plugins/jsp-api-2.1-6.1.14.jar
# gradle/lib/plugins/servlet-api-2.5-20081211.jar

# FIXME http://issues.gradle.org/browse/GRADLE-2210

Name:          gradle
Version:       1.0
Release:       alt1_13jpp7
Summary:       Groovy based build system
Group:         Development/Java
License:       ASL 2.0
Url:           http://www.gradle.org/
Source0:       http://services.gradle.org/distributions/gradle-%{namedversion}-src.zip
Source3:       gradle-%{namedversion}-wrapper
#Source4:       gradle-%{namedversion}-build.xml
Source4:       gradle-%{namedversion}-build.xml
Source5:       gradle.desktop

# Tanks to C. de Wolf, A. Grimm, J. Hernandez, M. Goldmann, M. Izdebski for their contribution
# mgoldmann
# On Fedora we have the jnidispatch.so file in a well known location, so we use it directly from there
Patch0:        gradle-%{namedversion}-Proper-path-to-jnidispatch.patch
# unavailable deps polyglot-maven
Patch1:        gradle-%{namedversion}-Disabled-polyglot-maven-support.patch
# fix for maven plugin
Patch2:        gradle-%{namedversion}-Missing-method-in-PlexusLoggerAdapter.patch
# jhernand unavailable file
Patch3:        gradle-%{namedversion}-css3-pie-not-available.patch
# jhernand  use jnr-posix instead of jna-posix
Patch4:        gradle-%{namedversion}-POSIX-changes.patch

Patch5:        gradle-%{namedversion}-script.patch
# fix setting.xml in non boostrap mode
Patch6:        gradle-%{namedversion}-core-releases_xml.patch
# mgoldmann
Patch7:        gradle-%{namedversion}-Use-Exception-instead-CloneNotSupportedException.patch
# jhernand
# fix user home for gradle applications
Patch8:        gradle-%{namedversion}-Use-proper-system-environment-variables.patch
# mgoldmann
# fix for http://issues.gradle.org/browse/GRADLE-2210 
Patch9:        gradle-%{namedversion}-Maven-3-support.patch
# Since Gradle uses groovy-all.jar which bundles all dependencies and this is NOT allowed in Fedora
# we need to use clean groovy.jar and point Gradle to its dependencies
Patch10:       gradle-%{namedversion}-Fix-classpath-after-splitting-groovy-all-into-multip.patch
# Related to PATCH10 - we need to use the deps (asm, antlr) directly, not bundled versions
Patch11:       gradle-%{namedversion}-Change-groovy-all-references-to-valid-package-names.patch
# mgoldmann
# Checkstyle requires antlr, it was provided by groovy-all, but we removed it
# We cannot have two antlr libraries in classpath when executing checkstyle
Patch12:       gradle-%{namedversion}-Add-proper-checkstyle-dependencies.patch
# Another tricky one, but I remember I had serious issues with classpath creation for codenarc
# Using LOCAL_GROOVY instead of GROOVY did the trick. Yep, ugly
Patch13:       gradle-%{namedversion}-Add-proper-codenarc-dependencies.patch
# disable this modules for unavailable build deps
# depend on maven2
Patch14:       gradle-%{namedversion}-Disable-maven-plugin.patch
# depend on gradle-maven module
Patch15:       gradle-%{namedversion}-Disable-signing-plugin.patch
# disable. require sonar http://www.sonarsource.org/
Patch16:       gradle-%{namedversion}-Disable-sonar-plugin.patch
# jhernand
# change jna-posix with jnr-posix and add jnr-constant and jaffl
Patch17:       gradle-%{namedversion}-Change-dependency-from-jna-to-jnr-for-native.patch
# mgoldmann
# Since we operate on symlinks Java is fooled by it and we need to specify the patch to gradle home manually
Patch18:       gradle-%{namedversion}-Set-the-libdir-to-usr-share-gradle.patch
# TODO remove this patch when spock-core is available in rawhide
Patch19:       gradle-%{namedversion}-No-spock-library-available.patch
# fix gradle checkstyle deps
Patch20:       gradle-%{namedversion}-Add-missing-dependencies-when-using-clean-checkstyle.patch
# TODO remove this patch when codenarc is available in rawhide
Patch21:       gradle-%{namedversion}-Disable-codenarc-plugin-since-CodeNarc-is-not-avaial.patch
# remove docbook-xml@zip references
Patch22:       gradle-%{namedversion}-No-zipped-docbook-available.patch
# disable require jets3t (not available for now... see https://bugzilla.redhat.com/show_bug.cgi?id=847109 ) 
Patch23:       gradle-%{namedversion}-Disable-website-module.patch
# fix the location of the build deps
Patch24:       gradle-%{namedversion}-Use-local-available-libraries.patch
# remove jetty plugin references, prevent gradle error: unavailable module, gradle-jetty
Patch25:       gradle-%{namedversion}-Disable-jetty-plugin.patch
# remove not required timestamp from artifacts version
Patch26:       gradle-%{namedversion}-Fix-version-remove-timestamp.patch
# unavailable deps require jmock 2.5.1
# disable also the releaseArtifacts, docs and samples tasks (require gradle maven plugin)
Patch27:       gradle-%{namedversion}-disable-tests.patch
# workaround
# disable userguide and dslHtml tasks (unavailable deps: docbook:docbook-xsl:1.75.2@zip)
# docs depend on test tasks
Patch28:       gradle-%{namedversion}-docs.patch
# build fix for jnr-posix 2.4.0
Patch29:       gradle-1.0-jnr-posix2.patch
# build fix for ivy 2.3.0
Patch30:       gradle-1.0-ivy23.patch

Patch31:       gradle-1.0-printStackTrace.patch
# jnr-posix 2.x depend on jnr-ffi 0.7.x caused
# java.lang.NoClassDefFoundError: jnr/ffi/Struct
Patch32:       gradle-1.0-jnr-ffi.patch

# Build requirements (alphabetical):
BuildRequires: aether
BuildRequires: ant
BuildRequires: ant-antlr
BuildRequires: antlr
BuildRequires: antlr-tool
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-ivy
# require bnd ant task
BuildRequires: aqute-bnd
BuildRequires: aqute-bndlib
BuildRequires: beust-jcommander
BuildRequires: bouncycastle
BuildRequires: bouncycastle-pg
BuildRequires: bsh
BuildRequires: checkstyle
BuildRequires: desktop-file-utils
BuildRequires: dom4j
BuildRequires: findbugs
BuildRequires: findbugs-bcel
BuildRequires: git
BuildRequires: groovy >= 1.8.6
BuildRequires: groovy-javadoc >= 1.8.6
BuildRequires: guava
BuildRequires: hamcrest
BuildRequires: httpcomponents-client
BuildRequires: httpcomponents-core
BuildRequires: jaffl
BuildRequires: jansi
BuildRequires: java-javadoc
BuildRequires: jaxen
BuildRequires: jcifs
BuildRequires: jcip-annotations
BuildRequires: jna
BuildRequires: jnr-constants
BuildRequires: jnr-posix >= 1.1.8
BuildRequires: jnr-ffi
BuildRequires: jpackage-utils
BuildRequires: jsch
BuildRequires: junit
BuildRequires: logback >= 1.0.1
BuildRequires: maven
BuildRequires: objectweb-asm
BuildRequires: plexus-classworlds
BuildRequires: plexus-component-api
BuildRequires: plexus-containers-component-annotations
BuildRequires: plexus-container-default
BuildRequires: plexus-interpolation
BuildRequires: plexus-utils
# unavailable build/requires deps
# FIXME BuildRequires: polyglot-maven https://bugzilla.redhat.com/show_bug.cgi?id=855331
BuildRequires: slf4j
BuildRequires: snakeyaml
BuildRequires: testng

%if !%bootstrap
BuildRequires: gradle
BuildRequires: cglib
BuildRequires: classycle
BuildRequires: codenarc
BuildRequires: flyingsaucer
BuildRequires: jmock
BuildRequires: jsoup
BuildRequires: nekohtml
BuildRequires: objenesis
BuildRequires: pegdown
BuildRequires: spock-core
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xmlunit
# unavailable docs deps
# TODO BuildRequires: xslthl https://bugzilla.redhat.com/show_bug.cgi?id=844179
%endif
# work in progress BuildRequires: sonar https://bugzilla.redhat.com/show_bug.cgi?id=848096

Requires:      aether
Requires:      ant
Requires:      ant-antlr
Requires:      antlr
Requires:      antlr-tool
Requires:      apache-commons-beanutils
Requires:      apache-commons-cli
Requires:      apache-commons-codec
Requires:      apache-commons-collections
Requires:      apache-commons-io
Requires:      apache-commons-lang
Requires:      apache-ivy
Requires:      aqute-bnd
Requires:      aqute-bndlib
Requires:      beust-jcommander
Requires:      bouncycastle
Requires:      bouncycastle-pg
# Requires:      bsh2
Requires:      bsh
Requires:      checkstyle
Requires:      dom4j
Requires:      findbugs
Requires:      findbugs-bcel
Requires:      groovy
Requires:      guava
Requires:      hamcrest
Requires:      httpcomponents-client
Requires:      httpcomponents-core
Requires:      jaffl
Requires:      jansi
Requires:      jaxen
Requires:      jcifs
Requires:      jcip-annotations
Requires:      jna
Requires:      jnr-constants
Requires:      jnr-posix
Requires:      jnr-ffi
Requires:      jsch
Requires:      junit
Requires:      logback
Requires:      maven

# BuildRequires: bsh2 already packaged
BuildRequires: maven-ant-tasks
# BuildRequires: maven-artifact-manager
# BuildRequires: maven-error-diagnostics
# BuildRequires: maven-model
# BuildRequires: maven-project
# BuildRequires: maven-wagon
Requires:      maven-ant-tasks
# Requires:      maven-artifact-manager
# Requires:      maven-error-diagnostics
# Requires:      maven-model
# Requires:      maven-project
# Requires:      maven-wagon

Requires:      objectweb-asm
Requires:      plexus-classworlds
Requires:      plexus-component-api
Requires:      plexus-containers-component-annotations
Requires:      plexus-container-default
Requires:      plexus-interpolation
Requires:      plexus-utils
Requires:      slf4j
Requires:      snakeyaml
Requires:      testng

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Gradle is a build system written in Groovy. It uses Groovy
also as the language for its build scripts. It has a powerful
multi-project build support. It has a layer on top of Ivy
that provides a build-by-convention integration for Ivy. It
gives you always the choice between the flexibility of Ant
and the convenience of a build-by-convention behavior.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
# cleanup
find . -name '*.jar' -delete
find . -name '*.class' -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if %bootstrap
# gradle bin is generate during the non bootstrap build (task assemble only...?)
cat gradlew >> gradle.sh
%patch5 -p0
# setting.xml is generate during the non bootstrap build
%patch6 -p0
%endif
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p0

cp -p %{SOURCE4} build.xml
cp -p %{SOURCE5} .

# fix non ASCII chars
for s in subprojects/core/src/main/groovy/org/gradle/api/Named.java \
 subprojects/core/src/main/groovy/org/gradle/api/internal/ExtensibleDynamicObject.java \
 subprojects/core/src/main/groovy/org/gradle/api/internal/plugins/DslObject.java \
 subprojects/core/src/main/groovy/org/gradle/api/plugins/ExtensionAware.java \
 subprojects/core/src/main/groovy/org/gradle/api/plugins/ExtensionContainer.java \
 subprojects/core/src/main/groovy/org/gradle/api/plugins/ExtraPropertiesExtension.java \
 subprojects/core/src/main/groovy/org/gradle/initialization/GradleLauncherAction.java \
 subprojects/core/src/main/groovy/org/gradle/process/internal/JvmOptions.java \
 subprojects/core-impl/src/main/groovy/org/gradle/api/internal/externalresource/cached/CachedExternalResource.java \
 subprojects/core-impl/src/main/groovy/org/gradle/api/internal/externalresource/transfer/DefaultCacheAwareExternalResourceAccessor.java \
 subprojects/core-impl/src/main/groovy/org/gradle/api/internal/externalresource/transfer/ExternalResourceAccessor.java \
 subprojects/core-impl/src/main/groovy/org/gradle/api/internal/externalresource/metadata/ExternalResourceMetaData.java \
 subprojects/core-impl/src/main/groovy/org/gradle/api/internal/externalresource/local/LocallyAvailableResourceCandidates.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/client/DaemonClientInputForwarder.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/protocol/Failure.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/registry/EmbeddedDaemonRegistry.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/server/DaemonStateCoordinator.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/BuildCommandOnly.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/DaemonCommandAction.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/DaemonCommandExecution.java \
 subprojects/launcher/src/main/java/org/gradle/launcher/daemon/server/exec/ExecuteBuild.java \
 subprojects/plugins/src/main/groovy/org/gradle/api/reporting/Reporting.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%if %{?fedora} > 18
%patch29 -p1
#sed -i "s|org.jruby.ext.posix|jnr.posix|" \
#  subprojects/native/src/test/groovy/org/gradle/internal/nativeplatform/filesystem/FallbackPOSIXTest.groovy \
#  subprojects/native/src/test/groovy/org/gradle/internal/nativeplatform/filesystem/ComposableFilePermissionHandlerTest.groovy \
#  subprojects/native/src/test/groovy/org/gradle/internal/nativeplatform/filesystem/ComposableFilePermissionHandlerTest.groovy
%patch30 -p1
%patch32 -p0
%endif

%patch31 -p0
# print the stack trace even when failure is not instance of GradleException
sed -i "s|//failure.printStackTrace();|failure.printStackTrace();|" subprojects/core/src/main/groovy/org/gradle/BuildExceptionReporter.java

%build

%if %bootstrap
  ant dist javadoc
%else

# TODO maven signing
# java/docs and test suite for unavailable deps require jmock, jets3t, docbook-xml@zip, xslthl,...
# fix deps proper name
sed -i "s|xercesImpl:2.9.1|xerces-j2:2.9.1|" subprojects/core/core.gradle
sed -i "s|cglib-nodep|cglib|" buildSrc/build.gradle
sed -i "s|bndlib|aqute-bnd|" subprojects/osgi/osgi.gradle
sed -i "s|constantine|jnr-constants|" subprojects/native/native.gradle

# groovydoc (more complete than javadoc) task could derail the compilation (requires groovy-all.jar) docs:userguide 
gradle --full-stacktrace --debug assemble javadoc \
  -g $PWD/gradlehome -b $PWD/build.gradle
%endif

%install

mkdir -p %{buildroot}%{_datadir}/%{name}/{bin,lib,lib/plugins,media}
mkdir -p %{buildroot}%{_javadir}/%{name}

# TODO maven signing
%if %bootstrap

   cp -pr src/toplevel/media/* %{buildroot}%{_datadir}/%{name}/media/
   cp -p src/toplevel/LICENSE %{buildroot}%{_datadir}/%{name}/
   cp -p src/toplevel/NOTICE %{buildroot}%{_datadir}/%{name}/
   cp -p src/toplevel/changelog.txt %{buildroot}%{_datadir}/%{name}/
   cp -p src/toplevel/LICENSE .
   cp -p src/toplevel/NOTICE .
   install -pm 755 %{name}.sh %{buildroot}%{_datadir}/%{name}/bin/%{name}
# WARNING in newer release there are new artifacts, please update these lists

#    gradle-launcher-%%{namedversion}.jar is special and cannot be moved,
#    because the launcher inspects its own _dereferenced_ file path to determine where to find other jars.
#    The others can be in javadir
   install -pm 644 dist/lib/%{name}-launcher-%{namedversion}.jar %{buildroot}%{_datadir}/%{name}/lib/%{name}-launcher-%{namedversion}.jar

   for m in base-services cli core native open-api tooling-api ui wrapper; do
     install -pm 644 dist/lib/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
     ln -sf %{_javadir}/%{name}/%{name}-${m}.jar %{buildroot}%{_datadir}/%{name}/lib/%{name}-${m}-%{namedversion}.jar
   done

   for m in announce antlr code-quality core-impl cpp ear ide osgi plugins scala; do
     install -pm 644 dist/lib/plugins/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
     ln -sf %{_javadir}/%{name}/%{name}-${m}.jar %{buildroot}%{_datadir}/%{name}/lib/plugins/%{name}-${m}-%{namedversion}.jar
   done

%else
mkdir -p gradlehome
(
   cd gradlehome
   rm -rf *
   unzip ../build/distributions/%{name}-%{namedversion}-all.zip
   rm -rf src
   find %{name}-%{namedversion} -name "*.bat" -delete
   (
     cd %{name}-%{namedversion}
     sed -i "s|# Attempt to set APP_HOME|export JAVA_HOME=/usr/lib/jvm/java|" bin/%{name}
     sed -i 's|APP_HOME="`pwd -P`"|export APP_HOME=$GRADLE_HOME|'  bin/%{name}
     install -pm 755 bin/%{name} %{buildroot}%{_datadir}/%{name}/bin/

     cp -pr media/* %{buildroot}%{_datadir}/%{name}/media/
     cp -p LICENSE %{buildroot}%{_datadir}/%{name}/
     cp -p NOTICE %{buildroot}%{_datadir}/%{name}/
     cp -p changelog.txt %{buildroot}%{_datadir}/%{name}/
# WARNING in newer release there are new artifacts, please update these lists

#    gradle-launcher-%%{namedversion}.jar is special and cannot be moved,
#    because the launcher inspects its own _dereferenced_ file path to determine where to find other jars.
#    The others can be in javadir
     install -pm 644 lib/%{name}-launcher-%{namedversion}.jar %{buildroot}%{_datadir}/%{name}/lib/%{name}-launcher-%{namedversion}.jar

     for m in base-services cli core native open-api tooling-api ui wrapper; do
       install -pm 644 lib/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
       ln -sf %{_javadir}/%{name}/%{name}-${m}.jar %{buildroot}%{_datadir}/%{name}/lib/%{name}-${m}-%{namedversion}.jar
     done

     for m in announce antlr code-quality core-impl cpp ear ide osgi plugins scala; do
       install -pm 644 lib/plugins/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
       ln -sf %{_javadir}/%{name}/%{name}-${m}.jar %{buildroot}%{_datadir}/%{name}/lib/plugins/%{name}-${m}-%{namedversion}.jar
     done
     cp -p LICENSE ../../
     cp -p NOTICE ../../
   )
)

%endif

# TODO once the tests task is fixed... change with the proper dir (docs/)
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr subprojects/docs/build/docs/*doc*/* %{buildroot}%{_javadocdir}/%{name}


ln -sf %{_javadir}/ant.jar %{buildroot}%{_datadir}/%{name}/lib/ant-1.8.2.jar
ln -sf $(build-classpath ant-launcher) %{buildroot}%{_datadir}/%{name}/lib/ant-launcher-1.8.2.jar
# groovy deps
ln -sf $(build-classpath antlr) %{buildroot}%{_datadir}/%{name}/lib/antlr-2.7.7.jar
ln -sf $(build-classpath objectweb-asm/asm-all) %{buildroot}%{_datadir}/%{name}/lib/asm-all-3.3.1.jar
ln -sf $(build-classpath commons-cli) %{buildroot}%{_datadir}/%{name}/lib/commons-cli-1.2.jar

ln -sf $(build-classpath commons-collections) %{buildroot}%{_datadir}/%{name}/lib/commons-collections-3.2.1.jar
ln -sf $(build-classpath commons-io) %{buildroot}%{_datadir}/%{name}/lib/commons-io-1.4.jar
ln -sf $(build-classpath commons-lang) %{buildroot}%{_datadir}/%{name}/lib/commons-lang-2.6.jar
ln -sf $(build-classpath constantine) %{buildroot}%{_datadir}/%{name}/lib/constantine-0.7.jar
ln -sf $(build-classpath dom4j) %{buildroot}%{_datadir}/%{name}/lib/dom4j-1.6.1.jar
ln -sf $(build-classpath groovy) %{buildroot}%{_datadir}/%{name}/lib/groovy-all-1.8.6.jar
ln -sf $(build-classpath groovy) %{buildroot}%{_datadir}/%{name}/lib/groovy-1.8.6.jar
ln -sf $(build-classpath guava) %{buildroot}%{_datadir}/%{name}/lib/guava-11.0.1.jar
ln -sf $(build-classpath ivy) %{buildroot}%{_datadir}/%{name}/lib/ivy-2.2.0.jar
ln -sf $(build-classpath jansi) %{buildroot}%{_datadir}/%{name}/lib/jansi-1.2.1.jar
ln -sf $(build-classpath jaxen) %{buildroot}%{_datadir}/%{name}/lib/jaxen-1.1.jar
ln -sf $(build-classpath jcip-annotations) %{buildroot}%{_datadir}/%{name}/lib/jcip-annotations-1.0.jar
ln -sf $(build-classpath jna) %{buildroot}%{_datadir}/%{name}/lib/jna-3.2.7.jar
ln -sf $(build-classpath jnr-constants) %{buildroot}%{_datadir}/%{name}/lib/jnr-constants.jar
ln -sf $(build-classpath jnr-posix) %{buildroot}%{_datadir}/%{name}/lib/jnr-posix-1.0.3.jar
%if %{?fedora} > 18
ln -sf $(build-classpath jnr-ffi) %{buildroot}%{_datadir}/%{name}/lib/jnr-ffi.jar
ln -sf $(build-classpath plexus-component-api/plexus-component-api) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-component-api.jar
ln -sf $(build-classpath plexus-containers/plexus-component-annotations) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-component-annotations-1.5.2.jar
%else
ln -sf $(build-classpath plexus/plexus-component-api) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-component-api.jar
ln -sf $(build-classpath plexus/containers-component-annotations) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-component-annotations-1.5.2.jar
%endif
# gradle -gui Starting external process java.lang.NoClassDefFoundError: com/kenai/jaffl/struct/Struct
ln -sf $(build-classpath jaffl) %{buildroot}%{_datadir}/%{name}/lib/jaffl.jar
ln -sf $(build-classpath jsch) %{buildroot}%{_datadir}/%{name}/lib/jsch-0.1.46.jar
ln -sf $(build-classpath logback/logback-classic) %{buildroot}%{_datadir}/%{name}/lib/logback-classic-1.0.0.jar
ln -sf $(build-classpath logback/logback-core) %{buildroot}%{_datadir}/%{name}/lib/logback-core-1.0.0.jar
ln -sf $(build-classpath slf4j/api) %{buildroot}%{_datadir}/%{name}/lib/slf4j-api-1.6.4.jar
ln -sf $(build-classpath slf4j/jcl-over-slf4j) %{buildroot}%{_datadir}/%{name}/lib/jcl-over-slf4j-1.6.4.jar
ln -sf $(build-classpath slf4j/jul-to-slf4j) %{buildroot}%{_datadir}/%{name}/lib/jul-to-slf4j-1.6.4.jar
ln -sf $(build-classpath slf4j/log4j-over-slf4j) %{buildroot}%{_datadir}/%{name}/lib/log4j-over-slf4j-1.6.4.jar

ln -sf $(build-classpath ant/ant-antlr) %{buildroot}%{_datadir}/%{name}/lib/plugins/ant-antlr-1.8.2.jar
ln -sf $(build-classpath antlr) %{buildroot}%{_datadir}/%{name}/lib/plugins/antlr-2.7.7.jar
ln -sf $(build-classpath bcpg) %{buildroot}%{_datadir}/%{name}/lib/plugins/bcpg-jdk15-1.46.jar
ln -sf $(build-classpath bcprov) %{buildroot}%{_datadir}/%{name}/lib/plugins/bcprov-jdk15-1.46.jar
ln -sf $(build-classpath bsh) %{buildroot}%{_datadir}/%{name}/lib/plugins/bsh-2.0b4.jar
# bsh2/bsh
ln -sf $(build-classpath commons-beanutils) %{buildroot}%{_datadir}/%{name}/lib/plugins/commons-beanutils.jar
ln -sf $(build-classpath commons-cli) %{buildroot}%{_datadir}/%{name}/lib/plugins/commons-cli-1.2.jar
ln -sf $(build-classpath commons-codec) %{buildroot}%{_datadir}/%{name}/lib/plugins/commons-codec-1.4.jar
ln -sf $(build-classpath hamcrest/core) %{buildroot}%{_datadir}/%{name}/lib/plugins/hamcrest-core-1.1.jar
ln -sf $(build-classpath httpcomponents/httpclient) %{buildroot}%{_datadir}/%{name}/lib/plugins/httpclient-4.1.2.jar
ln -sf $(build-classpath httpcomponents/httpcore) %{buildroot}%{_datadir}/%{name}/lib/plugins/httpcore-4.1.2.jar
ln -sf $(build-classpath jcifs) %{buildroot}%{_datadir}/%{name}/lib/plugins/jcifs-1.3.17.jar
ln -sf $(build-classpath beust-jcommander) %{buildroot}%{_datadir}/%{name}/lib/plugins/jcommander-1.12.jar
ln -sf $(build-classpath aqute-bnd) %{buildroot}%{_datadir}/%{name}/lib/plugins/bndlib-1.50.0.jar
ln -sf $(build-classpath junit) %{buildroot}%{_datadir}/%{name}/lib/plugins/junit-4.10.jar
ln -sf $(build-classpath checkstyle) %{buildroot}%{_datadir}/%{name}/lib/plugins/checkstyle.jar
ln -sf $(build-classpath maven-ant-tasks) %{buildroot}%{_datadir}/%{name}/lib/plugins/maven-ant-tasks-2.1.3.jar
ln -sf $(build-classpath maven/maven-artifact) %{buildroot}%{_datadir}/%{name}/lib/plugins/maven-artifact.jar
ln -sf $(build-classpath maven/maven-compat) %{buildroot}%{_datadir}/%{name}/lib/plugins/maven-compat.jar
ln -sf $(build-classpath maven/maven-core) %{buildroot}%{_datadir}/%{name}/lib/plugins/maven-core.jar
# java.lang.ClassNotFoundException: org.sonatype.aether.* aether-api.jar,aether-util.jar
ln -sf $(build-classpath aether/api) %{buildroot}%{_datadir}/%{name}/lib/plugins/aether-api.jar
ln -sf $(build-classpath aether/util) %{buildroot}%{_datadir}/%{name}/lib/plugins/aether-util.jar
ln -sf $(build-classpath maven/maven-model) %{buildroot}%{_datadir}/%{name}/lib/plugins/maven-model.jar
ln -sf $(build-classpath maven/maven-settings) %{buildroot}%{_datadir}/%{name}/lib/plugins/maven-settings.jar
ln -sf $(build-classpath maven/maven-settings-builder) %{buildroot}%{_datadir}/%{name}/lib/plugins/maven-settings-builder.jar
ln -sf $(build-classpath plexus/container-default) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-container-default.jar
ln -sf $(build-classpath plexus/classworlds) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-classworlds.jar
ln -sf $(build-classpath plexus/interpolation) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-interpolation.jar
ln -sf $(build-classpath plexus/utils) %{buildroot}%{_datadir}/%{name}/lib/plugins/plexus-utils.jar
ln -sf $(build-classpath snakeyaml) %{buildroot}%{_datadir}/%{name}/lib/plugins/snakeyaml-1.6.jar
ln -sf $(build-classpath testng) %{buildroot}%{_datadir}/%{name}/lib/plugins/testng-6.3.1.jar

mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}
(
  cd %{buildroot}%{_datadir}/%{name}/media
  for png in 16x16 24x24 32x32 48x48 64x64 128x128 256x256 512x512;do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${png}/apps
    ln -sf ../../../../%{name}/media/%{name}-icon-${png}.png %{buildroot}%{_datadir}/icons/hicolor/${png}/apps/%{name}.png
  done
)
desktop-file-validate %{name}.desktop
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
    --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

%files
%{_bindir}/%{name}
%{_javadir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%{_datadir}/%{name}/bin/%{name}
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/media
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%doc %{_datadir}/%{name}/LICENSE
%doc %{_datadir}/%{name}/NOTICE
%doc %{_datadir}/%{name}/changelog.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_13jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

