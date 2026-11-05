%define _unpackaged_files_terminate_build 1

Name: archunit
Version: 1.5.1
Release: alt1

Summary: Java architecture rule checking with JUnit integrations
License: Apache-2.0
Group: Development/Java
URL: https://www.archunit.org/
VCS: https://github.com/TNG/ArchUnit.git

Source0: %name-%version.tar
Patch0: %name-%version-alt-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.vintage:junit-vintage-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-commons)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mockito-junit-jupiter
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.assertj:assertj-guava)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.logging.log4j:log4j-slf4j-impl)

%description
ArchUnit imports Java bytecode and checks architectural rules about packages,
classes and dependencies. This package includes the core library, JUnit 4
runner and JUnit 5 API and engine, using system Guava and ASM implementations.

%package javadoc
Summary: API documentation for ArchUnit
Group: Development/Documentation

%description javadoc
API documentation for the ArchUnit core library and JUnit integrations.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=archunit- \
    --exclude-artifacts=archunit-self-test-library-
%gradle_register_javadoc --artifacts=archunit- \
    --exclude-artifacts=archunit-self-test-library-
%gradle_install

%check
%gradle_check --max-workers=2

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 1.5.1-alt1
- Initial build for ALT.
