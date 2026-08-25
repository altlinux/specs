%define _unpackaged_files_terminate_build 1
%def_with bootstrap

%ifarch %ix86
%def_without java21plus
%else
%def_with java21plus
%endif

Name: gradle
Version: 9.7.1
Release: alt2

Summary: A highly scalable build automation tool
License: Apache-2.0
Group: Development/Java
Url: https://gradle.org
Vcs: https://github.com/gradle/gradle.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name-%version-tags.tar
%{?_with_bootstrap:Source3: %name-bin.tar}
Source4: commit.sh

Patch0: 0001-Gradle-adoptium-alt-patch.patch
Patch1: 0002-Gradle-set-buildtime-alt-patch.patch
Patch2: 0003-Gradle-set-git-specifications-alt-patch.patch
# https://github.com/gradle/gradle/issues/38911
# https://github.com/gradle/gradle/pull/38913
Patch3: 0004-Stop-capturing-the-release-notes-date-formatters-alt-patch.patch
# Error Prone 2.43 and later are compiled for Java 21, which %ix86 has no JDK for.
# 2.42.0 is the last release still running on Java 17.
# The annotations artifact ships inside the distribution, so it stays at 2.50.0.
Patch4: 0005-Gradle-downgrade-error-prone-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
%{!?_with_bootstrap:BuildRequires: gradle}
BuildRequires: rpm-build-java-osgi
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-11-openjdk-devel
BuildRequires: java-17-openjdk-devel
%{?_with_java21plus:BuildRequires: java-21-openjdk-devel}
%{?_with_java21plus:BuildRequires: java-25-openjdk-devel}
BuildRequires: git
%add_findreq_skiplist %_datadir/gradle/lib/plugins/org.eclipse.jgit.ssh.apache.agent-*.jar
Requires: jna-contrib

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

%if_without java21plus
find -type f -name gradle.properties -print0 |
        xargs -r0 sed -i 's,-Xmx[0-9][0-9]*m,-Xmx1500m,'

# No JDK 21+ here, so run the daemon on the newest JDK this arch has.
# Upstream rewrites this file the same way for its Gradleception builds.
sed -i 's,^toolchainVersion=.*,toolchainVersion=17,' \
    gradle/gradle-daemon-jvm.properties
%endif

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
%{?_with_bootstrap:./gradlew installAll} \
%{!?_with_bootstrap:gradle installAll} \
  -x :docs:javadocAll \
  %{!?_with_java21plus:-x :docs:compileJava} \
  %{?_with_java21plus:\
  -Porg.gradle.java.installations.paths="%_jvmdir/java-1.8.0-openjdk,%_jvmdir/java-11-openjdk,%_jvmdir/java-17-openjdk,%_jvmdir/java-21-openjdk,%_jvmdir/java-25-openjdk"\
  } \
  %{!?_with_java21plus:\
  -Porg.gradle.java.installations.paths="%_jvmdir/java-1.8.0-openjdk,%_jvmdir/java-11-openjdk,%_jvmdir/java-17-openjdk" \
  } \
  -Porg.gradle.java.installations.auto-detect=false \
  -Pgradle_installPath="$PWD/dist" \
  -PfinalRelease=true \
  -DbuildTimestampIso="$(date -u -d "@${SOURCE_DATE_EPOCH}" +"%%Y-%%m-%%d %%H:%%M:%%S")" \
  -DgitCommitId="$COMMITHASH" \
  -DgitBranch="sisyphus" \
  -Dorg.gradle.java.installations.auto-download=false \
  -Dorg.gradle.unsafe.isolated-projects=false \
  --no-configuration-cache \
  --no-build-cache \
  --offline \
  #

%install
install -d %buildroot%_datadir/gradle/lib
cp -a dist/lib/. %buildroot%_datadir/gradle/lib/
find %buildroot%_datadir/gradle/lib -type d -exec chmod 755 {} +
find %buildroot%_datadir/gradle/lib -type f -exec chmod 644 {} +

install -Dm 755 dist/bin/gradle \
  -t %buildroot%_datadir/gradle/bin/

install -d %buildroot%_bindir

ln -s %_datadir/gradle/bin/gradle \
  -t %buildroot%_bindir/

%files
%_bindir/gradle
%_datadir/gradle/

%changelog
* Tue Aug 25 2026 Ivan Khanas <xeno@altlinux.org> 9.7.1-alt2
- Start to package descriptors.

* Fri Aug 21 2026 Ivan Khanas <xeno@altlinux.org> 9.7.1-alt1
- New version.

* Fri Oct 17 2025 Ivan Khanas <xeno@altlinux.org> 8.14.3-alt2
- Noarch packaging.

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
