%define _unpackaged_files_terminate_build 1

Name: jemoji
Version: 2.1.0
Release: alt1

Summary: Java library for Unicode emoji
License: Apache-2.0 AND MIT AND Unicode-3.0
Group: Development/Java
URL: https://github.com/felldo/JEmoji
VCS: https://github.com/felldo/JEmoji.git

Source: %name-%version.tar
Source1: %name-offline-data.tar
Patch0: 0001-Use-system-Gradle-and-libraries.patch
Patch1: 0002-Generate-emoji-data-offline.patch
Patch2: 0003-Build-the-generator-from-source.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-gradle-plugin)
BuildRequires: mvn(tools.jackson.core:jackson-databind)
BuildRequires: mvn(tools.jackson.module:jackson-module-kotlin)
BuildRequires: mvn(org.jsoup:jsoup)
BuildRequires: mvn(com.squareup.okhttp3:okhttp)
BuildRequires: mvn(com.squareup:javapoet)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)

%description
A Java library for looking up and parsing Unicode emoji.

%package languages
Summary: Localized descriptions and keywords for JEmoji
Group: Development/Java

%description languages
The CLDR translations of emoji names and keywords used by JEmoji.

%prep
%setup -q -a 1
cp -a %name-offline-data/. emoji_source_files/
%autopatch -p1
%mvn_package :jemoji-languages languages

%build
%gradle_publish

%install
%gradle_register --artifacts=jemoji,jemoji-languages
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE
%doc emoji_source_files/EMOJI-DATA-LICENSE
%doc emoji_source_files/UNICODE-LICENSE.txt

%files languages -f .mfiles-languages

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
