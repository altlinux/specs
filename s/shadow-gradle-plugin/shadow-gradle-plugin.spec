%define _unpackaged_files_terminate_build 1

Name: shadow-gradle-plugin
Version: 8.3.8
Release: alt1

Summary: Gradle plugin for creating fat/uber JARs
License: Apache-2.0
Group: Development/Java
Url: https://gradleup.com/shadow
Vcs: https://github.com/GradleUp/shadow.git
ExcludeArch: i586

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: 0001-Disable-signing-with-key.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
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

%build
gradle publishToMavenLocal \
  -x :javadoc \
  -g "$PWD/.gradle" \
  --offline
  #

%install
install -Dm 644 build/libs/shadow-%version.jar \
  %buildroot%_javadir/gradleUp-shadow/shadow-gradle-plugin.jar

find ~/.m2 -name shadow-gradle-plugin-%version.pom -exec \
  install -Dm 644 \
  -t %buildroot%_datadir/maven-poms/gradleUp-shadow/shadow-gradle-plugin.pom \
  {} + \
  #

%check
# Skip tests that require network(maven central) access.
gradle check \
  -x :compileTestGroovy \
  -g "$PWD/.gradle" \
  #

%files
%_javadir/gradleUp-shadow/shadow-gradle-plugin.jar
%_datadir/maven-poms/gradleUp-shadow/shadow-gradle-plugin.pom

%changelog
* Sat Aug 02 2025 Ivan Khanas <xeno@altlinux.org> 8.3.8-alt1
- First build for ALT.
