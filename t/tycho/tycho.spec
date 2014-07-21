# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# Bootstrap build
# Set this if Tycho and Eclipse are not in buildroot
%global bootstrap 0
# When building version under development (non-release)
# %%global snap -SNAPSHOT

%define __requires_exclude osgi*

Name:           tycho
Version:        0.16.0
Release:        alt1_19jpp7
Summary:        Plugins and extensions for building Eclipse plugins and OSGI bundles with Maven

Group:          Development/Java
# license file is missing but all files having some licensing information are ASL 2.0
License:        ASL 2.0
URL:            http://tycho.sonatype.org/
Source0:        http://git.eclipse.org/c/tycho/org.eclipse.tycho.git/snapshot/tycho-0.16.x.tar.bz2

# this is a workaround for maven-plugin-plugin changes that happened after
# version 2.4.3 (impossible to have empty mojo created as aggregate). This
# should be fixed upstream properly
Source1:        EmptyMojo.java
# we need to make sure we are using maven 3 deps
Source2:        depmap.xml
Source3:        copy-platform-all
# Bootstrap repo for building when Tycho and Eclipse not built.
%if %{bootstrap}
Source4:        maven-repo.tar.xz
%endif

Patch0:         %{name}-fix-build.patch
# Upstream builds against maven-surefire 2.12.3
Patch1:         %{name}-maven-surefire.patch
Patch2:         %{name}-fix-surefire.patch
Patch3:         %{name}-use-custom-resolver.patch
# Set some temporary build version so that the bootstrapped build has
# a different version from the nonbootstrapped. Otherwise there will
# be cyclic dependencies.
Patch4:         %{name}-bootstrap.patch
# Maven local mode will look in reactor cache for exact version (path lookup)
# Set the built intermediary version of Tycho to be found in the reactor cache
Patch5:         %{name}-set-reactor-cache-version.patch
# These units cannot be found during a regular build
Patch6:         %{name}-remove-units.patch
# Additional changes needed just for bootstrap build
Patch7:         %{name}-fix-bootstrap-build.patch
# Fix https://bugs.eclipse.org/bugs/show_bug.cgi?id=361204
Patch8:         %{name}-361204.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-shared-verifier
BuildRequires:  maven-shared-osgi
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  objectweb-asm4
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  decentxml
BuildRequires:  ecj
%if ! %{bootstrap}
BuildRequires:  osgi(org.eclipse.jdt)
BuildRequires:  %{name}
%endif

Requires:       jpackage-utils
Requires:       decentxml
Requires:       maven
Requires:       maven-clean-plugin
Requires:       maven-dependency-plugin
Requires:       maven-shared-verifier
Requires:       maven-surefire-provider-junit4
Requires:       objectweb-asm4
Requires:       ecj
%if ! %{bootstrap}
Requires:       osgi(org.eclipse.platform)
%endif
Source44: import.info


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



%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-0.16.x

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch8 -p1

find tycho-core -iname '*html' -delete

# place empty mojo in place
mkdir -p tycho-maven-plugin/src/main/java/org/fedoraproject
pushd tycho-maven-plugin/src/main/java/org/fedoraproject
cp %{SOURCE1} .
popd

# Bootstrap Build
%if %{bootstrap}
tar -xf %{SOURCE4}
%patch7 -p1

# Non-Bootstrap Build
%else

%patch6 -p1

# installed version of Tycho
sysVer=`grep -C 1 "<artifactId>tycho</artifactId>" %{_mavenpomdir}/JPP.tycho-main.pom | grep "version" | sed 's/.*>\(.*\)<.*/\1/'`

# build version of Tycho
buildVer=`grep -C 1 "<artifactId>tycho</artifactId>" pom.xml | grep "version" | sed 's/.*>\(.*\)<.*/\1/'`

echo "System version is ${sysVer} and attempting to build ${buildVer}."

# If version installed on system is the same as the version being built
# an intermediary build must be done to prevent a cycle at build time.
if [ "${sysVer}" == "${buildVer}" ]; then
echo "Performing intermediary build"
%patch4 -p1

mvn-rpmbuild -Dmaven.local.depmap.file=%{SOURCE2} -DskipTychoVersionCheck -Dmaven.test.skip=true install javadoc:aggregate

%patch4 -p1 -R
%patch5 -p1
fi

%endif

%build
mvn-rpmbuild -Dmaven.local.depmap.file=%{SOURCE2} -DskipTychoVersionCheck -Dmaven.test.skip=true clean install javadoc:aggregate

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

# pom and jar installation
for mod in target-platform-configuration tycho-compiler-{jdt,plugin} \
           tycho-{artifactcomparator,core,embedder-api,metadata-model,testing-harness} \
           sisu-equinox/sisu-equinox{-api,-launching,-embedder} \
           tycho-p2/tycho-p2-{facade,plugin,{director,publisher,repository}-plugin} \
           tycho-{maven,packaging,pomgenerator,release/tycho-versions,source}-plugin \
           tycho-bundles/org*  \
           tycho-surefire/{tycho-surefire-plugin,org.eclipse.tycho.surefire.{osgibooter,junit,junit4{,7}}}; do
   echo $mod
   aid=`basename $mod`
   install -pm 644 $mod/pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-$aid.pom
   install -m 644 $mod/target/$aid-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$aid.jar
   %add_maven_depmap JPP.%{name}-$aid.pom %{name}/$aid.jar -a "org.eclipse.tycho:$aid,org.sonatype.tycho:$aid"
done

# pom installation
for pommod in tycho-p2 tycho-bundles tycho-surefire \
              tycho-release sisu-equinox; do
   aid=`basename $pommod`
   install -pm 644 $pommod/pom.xml \
               $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-$aid.pom
   %add_maven_depmap JPP.%{name}-$aid.pom -a "org.eclipse.tycho:$aid,org.sonatype.tycho:$aid"
done

# p2 runtime
pushd tycho-bundles/tycho-bundles-external
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-tycho-bundles-external.pom
install -m 644 target/tycho-bundles-external-%{version}*.zip $RPM_BUILD_ROOT%{_javadir}/%{name}/tycho-bundles-external.zip
%add_maven_depmap JPP.%{name}-tycho-bundles-external.pom %{name}/tycho-bundles-external.zip -a "org.eclipse.tycho:tycho-bundles-external,org.sonatype.tycho:tycho-bundles-external"
popd

# main
install -pm 644 pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-main.pom
%add_maven_depmap JPP.%{name}-main.pom -a "org.eclipse.tycho:$aid,org.sonatype.tycho:$aid"

# standalone p2 director
pushd .m2/org/eclipse/tycho/tycho-standalone-p2-director/%{version}*/
install -m 644 tycho-standalone-p2-director-%{version}*.zip $RPM_BUILD_ROOT%{_javadir}/%{name}/tycho-standalone-p2-director.zip
install -pm 644 tycho-standalone-p2-director-%{version}*.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-tycho-standalone-p2-director.pom
popd
%add_maven_depmap JPP.%{name}-tycho-standalone-p2-director.pom tycho/tycho-standalone-p2-director.zip -a "org.eclipse.tycho:tycho-standalone-p2-director,org.sonatype.tycho:tycho-standalone-p2-director"

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/api*/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -pm 755 %{SOURCE3} $RPM_BUILD_ROOT%{_javadir}/%{name}/copy-platform-all

%if %{bootstrap}
# org.eclipse.osgi
osgiJarPath=`find ".m2" -name "org.eclipse.osgi_*.jar"`
osgiJar=`basename $osgiJarPath`
osgiVer=`echo $osgiJar | sed 's/^.*_//' | sed 's/.jar//'`

mvn-rpmbuild org.apache.maven.plugins:maven-install-plugin:install-file \
-Dfile=$osgiJarPath \
-Dpackaging=jar \
-DgroupId=org.eclipse.tycho \
-DartifactId=org.eclipse.osgi \
-Dversion=$osgiVer

osgiPomPath=`find ".m2/org/eclipse/tycho/org.eclipse.osgi" -name "org.eclipse.osgi-$osgiVer.pom"`

install -pm 644 $osgiPomPath $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.tycho-osgi.pom
install -m 644 $osgiJarPath $RPM_BUILD_ROOT%{_javadir}/%{name}/osgi.jar
%add_maven_depmap JPP.%{name}-osgi.pom %{name}/osgi.jar -a "org.eclipse.tycho:org.eclipse.osgi"
%endif

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}/
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_19jpp7
- update

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

