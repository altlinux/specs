%define _unpackaged_files_terminate_build 1
%define framework_version 8.0.11

Name: knopflerfish
Version: 6.1.5
Release: alt1

Summary: Knopflerfish OSGi Service Platform
License: BSD-3-Clause
Group: Development/Java
Url: https://www.knopflerfish.org/
Vcs: https://github.com/knopflerfish/knopflerfish.org
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: ant
BuildRequires: jpackage-default
BuildRequires: javapackages-local
BuildRequires: objectweb-asm3
BuildRequires: osgi-annotation

# This is a multi-module legacy project that requires a lot of time to
# build the entire project. For the purposes of building freeplane,
# I only needed the knopflerfish-framework. If for some reasons you need
# other modules, the acl is always open for you. You can also create a
# request to build other modules via https://bugzilla.altlinux.org/
%package framework
Summary: Knopflerfish OSGi Framework
Group: Development/Java

%description
Knopflerfish is a leading universal open source OSGi Service Platform.
Knopflerfish implements it's own OSGi framework as defined by the OSGi
Core Specification and a o a large set of the bundles / services defined
by OSGi Compendium Specification.

%description framework
Knopflerfish is a leading universal open source OSGi Service Platform.
Knopflerfish implements it's own OSGi framework as defined by the OSGi
Core Specification and a o a large set of the bundles / services defined
by OSGi Compendium Specification.

This package contains Knopflerfish OSGi framework system bundle.

%prep
%setup
%autopatch -p1
find -type f '(' -name '*.jar' -o -iname '*.class' ')' -print -delete

ln -s "$(xmvn-resolve asm:asm)" osgi/framework/libs/asm-3.2.jar
ln -s "$(xmvn-resolve org.osgi:osgi.annotation)" osgi/annotations/osgi.annotation-6.0.1.jar

cat > framework.pom <<'EOF'
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.knopflerfish.kf6</groupId>
  <artifactId>framework</artifactId>
  <version>%framework_version</version>
  <packaging>jar</packaging>
  <name>Knopflerfish Framework</name>
</project>
EOF

%build
ANT_OPTS='-Dfile.encoding=UTF-8' ant -f osgi/framework/build.xml clean jar

%install
%mvn_artifact framework.pom osgi/framework.jar
%mvn_package :framework knopflerfish-framework
%mvn_install

%files framework -f .mfiles-knopflerfish-framework
%doc NOTICE.txt LICENSE.txt

%changelog
* Wed Apr 22 2026 Arseniy Kostevich <faux@altlinux.org> 6.1.5-alt1
- Initial build for ALT.
