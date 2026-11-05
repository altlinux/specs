%define _unpackaged_files_terminate_build 1

Name: plumelib-javac-parse
Version: 1.0.0
Release: alt1

Summary: Java source parser using javac
License: GPL-2.0-only WITH Classpath-exception-2.0
Group: Development/Java
URL: https://github.com/plume-lib/javac-parse
VCS: https://github.com/plume-lib/javac-parse.git

Source: %name-%version.tar
Patch: javac-parse-%version-alt-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: glibc-utils
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.checkerframework:checker-qual)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.plumelib:plume-util)

%description
Javac Parse wraps the javac parser to parse Java compilation units,
expressions, type declarations, and members with diagnostic information.
It requires JDK 17 or later and access to internal jdk.compiler packages.

%prep
%setup -q
if [ "$(getconf LONG_BIT)" = 32 ]; then
    sed -i 's/-Xmx6g/-Xmx1g/' gradle.properties
fi
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=javac-parse
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- Initial build for ALT.
