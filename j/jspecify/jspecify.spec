%define _unpackaged_files_terminate_build 1
%def_with check

Name: jspecify
Version: 1.0.0
Release: alt1

Summary: Well-specified annotations to power static analysis checks and JVM language interop
License: Apache-2.0
Group: Development/Java
Url: https://jspecify.dev
Vcs: https://github.com/jspecify/jspecify.git
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-11-openjdk-devel
BuildRequires: java-17-openjdk-devel
BuildRequires: biz-aQute-bnd-gradle-plugins
%if_with check
BuildRequires: opentest4j
BuildRequires: apiguardian
BuildRequires: junit5
BuildRequires: java-1.8.0-openjdk-devel
%endif

Source0: %name-%version.tar
Patch0: 0001-Remove-unnecessary-gradle-plugins-alt-patch.patch
%if_with check
Patch1: 0002-Specify-dependencies-explicitly-for-integration-test.patch
%endif

%description
JSpecify is an industry-led effort to create a unified, standard set of
nullness annotations for Java. By annotating your code with
@Nullableand@NonNull, you provide crucial hints to static analysis tools and
IDEs, enabling them to detect potential null-pointer exceptions at compile
time. This leads to safer, more reliable code and reduces the need for
boilerplate null checks.

%prep
%setup
%autopatch -p1

sed -i 's/0\.0\.0-SNAPSHOT/1.0.0/g' gradle.properties
sed -i 's/21/17/g' gradle/gradle-daemon-jvm.properties

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%check
# Skip test for java8 (class file version 53.0 this version of the Java Runtime only recognizes class file versions up to 52.0).
# This is about junit.
%gradle_check -x :integrationTestOnJava8

%files -f .mfiles

%changelog
* Fri Oct 24 2025 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- First build for ALT.
