%define _unpackaged_files_terminate_build 1

Name: java-caffeine
Version: 3.2.3
Release: alt1

Summary: High performance Java caching library
License: Apache-2.0
Group: Development/Java
Url: https://github.com/ben-manes/caffeine
VCS: https://github.com/ben-manes/caffeine.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.googlejavaformat:google-java-format)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.palantir.javapoet:javapoet)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.jspecify:jspecify)

%description
Caffeine provides bounded and unbounded local caches for Java applications.

%package javadoc
Summary: API documentation for Caffeine
Group: Development/Java

%description javadoc
API documentation for Caffeine.

%prep
%setup
%autopatch -p1
# Use the packaged JDK instead of upstream daemon download criteria.
rm -f gradle/gradle-daemon-jvm.properties

%build
%gradle_publish -Prelease --rerun-tasks --no-build-cache

%install
%gradle_register --artifacts=caffeine-
%gradle_register_javadoc --artifacts=caffeine-
%gradle_install

%files -f .mfiles
%doc LICENSE README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 3.2.3-alt1
- Initial build for ALT.
