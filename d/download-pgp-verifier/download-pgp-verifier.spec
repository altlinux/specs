%define _unpackaged_files_terminate_build 1

Name: download-pgp-verifier
Version: 1.0.1
Release: alt1

Summary: JetBrains PGP signature verification library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/download-pgp-verifier
VCS: https://github.com/JetBrains/download-pgp-verifier.git

Source: %name-%version.tar
Patch: publish-version.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.bouncycastle:bcpg-jdk18on)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)

BuildArch: noarch

%description
A JVM library for verifying PGP signatures and SHA-256 checksums of JetBrains
software downloads.

%prep
%setup
%autopatch -p1

%build
cd jvm
%gradle_publish --no-daemon

%install
cd jvm
%gradle_register --artifacts=download-pgp-verifier
%gradle_install

%check
cd jvm
%gradle_check --no-daemon

%files -f jvm/.mfiles
%doc LICENSE

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
