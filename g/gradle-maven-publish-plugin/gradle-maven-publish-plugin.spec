%define _unpackaged_files_terminate_build 1

Name: gradle-maven-publish-plugin
Version: 0.34.0
Release: alt2

Summary: Plugin that creates a publish task
License: Apache-2.0
Group: Development/Java
Url: https://vanniktech.github.io/gradle-maven-publish-plugin
Vcs: https://github.com/vanniktech/gradle-maven-publish-plugin.git
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: https://downloads.gradle.org/distributions/gradle-8.14.1-bin.zip
Patch0: 0001-Disable-gpg-signing-and-fix-groupId-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: unzip

%description
Gradle plugin that creates a publish task to automatically upload all of your
Java, Kotlin or Android libraries to any Maven instance. This plugin is based
on Chris Banes initial implementation and has been enhanced to add Kotlin
support and keep up with the latest changes.

%prep
%setup -a1
%autopatch -p1
# The inherited Android build cache was populated with Gradle 8.14.1.
echo "845952a9d6afa783db70bb3b0effaae45ae5542ca2bb7929619e8af49cb634cf  %SOURCE2" | sha256sum -c
unzip -q %SOURCE2
sed -i 's/0\.1\.0-SNAPSHOT/%version/g' gradle.properties

%build
./gradle-8.14.1/bin/gradle --no-daemon --max-workers=2 publishToMavenLocal \
  -g "$PWD/.gradle" \
  --offline \
  #

%install
install -Dm 644 plugin/build/libs/plugin.jar \
  %buildroot%_javadir/gradle-maven-publish-plugin/gradle-maven-publish-plugin.jar

find ~/.m2 -name gradle-maven-publish-plugin-%version.pom -exec \
  install -Dm 644 \
  -t %buildroot%_datadir/maven-poms/gradle-maven-publish-plugin/gradle-maven-publish-plugin.pom \
  {} + \
  #

%check
./gradle-8.14.1/bin/gradle --no-daemon --max-workers=2 check \
  -g "$PWD/.gradle" \
  -x plugin:integrationTest \
  --info \
  --offline \
  #

%files
%_javadir/gradle-maven-publish-plugin/gradle-maven-publish-plugin.jar
%_datadir/maven-poms/gradle-maven-publish-plugin/gradle-maven-publish-plugin.pom

%changelog
* Thu Nov 19 2026 Ivan Khanas <xeno@altlinux.org> 0.34.0-alt2
- Fix FTBFS: Match Gradle to the offline Android cache.

* Mon Jul 28 2025 Ivan Khanas <xeno@altlinux.org> 0.34.0-alt1
- First build for ALT.
