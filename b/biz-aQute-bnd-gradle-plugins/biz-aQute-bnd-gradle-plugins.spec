%define _unpackaged_files_terminate_build 1

Name: biz-aQute-bnd-gradle-plugins
Version: 7.1.0
Release: alt3

Summary: Gradle plugins for bnd - tools for OSGi bundle development and management
License: Apache-2.0
Group: Development/Java
Url: https://bndtools.org
Vcs: https://github.com/bndtools/bnd
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: install_poms.sh
Source3: install_jars.sh
Source4: stage-maven-cache.py
Source5: https://downloads.gradle.org/distributions/gradle-8.14.1-bin.zip
Patch0: 0001-Build-shadowJar-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-17-openjdk-devel
BuildRequires: git
BuildRequires: python3-base
BuildRequires: unzip

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
# Use the Gradle line for which the offline cache contains the full Kotlin toolchain.
echo "845952a9d6afa783db70bb3b0effaae45ae5542ca2bb7929619e8af49cb634cf  %SOURCE5" | sha256sum -c
unzip -q %SOURCE5
python3 %SOURCE4 .gradle/caches/modules-2/files-2.1 .maven-cache
./gradle-8.14.1/bin/gradle publishToMavenLocal \
  -Dmaven.repo.local="$PWD/.maven-cache" \
  --no-daemon --max-workers=%__nprocs \
  -g "$PWD/.gradle" \
  -x check \
  --offline \
  #
popd

%install
./install_poms.sh gradle-plugins/.maven-cache %buildroot%_mavenpomdir/biz-aQute-bnd-gradle-plugins

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
* Thu Nov 19 2026 Ivan Khanas <xeno@altlinux.org> 7.1.0-alt3
- Fix FTBFS: Match Gradle to the offline cache.

* Tue Oct 21 2025 Ivan Khanas <xeno@altlinux.org> 7.1.0-alt2
- Noarch packaging.

* Thu Aug 21 2025 Ivan Khanas <xeno@altlinux.org> 7.1.0-alt1
- First build for ALT.
