%define _unpackaged_files_terminate_build 1
%def_without bootstrap

Name: gradle
Version: 8.14.3
Release: alt1

Summary: A highly scalable build automation tool
License: Apache-2.0
Group: Development/Java
Url: https://gradle.org
Vcs: https://github.com/gradle/gradle.git
ExcludeArch: i586

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-%version-tags.tar
%if_with bootstrap
Source3: %name-bin.tar
%endif
Source4: commit.sh

Patch0: 0001-Gradle-adoptium-alt-patch.patch
Patch1: 0002-Gradle-set-buildtime-alt-patch.patch
Patch2: 0003-Gradle-set-git-specifications-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: gradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-11-openjdk-devel
BuildRequires: java-17-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: git

%description
Gradle is a highly scalable build automation tool designed to handle everything
from large, multi-project enterprise builds to quick development tasks across
various languages. Gradles modular, performance-oriented architecture
seamlessly integrates with development environments, making it a go-to solution
for building, testing, and deploying applications on Java, Kotlin, Scala,
Android, Groovy, C++, and Swift.

%prep
%setup -a1 -a2
%autopatch -p1

%if_with bootstrap
tar -xf %SOURCE3

# Specify the archive location.
sed -i "s#distributionUrl=.*#distributionUrl=file\:$PWD/%name-bin.zip#" \
    gradle/wrapper/gradle-wrapper.properties
%endif

cp %SOURCE4 .
chmod +x commit.sh

%build
export GRADLE_USER_HOME="$PWD/.gradle"

COMMITHASH=$(./commit.sh)

# Skip task :docs:javadocAll that requires .git directory.
gradle installAll \
  -x :docs:javadocAll \
  -Porg.gradle.java.installations.paths="%_jvmdir/java-11-openjdk,%_jvmdir/java-17-openjdk,%_jvmdir/java-21-openjdk" \
  -Porg.gradle.java.installations.auto-detect=false \
  -Pgradle_installPath="$PWD/dist" \
  -PfinalRelease=true \
  -DbuildTimestampIso="$(date -u -d "@${SOURCE_DATE_EPOCH}" +"%%Y-%%m-%%d %%H:%%M:%%S")" \
  -DgitCommitId="$COMMITHASH" \
  -DgitBranch="sisyphus" \
  -Dorg.gradle.java.installations.auto-download=false \
  --no-configuration-cache \
  --no-build-cache \
  --offline \
  #

%install
install -Dm 644 dist/lib/*.jar \
  -t %buildroot%_datadir/gradle/lib/

install -Dm 644 dist/lib/plugins/*.jar \
  -t %buildroot%_datadir/gradle/lib/plugins/

install -Dm 644 dist/lib/agents/gradle-instrumentation-agent-%version.jar \
  -t %buildroot%_datadir/gradle/lib/agents/

install -Dm 755 dist/bin/gradle \
  -t %buildroot%_datadir/gradle/bin/

install -d %buildroot%_bindir

ln -s %_datadir/gradle/bin/gradle \
  -t %buildroot%_bindir/

%files
%_bindir/gradle
%_datadir/gradle/

%changelog
* Mon Aug 18 2025 Ivan Khanas <xeno@altlinux.org> 8.14.3-alt1
- New version.
- Change installation paths.

* Thu Jul 31 2025 Ivan Khanas <xeno@altlinux.org> 8.14.1-alt2
- Disable bootstrap.

* Thu May 29 2025 Ivan Khanas <xeno@altlinux.org> 8.14.1-alt1
- New version.
- Bootstrap build.

* Thu Apr 02 2020 Igor Vlasenko <viy@altlinux.ru> 4.4.1-alt2_3jpp8
- fixed build

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.4.1-alt1_3jpp8
- new version

* Mon Jun 04 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt3_7jpp8
- unbootstrap rebuild with new guava and objectweb-asm

* Mon Jun 04 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt2_7jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1_7jpp8
- java fc28+ update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1_5jpp8
- unbootstrap build

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_10jpp8
- fixed build with new checkstyle

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1_7jpp8
- rebuild with new xpp3

* Wed Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_1jpp8
- unbootstrap build

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_3jpp8
- unbootstrap build

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

