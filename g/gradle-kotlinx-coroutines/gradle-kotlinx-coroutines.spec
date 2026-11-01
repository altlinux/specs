%define _unpackaged_files_terminate_build 1
%add_findreq_skiplist %_javadir/%name/kotlinx-coroutines-core-jvm.jar
%define gradle_evr 9.7.1-alt2
%define componentname kotlinx-coroutines-core-jvm-%version.jar
%define componentjar %_datadir/gradle/lib/%componentname

Name: gradle-kotlinx-coroutines
Version: 1.10.2
Release: alt1

Summary: XMvn metadata for the coroutines library supplied by Gradle
License: Apache-2.0
Group: Development/Java
BuildArch: noarch
Url: https://github.com/Kotlin/kotlinx.coroutines
VCS: https://github.com/gradle/gradle.git

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-java
BuildRequires: gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin
BuildRequires: maven-local
BuildRequires: mvn(org.jetbrains:annotations)
Requires: gradle = %gradle_evr

%description
Maven metadata and a Java library symlink for the genuine Kotlin coroutines
component already supplied by ALT Gradle. The target is checked against the
upstream artifact checksum. This package does not copy the compiled library.
Its exact Gradle dependency keeps the provider and component path aligned.

%prep
%setup
# Both runtime dependencies have explicit versions; no BOM provider is needed.
%pom_xpath_remove 'pom:dependencyManagement' coroutines.pom

%build
# XMvn may inject a manifest into its input; use a private working copy.
cp -p %componentjar component.jar
sha256sum -c gradle-component.sha256
%mvn_artifact coroutines.pom component.jar
%mvn_file org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm \
    %name/kotlinx-coroutines-core-jvm

%install
%mvn_install
rm %buildroot%_javadir/%name/kotlinx-coroutines-core-jvm.jar
ln -s %componentjar \
    %buildroot%_javadir/%name/kotlinx-coroutines-core-jvm.jar

%check
bash check.sh %buildroot%_javadir/%name/kotlinx-coroutines-core-jvm.jar \
    %_javadir/kotlin/kotlin-stdlib.jar %_bindir/kotlinc \
    %_jvmdir/java-21-openjdk/bin/java check-classes

%files -f .mfiles
%doc README ORIGINS.json LICENSE.txt

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.10.2-alt1
- Initial build for ALT.
