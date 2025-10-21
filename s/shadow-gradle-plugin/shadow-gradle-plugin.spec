%define _unpackaged_files_terminate_build 1
%ifarch %ix86
%def_with heap_optimization
%endif

Name: shadow-gradle-plugin
Version: 8.3.8
Release: alt3

Summary: Gradle plugin for creating fat/uber JARs
License: Apache-2.0
Group: Development/Java
Url: https://gradleup.com/shadow
Vcs: https://github.com/GradleUp/shadow.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: 0001-Disable-signing-with-key.patch
Patch1: 0002-Build-plugin-jar-in-fat-jar.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-17-openjdk-devel
BuildRequires: gradle

%description
Creates executable fat JARs by merging dependencies and resources into a single
archive.  Supports advanced shading/relocation to prevent dependency conflicts
in classpaths.  Enables building self-contained applications for simplified
deployment and distribution.  Essential for standalone Java services and
executable command-line tools.

%prep
%setup -a1
%autopatch -p1

%if_with heap_optimization
sed -i 's/\(-Xmx\)4g/\12g/' gradle.properties
%endif

%build
gradle publishToMavenLocal \
  -x :compileTestGroovy \
  -x :javadoc \
  -g "$PWD/.gradle" \
  --offline
  #

%install

find ~/.m2 -name shadow-gradle-plugin-%version.jar -exec \
  install -Dm 644 {} \
  %buildroot%_javadir/shadow-gradle-plugin/shadow-gradle-plugin.jar \;

find ~/.m2 -name shadow-gradle-plugin-%version.pom -exec \
  install -Dm 644 {} \
  %buildroot%_datadir/maven-poms/shadow-gradle-plugin/shadow-gradle-plugin.pom \;

%check
gradle spotlessApply \
  check \
  -x :compileTestGroovy \
  -g "$PWD/.gradle" \
  #

%files
%_javadir/shadow-gradle-plugin/shadow-gradle-plugin.jar
%_datadir/maven-poms/shadow-gradle-plugin/shadow-gradle-plugin.pom

%changelog
* Tue Oct 21 2025 Ivan Khanas <xeno@altlinux.org> 8.3.8-alt3
- Noarch packaging.

* Thu Aug 07 2025 Ivan Khanas <xeno@altlinux.org> 8.3.8-alt2
- Start packing in fat jar.

* Sat Aug 02 2025 Ivan Khanas <xeno@altlinux.org> 8.3.8-alt1
- First build for ALT.
