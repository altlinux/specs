%define _unpackaged_files_terminate_build 1

Name: cryptohash
Version: 1.0.2
Release: alt1

Summary: Cryptographic hashing functions for Kotlin and Java
License: Apache-2.0 AND MIT AND BSD-2-Clause
Group: Development/Java
URL: https://github.com/appmattus/crypto
VCS: https://github.com/appmattus/crypto.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: gradle-coroutines.xml

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-11-openjdk-devel
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-stdlib
BuildRequires: kotlin-test
BuildRequires: junit
BuildRequires: bouncycastle

%description
Cryptographic hashing functions implemented in Kotlin, including cryptographic
and non-cryptographic digest algorithms. This package publishes the common
metadata and JVM implementation for Gradle and Java consumers.

%prep
%setup -q
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
test -s %_datadir/gradle/lib/kotlinx-coroutines-core-jvm-1.10.2.jar
mkdir -p .xmvn/gradle-metadata
cp %SOURCE1 .xmvn/gradle-metadata/coroutines.xml
subst 's|@DATADIR@|%_datadir|g' .xmvn/gradle-metadata/coroutines.xml

%build
system_data=%_datadir
%mvn_config resolverSettings/metadataRepositories \
    "<repository>$PWD/.xmvn/gradle-metadata</repository>\
<repository>$system_data/maven-metadata</repository>\
<repository>$system_data/javapackages-bootstrap/maven-metadata</repository>"
%gradle_publish -PpackageVersion=%version

%install
%gradle_register --artifacts=cryptohash
%gradle_install

%check
%gradle_check -PpackageVersion=%version

%files -f .mfiles
%doc LICENSE cryptohash/NOTICE.md

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
