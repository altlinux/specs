BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
AutoReq: yes,noosgi
Name: tycho
Version: 0.16.0
Summary: Plugins and extensions for building Eclipse plugins and OSGI bundles with Maven
License: ASL 2.0
Url: http://tycho.sonatype.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: decentxml
Requires: eclipse-jdt
Requires: jpackage-utils
Requires: maven
Requires: maven-clean-plugin
Requires: maven-dependency-plugin
Requires: maven-shared-verifier
Requires: maven-surefire-provider-junit4
Requires: objectweb-asm4

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tycho-0.16.0-7.df2c35.fc19.cpio

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
* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

