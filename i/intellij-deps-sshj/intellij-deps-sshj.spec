%define _unpackaged_files_terminate_build 1

Name: intellij-deps-sshj
Version: 0.41.1
Release: alt1

Summary: JetBrains SSHJ fork for the IntelliJ Platform
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/intellij-deps-sshj
VCS: https://github.com/JetBrains/intellij-deps-sshj.git

Source: %name-%version.tar
Patch0: 0001-Use-system-Gradle-dependencies.patch
Patch1: 0002-Manage-SSH-fixtures-with-Spock.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.jacoco:org.jacoco.ant)
BuildRequires: biz-aQute-bnd-gradle-plugins

BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires: mvn(com.hierynomus:asn-one)

BuildRequires: mvn(org.apache.groovy:groovy)
BuildRequires: mvn(org.spockframework:spock-core)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.apache.sshd:sshd-core)
BuildRequires: mvn(org.apache.sshd:sshd-sftp)
BuildRequires: mvn(org.apache.sshd:sshd-scp)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)

%description
JetBrains' fork of SSHJ, an SSH, SCP, and SFTP library for Java. It publishes
the org.jetbrains.intellij.deps:sshj Maven artifact used by the IntelliJ
Platform.

%prep
%setup -q
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=sshj
%gradle_install
test -s %buildroot%_javadir/%name/sshj.jar

%check
# This upstream Testcontainers integration suite has no current offline RPM providers.
%gradle_check -x integrationTest

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 0.41.1-alt1
- Initial build for ALT.
