%define _unpackaged_files_terminate_build 1

Name:           ion-java
Version:        1.12.1
Release:        alt1
Summary:        Java implementation of the Amazon Ion data notation
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/amazon-ion/ion-java
VCS:            https://github.com/amazon-ion/ion-java

Source0:        %name-%version.tar
Source1:        ion-tests.tar.xz
Patch0:         %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.vintage:junit-vintage-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(pl.pragmatists:JUnitParams)
BuildRequires: mvn(com.github.luben:zstd-jni)

BuildArch:      noarch

%description
Ion Java is Amazon's Java implementation of the Ion data notation.
It publishes the upstream com.amazon.ion:ion-java API with Java 8 bytecode
and the system Kotlin runtime dependency.

%prep
%setup -q -a1
%patch0 -p1
cp build-alt.gradle.kts build.gradle.kts
cp settings-alt.gradle.kts settings.gradle.kts

%build
%gradle_publish

%install
%gradle_register --artifacts=ion-java
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE NOTICE THIRD_PARTY_LICENSES.md

%changelog
* Fri Nov 13 2026 Ivan Khanas <xeno@altlinux.org> 1.12.1-alt1
- Initial build for ALT.
