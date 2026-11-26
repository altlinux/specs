%define _unpackaged_files_terminate_build 1

Name: koin
Version: 4.2.2
Release: alt1
Summary: Dependency injection framework for Kotlin

License: Apache-2.0
Group: Development/Java
Url: https://github.com/InsertKoinIO/koin
VCS: https://github.com/InsertKoinIO/koin.git

# Source-url: https://github.com/InsertKoinIO/koin/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: java-devel
BuildRequires: maven-local
BuildRequires: kotlin-plugins
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-maven-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-compose-compiler-plugin-embeddable)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains.compose.runtime:runtime)
BuildRequires: mvn(org.jetbrains.compose.foundation:foundation)
BuildRequires: mvn(org.jetbrains.androidx.lifecycle:lifecycle-viewmodel-compose)
BuildRequires: stately-concurrency
BuildRequires: stately-concurrent-collections

%description
Koin is a lightweight dependency injection framework for Kotlin applications.
This package builds the core and Compose JVM libraries from upstream sources.

%package core-viewmodel
Summary: Koin ViewModel integration for Kotlin applications
Group: Development/Java

%description core-viewmodel
JVM library integrating Koin with the multiplatform lifecycle ViewModel API.

%package compose
Summary: Koin integration for Jetpack Compose Multiplatform
Group: Development/Java

%description compose
JVM library providing Koin APIs for Compose Multiplatform applications.

%package compose-viewmodel
Summary: Koin ViewModel integration for Compose Multiplatform
Group: Development/Java

%description compose-viewmodel
JVM library providing Koin ViewModel APIs for Compose Multiplatform.

%prep
%setup
mkdir -p maven/koin-core maven/koin-core-viewmodel maven/koin-compose maven/koin-compose-viewmodel
cp packaging-alt/maven-parent.xml maven/pom.xml
cp packaging-alt/maven-koin-core.xml maven/koin-core/pom.xml
cp packaging-alt/maven-koin-core-viewmodel.xml maven/koin-core-viewmodel/pom.xml
cp packaging-alt/maven-koin-compose.xml maven/koin-compose/pom.xml
cp packaging-alt/maven-koin-compose-viewmodel.xml maven/koin-compose-viewmodel/pom.xml
for module in koin-core koin-compose; do
    case $module in
        koin-core) src=projects/core/koin-core ;;
        koin-compose) src=projects/compose/koin-compose ;;
    esac
    common=$(find "$src/src/commonMain/kotlin" -type f -name '*.kt' -print | LC_ALL=C sort | sed "s|^|\${project.basedir}/../../|" | paste -sd, -)
    sed -i "s|@COMMON_SOURCES@|$common|" "maven/$module/pom.xml"
done

%build
cd maven
%mvn_package :koin-parent %name
%mvn_package :koin-core %name
%mvn_package :koin-core-viewmodel core-viewmodel
%mvn_package :koin-compose compose
%mvn_package :koin-compose-viewmodel compose-viewmodel
%mvn_build -s

%install
cd maven
%mvn_install

%files -f maven/.mfiles-%name
%doc README.md LICENSE

%files core-viewmodel -f maven/.mfiles-core-viewmodel

%files compose -f maven/.mfiles-compose

%files compose-viewmodel -f maven/.mfiles-compose-viewmodel

%changelog
* Wed Nov 25 2026 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt1
- initial build for ALT.
