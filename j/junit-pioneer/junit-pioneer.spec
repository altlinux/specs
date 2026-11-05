%define _unpackaged_files_terminate_build 1

Name: junit-pioneer
Version: 2.3.0
Release: alt1

Summary: JUnit Jupiter extension pack
License: EPL-2.0
Group: Development/Java
URL: https://junit-pioneer.org/
VCS: https://github.com/junit-pioneer/junit-pioneer.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.junit.platform:junit-platform-testkit)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: equalsverifier
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(org.jacoco:org.jacoco.agent)
BuildRequires: mvn(org.jacoco:org.jacoco.ant)

%description
JUnit Pioneer provides extensions for JUnit Jupiter, including environment,
locale, resource, retry, cartesian and parameterized test utilities.

%package javadoc
Summary: API documentation for JUnit Pioneer
Group: Development/Java

%description javadoc
API documentation for JUnit Pioneer.

%prep
%setup
%autopatch -p1

# 32-bit x86 cannot reserve the upstream 8 GiB Gradle daemon heap.
if [ "$(getconf LONG_BIT)" = 32 ]; then
  case "$(uname -m)" in
    i?86|x86_64)
      sed -i 's/^org.gradle.jvmargs=-Xmx8g$/org.gradle.jvmargs=-Xmx1g/' \
        gradle.properties
      ;;
  esac
fi

%build
%gradle_publish -Pversion=%version -Dfile.encoding=UTF-8

%install
%gradle_register --artifacts=junit-pioneer-
%gradle_register_javadoc --artifacts=junit-pioneer-
%gradle_install

%check
%gradle_check -Pversion=%version -Dfile.encoding=UTF-8 jacocoTestReport

%files -f .mfiles
%doc LICENSE.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 2.3.0-alt1
- Initial build for ALT.
