Name: event-studio
Version: 5.0.1
Release: alt1

Summary: Event bus implementation providing pub/sub pattern with events queue

License: Apache-2.0
Group: Development/Java
Url: https://github.com/torakiki/event-studio
BuildArch: noarch
ExcludeArch: %ix86

Source0: https://github.com/torakiki/%name/archive/v%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: java-21-openjdk-devel

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api:2)

%description
EventStudio is yet another pure Java event bus implementation providing pub/sub pattern
with events queue capabilities for intra-jvm event communication.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
This package contains the API documentation for %name.

%prep
%setup
%pom_change_dep org.slf4j:slf4j-api org.slf4j:slf4j-api:2

%build
export JAVA_HOME=%_jvmdir/java-21-openjdk
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 5.0.1-alt1
- New version 5.0.1.

* Mon Mar 02 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.4-alt1
- Initial build for Sisyphus.
