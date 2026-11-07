%define _unpackaged_files_terminate_build 1

Name: urlencoder
Version: 1.6.0
Release: alt1

Summary: Defensive URL encoding and decoding for Kotlin
License: Apache-2.0
Group: Development/Java
URL: https://github.com/ethauvin/urlencoder
VCS: https://github.com/ethauvin/urlencoder.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: system-gradle.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit5)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)

%description
Kotlin library for defensive UTF-8 URL component encoding and decoding,
with its command-line application. Includes JVM libraries and genuine
multiplatform metadata from the complete upstream source release.

%prep
%setup
%autopatch -p1

%build
%gradle_publish --no-configuration-cache

%install
%gradle_register --artifacts=urlencoder
%gradle_install
install -d %buildroot%_bindir
cat > %buildroot%_bindir/urlencoder <<'SH'
#!/bin/sh
exec java -cp "%_javadir/urlencoder/*:%_javadir/kotlin/kotlin-stdlib.jar" \
    net.thauvin.erik.urlencoder.UrlEncoder "$@"
SH
chmod 755 %buildroot%_bindir/urlencoder

%check
%gradle_check --no-configuration-cache

%files -f .mfiles
%_bindir/urlencoder
%doc LICENSE.txt

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.6.0-alt1
- Initial build for ALT.
