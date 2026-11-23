%define _unpackaged_files_terminate_build 1

Name: intellij-deps-jdi
Version: 2.48
Release: alt1

Summary: JetBrains JDI fork for IntelliJ Platform
License: GPL-2.0-only WITH Classpath-exception-2.0
Group: Development/Java
URL: https://github.com/JetBrains/intellij-deps-jdi
VCS: https://github.com/JetBrains/intellij-deps-jdi.git

Source: %name-%version.tar
Patch0: 0001-Use-system-Gradle-and-test-libraries.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.apiguardian:apiguardian-api)

%description
JetBrains' fork of the JDK Java Debug Interface implementation used by the
IntelliJ Platform. It publishes the org.jetbrains.intellij.deps:jb-jdi API.

%prep
%setup -q
%autopatch -p1
bash test/prepare.sh

%build
%gradle_publish

%install
%gradle_register --artifacts=jb-jdi
%gradle_install
test -s %buildroot%_javadir/%name/jb-jdi.jar

%check
%gradle_check

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.48-alt1
- Initial build for ALT.
