Name: event-studio
Version: 3.0.4
Release: alt1

Summary: Event bus implementation providing pub/sub pattern with events queue
License: Apache-2.0
Group: Development/Java
Url: https://github.com/torakiki/event-studio
BuildArch: noarch

Source0: https://github.com/torakiki/%name/archive/v%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)

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

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Mar 02 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.4-alt1
- Initial build for Sisyphus.
