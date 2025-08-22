%define _unpackaged_files_terminate_build 1

Name: biz-aQute-bnd-gradle-plugins
Version: 7.1.0
Release: alt1

Summary: Gradle plugins for bnd - tools for OSGi bundle development and management
License: Apache-2.0
Group: Development/Java
Url: https://bndtools.org
Vcs: https://github.com/bndtools/bnd
ExcludeArch: i586

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: install_poms.sh
Source3: install_jars.sh
Patch0: 0001-Build-shadowJar-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: gradle
BuildRequires: git

%package javadoc
Summary: API documentation for bnd Gradle plugins
Group: Development/Java

%description
The biz-aQute-bnd-gradle-plugins package provides Gradle plugins for the bnd
toolset used for OSGi bundle development and management. These plugins
integrate bnd's capabilities into Gradle builds, allowing developers to create
and manage OSGi bundles with proper manifest generation, handle bundle
dependencies and versioning, perform bundle analysis and validation, support
bnd workspace configuration, and simplify OSGi development workflow in Gradle
projects.

%description javadoc
This package contains API documentation for the bnd Gradle plugins, providing
detailed information about plugin configuration options, task definitions,
extension points, and API references for developers working with OSGi bundle
development in Gradle projects.

%prep
%setup
%autopatch -p1

tar -xf %SOURCE1 -C "$PWD/gradle-plugins"

cp %SOURCE2 .
chmod +x install_poms.sh

cp %SOURCE3 .
chmod +x install_jars.sh

%build
pushd gradle-plugins
gradle publishToMavenLocal \
  -g "$PWD/.gradle" \
  -x check \
  --offline \
  #
popd

%install
./install_poms.sh ~/.m2 %buildroot%_mavenpomdir/biz-aQute-bnd-gradle-plugins

./install_jars.sh $PWD/gradle-plugins/biz.aQute.bnd.gradle/build/libs \
  %buildroot%_javadir/biz-aQute-bnd-gradle-plugins \
  %buildroot%_javadocdir/biz-aQute-bnd-gradle-plugins \
  #

%files
%_javadir/biz-aQute-bnd-gradle-plugins/biz.aQute.bnd.gradle.jar
%_mavenpomdir/biz-aQute-bnd-gradle-plugins/biz.aQute.bnd.builder.gradle.plugin.pom
%_mavenpomdir/biz-aQute-bnd-gradle-plugins/biz.aQute.bnd.gradle.plugin.pom
%_mavenpomdir/biz-aQute-bnd-gradle-plugins/biz.aQute.bnd.gradle.pom
%_mavenpomdir/biz-aQute-bnd-gradle-plugins/biz.aQute.bnd.workspace.gradle.plugin.pom

%files javadoc
%_javadocdir/biz-aQute-bnd-gradle-plugins/biz.aQute.bnd.gradle-javadoc.jar

%changelog
* Thu Aug 21 2025 Ivan Khanas <xeno@altlinux.org> 7.1.0-alt1
- First build for ALT.
