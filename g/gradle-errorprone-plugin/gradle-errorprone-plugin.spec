%define _unpackaged_files_terminate_build 1

Name: gradle-errorprone-plugin
Version: 5.2.0
Release: alt1

Summary: Gradle plugin to use the Error Prone compiler for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/tbroyer/gradle-errorprone-plugin
VCS: https://github.com/tbroyer/gradle-errorprone-plugin.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-stdlib
BuildRequires: gradle-kotlin-accessors-generator
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.google.errorprone:error_prone_check_api)

%description
Gradle plugin that configures the Error Prone static analysis compiler
for Java compilation tasks.

%prep
%setup -q -n %name-%version
%autopatch -p1

%build
# The upstream build self-applies this plugin only to run optional lint; this
# bootstrap is unavailable offline. Production plugin sources are compiled.
%gradle_publish -PpackageVersion=%version

%install
%gradle_register --artifacts=gradle-errorprone-plugin-
%mvn_artifact $HOME/.m2/repository/net/ltgt/errorprone/net.ltgt.errorprone.gradle.plugin/%version/net.ltgt.errorprone.gradle.plugin-%version.pom
%gradle_install

%check
# TestKit integration tests download Gradle distributions and Maven Central inputs.
%gradle_check -PpackageVersion=%version -x integrationTest

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 5.2.0-alt1
- Initial build for ALT.
